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
  var AUTOPLAY_DELAY = 5000;
  var timer = null;
  var visible = true;
  var hoverPauses = 0;

  function render() {
    slides.forEach(function(slide, i) {
      slide.style.display = i === activeIndex ? 'flex' : 'none';
    });
    dots.forEach(function(dot, i) {
      dot.classList.toggle('is-active', i === activeIndex);
      dot.innerHTML = i === activeIndex ? ACTIVE_DOT_SVG : INACTIVE_DOT_SVG;
    });
    if (data && data[activeIndex]) {
      if (nameEl) nameEl.textContent = data[activeIndex].author;
      if (roleEl) roleEl.textContent = data[activeIndex].title;
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

  function startAuto() {
    stopAuto();
    if (visible && hoverPauses === 0) {
      timer = setInterval(next, AUTOPLAY_DELAY);
    }
  }

  function stopAuto() {
    if (timer) { clearInterval(timer); timer = null; }
  }

  function pause() {
    hoverPauses += 1;
    stopAuto();
  }

  function unpause() {
    hoverPauses = Math.max(0, hoverPauses - 1);
    startAuto();
  }

  function resetAuto() {
    startAuto();
  }

  dots.forEach(function(dot, i) {
    dot.addEventListener('click', function() { goTo(i); resetAuto(); });
    dot.addEventListener('mouseenter', pause);
    dot.addEventListener('mouseleave', unpause);
  });
  if (prevBtn) {
    prevBtn.addEventListener('click', function() { prev(); resetAuto(); });
    prevBtn.addEventListener('mouseenter', pause);
    prevBtn.addEventListener('mouseleave', unpause);
  }
  if (nextBtn) {
    nextBtn.addEventListener('click', function() { next(); resetAuto(); });
    nextBtn.addEventListener('mouseenter', pause);
    nextBtn.addEventListener('mouseleave', unpause);
  }

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        visible = entry.isIntersecting;
        if (visible) startAuto(); else stopAuto();
      });
    }, { threshold: 0.15 });
    io.observe(section);
  }

  render();
  startAuto();
})();