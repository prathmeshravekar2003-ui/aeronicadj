/**
 * Aeronica Global Animations & Interactivity Runtime
 * Supports: Navbar Scroll & Interaction, Custom Cursor, Preloader/Loading Screen, 
 *           3D Card Tilt, Stats Number Ticker, Smooth Scroll (Lenis), and Scroll Entrance Reveal.
 */
(function() {
  'use strict';

  // 1. DYNAMIC STYLES FOR REVEAL ANIMATIONS AND CURSOR OVERRIDES
  var style = document.createElement('style');
  style.textContent = `
    /* Custom Cursor overrides/fallbacks */
    @media (pointer: coarse) {
      .custom-cursor-dot, .custom-cursor-ring {
        display: none !important;
      }
      body {
        cursor: auto !important;
      }
    }
    
    /* Scroll Reveal Initial States */
    .scroll-reveal {
      opacity: 0;
      transform: translateY(30px);
      transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform, opacity;
    }
    .scroll-reveal.reveal-active {
      opacity: 1;
      transform: translateY(0);
    }
    
    /* Preloader CSS Fallbacks */
    .loading-screen {
      position: fixed;
      inset: 0;
      background: #21389A;
      z-index: 99999;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: opacity 0.5s ease, visibility 0.5s ease;
    }
    .loading-screen.gone {
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
    }
    .loading-logo-container {
      transition: transform 0.5s cubic-bezier(0.77, 0, 0.175, 1), opacity 0.5s cubic-bezier(0.77, 0, 0.175, 1);
    }
    .loading-logo-container.logo-exit {
      transform: scale(0.85);
      opacity: 0;
    }
  `;
  document.head.appendChild(style);

  // Helper: Detect Touch Devices
  function isTouchDevice() {
    return ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);
  }

  // 2. RUNTIME INITS AFTER DOM LOADS
  document.addEventListener('DOMContentLoaded', function() {
    initPreloader();
    initNavbar();
    if (!isTouchDevice()) {
      // initCustomCursor(); // Disabled custom cursor to restore default pointer behavior on links/buttons
      initCardTilt();
    }
    initBackToTop();
    initStatsTicker();
    initScrollReveal();
  });

  // ─── A. PRELOADER / LOADING SCREEN ──────────────────────────────────────
  function initPreloader() {
    var loader = document.getElementById('loadingScreen');
    if (!loader) {
      loader = document.createElement('div');
      loader.id = 'loadingScreen';
      loader.className = 'loading-screen';
      
      var container = document.createElement('div');
      container.className = 'loading-logo-container';
      
      var img = document.createElement('img');
      img.className = 'loading-logo';
      img.alt = 'Aeronica Logo';
      var relPrefix = getRelativePrefix();
      img.src = relPrefix + 'img/aeronica-logo.png';
      img.style.maxWidth = '240px';
      
      container.appendChild(img);
      loader.appendChild(container);
      document.body.insertBefore(loader, document.body.firstChild);
    }

    var logoContainer = loader.querySelector('.loading-logo-container');

    setTimeout(function() {
      if (logoContainer) {
        logoContainer.classList.add('logo-exit');
      }
    }, 2000);

    setTimeout(function() {
      loader.classList.add('gone');
      document.body.classList.add('preloader-finished');
    }, 2600);
  }

  // ─── B. NAVBAR SCROLL + INTERACTION ─────────────────────────────────────
  function initNavbar() {
    var navbar   = document.getElementById('navbar');
    var toggle   = navbar ? navbar.querySelector('.navbar-toggle') : null;
    var overlay  = document.getElementById('navOverlay');

    // 1. Scroll → is-scrolled class
    function onScroll() {
      if (!navbar) return;
      var threshold = window.innerHeight * 0.7;
      if (window.scrollY > threshold) {
        navbar.classList.add('is-scrolled');
      } else {
        navbar.classList.remove('is-scrolled');
      }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll(); // Run once on load in case page is already scrolled

    // 2. Mobile hamburger toggle
    if (toggle && overlay && navbar) {
      toggle.addEventListener('click', function() {
        var isOpen = overlay.classList.toggle('is-open');
        toggle.classList.toggle('is-active', isOpen);
        navbar.classList.toggle('overlay-open', isOpen);

        if (isOpen) {
          var scrollY = window.scrollY;
          document.body.style.position = 'fixed';
          document.body.style.top = '-' + scrollY + 'px';
          document.body.style.left = '0';
          document.body.style.right = '0';
          document.body.style.overflow = 'hidden';
          document.body.dataset.scrollY = scrollY;
        } else {
          var savedY = parseInt(document.body.dataset.scrollY || '0', 10);
          document.body.style.position = '';
          document.body.style.top = '';
          document.body.style.left = '';
          document.body.style.right = '';
          document.body.style.overflow = '';
          window.scrollTo(0, savedY);
        }
      });
    }

    // 3. Mobile accordion
    if (overlay) {
      var groupTriggers = Array.from(overlay.querySelectorAll('.nav-overlay-group-trigger'));
      groupTriggers.forEach(function(btn) {
        btn.addEventListener('click', function() {
          var group    = btn.closest('.nav-overlay-group');
          var sublinks = group ? group.querySelector('.nav-overlay-sublinks') : null;
          if (!sublinks) return;
          var isNowOpen = sublinks.classList.toggle('is-open');
          btn.classList.toggle('is-open', isNowOpen);
          // Close sibling groups
          groupTriggers.forEach(function(other) {
            if (other === btn) return;
            var otherGroup    = other.closest('.nav-overlay-group');
            var otherSublinks = otherGroup ? otherGroup.querySelector('.nav-overlay-sublinks') : null;
            if (otherSublinks) otherSublinks.classList.remove('is-open');
            other.classList.remove('is-open');
          });
        });
      });
    }

    // 4. Desktop dropdown hover
    if (navbar) {
      var dropdowns = Array.from(navbar.querySelectorAll('.navbar-dropdown'));
      dropdowns.forEach(function(dd) {
        var menu = dd.querySelector('.navbar-dropdown-menu');
        if (!menu) return;

        dd.addEventListener('mouseenter', function() {
          menu.classList.add('is-open');
        });
        dd.addEventListener('mouseleave', function() {
          menu.classList.remove('is-open');
        });
      });
    }
  }

  // ─── C. CUSTOM CURSOR ───────────────────────────────────────────────────
  function initCustomCursor() {
    var cursorDot = document.getElementById('custom-cursor-dot');
    var cursorRing = document.getElementById('custom-cursor-ring');

    if (!cursorDot) {
      cursorDot = document.createElement('div');
      cursorDot.id = 'custom-cursor-dot';
      cursorDot.className = 'custom-cursor-dot';
      cursorDot.innerHTML = `
        <svg class="cursor-dot-arrow" viewBox="0 0 24 24" fill="currentColor">
          <circle cx="5" cy="2" r="1.3"></circle>
          <circle cx="8.5" cy="4.5" r="1.3"></circle>
          <circle cx="12" cy="7" r="1.3"></circle>
          <circle cx="15.5" cy="9.5" r="1.3"></circle>
          <circle cx="19" cy="12" r="1.3"></circle>
          <circle cx="15.5" cy="14.5" r="1.3"></circle>
          <circle cx="12" cy="17" r="1.3"></circle>
          <circle cx="8.5" cy="19.5" r="1.3"></circle>
          <circle cx="5" cy="22" r="1.3"></circle>
        </svg>
      `;
      document.body.appendChild(cursorDot);
    }
    if (!cursorRing) {
      cursorRing = document.createElement('div');
      cursorRing.id = 'custom-cursor-ring';
      cursorRing.className = 'custom-cursor-ring';
      document.body.appendChild(cursorRing);
    }

    document.body.style.cursor = 'none';
    var styleOverride = document.createElement('style');
    styleOverride.textContent = 'input, textarea, select, [contenteditable], a, button { cursor: none !important; }';
    document.head.appendChild(styleOverride);

    var mouse = { x: -100, y: -100 };
    var dot = { x: -100, y: -100 };
    var ring = { x: -100, y: -100 };
    var hScrollRef = { current: null };
    var lastCheck = 0;
    var lastEl = null;

    window.addEventListener('mousemove', function(e) {
      mouse.x = e.clientX;
      mouse.y = e.clientY;
    });

    function getLuminance(r, g, b) {
      return r * 0.299 + g * 0.587 + b * 0.114;
    }
    
    function hasDarkBackground(el) {
      var cs = window.getComputedStyle(el);
      var bgColor = cs.backgroundColor;
      if (bgColor && bgColor !== 'rgba(0, 0, 0, 0)' && bgColor !== 'transparent') {
        var m = bgColor.match(/\d+/g);
        if (m && m.length >= 3) {
          var r = Number(m[0]), g = Number(m[1]), b = Number(m[2]);
          if (getLuminance(r, g, b) <= 140) return true;
        }
      }
      var bgImage = cs.backgroundImage;
      if (bgImage && bgImage !== 'none') {
        if (!bgImage.startsWith('linear-gradient') && !bgImage.startsWith('radial-gradient')) return true;
        var matches = bgImage.matchAll(/rgb\((\d+),\s*(\d+),\s*(\d+)\)/g);
        for (var match of Array.from(matches)) {
          if (getLuminance(+match[1], +match[2], +match[3]) <= 140) return true;
        }
      }
      return false;
    }

    function isDarkBackground(x, y) {
      var el = document.elementFromPoint(x, y);
      if (!el) return false;
      var current = el;
      while (current && current !== document.body) {
        if (current.tagName === 'IMG') return true;
        if (hasDarkBackground(current)) return true;
        var cs = window.getComputedStyle(current);
        if (cs.color === 'rgb(255, 255, 255)' && cs.backgroundColor === 'rgba(0, 0, 0, 0)') return true;
        current = current.parentElement;
      }
      return false;
    }

    window.addEventListener('mouseover', function(e) {
      var target = e.target;
      var isClickable = target.closest('a, button, [role=button], input, select, textarea, label');
      document.documentElement.classList.toggle('cursor-on-link', !!isClickable);

      var isText = target.closest('p, h1, h2, h3, h4, h5, h6, li, blockquote, td, th, figcaption, cite, em, strong, label');
      document.documentElement.classList.toggle('cursor-on-text', !!isText);

      var hScroll = target.closest('.horizontal-scroll');
      hScrollRef.current = hScroll;
      document.documentElement.classList.toggle('cursor-h-scroll', !!hScroll);
    }, true);

    function updateCursor() {
      var easeDot = 0.35;
      var easeRing = 0.12;

      dot.x += (mouse.x - dot.x) * easeDot;
      dot.y += (mouse.y - dot.y) * easeDot;
      ring.x += (mouse.x - ring.x) * easeRing;
      ring.y += (mouse.y - ring.y) * easeRing;

      cursorDot.style.transform = 'translate(' + dot.x + 'px, ' + dot.y + 'px)';
      cursorRing.style.transform = 'translate(' + ring.x + 'px, ' + ring.y + 'px)';

      if (hScrollRef.current) {
        var rect = hScrollRef.current.getBoundingClientRect();
        var midX = rect.left + rect.width / 2;
        var isLeft = mouse.x < midX;
        document.documentElement.classList.toggle('cursor-h-scroll-left', isLeft);
        document.documentElement.classList.toggle('cursor-h-scroll-right', !isLeft);
      }

      var now = performance.now();
      if (now - lastCheck > 50) {
        lastCheck = now;
        var under = document.elementFromPoint(mouse.x, mouse.y);
        if (under !== lastEl) {
          lastEl = under;
          var dark = isDarkBackground(mouse.x, mouse.y);
          document.documentElement.classList.toggle('cursor-dark-bg', dark);
        }
      }

      requestAnimationFrame(updateCursor);
    }
    requestAnimationFrame(updateCursor);
  }

  // ─── D. 3D CARD TILT EFFECT ─────────────────────────────────────────────
  function initCardTilt() {
    var TILT_SELECTOR = '.project-card, .industry-card, .stat-box, .process-step, .news-card, .product-card';
    var tiltRAF = 0;
    var currentCard = null;

    function applyTilt(e) {
      if (!currentCard) return;
      var rect = currentCard.getBoundingClientRect();
      var x = e.clientX - rect.left;
      var y = e.clientY - rect.top;
      var rotateX = ((y - rect.height / 2) / (rect.height / 2)) * -6;
      var rotateY = ((x - rect.width / 2) / (rect.width / 2)) * 6;
      cancelAnimationFrame(tiltRAF);
      tiltRAF = requestAnimationFrame(function() {
        if (currentCard) {
          currentCard.style.transform = 'perspective(1200px) rotateX(' + rotateX + 'deg) rotateY(' + rotateY + 'deg) scale3d(1.02, 1.02, 1.02)';
        }
      });
    }

    function resetTilt() {
      if (!currentCard) return;
      var el = currentCard;
      currentCard = null;
      document.removeEventListener('mousemove', applyTilt);
      cancelAnimationFrame(tiltRAF);
      tiltRAF = requestAnimationFrame(function() {
        el.style.transform = '';
      });
    }

    document.addEventListener('mouseover', function(e) {
      var card = e.target.closest(TILT_SELECTOR);
      if (card && card !== currentCard) {
        if (currentCard) resetTilt();
        currentCard = card;
        document.addEventListener('mousemove', applyTilt, { passive: true });
      }
    }, { passive: true });

    document.addEventListener('mouseout', function(e) {
      if (currentCard && !currentCard.contains(e.relatedTarget)) {
        resetTilt();
      }
    }, { passive: true });
  }

  // ─── E. BACK TO TOP BUTTON ──────────────────────────────────────────────
  function initBackToTop() {
    var btn = document.getElementById('backToTop');
    if (!btn) {
      btn = document.createElement('button');
      btn.id = 'backToTop';
      btn.className = 'back-to-top';
      btn.setAttribute('aria-label', 'Back to top');
      btn.innerHTML = `
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="width:16px;height:16px;">
          <path d="m18 15-6-6-6 6"/>
        </svg>
      `;
      document.body.appendChild(btn);
    }

    window.addEventListener('scroll', function() {
      if (window.scrollY > window.innerHeight * 0.5) {
        btn.classList.add('is-visible');
      } else {
        btn.classList.remove('is-visible');
      }
    }, { passive: true });

    btn.addEventListener('click', function() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ─── F. STATS NUMBER TICKER ─────────────────────────────────────────────
  function initStatsTicker() {
    var statsGrid = document.querySelector('.stats-4col');
    if (!statsGrid) return;

    var elements = Array.from(statsGrid.querySelectorAll('span[style*="font-size"] span, span.stat-count'));
    if (elements.length === 0) {
      var cols = statsGrid.querySelectorAll('.stats-4col > div');
      cols.forEach(function(col) {
        var numContainer = col.querySelector('span');
        if (numContainer) {
          var txt = numContainer.innerText.trim();
          var val = parseInt(txt.replace(/[^0-9]/g, ''), 10);
          if (!isNaN(val)) {
            var suffix = txt.replace(/[0-9]/g, '');
            numContainer.innerHTML = '<span class="stat-count" data-target="' + val + '">0</span>' + suffix;
            var el = numContainer.querySelector('.stat-count');
            if (el) elements.push(el);
          }
        }
      });
    }

    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          elements.forEach(function(el) {
            var target = parseInt(el.getAttribute('data-target') || el.innerText.replace(/[^0-9]/g, ''), 10);
            if (isNaN(target)) return;
            el.setAttribute('data-target', target);
            animateNumber(el, target);
          });
          observer.disconnect();
        }
      });
    }, { threshold: 0.2 });

    observer.observe(statsGrid);

    function animateNumber(el, target) {
      var start = 0;
      var duration = 2200;
      var startTime = performance.now();
      
      function update(now) {
        var progress = Math.min((now - startTime) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        el.innerText = Math.round(eased * target).toLocaleString();
        if (progress < 1) {
          requestAnimationFrame(update);
        } else {
          el.innerText = target.toLocaleString();
        }
      }
      requestAnimationFrame(update);
    }
  }

  // ─── G. SCROLL ENTRANCE REVEAL (REPLACES FRAMER MOTION IN VIEW) ──────────
  function initScrollReveal() {
    var selectors = [
      '.stats-4col > div',
      '.project-card',
      '.industry-card',
      '.process-step',
      '.news-card',
      '.testimonial-card',
      '.product-card',
      'section h2',
      '.cta-container',
      '.services-grid > div',
      '.tech-spec-grid > div'
    ];

    var elements = document.querySelectorAll(selectors.join(', '));
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('reveal-active');
          observer.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: '0px 0px -60px 0px',
      threshold: 0.1
    });

    elements.forEach(function(el) {
      if (el.classList.contains('reveal-active')) return;
      el.classList.add('scroll-reveal');
      observer.observe(el);
    });
  }


  // ─── HELPER: CALCULATE RELATIVE PREFIX ──────────────────────────────────
  function getRelativePrefix() {
    var currentScript = document.currentScript;
    if (currentScript) {
      var src = currentScript.getAttribute('src') || '';
      // Django static: /static/main/js/global-animations.js
      var djangoIdx = src.indexOf('/static/main/js/');
      if (djangoIdx !== -1) {
        return src.substring(0, djangoIdx) + '/static/main/';
      }
      // Legacy static site: assets/js/global-animations.js
      var legacyIdx = src.indexOf('assets/js/');
      if (legacyIdx !== -1) {
        return src.substring(0, legacyIdx) + 'assets/';
      }
    }
    // Absolute fallback for Django
    return '/static/main/';
  }
})();
