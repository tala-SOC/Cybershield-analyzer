
document.addEventListener("DOMContentLoaded", () => {

    // 1. Animate security score numbers
    const counters = document.querySelectorAll(".count-up");

    counters.forEach(counter => {
        const target = Number(counter.dataset.count);

        if (!Number.isFinite(target)) return;

        const duration = 1400;
        const startTime = performance.now();

        function updateCounter(currentTime) {
            const progress = Math.min(
                (currentTime - startTime) / duration,
                1
            );

            const eased = 1 - Math.pow(1 - progress, 3);

            counter.textContent = Math.round(target * eased);

            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            }
        }

        requestAnimationFrame(updateCounter);
    });


    // 2. Animate progress bars
    const progressBars = document.querySelectorAll(
        ".animated-progress"
    );

    progressBars.forEach(bar => {
        const target = Number(bar.dataset.target);

        if (!Number.isFinite(target)) return;

        requestAnimationFrame(() => {
            bar.value = target;
        });
    });


    // 3. Copy analyzed URL
    const copyButton = document.getElementById("copy-url");
    const feedback = document.getElementById("copy-feedback");

    if (copyButton) {
        copyButton.addEventListener("click", async () => {

            const url = copyButton.dataset.copy;

            try {
                await navigator.clipboard.writeText(url);

                feedback.textContent = "URL copied successfully!";
                copyButton.classList.add("copied");

                copyButton.innerHTML = "✓ Copied";

                setTimeout(() => {
                    feedback.textContent = "";
                    copyButton.classList.remove("copied");
                    copyButton.innerHTML = "▣ Copy URL";
                }, 2200);

            } catch (error) {
                feedback.textContent =
                    "Copy unavailable. Please copy the URL manually.";
            }
        });
    }


    // 4. Reveal cards while scrolling
    const revealElements = document.querySelectorAll(
        ".panel, .score-card, .interpretation"
    );

    if ("IntersectionObserver" in window) {

        const observer = new IntersectionObserver(
            (entries, observer) => {

                entries.forEach(entry => {

                    if (entry.isIntersecting) {

                        entry.target.classList.add("revealed");

                        observer.unobserve(entry.target);
                    }

                });

            },
            {
                threshold: 0.12
            }
        );

        revealElements.forEach(element => {
            element.classList.add("reveal");
            observer.observe(element);
        });

    } else {
        revealElements.forEach(element => {
            element.classList.add("revealed");
        });
    }


    // 5. Back to top button
    const topButton = document.getElementById("back-to-top");

    if (topButton) {

        window.addEventListener("scroll", () => {

            topButton.classList.toggle(
                "show",
                window.scrollY > 450
            );

        }, { passive: true });

        topButton.addEventListener("click", () => {

            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });

        });

    }

});
