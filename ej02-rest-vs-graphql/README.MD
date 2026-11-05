# Ejericio 2: Comparacion de REST y GraphQL

se compararon REST y GraphQL utilizando la API de Pokémon para consultar información de 10 Pokémon

se analizaron las diferencias en el número de peticiones, tiempo de respuesta y cantidad de datos transferidos

tmbn se utilizaron tres scripts en Python: consumo_rest.py, consumo_graphql.py y comparacion.py, con ellos se realizaron consultas y se midió el rendimiento de ambas arquitecturas

Conclusión
REST realiza una petición por cada Pokémon, mientras que GraphQL permite consultar varios en una sola. Esto puede reducir el tiempo de respuesta y la cantidad de datos transferidos, dependiendo de las condiciones de la prueba.