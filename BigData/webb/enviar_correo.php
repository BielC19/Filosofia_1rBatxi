<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST["nombre"];
    $email = $_POST["email"];
    $asunto = $_POST["asunto"];
    $mensaje = $_POST["mensaje"];

    $destinatario = "bielcostasmso@insalba.cat";
    $encabezados = "From: $nombre <$email>";

    // Envía el correo electrónico
    mail($destinatario, $asunto, $mensaje, $encabezados);

    echo "¡El correo ha sido enviado correctamente!";
} else {
    echo "Error: El formulario no ha sido enviado.";
}
?>