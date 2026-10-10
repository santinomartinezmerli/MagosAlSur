// Magos al Sur: menú móvil y visor de fotos. Sin dependencias.
(function () {
  // Menú
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('menu');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Visor de fotos
  var links = Array.prototype.slice.call(document.querySelectorAll('a[data-lightbox]'));
  if (!links.length || typeof HTMLDialogElement === 'undefined') return;

  var dlg = document.createElement('dialog');
  dlg.className = 'lightbox';
  dlg.setAttribute('aria-label', 'Galería de fotos');
  dlg.innerHTML =
    '<div class="lightbox__stage"><img class="lightbox__img" alt=""></div>' +
    '<button class="lightbox__btn lightbox__close" type="button" aria-label="Cerrar">&times;</button>' +
    '<button class="lightbox__btn lightbox__prev" type="button" aria-label="Foto anterior">&#8249;</button>' +
    '<button class="lightbox__btn lightbox__next" type="button" aria-label="Foto siguiente">&#8250;</button>' +
    '<p class="lightbox__count" aria-live="polite"></p>';
  document.body.appendChild(dlg);

  var img = dlg.querySelector('.lightbox__img');
  var count = dlg.querySelector('.lightbox__count');
  var index = 0;

  function show(i) {
    index = (i + links.length) % links.length;
    var a = links[index];
    var thumb = a.querySelector('img');
    img.src = a.getAttribute('href');
    img.alt = thumb ? thumb.alt : '';
    count.textContent = (index + 1) + ' de ' + links.length;
  }

  links.forEach(function (a, i) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      show(i);
      dlg.showModal();
    });
  });

  dlg.querySelector('.lightbox__close').addEventListener('click', function () { dlg.close(); });
  dlg.querySelector('.lightbox__prev').addEventListener('click', function () { show(index - 1); });
  dlg.querySelector('.lightbox__next').addEventListener('click', function () { show(index + 1); });
  dlg.addEventListener('click', function (e) {
    if (e.target === dlg || e.target.classList.contains('lightbox__stage')) dlg.close();
  });
  dlg.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') show(index - 1);
    if (e.key === 'ArrowRight') show(index + 1);
  });
})();

// Contador de visitas de hoy (chico, al pie). Si el servicio no responde, no se muestra nada.
(function () {
  var el = document.getElementById('visits');
  if (!el || !window.fetch) return;

  // Hora de Argentina, para que "hoy" coincida con el día del cliente.
  var day;
  try {
    day = new Intl.DateTimeFormat('en-CA', { timeZone: 'America/Argentina/Buenos_Aires' }).format(new Date());
  } catch (e) { day = new Date().toISOString().slice(0, 10); }

  // Cada navegador suma una sola vez por día.
  var counted = false;
  try { counted = localStorage.getItem('mas-visit') === day; } catch (e) {}

  fetch('/api/visits' + (counted ? '' : '?hit=1'), { cache: 'no-store' })
    .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
    .then(function (d) {
      if (!d || d.ok !== true || typeof d.today !== 'number') return;
      try { localStorage.setItem('mas-visit', day); } catch (e) {}
      el.textContent = d.today === 1
        ? 'Hoy visitó el sitio 1 persona.'
        : 'Hoy visitaron el sitio ' + d.today.toLocaleString('es-AR') + ' personas.';
      el.hidden = false;
    })
    .catch(function () {});
})();
