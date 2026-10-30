document.addEventListener("DOMContentLoaded", () => {

    const carousel = document.querySelector(".project-carousel");

    if (!carousel) {
        return;
    }

    const slidesContainer = carousel.querySelector(".project-slides");
    const slides = carousel.querySelectorAll(".project-slide");
    const indicators = carousel.querySelectorAll(".carousel-indicator");

    const lightbox = document.querySelector(".image-lightbox");
    const lightboxImage = document.querySelector(".lightbox-image");
    const lightboxClose = document.querySelector(".lightbox-close");

    let currentSlide = 0;
    let startX = 0;
    let isDragging = false;

    const gap = 30;

    function getVisibleSlides() {
        return window.innerWidth <= 768 ? 1 : 3;
    }

    function getMaxSlide() {
        return Math.max(0, slides.length - getVisibleSlides());
    }

    function showSlide(index) {

        const maxSlide = getMaxSlide();

        index = Math.max(0, Math.min(index, maxSlide));

        const slideWidth = slides[0].getBoundingClientRect().width;

        slidesContainer.style.transform =
            `translateX(-${index * (slideWidth + gap)}px)`;

        indicators.forEach((indicator, i) => {
            indicator.classList.toggle("active", i === index);
        });

        currentSlide = index;

        updateIndicators();
    }

    function updateIndicators() {
    const maxSlide = getMaxSlide();

    indicators.forEach((indicator, index) => {
        indicator.style.display = index <= maxSlide ? "block" : "none";
    });
}

    /* =========================
       PUNTOS
       ========================= */

    indicators.forEach((indicator, index) => {

        indicator.addEventListener("click", () => {
            showSlide(index);
        });

    });


    /* =========================
       RATÓN
       ========================= */

    slidesContainer.addEventListener("mousedown", (event) => {

        isDragging = true;
        startX = event.clientX;

        slidesContainer.classList.add("dragging");

    });


    document.addEventListener("mouseup", (event) => {

        if (!isDragging) {
            return;
        }

        isDragging = false;

        slidesContainer.classList.remove("dragging");

        const distance = event.clientX - startX;

        if (Math.abs(distance) < 50) {
            return;
        }

        if (distance < 0) {
            showSlide(currentSlide + 1);
        } else {
            showSlide(currentSlide - 1);
        }

    });


    /* =========================
       TOUCH / MÓVIL
       ========================= */

    slidesContainer.addEventListener("touchstart", (event) => {

        startX = event.touches[0].clientX;

    }, { passive: true });


    slidesContainer.addEventListener("touchend", (event) => {

        const endX = event.changedTouches[0].clientX;
        const distance = endX - startX;

        if (Math.abs(distance) < 50) {
            return;
        }

        if (distance < 0) {
            showSlide(currentSlide + 1);
        } else {
            showSlide(currentSlide - 1);
        }

    }, { passive: true });


    /* =========================
       TECLADO
       ========================= */

    document.addEventListener("keydown", (event) => {

        /*
         * Si el lightbox está abierto,
         * Escape lo cierra.
         */

        if (lightbox.classList.contains("active")) {
            return;
        }

        if (event.key === "ArrowRight") {

            event.preventDefault();
            showSlide(currentSlide + 1);

        }

        if (event.key === "ArrowLeft") {

            event.preventDefault();
            showSlide(currentSlide - 1);

        }

    });


    /* =========================
       LIGHTBOX
       ========================= */

    const imageButtons =
        carousel.querySelectorAll(".project-image-button");


    imageButtons.forEach((button) => {

        button.addEventListener("click", () => {

            /*
             * Si acabamos de arrastrar,
             * no abrimos el zoom.
             */

            if (isDragging) {
                return;
            }

            const image = button.querySelector("img");

            if (!image) {
                return;
            }

            lightboxImage.src = image.src;
            lightboxImage.alt = image.alt;

            lightbox.classList.add("active");
            lightbox.setAttribute("aria-hidden", "false");

        });

    });


    function closeLightbox() {

        lightbox.classList.remove("active");
        lightbox.setAttribute("aria-hidden", "true");

        lightboxImage.src = "";

    }


    lightboxClose.addEventListener("click", closeLightbox);


    lightbox.addEventListener("click", (event) => {

        if (event.target === lightbox) {
            closeLightbox();
        }

    });


    document.addEventListener("keydown", (event) => {

        if (event.key === "Escape") {
            closeLightbox();
        }

    });


    /* =========================
       REDIMENSIONADO
       ========================= */

    window.addEventListener("resize", () => {
        showSlide(currentSlide);
    });


    /* Posición inicial */

    showSlide(0);

});