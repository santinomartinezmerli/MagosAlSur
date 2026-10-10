# Magos al Sur - Sitio web (demo)

Sitio de **Magos al Sur**, alojamientos turísticos de la familia Merli en Bariloche, Las Grutas y la Toscana (Chianciano Terme).
HTML y CSS puros, sin framework y sin build para publicar. Pensado para presentar al cliente.

> Los textos, tarifas y datos de contacto salen del material que pasó el cliente. Conviene que los valide antes de publicar (ver "Pendientes").

## Qué incluye

| Página | Archivo |
| --- | --- |
| Inicio: hero, tres destinos, los 7 alojamientos, familia Merli, contacto | `index.html` |
| Bariloche (5 alojamientos) | `bariloche.html` |
| Las Grutas (1 alojamiento) | `las-grutas.html` |
| La Toscana (1 alojamiento) | `la-toscana.html` |
| Un alojamiento por página: fotos, descripción, qué incluye, condiciones y tarifas | `alojamientos/*.html` |

Alojamientos: Lake Águilas, Lake Bandurrias, Downtown Mitre, Vintage, Lake Colibríes (Bariloche), Magos al Mar (Las Grutas) y Monastero Abadesa (Chianciano Terme).

Cada alojamiento tiene un botón **Consultar por WhatsApp** que abre el chat con el mensaje ya escrito (nombre y destino), y otro por email.
Las fotos se abren en un visor con flechas (teclado incluido).

## Tecnología

- HTML y CSS puros; un script chico (`script.js`) para el menú móvil y el visor de fotos.
- Tipografías autoalojadas en `assets/fonts` (Fraunces para títulos, Hanken Grotesk para texto): no depende de Google Fonts.
- Fotos en WebP: versión grande (`nombre.webp`) y chica para listados (`nombre-sm.webp`).
- Responsive: probado en 1440 px y 390 px, sin desborde horizontal.

## Estructura

```
index.html, bariloche.html, las-grutas.html, la-toscana.html
alojamientos/            una página por alojamiento
styles.css               estilos y variables de marca (:root)
script.js                menú móvil y visor de fotos
favicon.svg
assets/img/              fotos (WebP)
assets/fonts/            tipografías
tools/build.py           generador de las páginas (opcional)
```

## Identidad visual

| Uso | Color |
| --- | --- |
| Violeta de marca (botones, detalles, bloque de contacto) | `#5B2A86` |
| Fondo | `#F6F5FA` |
| Tinta (texto, pie) | `#1E1830` |
| Lila suave (secciones alternas) | `#ECE8F4` |
| Plata (líneas) | `#C4C7D2` |

Los colores se cambian en un solo lugar: las variables al inicio de `styles.css`.

## Probar en local

Abrí `index.html` con doble click, o levantá un servidor:

```
python3 -m http.server 8000
```

y entrá a http://localhost:8000

## Publicar en Vercel

Es un sitio estático: no hay comando de build y el directorio a publicar es la raíz.
Importá el repositorio en Vercel (Framework Preset: Other) o arrastrá la carpeta.

## Cómo editar

**Cambios de texto, tarifas o fotos:** editá el HTML directamente, o (recomendado) cambiá los datos en `tools/build.py`
y volvé a generar las páginas, así quedan todas coherentes:

```
pip install pillow
python3 tools/build.py
```

Ahí están, en listas simples: contacto (WhatsApp, email, Instagram), destinos, y cada alojamiento con su descripción,
qué incluye, condiciones, tarifas y fotos.

**Agregar un alojamiento:** sumá las fotos a `assets/img/` (`slug-1.webp`, `slug-1-sm.webp`, ...), agregá un bloque
en `STAYS` y las descripciones de las fotos en `ALTS`, y corré el generador.

**Agregar un destino:** sumá un bloque en `DESTINOS` y corré el generador (aparece en el menú, la home y el pie).

## Pendientes y cosas a validar con el cliente

- **IVA en Vintage y Lake Colibríes:** el texto que pasó el cliente no aclara si las tarifas llevan IVA, así que se muestran sin "+ IVA". En los demás alojamientos sí lo dice.
- **"Por noche":** ningún texto indica el período de la tarifa; el sitio aclara "por noche". Confirmar.
- **Magos al Mar, enero y febrero:** el texto dice USD 120 "por reserva anticipada" para enero y febrero, y USD 140 como tarifa general. Siendo temporada alta, el valor menor llama la atención. Confirmar que no esté invertido.
- **Lake Águilas, capacidad:** el texto dice "seis / 7". Se muestra 6 pasajeros; la tarifa es base 4 y dos pasajeros más con suplemento.
- **Lake Colibríes:** no hay horarios de entrada y salida ni condiciones (mascotas, ropa de cama, toallas). La sección "Condiciones" queda oculta hasta que las pasen.
- **Monastero Abadesa:** no hay tarifa ni horarios; muestra "Consultar tarifas".
- **Temporadas de Bariloche:** el sitio dice "alta: verano e invierno, baja: el resto del año". Convendría definir los meses exactos.
- **Logo:** la imagen que pasaron incluye un email viejo (`poeta964@hotmail.com`), así que no se usó. La marca del sitio es un símbolo provisorio de tres círculos entrelazados (los tres destinos). Si tienen el logo original en PNG con fondo transparente o vectorial, se reemplaza.
- **Fotos:** Las Grutas y la Toscana no tienen fotos de la playa ni de los alrededores de la casa. Algunas imágenes muestran objetos personales (estantes, secaplatos) y convendría reemplazarlas por otras más ordenadas.
- **Dominio:** al tener dominio, agregar `sitemap.xml`, `og:image` (URL absoluta) y la URL canónica.
- **Consejos y experiencias de viaje:** no se incluyó una sección propia; hoy se deriva a Instagram. Queda como siguiente fase.

## Créditos y derechos

Logo, fotos y textos pertenecen a Magos al Sur y a la familia Merli. Tipografías Fraunces y Hanken Grotesk con licencia SIL Open Font License.
