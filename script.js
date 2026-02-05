function searchProduct() {
    const product = document.getElementById("productInput").value;
    const resultsDiv = document.getElementById("results");

    resultsDiv.innerHTML = "";

    if (product === "") {
        resultsDiv.innerHTML = "<p>Please enter a product name.</p>";
        return;
    }

    // Dummy data (backend will replace this later)
    const platforms = [
        { name: "Amazon", price: "₹52,999" },
        { name: "Flipkart", price: "₹51,499" },
        { name: "Reliance Digital", price: "₹53,200" }
    ];

    platforms.forEach(p => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
            <h3>${p.name}</h3>
            <p>Price: <strong>${p.price}</strong></p>
        `;
        resultsDiv.appendChild(card);
    });
}
