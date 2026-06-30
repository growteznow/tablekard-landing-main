
      document.addEventListener("DOMContentLoaded", () => {
        const phone = document.getElementById('anim-phone');

        const observer = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              // Slide phone up to align top bezel with the highest cards
              phone.style.bottom = "50px";
              observer.unobserve(entry.target);
            }
          });
        }, { threshold: 0.3 });

        observer.observe(document.getElementById('features'));
      });
    