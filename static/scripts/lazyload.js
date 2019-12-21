(function() {
    if ("loading" in HTMLImageElement.prototype) {
      var lazyEls = document.querySelectorAll("[loading=lazy]");
      lazyEls.forEach(function(lazyEl) {
        lazyEl.setAttribute(
          "src",
          lazyEl.getAttribute("data-src")
        );
      });
    } else {
      var script = document.createElement("script");
      script.async = true;
      script.src =
        "https://cdn.statically.io/gh/verlok/lazyload/12.3.0/dist/lazyload.min.js";
      window.lazyLoadOptions = {
        elements_selector: "[loading=lazy]"
      };
      document.body.appendChild(script);
    }
  })();
