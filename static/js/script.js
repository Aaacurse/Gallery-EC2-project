
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

            const img = document.createElement("img");

            const encodedPath = photo
                .split("/")
                .map(encodeURIComponent)
                .join("/");

            img.src = `/photos/${encodedPath}`;
            img.alt = photo;
            img.loading = "lazy";

            const name = document.createElement("p");
            name.textContent = photo;

            card.appendChild(img);
            card.appendChild(name);

            gallery.appendChild(card);
        });

    } catch (error) {
        photoCount.textContent = "Unable to load photos.";
        console.error(error);
    }
}

loadPhotos();
