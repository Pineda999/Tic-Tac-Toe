function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function miclick(numero){
    var numeroUsuario = numero;
    var posicion = document.getElementById('posiciones');

    fetch('',{
        method : 'POST',
        body: JSON.stringify({'posicion':numeroUsuario}),
        headers:{
            "X-CSRFToken":getCookie('csrftoken'),
            "X-Requested-With":"XMLHttpRequest",
        } 
    }).then(
        function(response){
            return response.json()
        }
    ).then( data =>{
        const usuario =data.jugador
        const Maquina = data.maquina
        const ganador = data.ganador;

        if(usuario){
            const boton = document.querySelector(`button[data-pos='${data.jugador.posicion}']`);
            console.log(data.jugador.posicion)
            if (boton) {
                boton.textContent = data.jugador.simbolo;
                boton.disabled = true;
            }
        }
        if(Maquina){
            const boton = document.querySelector(`button[data-pos='${data.maquina.posicion}']`);
            console.log(data.maquina.posicion)
            if (boton) {
                boton.textContent = data.maquina.simbolo;
                boton.disabled = true;
            }
        }
        if (ganador) {
            Swal.fire({
                title: ganador === 'X' ? '¡Ganaste! 🎉' : ganador === 'O' ? 'La máquina ganó 🤖' : 'Empate 😐',
                confirmButtonText: 'Reiniciar',
            }).then(() => {
                fetch('/reiniciar/', { 
                    method: 'POST',
                     headers:{
                        "X-CSRFToken":getCookie('csrftoken'),
                        "X-Requested-With":"XMLHttpRequest",
                    } 

                })
                    .then(() => location.reload());
            });
        }
    })
     .catch(error => {
        console.error('Error al enviar jugada:', error);
    });

}
