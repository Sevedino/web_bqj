# 🌐 El Podcast Oficial – Web de Pruebas

Este proyecto es una **web experimental de pruebas** para un podcast ficticio titulado *El Podcast Oficial*. Se desarrolló para evaluar una estructura moderna, dinámica y automatizada que conecta directamente con contenido de YouTube.

## 🎯 Características principales

- Diseño responsivo con una paleta vibrante: amarillo, negro, rojo oscuro y blanco.
- Página principal (`index.html`) que muestra automáticamente el último episodio.
- Página de listado (`episodios.html`) con todos los capítulos de una playlist de YouTube.
- Carga automática de videos, miniaturas, descripciones e invitados desde la API de YouTube.
- Integración visual del logo y secciones claves como “Sobre el podcast”, redes sociales y botón de apoyo (PayPal).
- Estilo coherente y animaciones suaves.

## 📁 Estructura del proyecto

📦 podcast-web/
├── index.html → Página principal
├── episodios.html → Página con lista completa de episodios
├── estilos.css → Estilos compartidos
├── episodios.css → Estilos específicos para la lista de capítulos
├── main.js → Carga el último episodio desde JSON
├── episodios.js → Carga dinámica de episodios completos
├── generar_json.py → Script que genera episodios.json desde YouTube
├── episodios.json → Datos generados desde la API (miniaturas, títulos, etc.)
├── logo.png → Logo del podcast
└── README.md → Este archivo de documentación

## 🛠️ Requisitos

- Python 3.x
- Librería `requests` instalada:
  ```bash
  pip install requests
