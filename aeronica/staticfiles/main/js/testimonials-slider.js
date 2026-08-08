(function() {
  var section = document.getElementById('testimonials');
  if (!section) return;

  var slides = Array.from(section.querySelectorAll('.testimonial-slide'));
  var dots = Array.from(section.querySelectorAll('.testimonial-dot'));
  var prevBtn = section.querySelector('.testimonial-prev');
  var nextBtn = section.querySelector('.testimonial-next');
  var nameEl = document.getElementById('testimonialName');
  var roleEl = document.getElementById('testimonialRole');

  function decodeHTML(html) {
    var txt = document.createElement('textarea');
    txt.innerHTML = html;
    return txt.value;
  }

  var data = null;
  try {
    var el = section.querySelector('.testimonials-data');
    if (el) {
      var raw = el.textContent || '';
      // Decode html entities in case django autoescapes inside script tags
      if (raw.indexOf('&') !== -1) {
        raw = decodeHTML(raw);
      }
      data = JSON.parse(raw || '[]');
    }
  } catch (e) {
    console.error('Error parsing testimonials JSON:', e);
    data = null;
  }

  if (slides.length === 0) return;

  var ACTIVE_DOT_SVG = '<svg viewBox="0 0 12 12" fill="currentColor" width="14" height="14">' +
    '<circle cx="6" cy="6" r="1.6" fill="#fff"></circle>' +
    '<circle cx="6" cy="6" r="0.7" fill="#fff" opacity="0.3"></circle></svg>';
  var INACTIVE_DOT_SVG = '<svg viewBox="0 0 12 12" fill="currentColor" width="14" height="14">' +
    '<circle cx="6" cy="6" r="0.7" fill="#fff" opacity="0.25"></circle></svg>';

  var activeIndex = 0;
  var AUTOPLAY_DELAY = 5000;
  var timer = null;
  var hoverPauses = 0;
  var transitioning = false;

  // Initialize transition styling
  slides.forEach(function(slide, i) {
    slide.style.transition = 'opacity 0.4s ease';
    if (i === activeIndex) {
      slide.style.display = 'flex';
      slide.style.opacity = '1';
    } else {
      slide.style.display = 'none';
      slide.style.opacity = '0';
    }
  });
  if (nameEl) {
    nameEl.style.transition = 'opacity 0.4s ease';
    nameEl.style.opacity = '1';
  }
  if (roleEl) {
    roleEl.style.transition = 'opacity 0.4s ease';
    roleEl.style.opacity = '1';
  }

  function updateDots() {
    dots.forEach(function(dot, i) {
      dot.classList.toggle('is-active', i === activeIndex);
      dot.innerHTML = i === activeIndex ? ACTIVE_DOT_SVG : INACTIVE_DOT_SVG;
    });
  }

  function goTo(index) {
    if (index < 0 || index >= slides.length || index === activeIndex || transitioning) return;

    transitioning = true;
    var currentSlide = slides[activeIndex];
    var nextSlide = slides[index];

    // Fade out current slide and texts
    if (currentSlide) currentSlide.style.opacity = '0';
    if (nameEl) nameEl.style.opacity = '0';
    if (roleEl) roleEl.style.opacity = '0';

    setTimeout(function() {
      if (currentSlide) currentSlide.style.display = 'none';

      activeIndex = index;
      updateDots();

      // Update text content
      if (data && data[activeIndex]) {
        if (nameEl) nameEl.textContent = data[activeIndex].author;
        if (roleEl) roleEl.textContent = data[activeIndex].title;
      }

      // Prepare next slide
      nextSlide.style.display = 'flex';
      nextSlide.style.opacity = '0';

      // Force reflow
      void nextSlide.offsetWidth;

      // Fade in next slide and texts
      nextSlide.style.opacity = '1';
      if (nameEl) nameEl.style.opacity = '1';
      if (roleEl) roleEl.style.opacity = '1';

      transitioning = false;
    }, 400); // match CSS transition duration
  }

  function next() {
    goTo((activeIndex + 1) % slides.length);
  }

  function prev() {
    goTo((activeIndex - 1 + slides.length) % slides.length);
  }

  function startAuto() {
    stopAuto();
    if (hoverPauses === 0) {
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

  // Hover pauses autoplay
  section.addEventListener('mouseenter', pause);
  section.addEventListener('mouseleave', unpause);

  dots.forEach(function(dot, i) {
    dot.addEventListener('click', function() { goTo(i); resetAuto(); });
  });
  if (prevBtn) {
    prevBtn.addEventListener('click', function() { prev(); resetAuto(); });
  }
  if (nextBtn) {
    nextBtn.addEventListener('click', function() { next(); resetAuto(); });
  }

  updateDots();
  startAuto();
})();