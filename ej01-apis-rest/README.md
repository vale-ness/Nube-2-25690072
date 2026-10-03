## Ejercicio 1: APIs REST

### tabla de resultados

| API / Endpoint | Método | Código | Tiempo (ms) | Bytes |
| :--- | :---: | :---: | :---: | :---: |
| JSONPlaceholder (Listar posts) | GET | 200 | 244 ms | 27520 B |
| JSONPlaceholder (Crear post) | POST | 201 | 270 ms | 35 B |
| PokéAPI (Pikachu) | GET | 200 | 253 ms | 300521 B |
| OpenWeatherMap (Cd. Valles) | GET | 200 | 281 ms | 508 B |
| Recurso Inexistente | GET | 404 | 207 ms | 2 B |
| Sin Clave / Clave inválida | GET | 401 | 277 ms | 108 B |

---
Ej1. con los curl tuve algunos problemas al momento de escribirlos en cmd porque los estaba acomodando mal. Después pude hacerlos

Ej2. con la PokeAPI solo copié el código y pedí la información de Pikachu. Con datos=json pude entrar a "abilities" para obtener sus habilidades y la petición fue GET y dio 200.

Ej3. después hice el pronóstico de Ciudad Valles con OpenWeatherMap, tuve que conseguir una API key, guardarla en un archivo .env y usar dotenv para poder leerla desde el código.

Ej4. hice pruebas con los errores, para el 404 lo provoqué poniendo algo que no existe en la URL, y el 401 salió al intentar usar WeatherMap sin la API key.
---

## preguntas

* **¿Qué parte de la respuesta realmente usaste?**
Solo los datos que pedí como la altura y habilidades de Pikachu, confirmación de las publicaciones, temperatura y descripción del clima, y los códigos de estado. Todo el resto de la información que llegó no la usé.

* **¿Qué porcentaje de los bytes recibidos fue innecesario?**
más del 95% de lo que bajó no se utilizó

