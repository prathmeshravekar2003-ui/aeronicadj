(function() {
  var heroSection = document.getElementById('hero');
  if (!heroSection) return;

  var slides = JSON.parse(heroSection.getAttribute('data-hero-slides') || '[]');
  if (slides.length === 0) return;

  var activeIndex = 0;
  var AUTOPLAY_DELAY = 6000;
  var isPaused = false;
  var autoplayTimer = null;
  var progressTimer = null;

  // Elements
  var bgCurrent    = document.getElementById('heroBgCurrent');
  var bgNext       = document.getElementById('heroBgNext');
  var bgImgCurrent = document.getElementById('heroBgImgCurrent');
  var bgImgNext    = document.getElementById('heroBgImgNext');
  var titleEl      = document.getElementById('heroTitle');
  var descEl       = document.getElementById('heroDesc');
  var ctaEl        = document.getElementById('heroCta');
  var ctaLabelEl   = document.getElementById('heroCtaLabel');
  var prevBtn      = document.getElementById('heroPrev');
  var nextBtn      = document.getElementById('heroNext');
  var controlsEl   = document.getElementById('heroControls');
  var controlBtns  = controlsEl ? Array.from(controlsEl.querySelectorAll('.hero-control-item')) : [];

  function preloadImage(src) {
    var img = new Image();
    img.src = src;
  }

  // Pre-load all slide images
  slides.forEach(function(s) { preloadImage(s.image); });

  function stopProgress() {
    if (progressTimer) { clearTimeout(progressTimer); progressTimer = null; }
    controlBtns.forEach(function(btn, i) {
      var fill = btn.querySelector('.hero-control-fill');
      if (fill) {
        fill.style.transition = 'none';
        fill.style.transform = 'scaleX(0)';
      }
      btn.classList.remove('is-active');
    });
  }

  function startProgress(index) {
    stopProgress();
    var btn = controlBtns[index];
    if (!btn) return;
    btn.classList.add('is-active');
    var fill = btn.querySelector('.hero-control-fill');
    if (fill) {
      // Force reflow so the transition starts from scaleX(0)
      fill.style.transition = 'none';
      fill.style.transform = 'scaleX(0)';
      void fill.offsetWidth;
      fill.style.transition = 'transform ' + (AUTOPLAY_DELAY / 1000) + 's linear';
      fill.style.transform = 'scaleX(1)';
    }
  }

  function goTo(newIndex) {
    if (newIndex === activeIndex) return;
    var slide = slides[newIndex];
    if (!slide) return;

    // Cross-fade background
    bgImgNext.src = slide.image;
    bgImgNext.alt = slide.title;
    bgNext.style.opacity = '0';

    // Brief delay to let browser paint the src swap
    requestAnimationFrame(function() {
      requestAnimationFrame(function() {
        bgNext.style.opacity = '1';
        bgCurrent.style.opacity = '0';

        setTimeout(function() {
          // Swap layers
          bgImgCurrent.src = slide.image;
          bgImgCurrent.alt = slide.title;
          bgCurrent.style.transition = 'none';
          bgCurrent.style.opacity = '1';
          bgNext.style.transition = 'none';
          bgNext.style.opacity = '0';
          // Re-enable transitions for next cycle
          setTimeout(function() {
            bgCurrent.style.transition = 'opacity 0.7s ease';
            bgNext.style.transition = 'opacity 0.7s ease';
          }, 20);
        }, 750);
      });
    });

    // Fade out text
    titleEl.style.opacity = '0';
    descEl.style.opacity = '0';
    ctaEl.style.opacity = '0';

    setTimeout(function() {
      titleEl.textContent = slide.title;
      descEl.textContent = slide.description;
      ctaLabelEl.textContent = slide.ctaLabel;
      ctaEl.href = slide.ctaHref;
      titleEl.style.opacity = '1';
      descEl.style.opacity = '1';
      ctaEl.style.opacity = '1';
    }, 350);

    activeIndex = newIndex;
    startProgress(activeIndex);
    resetAutoplay();
  }

  function next() { goTo((activeIndex + 1) % slides.length); }
  function prev() { goTo((activeIndex - 1 + slides.length) % slides.length); }

  function resetAutoplay() {
    if (autoplayTimer) clearTimeout(autoplayTimer);
    if (!isPaused) {
      autoplayTimer = setTimeout(function() { next(); }, AUTOPLAY_DELAY);
    }
  }

  // Wire up arrows
  if (prevBtn) {
    prevBtn.addEventListener('click', function() { prev(); });
    prevBtn.addEventListener('mouseenter', function() { isPaused = true; if (autoplayTimer) clearTimeout(autoplayTimer); });
    prevBtn.addEventListener('mouseleave', function() { isPaused = false; resetAutoplay(); });
  }
  if (nextBtn) {
    nextBtn.addEventListener('click', function() { next(); });
    nextBtn.addEventListener('mouseenter', function() { isPaused = true; if (autoplayTimer) clearTimeout(autoplayTimer); });
    nextBtn.addEventListener('mouseleave', function() { isPaused = false; resetAutoplay(); });
  }

  // Wire up control dots
  controlBtns.forEach(function(btn) {
    var idx = parseInt(btn.getAttribute('data-slide'), 10);
    btn.addEventListener('click', function() { if (idx !== activeIndex) goTo(idx); });
    btn.addEventListener('mouseenter', function() { isPaused = true; if (autoplayTimer) clearTimeout(autoplayTimer); });
    btn.addEventListener('mouseleave', function() { isPaused = false; resetAutoplay(); });
  });

  // Init
  startProgress(0);
  resetAutoplay();
})();
