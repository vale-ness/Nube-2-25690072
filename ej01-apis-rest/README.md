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


## preguntas

* **¿Qué parte de la respuesta realmente usaste?**
Solo los datos que pedí como la altura y habilidades de Pikachu, confirmación de las publicaciones, temperatura y descripción del clima, y los códigos de estado. Todo el resto de la información que llegó no la usé.

* **¿qué porcentaje de los bytes recibidos fue innecesario?**
más del 95% de lo que bajó no se utilizó

Reflexión
En esta actividad aprendí a realizar peticiones a diferentes APIs y a interpretar sus respuestas, tmbn aprendí a manejar errores como el 404 cuando un recurso no existe, y el 401 cuando falta una clave de acceso o es inválida. En los resultados observe de que recibimos mucha información que no siempre necesitamos, por lo que es importante solicitar solo los datos necesarios para aprovechar mejor los recursos.
