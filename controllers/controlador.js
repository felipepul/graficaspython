let boton = document.getElementById('btnreporte')
boton.addEventListener("click",function(evento){
    evento.preventDefault()
    let contenedor = document.getElementById('contenedor')
    contenedor.classList.remove("d-none")

    let nombreusuario = document.getElementById("nombres").value
    let message = document.querySelector('mensaje')
    mensaje.textContent = `Apreciado usuario ${nombreusuario}, el reporte generado es:`
})