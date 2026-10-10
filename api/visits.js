// Contador de visitas de hoy para Vercel.
// Guarda un número por día (sin datos personales) en una base Redis de Upstash.
//
// Variables de entorno (las crea Vercel al conectar Upstash Redis al proyecto):
//   KV_REST_API_URL y KV_REST_API_TOKEN   (o UPSTASH_REDIS_REST_URL y UPSTASH_REDIS_REST_TOKEN)
//
// Para poder diagnosticarlo desde el navegador, esta función siempre responde 200
// con un JSON. Si algo falla, el JSON trae ok:false y el motivo en "reason":
//   {"ok":true,"today":12}                    -> funciona
//   {"ok":false,"reason":"sin-configurar"}    -> falta conectar la base en Vercel
//   {"ok":false,"reason":"redis", ...}        -> la base respondió con error
// El sitio solo muestra el contador cuando llega ok:true.

const URL_ = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL;
const TOKEN = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;

async function redis(command) {
  const res = await fetch(URL_, {
    method: 'POST',
    headers: { Authorization: 'Bearer ' + TOKEN, 'Content-Type': 'application/json' },
    body: JSON.stringify(command),
  });
  if (!res.ok) throw new Error('HTTP ' + res.status);
  const data = await res.json();
  if (data && data.error) throw new Error(String(data.error));
  return data.result;
}

function todayAR() {
  // yyyy-mm-dd en hora de Argentina
  return new Intl.DateTimeFormat('en-CA', { timeZone: 'America/Argentina/Buenos_Aires' }).format(new Date());
}

module.exports = async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('Content-Type', 'application/json; charset=utf-8');

  if (req.method !== 'GET') return res.status(405).json({ ok: false, reason: 'metodo-no-permitido' });

  if (!URL_ || !TOKEN) {
    return res.status(200).json({
      ok: false,
      reason: 'sin-configurar',
      ayuda: 'Conectar una base Upstash Redis al proyecto en Vercel (Storage) y volver a desplegar.',
    });
  }

  let hit = false;
  try {
    hit = new URL(req.url || '/', 'http://localhost').searchParams.get('hit') === '1';
  } catch (e) { /* sin query */ }
  const ua = String(req.headers['user-agent'] || '');
  if (/bot|crawl|spider|preview|monitor|headless|lighthouse/i.test(ua)) hit = false;

  const key = 'visits:' + todayAR();
  try {
    let today;
    if (hit) {
      today = Number(await redis(['INCR', key]));
      if (today === 1) await redis(['EXPIRE', key, 60 * 60 * 24 * 60]); // se conserva 60 días
    } else {
      today = Number((await redis(['GET', key])) || 0);
    }
    return res.status(200).json({ ok: true, today });
  } catch (e) {
    return res.status(200).json({ ok: false, reason: 'redis', detalle: String(e && e.message).slice(0, 80) });
  }
};
