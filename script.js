async function convert(type, event) {
    event.preventDefault();
    
    // Obtener elementos del DOM
    const inputElement = document.getElementById(`${type}Value`);
    const value = inputElement.value.trim(); // Eliminar espacios en blanco
    const from = document.getElementById(`${type}From`).value;
    const to = document.getElementById(`${type}To`).value;
    const resultElement = document.getElementById(`${type}Result`);

    // Validar entrada
    if (value === "") {
        resultElement.textContent = "Error: El campo no puede estar vacío";
        return;
    }

    const numericValue = parseFloat(value);
    if (isNaN(numericValue)) {
        resultElement.textContent = "Error: Ingresa un número válido";
        return;
    }

    try {
        // Enviar solicitud al servidor
        const response = await fetch('http://localhost:5000/convert', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ type, value: numericValue, from, to }),
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Error en la conversión");
        }

        // Mostrar resultado con formato
        const decimalPlaces = type === "temperature" ? 2 : 4;
        resultElement.textContent = `Resultado: ${data.result.toFixed(decimalPlaces)}`;

    } catch (error) {
        resultElement.textContent = `Error: ${error.message}`;
    }
}