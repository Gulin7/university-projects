<?php
$hostname = "localhost";
$username = "root";
$password = "";
$database = "websitesdocumentsphp";

$conn = new mysqli($hostname, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$webpage_id = $_GET['id'];

$sql = "SELECT count(*) as cnt FROM documents WHERE idWebSite = '$webpage_id'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $numar = $result->fetch_assoc();
    header('Content-Type: application/json');
    echo json_encode($numar);
}

$conn->close();

?>