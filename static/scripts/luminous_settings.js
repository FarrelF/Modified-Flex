new LuminousGallery(
    document.querySelectorAll(".luminous-image-gallery"),
    {
      arrowNavigation: true
    },
    {
      caption: function(trigger) {
        return trigger.querySelector("img").getAttribute("alt");
      }
    }
);
