1. Ejecuta bench. py contra al menos dos destinos: SeaweedFS local y un servicio en la nube con API S3 (Supabase Storage o Backblaze B2).
2. Agrega la prueba de 1000 archivos pequeños (10 KB).
3. Verifica la integridad con SHA-256 y reporta errores.
4. Grafica MB/s por tamaño de archivo y destino.
5. Emite una recomendación: ¿cuál usarías para entrenar y cuál para respaldos?