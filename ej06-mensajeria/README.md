1. Agrega RabbitMQ como servicio.
2. POST /api/ia/solicitudes publica en la cola y responde 202
Accepted con un id.
3. Un worker consume, usa el modelo y guarda el resultado en Redis.
4. GET /api/ia/solicitudes/(id) devuelve pendiente o la predicción.
5. Mide el tiempo para procesar 100 solicitudes con 1, 2 y 4 workers.