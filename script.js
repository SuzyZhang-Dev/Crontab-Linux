async function loadRSS() {
    const res = await fetch('yle_fi_rss.txt');
    const text = await res.text();
    const rows = text.split(/\r?\n/);

    const newsDiv = document.getElementById("news");

    rows.forEach(line => {
        if (line.trim().length === 0) return;

        const [time, title, link] = line.split(";");

        const container = document.createElement("div");
        container.className = "news-item";

        container.innerHTML = `
            <div class="time">${time}</div>
            <a href="${link}" target="_blank">${title}</a>
        `;

        newsDiv.appendChild(container);
    });
}

loadRSS();