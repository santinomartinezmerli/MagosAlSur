#!/usr/bin/env python3
"""Genera las páginas HTML de Magos al Sur.

Uso (desde la raíz del proyecto):  python3 tools/build.py

El sitio publicado es HTML estático: este script solo evita copiar y pegar
cuando se agrega un alojamiento o un destino. Requiere Pillow (pip install pillow)
para leer el tamaño de las fotos.
"""
import html
import json
import os
from urllib.parse import quote

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(ROOT, "assets", "img")

# ---------------------------------------------------------------- contacto
WA_NUM = "5492944580000"
WA_PRETTY = "+54 9 294 458-0000"
EMAIL = "magosalsur@outlook.com.ar"
IG_URL = "https://www.instagram.com/magosalsur/"
IG_HANDLE = "@magosalsur"

esc = html.escape


def wa_link(text):
    return f"https://wa.me/{WA_NUM}?text={quote(text)}"


# ------------------------------------------------------------------ destinos
DESTINOS = [
    dict(
        slug="bariloche",
        nombre="Bariloche",
        rotulo="Montaña y lago",
        cover="aguilas-1",
        cover_pos="50% 50%",
        alt="Living de Lake Águilas con ventanal sobre el lago Nahuel Huapi",
        intro=(
            "Cinco alojamientos en Bariloche: una casa y un departamento con vista al lago, "
            "dos departamentos en pleno centro y uno nuevo a 7 km del microcentro."
        ),
        temporada="Temporada alta: verano e invierno. Temporada baja: el resto del año.",
        desc="Alojamientos turísticos en Bariloche: casa y departamentos con vista al lago y en el centro.",
    ),
    dict(
        slug="las-grutas",
        nombre="Las Grutas",
        rotulo="Mar",
        cover="grutas-5",
        cover_pos="50% 40%",
        alt="Patio con sillones, bancos de madera y un sol pintado en la pared",
        intro="Un alojamiento equipado para 6 pasajeros, a 200 metros de la quinta bajada.",
        temporada="Temporada alta: enero y febrero.",
        desc="Alojamiento turístico en Las Grutas para 6 pasajeros, a 200 metros de la quinta bajada.",
    ),
    dict(
        slug="la-toscana",
        nombre="La Toscana",
        rotulo="Valle",
        cover="monastero-2",
        cover_pos="50% 45%",
        alt="Torre del reloj iluminada al anochecer en Chianciano Terme",
        intro="Una casa para 4 pasajeros en Chianciano Terme, en la Toscana.",
        temporada="No hay una temporada definida.",
        desc="Casa turística en Chianciano Terme, Toscana, para 4 pasajeros.",
    ),
]
DEST = {d["slug"]: d for d in DESTINOS}

# --------------------------------------------------------------- fotos (alt)
ALTS = {
    "aguilas": {
        1: "Living con ventanal sobre el lago y mesa larga junto a la vista",
        2: "Atardecer rojo sobre el lago visto desde el living",
        3: "Parrilla con campana y revestimiento de piedra en el quincho interior",
    },
    "bandurrias": {
        1: "Estar con ventana al lago, mesa con banco esquinero y hogar blanco",
        2: "Living con vista al lago, banco esquinero, mesa y hogar",
        3: "Dormitorio con cama doble, mesas de luz blancas y placard",
    },
    "mitre": {
        1: "Living comedor luminoso con sillón cama y mesa con sillas",
        2: "Dormitorio principal con cama doble y cortinas turquesa",
        3: "Dormitorio con dos camas individuales y placard",
    },
    "vintage": {
        1: "Ambiente con cama individual, mesa de vidrio y cocina",
        2: "Dormitorio matrimonial con cabecera verde agua",
        3: "Cocina con bacha, cocina a gas y termotanque",
    },
    "colibries": {
        1: "Dormitorio con cama doble, televisor y estantes",
        2: "Baño con lavatorio de madera y ducha",
        3: "Rincón de comedor con mesa, microondas y pava eléctrica",
        4: "Cocina con bacha, anafe eléctrico y heladera bajo mesada",
    },
    "grutas": {
        1: "Cocina comedor y living con ventanal y ventilador de techo",
        2: "Baño con ducha y bidet",
        3: "Dormitorio con cama doble y cortinas turquesa",
        4: "Dormitorio con cama individual",
        5: "Patio con sillones, bancos de madera y un sol pintado en la pared",
    },
    "monastero": {
        1: "Entrada con arco de ladrillo y macetas con flores en Chianciano Terme",
        2: "Torre del reloj iluminada al anochecer en Chianciano Terme",
        3: "Living con vigas de madera y sillón rojo",
        4: "Dormitorio matrimonial con vigas de madera",
        5: "Dormitorio con dos camas individuales de hierro forjado",
        6: "Cocina con heladera, horno eléctrico y mesada de granito",
    },
}

# --------------------------------------------------------------- alojamientos
# tarifas: lista de (temporada, [(detalle, usd)]). iva=True agrega "+ IVA" a cada valor.
STAYS = [
    dict(
        slug="lake-aguilas",
        photos="aguilas",
        dest="bariloche",
        nombre="Lake Águilas",
        resumen="Casa para 6 pasajeros con vista al lago, parrilla y quincho interior.",
        hero=2,
        hero_pos="50% 55%",
        gallery=[1, 3],
        facts=[("Capacidad", "6 pasajeros"), ("Entrada", "14:30"), ("Salida", "10:00"), ("Vista", "Al lago")],
        descripcion=[
            "Casa exclusiva y equipada sobre el lago, con acceso propio y estacionamiento dentro del predio.",
            "El quincho interior tiene parrilla, y el living abre un ventanal hacia el agua.",
        ],
        incluye=[
            "Casa equipada",
            "Parrilla y quincho interior",
            "Estacionamiento dentro del predio",
            "Acceso propio",
            "Ropa de cama",
        ],
        condiciones=[
            "No se proveen toallas.",
            "La tarifa corresponde a 4 pasajeros. Pueden sumarse dos pasajeros más con suplemento.",
            "Tarifa por pago total al reservar. Otras modalidades de pago tienen un 10% adicional.",
            "Entrada a las 14:30 y salida a las 10:00, sin excepción.",
            "Las extensiones horarias están sujetas a disponibilidad: se piden con 48 horas de anticipación y se abonan por cada hora de extensión.",
        ],
        tarifas=[("Temporada baja", [("4 pasajeros", 140)]), ("Temporada alta", [("4 pasajeros", 180)])],
        iva=True,
        nota="Dos pasajeros más con suplemento.",
    ),
    dict(
        slug="lake-bandurrias",
        photos="bandurrias",
        dest="bariloche",
        nombre="Lake Bandurrias",
        resumen="Departamento de 60 m² para 2 a 4 pasajeros, con vista panorámica al lago.",
        hero=2,
        hero_pos="50% 50%",
        gallery=[1, 3],
        facts=[("Capacidad", "2 a 4 pasajeros"), ("Superficie", "60 m²"), ("Entrada", "Desde las 14:00"), ("Salida", "Hasta las 10:00")],
        descripcion=[
            "Amplio departamento de 60 m², totalmente equipado y con vista panorámica al lago.",
            "Tiene un porche con mobiliario exterior. La tarifa base es para dos pasajeros, con lugar para un tercero y, en carricama, para un cuarto pasajero (ideal para un niño o una persona de menos de 70 kg).",
        ],
        incluye=[
            "Totalmente equipado",
            "Vista panorámica al lago",
            "Porche con mobiliario exterior",
            "Ropa de cama",
        ],
        condiciones=[
            "No se admiten mascotas.",
            "No se proveen toallas.",
            "Entrada desde las 14:00 y salida hasta las 10:00, sin excepción.",
        ],
        tarifas=[("Temporada baja", [("2 pasajeros", 100)]), ("Temporada alta", [("2 pasajeros", 150)])],
        iva=True,
        nota="",
    ),
    dict(
        slug="downtown-mitre",
        photos="mitre",
        dest="bariloche",
        nombre="Downtown Mitre",
        resumen="Departamento de dos dormitorios para 6 pasajeros, con vista al lago y en pleno centro.",
        hero=1,
        hero_pos="50% 55%",
        gallery=[2, 3],
        facts=[("Capacidad", "6 pasajeros"), ("Dormitorios", "2"), ("Baños", "2"), ("Entrada", "14:00 a 14:30"), ("Salida", "10:00")],
        descripcion=[
            "Excelente y amplio departamento con dos dormitorios, dos baños y cocina separada, con hermosa vista al lago.",
            "Está en pleno centro de Bariloche, a pasos de todo, y tiene lugar para 6 pasajeros.",
        ],
        incluye=[
            "Dos dormitorios",
            "Dos baños",
            "Cocina separada",
            "Vista al lago",
            "Ubicación céntrica",
        ],
        condiciones=[
            "No se proveen toallas.",
            "El check-in y el check-out nocturnos tienen suplemento.",
            "Check-in de 14:00 a 14:30 y check-out a las 10:00, sin excepciones.",
            "Las extensiones horarias están sujetas a disponibilidad: se piden con anticipación y se abonan por cada hora de extensión.",
        ],
        tarifas=[("Temporada baja", [("Hasta 6 pasajeros", 130)]), ("Temporada alta", [("Hasta 6 pasajeros", 160)])],
        iva=True,
        nota="",
    ),
    dict(
        slug="vintage",
        photos="vintage",
        dest="bariloche",
        nombre="Vintage",
        resumen="Departamento para 3 pasajeros (máximo 4), en pleno centro y con estacionamiento.",
        hero=2,
        hero_pos="50% 55%",
        gallery=[1, 3],
        facts=[("Capacidad", "3 pasajeros, máximo 4"), ("Entrada", "14:00 a 14:30"), ("Salida", "Hasta las 10:30")],
        descripcion=[
            "Acogedor departamento equipado, con un dormitorio matrimonial y, en el living, una cama y una carricama individuales.",
            "Está en pleno centro, en la esquina del Carrefour, a la vuelta de Downtown Mitre. Tiene estacionamiento y todo queda cerca.",
        ],
        incluye=[
            "Departamento equipado",
            "Dormitorio matrimonial",
            "Cama y carricama individuales en el living",
            "Estacionamiento",
            "Ubicación céntrica",
        ],
        condiciones=[
            "No se proveen toallas.",
            "Se admite una mascota, sujeta a evaluación y con cargo.",
            "El check-in y el check-out nocturnos tienen suplemento.",
            "Check-in de 14:00 a 14:30 y check-out hasta las 10:30, sin excepciones.",
            "Las extensiones horarias están sujetas a disponibilidad y se abonan por hora.",
        ],
        tarifas=[
            ("Temporada baja", [("2 pasajeros", 65), ("2 adultos y 1 o 2 niños", 75)]),
            ("Temporada alta y fines de semana largos", [("2 pasajeros", 110), ("2 adultos y 2 niños", 125)]),
        ],
        iva=False,
        nota="",
    ),
    dict(
        slug="lake-colibries",
        photos="colibries",
        dest="bariloche",
        nombre="Lake Colibríes",
        resumen="Departamento nuevo para 2 pasajeros, a 7 km del microcentro.",
        hero=1,
        hero_pos="50% 55%",
        gallery=[2, 3, 4],
        facts=[("Capacidad", "2 pasajeros"), ("Ubicación", "A 7 km del microcentro")],
        descripcion=[
            "Departamento nuevo y totalmente equipado, pensado para dos personas.",
            "Está a 7 km del microcentro de Bariloche.",
        ],
        incluye=["Departamento nuevo", "Totalmente equipado"],
        condiciones=[],
        tarifas=[("Temporada baja", [("2 pasajeros", 65)]), ("Temporada alta", [("2 pasajeros", 90)])],
        iva=False,
        nota="",
    ),
    dict(
        slug="magos-al-mar",
        photos="grutas",
        dest="las-grutas",
        nombre="Magos al Mar",
        resumen="Alojamiento para 6 pasajeros, a 200 metros de la quinta bajada.",
        hero=1,
        hero_pos="50% 55%",
        gallery=[3, 4, 2, 5],
        facts=[("Capacidad", "6 pasajeros"), ("Ubicación", "A 200 m de la quinta bajada"), ("Entrada", "15:00"), ("Salida", "10:00")],
        descripcion=[
            "Alojamiento equipado para 6 pasajeros, a 200 metros de la quinta bajada de Las Grutas.",
            "La tarifa corresponde a 4 pasajeros. Pueden alojarse hasta seis con un suplemento.",
        ],
        incluye=[
            "Equipado para 6 pasajeros",
            "A 200 m de la quinta bajada",
            "Ropa de cama bajo petición",
        ],
        condiciones=[
            "No se proveen toallas.",
            "La ropa de cama se provee bajo petición y puede implicar un cargo adicional.",
            "Valores para 4 personas con pago adelantado.",
            "Entrada a las 15:00 y salida a las 10:00, sin excepciones.",
            "No se guardan valijas.",
        ],
        tarifas=[
            ("Tarifa general", [("4 pasajeros, pago adelantado", 140)]),
            ("Enero y febrero", [("Con reserva anticipada", 120)]),
        ],
        iva=True,
        nota="Hasta seis pasajeros con suplemento.",
    ),
    dict(
        slug="monastero-abadesa",
        photos="monastero",
        dest="la-toscana",
        nombre="Monastero Abadesa",
        resumen="Casa para 4 pasajeros en Chianciano Terme, en la Toscana.",
        hero=2,
        hero_pos="50% 45%",
        thumb=3,
        thumb_pos="50% 55%",
        gallery=[3, 4, 5, 6, 1],
        facts=[("Capacidad", "4 pasajeros"), ("Ubicación", "Chianciano Terme, Toscana")],
        descripcion=[
            "Casa equipada para 4 pasajeros en Chianciano Terme, en la Toscana.",
            "Se provee ropa de cama. Las toallas no están incluidas y se pueden solicitar con suplemento.",
        ],
        incluye=["Casa equipada", "Ropa de cama"],
        condiciones=[
            "No se permiten mascotas.",
            "No se proveen toallas. Si se solicitan, tienen suplemento.",
        ],
        tarifas=[],
        iva=False,
        nota="",
    ),
]


# ------------------------------------------------------------------- reseñas
# Solo se publican reseñas reales, copiadas tal cual de la plataforma.
# La clave es el slug del alojamiento. Campos:
#   fuente, url (ficha pública), puntaje, escala, cantidad,
#   promedio=True si el puntaje es el promedio calculado de las reseñas cargadas,
#   cats (puntajes por categoría, opcional) y quotes (comentarios textuales).
# Un alojamiento sin entrada no muestra la sección.
BOOKING = "Booking"
REVIEWS = {
    "lake-aguilas": dict(
        fuente=BOOKING,
        url="https://www.booking.com/hotel/ar/casa-en-el-lago-exclusiva.es.html",
        puntaje="9,7", escala="10", cantidad=12, promedio=True,
        quotes=[
            dict(texto="Alquilen acá… no se van a arrepentir. Propiedad impecable en todo el aspecto.",
                 autor="Ezequiel", origen="Argentina", fecha="noviembre de 2025"),
            dict(texto="La ubicacion frente al lago es fantastica , el ventanal tiene la mejor vista que se puede pedir!!",
                 autor="Cesar", origen="Argentina", fecha="octubre de 2025"),
            dict(texto="Lugar recomendable con excelente vista al lago. La tranquilidad y que todo estaba en orden. Muy agradecido.",
                 autor="Gareis", origen="Argentina", fecha="julio de 2026"),
        ],
    ),
    "lake-bandurrias": dict(
        fuente=BOOKING,
        url="https://www.booking.com/hotel/ar/departamento-moderno-con-vista-infinita-al-nahuel.es.html",
        puntaje="9,9", escala="10", cantidad=7, promedio=True,
        quotes=[
            dict(texto="Un lugar para volver. La excelente vista al lago Nahuel Huapi, la seguridad del lugar, lo equipado de la cocina.",
                 autor="Victoria", origen="Argentina", fecha="enero de 2025"),
            dict(texto="Departamento súper amplio y completo, con una maravillosa vista al lago.",
                 autor="Guillermo", origen="Argentina", fecha="enero de 2026"),
            dict(texto="Hermosa estadía. La casa tal cual se ve en las fotos, muy cómoda, y con todo lo necesario. La vista es maravillosa, realmente un sueño para disfrutar Bariloche. El entorno es tranquilo y la ubicación muy buena. Sin dudas volveríamos y la recomendamos totalmente.",
                 autor="Tesuri", origen="Argentina", fecha="enero de 2026"),
        ],
    ),
    "downtown-mitre": dict(
        fuente=BOOKING,
        url="https://www.booking.com/hotel/ar/magos-al-sur.es.html",
        puntaje="9,8", escala="10", cantidad=18, promedio=True,
        quotes=[
            dict(texto="Excelente atención y predisposición de la dueña atenta todo el tiempo, superó las expectativas todo lindo limpio cerca del centro cómodo y con mucho espacio",
                 autor="Ricardo", origen="Argentina", fecha="junio de 2025"),
            dict(texto="La ubicación es excelente, y la atención de la encargada dispuesta en todo momento",
                 autor="Mandrik", origen="Argentina", fecha="abril de 2025"),
            dict(texto="¡La ubicación y vista al lago únicas! muy completo y confortable el depto., Verónica muy atenta a toda consulta, lugar que recomiendo y al que volveremos próximamente.",
                 autor="Marcelo", origen="Argentina", fecha="diciembre de 2024"),
        ],
    ),
    "lake-colibries": dict(
        fuente=BOOKING,
        url="https://www.booking.com/hotel/ar/departamento-colibries-para-dos-sobre-el-lago.es.html",
        puntaje="9,5", escala="10", cantidad=2, promedio=True,
        quotes=[
            dict(texto="La ubicación hermosa! El micro pasa por la esquina para ir al centro, a la terminal... El depto muy lindo, limpio y cómodo con todo lo necesario (utensilios, pava eléctrica, heladera, etc). La anfitriona super amable ! La pasamos de diez.",
                 autor="Jimena", origen="Argentina", fecha="agosto de 2025"),
        ],
    ),
    "magos-al-mar": dict(
        fuente=BOOKING,
        url="https://www.booking.com/hotel/ar/magos-al-sur-mare.es.html",
        puntaje="9,3", escala="10", cantidad=7, promedio=True,
        cats=[
            ("Ubicación", "9,1"),
            ("Limpieza", "10"),
            ("Relación calidad-precio", "9,5"),
            ("Instalaciones y servicios", "10"),
            ("Confort", "9,5"),
            ("Personal", "10"),
        ],
        quotes=[],
    ),
    "vintage": dict(
        fuente="Airbnb",
        url="https://www.airbnb.com.ar/rooms/1310259972888945107",
        puntaje="5,0", escala="5", cantidad=4,
        cats=[
            ("Limpieza", "4,8"),
            ("Veracidad", "5,0"),
            ("Check-in", "5,0"),
            ("Comunicación", "5,0"),
            ("Ubicación", "5,0"),
            ("Precio según calidad", "5,0"),
        ],
        quotes=[],
    ),
}


def _count(r):
    n = r["cantidad"]
    return f"{n} reseña" + ("s" if n != 1 else "")


def rating_line(slug):
    r = REVIEWS.get(slug)
    if not r:
        return ""
    return (
        f'<span class="stay__rating">{esc(r["puntaje"])} sobre {esc(r["escala"])} '
        f'· {_count(r)} en {esc(r["fuente"])}</span>'
    )


def reviews_block(slug):
    r = REVIEWS.get(slug)
    if not r:
        return ""
    meta = (
        f"Promedio de {_count(r)} en {esc(r['fuente'])}"
        if r.get("promedio")
        else f"{_count(r)} en {esc(r['fuente'])}"
    )
    cats = ""
    if r.get("cats"):
        cats = '<dl class="rv__cats">' + "".join(
            f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in r["cats"]
        ) + "</dl>"
    quotes = ""
    if r.get("quotes"):
        items = ""
        for q in r["quotes"]:
            who = q["autor"] + (f", {q['origen']}" if q.get("origen") else "")
            when = f" · {q['fecha']}" if q.get("fecha") else ""
            items += (
                f'<figure class="rv__quote"><blockquote><p>{esc(q["texto"])}</p></blockquote>'
                f"<figcaption>{esc(who)}{esc(when)}</figcaption></figure>"
            )
        quotes = (
            f'<div class="rv__quotes">{items}</div>'
            f'<p class="rv__note">Comentarios copiados de {esc(r["fuente"])}. La fecha es la de la estadía.</p>'
        )
    return f"""
<section class="section section--tight" aria-labelledby="rv-title">
  <div class="wrap">
    <h2 id="rv-title">Reseñas de huéspedes</h2>
    <div class="rv">
      <div class="rv__score">
        <p class="rv__num">{esc(r['puntaje'])}<span> sobre {esc(r['escala'])}</span></p>
        <p class="rv__meta">{meta}</p>
        <a class="link" href="{esc(r['url'])}" target="_blank" rel="noopener">Ver en {esc(r['fuente'])}</a>
      </div>
      {cats}
    </div>
    {quotes}
  </div>
</section>"""


def home_reviews():
    out = ""
    for slug in ("lake-aguilas", "lake-bandurrias", "downtown-mitre"):
        r = REVIEWS.get(slug)
        stay = next((x for x in STAYS if x["slug"] == slug), None)
        if not r or not r.get("quotes") or not stay:
            continue
        q = r["quotes"][0]
        out += (
            f'<figure class="rv__quote"><blockquote><p>{esc(q["texto"])}</p></blockquote>'
            f'<figcaption>{esc(q["autor"])}, {esc(q["origen"])} · {esc(q["fecha"])} · '
            f'<a href="alojamientos/{slug}.html">{esc(stay["nombre"])}</a></figcaption></figure>'
        )
    if not out:
        return ""
    return f"""
<section class="section" id="huespedes" aria-labelledby="huespedes-title">
  <div class="wrap">
    <h2 id="huespedes-title">Lo que dicen los huéspedes</h2>
    <p class="section__lede">Comentarios de huéspedes en Booking. En cada alojamiento están el puntaje y más opiniones.</p>
    <div class="rv__quotes rv__quotes--home">{out}</div>
  </div>
</section>
"""


# ------------------------------------------------------------------- helpers
_dims = {}


def dims(name):
    if name not in _dims:
        with Image.open(os.path.join(IMG_DIR, name + ".webp")) as im:
            _dims[name] = im.size
    return _dims[name]


def photo_alt(stay, n):
    return ALTS[stay["photos"]][n]


def img_tag(name, alt, base, cls="", lazy=True, pos=None, priority=False):
    w, h = dims(name)
    attrs = [f'src="{base}assets/img/{name}.webp"', f'width="{w}"', f'height="{h}"', f'alt="{esc(alt)}"']
    if cls:
        attrs.append(f'class="{cls}"')
    if pos:
        attrs.append(f'style="object-position:{pos}"')
    if priority:
        attrs.append('fetchpriority="high"')
    elif lazy:
        attrs.append('loading="lazy"')
    attrs.append('decoding="async"')
    return "<img " + " ".join(attrs) + ">"


def usd(v, iva):
    return f"USD {v}" + (" + IVA" if iva else "")


def desde(stay):
    if not stay["tarifas"]:
        return None
    # valor más bajo publicado
    vals = [v for _, rows in stay["tarifas"] for _, v in rows]
    return usd(min(vals), stay["iva"])


def ring(size=28):
    # tres círculos entrelazados: los tres destinos
    return (
        f'<svg class="ring" width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" '
        'stroke="currentColor" stroke-width="1.6" aria-hidden="true">'
        '<circle cx="24" cy="17.5" r="11"/><circle cx="29.6" cy="27.2" r="11"/><circle cx="18.4" cy="27.2" r="11"/></svg>'
    )


def stays_of(dest_slug):
    return [s for s in STAYS if s["dest"] == dest_slug]


def stay_row(s, base):
    d = desde(s)
    price = (
        f'<span class="stay__from">Desde</span><span class="stay__amount">{esc(d)}</span><span class="stay__unit">por noche</span>'
        if d
        else '<span class="stay__amount stay__amount--ask">Consultar tarifas</span>'
    )
    tn = s.get("thumb", s["hero"])
    thumb = img_tag(f"{s['photos']}-{tn}-sm", photo_alt(s, tn), base, "stay__img", pos=s.get("thumb_pos", s["hero_pos"]))
    return f"""
        <a class="stay" href="{base}alojamientos/{s['slug']}.html">
          <span class="stay__media">{thumb}</span>
          <span class="stay__text">
            <span class="stay__name">{esc(s['nombre'])}</span>
            <span class="stay__summary">{esc(s['resumen'])}</span>
            {rating_line(s['slug'])}
          </span>
          <span class="stay__price">{price}</span>
        </a>"""


# ---------------------------------------------------------------- plantilla
def page(title, description, body, base="", extra_head="", current=""):
    cur = ' aria-current="page"'
    nav = "".join(
        '<li><a href="{}{}.html"{}>{}</a></li>'.format(base, d["slug"], cur if current == d["slug"] else "", esc(d["nombre"]))
        for d in DESTINOS
    )
    nav += f'<li><a href="{base}index.html#contacto">Contacto</a></li>'
    footer_dest = "".join(f'<li><a href="{base}{d["slug"]}.html">{esc(d["nombre"])}</a></li>' for d in DESTINOS)
    return f"""<!doctype html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_AR">
<meta property="og:site_name" content="Magos al Sur">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta name="theme-color" content="#5B2A86">
<link rel="icon" href="{base}favicon.svg" type="image/svg+xml">
<link rel="preload" href="{base}assets/fonts/fraunces-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{base}assets/fonts/hanken-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{base}styles.css">
{extra_head}
</head>
<body>
<a class="skip" href="#contenido">Ir al contenido</a>
<header class="site-header">
  <div class="wrap site-header__bar">
    <a class="brand" href="{base}index.html" aria-label="Magos al Sur, inicio">{ring(30)}<span>Magos al Sur</span></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="menu">Menú</button>
    <nav class="nav" id="menu" aria-label="Principal"><ul>{nav}</ul></nav>
  </div>
</header>
<main id="contenido">
{body}
</main>
<footer class="site-footer">
  <div class="wrap site-footer__grid">
    <div class="site-footer__brand">
      <span class="brand brand--footer">{ring(30)}<span>Magos al Sur</span></span>
      <p>Alojamientos turísticos de la familia Merli en Bariloche, Las Grutas y la Toscana.</p>
    </div>
    <div>
      <h2 class="site-footer__title">Destinos</h2>
      <ul class="plain">{footer_dest}</ul>
    </div>
    <div>
      <h2 class="site-footer__title">Contacto</h2>
      <ul class="plain">
        <li><a href="{wa_link('Hola! Quisiera hacer una consulta.')}" rel="noopener">WhatsApp {WA_PRETTY}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{IG_URL}" rel="noopener" target="_blank">Instagram {IG_HANDLE}</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap">
    <p class="site-footer__legal">Valores en dólares estadounidenses. Magos al Sur, 2026.
      <span class="visits" id="visits" hidden></span></p>
  </div>
</footer>
<script src="{base}script.js" defer></script>
</body>
</html>
"""


# ------------------------------------------------------------------- páginas
def build_home():
    hero = img_tag("aguilas-2", "Atardecer rojo sobre el lago desde el living de Lake Águilas", "", "hero__img", pos="50% 62%", priority=True)

    places = ""
    for d in DESTINOS:
        n = len(stays_of(d["slug"]))
        count = f"{n} alojamiento" + ("s" if n != 1 else "")
        places += f"""
        <a class="place" href="{d['slug']}.html">
          {img_tag(d['cover'], d['alt'], '', 'place__img', pos=d['cover_pos'])}
          <span class="place__body">
            <span class="place__name">{esc(d['nombre'])}</span>
            <span class="place__tag">{esc(d['rotulo'])}, {count}</span>
          </span>
        </a>"""

    groups = ""
    for d in DESTINOS:
        rows = "".join(stay_row(s, "") for s in stays_of(d["slug"]))
        groups += f"""
      <div class="group">
        <div class="group__head">
          <h3><a href="{d['slug']}.html">{esc(d['nombre'])}</a></h3>
          <p>{esc(d['temporada'])}</p>
        </div>
        <div class="stays">{rows}
        </div>
      </div>"""

    body = f"""
<section class="hero" aria-label="Magos al Sur">
  {hero}
  <div class="wrap hero__inner">
    <h1 class="hero__title">Magos al Sur</h1>
    <p class="hero__tagline">Montaña, mar y valle.</p>
    <p class="hero__sub">Alojamientos de la familia Merli en Bariloche, Las Grutas y la Toscana.</p>
    <div class="hero__actions">
      <a class="btn btn--light" href="#alojamientos">Ver alojamientos</a>
      <a class="btn btn--outline-light" href="{wa_link('Hola! Quisiera consultar disponibilidad.')}" rel="noopener">Consultar por WhatsApp</a>
    </div>
  </div>
</section>

<section class="section" id="destinos">
  <div class="wrap">
    <h2>Tres lugares para elegir</h2>
    <p class="section__lede">Un lago entre montañas, una playa en la costa patagónica y un pueblo de la Toscana.</p>
    <div class="places">{places}
    </div>
  </div>
</section>

<section class="section section--tint" id="alojamientos">
  <div class="wrap">
    <h2>Alojamientos</h2>
    <p class="section__lede">Siete opciones en tres destinos. Todas las tarifas están en dólares y se consultan por WhatsApp.</p>
    {groups}
  </div>
</section>

{home_reviews()}
<section class="section section--tint" id="familia">
  <div class="wrap family">
    <div>
      <h2>La familia Merli</h2>
      <p>Magos al Sur es de la familia Merli. Tenemos alojamientos en Bariloche, en Las Grutas y en Chianciano Terme, en la Toscana.</p>
      <p>En Instagram compartimos consejos y experiencias de viaje de cada lugar.</p>
      <p><a class="link" href="{IG_URL}" rel="noopener" target="_blank">Seguinos en Instagram {IG_HANDLE}</a></p>
    </div>
    <div class="family__mark">{ring(220)}</div>
  </div>
</section>

<section class="section section--violet" id="contacto">
  <div class="wrap contact">
    <div>
      <h2>Consultá disponibilidad</h2>
      <p class="section__lede">Escribinos con las fechas y la cantidad de pasajeros y te respondemos con la tarifa.</p>
      <a class="btn btn--light" href="{wa_link('Hola! Quisiera consultar disponibilidad.')}" rel="noopener">Escribir por WhatsApp</a>
    </div>
    <dl class="contact__list">
      <div><dt>WhatsApp</dt><dd><a href="{wa_link('Hola! Quisiera hacer una consulta.')}" rel="noopener">{WA_PRETTY}</a></dd></div>
      <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
      <div><dt>Instagram</dt><dd><a href="{IG_URL}" rel="noopener" target="_blank">{IG_HANDLE}</a></dd></div>
    </dl>
  </div>
</section>
"""
    ld = {
        "@context": "https://schema.org",
        "@type": "LodgingBusiness",
        "name": "Magos al Sur",
        "description": "Alojamientos turísticos de la familia Merli en Bariloche, Las Grutas y la Toscana.",
        "email": EMAIL,
        "telephone": "+5492944580000",
        "sameAs": [IG_URL],
    }
    head = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    write(
        "index.html",
        page(
            "Magos al Sur: alojamientos en Bariloche, Las Grutas y la Toscana",
            "Alojamientos turísticos de la familia Merli en Bariloche, Las Grutas y la Toscana. Montaña, mar y valle.",
            body,
            extra_head=head,
        ),
    )


def build_destino(d):
    rows = "".join(stay_row(s, "") for s in stays_of(d["slug"]))
    hero = img_tag(d["cover"], d["alt"], "", "dest-hero__img", pos=d["cover_pos"], priority=True)
    body = f"""
<section class="page-head">
  <div class="wrap">
    <p class="crumb"><a href="index.html">Inicio</a></p>
    <h1>{esc(d['nombre'])}</h1>
    <p class="page-head__lede">{esc(d['rotulo'])}. {esc(d['intro'])}</p>
    <p class="page-head__note">{esc(d['temporada'])}</p>
  </div>
</section>
<div class="wrap"><div class="dest-hero">{hero}</div></div>
<section class="section">
  <div class="wrap">
    <h2>Dónde alojarte en {esc(d['nombre'])}</h2>
    <div class="stays stays--page">{rows}
    </div>
  </div>
</section>
<section class="section section--violet">
  <div class="wrap contact">
    <div>
      <h2>¿No sabés cuál elegir?</h2>
      <p class="section__lede">Contanos cuántos son y en qué fechas y te recomendamos.</p>
    </div>
    <div><a class="btn btn--light" href="{wa_link('Hola! Quisiera consultar disponibilidad en ' + d['nombre'] + '.')}" rel="noopener">Escribir por WhatsApp</a></div>
  </div>
</section>
"""
    write(
        f"{d['slug']}.html",
        page(f"{d['nombre']}: alojamientos | Magos al Sur", d["desc"], body, current=d["slug"]),
    )


def build_stay(s):
    base = "../"
    d = DEST[s["dest"]]
    p = s["photos"]

    hero = (
        f'<a class="hero-photo" href="{base}assets/img/{p}-{s["hero"]}.webp" data-lightbox>'
        + img_tag(f"{p}-{s['hero']}", photo_alt(s, s["hero"]), base, "hero-photo__img", pos=s["hero_pos"], priority=True)
        + "</a>"
    )
    gallery = "".join(
        f'<a href="{base}assets/img/{p}-{n}.webp" data-lightbox>'
        + img_tag(f"{p}-{n}-sm", photo_alt(s, n), base)
        + "</a>"
        for n in s["gallery"]
    )
    facts = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in s["facts"])
    desc = "".join(f"<p>{esc(t)}</p>" for t in s["descripcion"])
    incluye = "".join(f"<li>{esc(t)}</li>" for t in s["incluye"])
    cond_block = ""
    if s["condiciones"]:
        cond = "".join(f"<li>{esc(t)}</li>" for t in s["condiciones"])
        cond_block = f'<h2>Condiciones</h2><ul class="checklist">{cond}</ul>'

    msg = f"Hola! Quisiera consultar disponibilidad en {s['nombre']} ({d['nombre']})."
    if s["tarifas"]:
        seasons = ""
        for season, rows in s["tarifas"]:
            lines = "".join(
                f'<div class="rate"><dt>{esc(lbl)}</dt><dd>{esc(usd(v, s["iva"]))}</dd></div>' for lbl, v in rows
            )
            seasons += f'<div class="season"><h3>{esc(season)}</h3><dl class="rates">{lines}</dl></div>'
        nota = f'<p class="aside__note">{esc(s["nota"])}</p>' if s["nota"] else ""
        rates = f'{seasons}{nota}<p class="aside__note">Valores en dólares, por noche.</p>'
    else:
        rates = '<p class="aside__ask">Consultá tarifas y disponibilidad por WhatsApp o por email.</p>'

    others = [x for x in stays_of(s["dest"]) if x["slug"] != s["slug"]]
    others_html = ""
    if others:
        rows = "".join(stay_row(x, base) for x in others)
        others_html = f"""
<section class="section section--tint">
  <div class="wrap">
    <h2>Otros alojamientos en {esc(d['nombre'])}</h2>
    <div class="stays stays--page">{rows}
    </div>
  </div>
</section>"""

    body = f"""
<section class="page-head">
  <div class="wrap">
    <p class="crumb"><a href="{base}{d['slug']}.html">{esc(d['nombre'])}</a></p>
    <h1>{esc(s['nombre'])}</h1>
    <p class="page-head__lede">{esc(s['resumen'])}</p>
    <dl class="facts">{facts}</dl>
  </div>
</section>
<div class="wrap">{hero}</div>
<section class="section section--tight">
  <div class="wrap detail">
    <div class="detail__main">
      <h2>Sobre este alojamiento</h2>
      {desc}
      <h2>Qué incluye</h2>
      <ul class="checklist">{incluye}</ul>
      {cond_block}
    </div>
    <aside class="aside" aria-label="Tarifas y consultas">
      <h2>Tarifas</h2>
      {rates}
      <a class="btn btn--primary btn--block" href="{wa_link(msg)}" rel="noopener">Consultar por WhatsApp</a>
      <a class="btn btn--outline btn--block" href="mailto:{EMAIL}?subject={quote('Consulta: ' + s['nombre'])}">Escribir por email</a>
    </aside>
  </div>
</section>
{reviews_block(s['slug'])}
<section class="section section--tight">
  <div class="wrap">
    <h2>Fotos</h2>
    <div class="gallery gallery--{min(len(s['gallery']), 3)}">{gallery}</div>
  </div>
</section>
{others_html}
"""
    ld = {
        "@context": "https://schema.org",
        "@type": "LodgingBusiness",
        "name": f"Magos al Sur {s['nombre']}",
        "description": s["resumen"],
        "email": EMAIL,
        "telephone": "+5492944580000",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Chianciano Terme" if s["dest"] == "la-toscana" else d["nombre"],
            "addressCountry": "IT" if s["dest"] == "la-toscana" else "AR",
        },
    }
    head = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    write(
        f"alojamientos/{s['slug']}.html",
        page(
            f"{s['nombre']}, {d['nombre']} | Magos al Sur",
            f"{s['resumen']} Alojamiento de Magos al Sur en {d['nombre']}.",
            body,
            base=base,
            extra_head=head,
            current=s["dest"],
        ),
    )


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("escrito", rel)


if __name__ == "__main__":
    build_home()
    for d in DESTINOS:
        build_destino(d)
    for s in STAYS:
        build_stay(s)
