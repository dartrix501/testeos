const form = document.getElementById("contactForm");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const nombre = document.getElementById("nombre").value;
    const email = document.getElementById("email").value;

    try {
        const res = await fetch("https://api-test-2hpy.onrender.com/procesar", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ nombre, email })
        });

        const data = await res.json();
        alert(data.mensaje);
    } catch (err) {
        console.error("Error:", err);
        alert("Ocurrió un error al enviar los datos");
    }
});
