document.addEventListener("DOMContentLoaded", () => {
  fetch("episodios.json")
    .then(res => res.json())
    .then(data => mostrarUltimoEpisodio(data[0]))
    .catch(err => {
      console.error("Error cargando el último episodio:", err);
      document.getElementById("episodio-destacado").innerHTML =
        "<p>No se pudo cargar el episodio más reciente.</p>";
    });
});

function mostrarUltimoEpisodio(episodio) {
  const contenedor = document.getElementById("episodio-destacado");

  const episodioHTML = `
    <a href="https://www.youtube.com/watch?v=${episodio.videoId}" target="_blank">
      <img src="${episodio.miniatura}" alt="Miniatura de ${episodio.titulo}" />
    </a>
    <div class="detalle">
      <h2>${episodio.titulo}</h2>
      <p>${recortarDescripcion(episodio.descripcion)}</p>
    </div>
  `;

  contenedor.innerHTML = episodioHTML;
}

function recortarDescripcion(texto, max = 300) {
  return texto.length > max ? texto.slice(0, max) + "…" : texto;
}
