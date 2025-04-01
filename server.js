const express = require("express");
const path = require("path");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());
app.use(express.static(path.join(__dirname, "public")));

// Ruta para multiplicar las matrices
app.post("/multiplicar", (req, res) => {
    const { matriz1, matriz2 } = req.body;
    
    // Validar las matrices
    if (!Array.isArray(matriz1) || !Array.isArray(matriz2)) {
        return res.status(400).json({ error: "Datos inválidos" });
    }

    const filas1 = matriz1.length;
    const columnas1 = matriz1[0].length;
    const filas2 = matriz2.length;
    const columnas2 = matriz2[0].length;

    if (columnas1 !== filas2) {
        return res.status(400).json({ error: "Las matrices no se pueden multiplicar, las columnas de la primera deben coincidir con las filas de la segunda." });
    }

    // Inicializar la matriz resultado con ceros
    let resultado = Array(filas1).fill().map(() => Array(columnas2).fill(0));

    // Multiplicación de matrices
    for (let i = 0; i < filas1; i++) {
        for (let j = 0; j < columnas2; j++) {
            for (let k = 0; k < columnas1; k++) {
                resultado[i][j] += matriz1[i][k] * matriz2[k][j];
            }
        }
    }

    res.json({ resultado });
});

app.listen(3000, () => console.log("Servidor en http://localhost:3000"));
