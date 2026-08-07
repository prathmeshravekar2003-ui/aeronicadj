(function() {
  var section = document.getElementById('testimonials');
  if (!section) return;

  var slides = Array.from(section.querySelectorAll('.testimonial-slide'));
  var dots = Array.from(section.querySelectorAll('.testimonial-dot'));
  var prevBtn = section.querySelector('.testimonial-prev');
  var nextBtn = section.querySelector('.testimonial-next');
  var nameEl = document.getElementById('testimonialName');
  var roleEl = document.getElementById('testimonialRole');

  var data = null;
  try {
    var el = section.querySelector('.testimonials-data');
    if (el) data = JSON.parse(el.textContent || '[]');
  } catch (e) { data = null; }

  if (slides.length === 0) return;

  var ACTIVE_DOT_SVG = '<svg viewBox="0 0 12 12" fill="currentColor" width="14" height="14">' +
    '<circle cx="6" cy="6" r="1.6" fill="#fff"></circle>' +
    '<circle cx="6" cy="6" r="0.7" fill="#fff" opacity="0.3"></circle></svg>';
  var INACTIVE_DOT_SVG = '<svg viewBox="0 0 12 12" fill="currentColor" width="14" height="14">' +
    '<circle cx="6" cy="6" r="0.7" fill="#fff" opacity="0.25"></circle></svg>';

  var activeIndex = 0;

  function render() {
    slides.forEach(function(slide, i) {
      slide.style.display = i === activeIndex ? 'flex' : 'none';
    });
    dots.forEach(function(dot, i) {
      dot.classList.toggle('is-active', i === activeIndex);
      dot.innerHTML = i === activeIndex ? ACTIVE_DOT_SVG : INACTIVE_DOT_SVG;
    });
    if (data && data[activeIndex]) {
      if (nameEl) nameEl.textContent = data[activeIndex].name;
      if (roleEl) roleEl.textContent = data[activeIndex].role;
    }
  }

  function goTo(index) {
    if (index < 0 || index >= slides.length) return;
    activeIndex = index;
    render();
  }

  function next() {
    goTo((activeIndex + 1) % slides.length);
  }

  function prev() {
    goTo((activeIndex - 1 + slides.length) % slides.length);
  }

  var timer = null;
  function startAuto() {
    stopAuto();
    timer = setInterval(next, 5000);
  }
  function stopAuto() {
    if (timer) { clearInterval(timer); timer = null; }
  }
  function resetAuto() {
    startAuto();
  }

  dots.forEach(function(dot, i) {
    dot.addEventListener('click', function() { goTo(i); resetAuto(); });
  });
  if (prevBtn) prevBtn.addEventListener('click', function() { prev(); resetAuto(); });
  if (nextBtn) nextBtn.addEventListener('click', function() { next(); resetAuto(); });

  section.addEventListener('mouseenter', stopAuto);
  section.addEventListener('mouseleave', startAuto);

  render();
  startAuto();
})();