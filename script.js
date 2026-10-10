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
