function tomarFoto(){

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(mediaStream) {
        // Crea un elemento video y asigna al flujo de video como fuente
        var video = document.getElementById('videoFoto');
        video.srcObject = mediaStream;
        video.onloadedmetadata = function(e) {
          // Inicia la reproducción del video para que podamos ver la imagen de la cámara
          video.play();
        };

        // Crea un elemento canvas y dibuja el video en él
        var canvas = document.getElementById('canvasfoto');
        var context = canvas.getContext('2d');
        setInterval(function() {
          context.drawImage(video, 0, 0, canvas.width, canvas.height);
        }, 16); // Dibuja el video cada 16 milisegundos (60 fps)

        // Cuando se haga clic en el botón "Tomar foto", obtén la imagen del canvas en formato data:URL
        let photoButton = $('#take-photo');
        photoButton.click(function() {
            console.log('Tomar Foto');
          var dataURL = canvas.toDataURL('image/png');
          // Aquí puedes hacer algo con la imagen como, por ejemplo, mostrarla en un elemento img
          var img = $('#fotoTomada');
          img.attr( "src", dataURL);
          //document.body.appendChild(img);
        });

      })
      .catch(function(err) {
          console.log('Ha ocurrido un error...');
          console.log(err);
      }
    );

}

$('input[name="nombre"]').attr("disabled", "disabled");


$('#live_webcam').css('width', '100%');

