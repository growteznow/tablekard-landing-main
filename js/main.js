document.addEventListener("DOMContentLoaded", () => {
  const video = document.getElementById('bg-video');
  if (video) {
    video.playbackRate = 0.6;
  }
  const preloader = document.getElementById('site-preloader');
  if (preloader) {
    let isLoaded = false;
    const hidePreloader = () => {
      if (!isLoaded) {
        isLoaded = true;
        preloader.classList.add('preloader--hidden');
        if (video) {
          video.classList.add('video-loaded');
          const previewSec = document.querySelector('.video-preview-section');
          if (previewSec) {
            previewSec.classList.add('section-loaded');
          }
        }
      }
    };
    if (video) {
      video.addEventListener('playing', hidePreloader);
      video.addEventListener('canplaythrough', hidePreloader);
      if (video.readyState >= 3) {
        hidePreloader();
      }
    } else {
      hidePreloader();
    }
    // Safety timeout fallback
    setTimeout(hidePreloader, 4000);
  }

  const header = document.querySelector(".navbar");
  const featureCards = document.querySelectorAll(".feature-card");

  window.addEventListener("scroll", () => {
    if (header) {
      header.classList.toggle("scrolled", window.scrollY > 20);
    }
  });

  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", (e) => {
      const targetId = anchor.getAttribute("href");
      if (targetId === "#") return;
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = "1";
          entry.target.style.transform = "translateY(0)";
        }
      });
    },
    { threshold: 0.15 }
  );

  featureCards.forEach((card, i) => {
    card.style.opacity = "0";
    card.style.transform = "translateY(24px)";
    card.style.transition = `opacity 0.5s ease ${i * 0.1}s, transform 0.5s ease ${i * 0.1}s`;
    observer.observe(card);
  });

  const countEl = document.querySelector(".partners__count");
  if (countEl) {
    const target = 200;
    const suffix = "+";

    const countObserver = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          animateCount(countEl, target, suffix);
          countObserver.disconnect();
        }
      },
      { threshold: 0.5 }
    );
    countObserver.observe(countEl);
  }

  function animateCount(el, target, suffix) {
    const duration = 2000;
    const start = performance.now();

    function tick(now) {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.floor(eased * target);
      el.textContent = current.toLocaleString("en-IN") + suffix;
      if (progress < 1) requestAnimationFrame(tick);
    }

    requestAnimationFrame(tick);
  }

  const qrCanvas = document.getElementById("qr-code");
  if (qrCanvas) {
    drawQRPlaceholder(qrCanvas);
  }

  function drawQRPlaceholder(canvas) {
    const ctx = canvas.getContext("2d");
    const size = 160;
    const cells = 21;
    const cellSize = size / cells;

    canvas.width = size;
    canvas.height = size;

    ctx.fillStyle = "#ffffff";
    ctx.fillRect(0, 0, size, size);

    const pattern = generateQRPattern(cells);

    for (let row = 0; row < cells; row++) {
      for (let col = 0; col < cells; col++) {
        if (pattern[row][col]) {
          ctx.fillStyle = "#1c1c1c";
          ctx.fillRect(col * cellSize, row * cellSize, cellSize, cellSize);
        }
      }
    }

    drawFinder(ctx, 0, 0, cellSize);
    drawFinder(ctx, (cells - 7) * cellSize, 0, cellSize);
    drawFinder(ctx, 0, (cells - 7) * cellSize, cellSize);

    const logoSize = cellSize * 5;
    const logoPos = (size - logoSize) / 2;
    ctx.fillStyle = "#ffffff";
    ctx.fillRect(logoPos, logoPos, logoSize, logoSize);
    ctx.fillStyle = "#7B1E34";
    ctx.font = `bold ${cellSize * 2.5}px Arial`;
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText("T", size / 2, size / 2);
  }

  function drawFinder(ctx, x, y, cellSize) {
    ctx.fillStyle = "#1c1c1c";
    ctx.fillRect(x, y, cellSize * 7, cellSize * 7);
    ctx.fillStyle = "#ffffff";
    ctx.fillRect(x + cellSize, y + cellSize, cellSize * 5, cellSize * 5);
    ctx.fillStyle = "#1c1c1c";
    ctx.fillRect(x + cellSize * 2, y + cellSize * 2, cellSize * 3, cellSize * 3);
  }

  function generateQRPattern(cells) {
    const pattern = Array.from({ length: cells }, () =>
      Array(cells).fill(false)
    );

    for (let row = 0; row < cells; row++) {
      for (let col = 0; col < cells; col++) {
        if (isFinderArea(row, col, cells)) continue;
        pattern[row][col] = ((row * 7 + col * 13) % 5) < 2;
      }
    }

    return pattern;
  }

  function isFinderArea(row, col, cells) {
    if (row < 8 && col < 8) return true;
    if (row < 8 && col >= cells - 8) return true;
    if (row >= cells - 8 && col < 8) return true;
    return false;
  }
});
