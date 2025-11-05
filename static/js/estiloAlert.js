/* Estilo del alert */
Swal.fire({
  title: "🎮 Bienvenido al juego Tic Tac Toe",
  text: "¡Diviértete jugando!",
  width: 600,
  padding: "3em",
  color: "#716add",
  background: "#fff url({% static 'imagenes/fondo.png' %})",
  backdrop: `
    rgba(0,0,123,0.4)
    url("${staticUrl}imagenes/cat2.gif")
    left top
    no-repeat
    `,
  confirmButtonText: "¡Comenzar!",
  confirmButtonColor: "#4CAF50",
  showClass: {
    popup: "animate__animated animate__fadeInDown"
  },
  hideClass: {
    popup: "animate__animated animate__fadeOutUp"
  }
});