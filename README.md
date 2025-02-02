# Conversor de Unidades Web 🌐📏⚖️🌡️  
*Aplicación web para convertir entre unidades de longitud, peso y temperatura.*

---

## Características ✨
- **Conversión en tiempo real** para:
  - **📏 Longitud**: Milímetros (mm), centímetros (cm), metros (m), kilómetros (km), pulgadas (in), pies (ft), yardas (yd), millas (mi).
  - **⚖️ Peso**: Miligramos (mg), gramos (g), kilogramos (kg), onzas (oz), libras (lb).
  - **🌡️ Temperatura**: Celsius (°C), Fahrenheit (°F), Kelvin (K).
- **Interfaz intuitiva** con selección de unidades mediante menús desplegables.
- **Validación de entradas**: Detecta campos vacíos y valores no numéricos.
- **Resultados precisos**: 
  - 4 decimales para longitud y peso.
  - 2 decimales para temperatura.
- **Diseño responsive**: Compatible con dispositivos móviles y desktop.

---

## Tecnologías 🛠️
| **Frontend**         | **Backend**          | **Herramientas**       |
|----------------------|----------------------|------------------------|
| HTML5                | Python 3             | Git & GitHub           |
| CSS3 (Flexbox/Grid)  | Flask (Microservicio)| Visual Studio Code     |
| JavaScript (ES6)     | Flask-CORS           | Postman (Testing API)  |

---

## Instalación 🚀

### Requisitos Previos
- Python 3.8+ ([Descargar](https://www.python.org/downloads/))
- Navegador web moderno (Chrome, Firefox, Edge).

### Pasos para Configurar el Proyecto
1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/conversor-unidades.git
   cd conversor-unidades
   ```

2. **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Iniciar el servidor backend:**
    ```bash
    python app.py # El servidor estará en: http://localhost:5000
    ```

4. **Abrir el frontend desde Live Server (si estás en Visual Studio Code):**
    En el Visual Studio Code, debes estar en la ventana del index.html para ejecutar el frontend desde el Live Server.

## Uso 🖱️

1- Selecciona una categoría: Longitud, Peso o Temperatura.

2- Ingresa el valor numérico en el campo de entrada.

3- Elige las unidades en los menús "De" y "A".

4- Haz clic en "Convertir":

5- El resultado se mostrará debajo del botón.

---

## Ejemplos de Conversión ✅

| **Categoría**  | **De**           | **A**            | **Entrada** | **Resultado**  |
|----------------|------------------|------------------|-------------|----------------|
| Temperatura    | Celsius (°C)     | Fahrenheit (°F)  | 0           | 32.00°F        |
| Longitud       | Pulgadas (in)    | Centímetros (cm) | 12          | 30.4800 cm     |
| Peso           | Kilogramos (kg)  | Libras (lb)      | 1           | 2.2046 lb      |

---


Link del proyecto acorde a lo solicitado: https://roadmap.sh/projects/unit-converter
