// Contador de visitas de hoy para Vercel.
// Guarda un número por día (sin datos personales) en una base Redis de Upstash.
// Variables de entorno (las crea Vercel al conectar Upstash Redis al proyecto):
//   KV_REST_API_URL y KV_REST_API_TOKEN   (o UPSTASH_REDIS_REST_URL y UPSTASH_REDIS_REST_TOKEN)
// Sin esas variables responde 503 y el sitio simplemente no muestra el contador.

const URL_ = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL;
const TOKEN = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;

async function redis(command) {
  const res = await fetch(URL_, {
    method: 'POST',
    headers: { Authorization: 'Bearer ' + TOKEN, 'Content-Type': 'application/json' },
    body: JSON.stringify(command),
  });
  if (!res.ok) throw new Error('redis ' + res.status);
  return (await res.json()).result;
}

function todayAR() {
  // yyyy-mm-dd en hora de Argentina
  return new Intl.DateTimeFormat('en-CA', { timeZone: 'America/Argentina/Buenos_Aires' }).format(new Date());
}

module.exports = async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store');
  if (!URL_ || !TOKEN) return res.status(503).json({ error: 'contador no configurado' });
  if (req.method !== 'GET') return res.status(405).json({ error: 'método no permitido' });

  const key = 'visits:' + todayAR();
  const ua = String(req.headers['user-agent'] || '');
  const isBot = /bot|crawl|spider|preview|monitor|headless|lighthouse/i.test(ua);
  const hit = req.query && req.query.hit === '1' && !isBot;

  try {
    let today;
    if (hit) {
      today = Number(await redis(['INCR', key]));
      if (today === 1) await redis(['EXPIRE', key, 60 * 60 * 24 * 60]); // se conserva 60 días
    } else {
      today = Number((await redis(['GET', key])) || 0);
    }
    return res.status(200).json({ today });
  } catch (e) {
    return res.status(502).json({ error: 'no se pudo leer el contador' });
  }
};
