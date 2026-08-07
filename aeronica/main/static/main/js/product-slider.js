(function() {
  var viewport = document.querySelector('.prod-viewport');
  if (!viewport) return;

  var slides = Array.from(viewport.querySelectorAll('.product-layout'));
  var tabs = Array.from(viewport.querySelectorAll('.prod-tab'));
  var dots = Array.from(viewport.querySelectorAll('.prod-pagination-btn'));
  var prevBtn = viewport.querySelector('.prod-nav-arrow-left');
  var nextBtn = viewport.querySelector('.prod-nav-arrow-right');
  if (slides.length === 0) return;

  var activeIndex = 0;

  var ACTIVE_DOT_SVG = '<svg viewBox="0 0 12 12" fill="currentColor" width="14" height="14">' +
    '<circle cx="6" cy="6" r="1.6" fill="#21389a"></circle>' +
    '<circle cx="6" cy="6" r="0.7" fill="#21389a" opacity="0.3"></circle></svg>';
  var INACTIVE_DOT_SVG = '<svg viewBox="0 0 12 12" fill="currentColor" width="14" height="14">' +
    '<circle cx="6" cy="6" r="0.7" fill="#888" opacity="0.25"></circle></svg>';

  function render() {
    slides.forEach(function(slide, i) {
      slide.style.display = i === activeIndex ? 'flex' : 'none';
    });
    tabs.forEach(function(tab, i) {
      var isActive = i === activeIndex;
      tab.classList.toggle('is-active', isActive);
      tab.style.color = isActive ? '#21389a' : '#888';
      tab.style.fontWeight = isActive ? '700' : '500';
    });
    dots.forEach(function(dot, i) {
      dot.classList.toggle('is-active', i === activeIndex);
      dot.innerHTML = i === activeIndex ? ACTIVE_DOT_SVG : INACTIVE_DOT_SVG;
    });
    if (prevBtn) {
      prevBtn.disabled = activeIndex === 0;
      prevBtn.style.color = activeIndex === 0 ? '#ccc' : '#111';
      prevBtn.style.cursor = activeIndex === 0 ? 'default' : 'pointer';
    }
    if (nextBtn) {
      nextBtn.disabled = activeIndex === slides.length - 1;
      nextBtn.style.color = activeIndex === slides.length - 1 ? '#ccc' : '#111';
      nextBtn.style.cursor = activeIndex === slides.length - 1 ? 'default' : 'pointer';
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

  tabs.forEach(function(tab, i) {
    tab.addEventListener('click', function() { goTo(i); resetAuto(); });
  });
  dots.forEach(function(dot, i) {
    dot.addEventListener('click', function() { goTo(i); resetAuto(); });
  });
  if (prevBtn) {
    prevBtn.addEventListener('click', function() { prev(); resetAuto(); });
  }
  if (nextBtn) {
    nextBtn.addEventListener('click', function() { next(); resetAuto(); });
  }

  viewport.addEventListener('mouseenter', stopAuto);
  viewport.addEventListener('mouseleave', startAuto);

  render();
  startAuto();
})();
