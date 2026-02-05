function searchProduct() {
    const product = document.getElementById("productInput").value;
    const dashboard = document.getElementById("dashboard");

    if (product === "") return;

    dashboard.classList.remove("hidden");

    const offers = [
        { platform: "Amazon", price: 52999, rating: 4.5 },
        { platform: "Flipkart", price: 51499, rating: 4.3 },
        { platform: "Reliance Digital", price: 53200, rating: 4.6 },
        { platform: "Croma", price: 52500, rating: 4.2 }
    ];

    // SORTED LISTS
    const bestPrice = [...offers].sort((a,b) => a.price - b.price)[0];
    const bestRating = [...offers].sort((a,b) => b.rating - a.rating)[0];

    displaySingle("bestPrice", bestPrice);
    displaySingle("bestRating", bestRating);
    displayAll("allOffers", offers);
}

function displaySingle(id, offer) {
    const div = document.getElementById(id);
    div.innerHTML = cardHTML(offer);
}

function displayAll(id, offers) {
    const div = document.getElementById(id);
    div.innerHTML = "";
    offers.forEach(o => div.innerHTML += cardHTML(o));
}

function cardHTML(o) {
    return `
        <div class="card">
            <h3>${o.platform}</h3>
            <p>💰 Price: ₹${o.price}</p>
            <p>⭐ Rating: ${o.rating}</p>
        </div>
    `;
}
