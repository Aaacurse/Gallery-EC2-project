
async function loadPhotos() {
    const gallery = document.getElementById("gallery");
    const photoCount = document.getElementById("photo-count");

    try {
        const response = await fetch("/api/photos");

        if (!response.ok) {
            throw new Error("Could not fetch photos");
        }

        const data = await response.json();

        photoCount.textContent = `${data.total} photos`;

        data.photos.forEach(photo => {
            const card = document.createElement("div");
            card.className = "photo-card";

            const encodedPath = photo
                .split("/")
                .map(encodeURIComponent)
                .join("/");

            // Image preview
            const img = document.createElement("img");
            img.src = `/photos/${encodedPath}`;
            img.alt = photo;
            img.loading = "lazy";

            // Open image in a new tab
            const imageLink = document.createElement("a");
            imageLink.href = `/photos/${encodedPath}`;
            imageLink.target = "_blank";
            imageLink.rel = "noopener noreferrer";

            imageLink.appendChild(img);

            // Filename
            const name = document.createElement("p");
            name.textContent = photo;

            // Download link
            const downloadLink = document.createElement("a");
            downloadLink.href = `/download/${encodedPath}`;
            downloadLink.textContent = "Download";
            downloadLink.className = "download-btn";

            card.appendChild(imageLink);
            card.appendChild(name);
            card.appendChild(downloadLink);

            gallery.appendChild(card);
        });

    } catch (error) {
        photoCount.textContent = "Unable to load photos.";
        console.error(error);
    }
}
function downloadAll() {
    window.location.href = "/download-all";
}

loadPhotos();
