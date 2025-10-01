export default function handler(req, res) {
  if (req.method === "POST") {
    const { nombre, email } = req.body;

    // Lógica equivalente a la de Python
    console.log(`Nombre: ${nombre}, Email: ${email}`);

    res.status(200).json({ mensaje: `Datos recibidos: ${nombre}, ${email}` });
  } else {
    res.status(405).json({ mensaje: "Método no permitido" });
  }
}
