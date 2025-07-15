// Al cargar el DOM, obtenemos y mostramos los episodios
document.addEventListener("DOMContentLoaded", () => {
  fetch("episodios.json")
    .then(response => response.json())
    .then(data => mostrarEpisodios(data))
    .catch(error => {
      console.error("Error al cargar los episodios:", error);
      document.getElementById("lista-episodios").innerHTML =
        "<p>No se pudieron cargar los episodios.</p>";
    });
});

function mostrarEpisodios(episodios) {
  const contenedor = document.getElementById("lista-episodios");

  episodios.forEach(episodio => {
    const elemento = document.createElement("article");
    elemento.classList.add("episodio");

    elemento.innerHTML = `
      <a href="https://www.youtube.com/watch?v=${episodio.videoId}" target="_blank">
        <img src="${episodio.miniatura}" alt="Miniatura de ${episodio.titulo}" />
      </a>
      <div class="episodio-detalles">
        <h2>${episodio.titulo}</h2>
        <p>${recortarDescripcion(episodio.descripcion)}</p>
      </div>
    `;

    contenedor.appendChild(elemento);
  });
}

function recortarDescripcion(texto, max = 300) {
  return texto.length > max ? texto.slice(0, max) + "…" : texto;
}
