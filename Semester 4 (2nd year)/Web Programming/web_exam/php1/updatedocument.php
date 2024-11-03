<?php
$hostname = "localhost";
$username = "root";
$password = "";
$database = "websitesdocumentsphp";

$conn = new mysqli($hostname, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$input = file_get_contents("php://input");
$data = json_decode($input, true);

$id = $data['id'];
$kw1 = $data['kw1'];
$kw2 = $data['kw2'];
$kw3 = $data['kw3'];
$kw4 = $data['kw4'];
$kw5 = $data['kw5'];

$sql = "UPDATE documents set keyword1 = '$kw1', keyword2 = '$kw2', keyword3 = '$kw3', keyword4 = '$kw4', keyword5 = '$kw5' WHERE id = '$id'";

if($conn->query($sql) === TRUE){
    $response = array("message" => "update successful");
}
else{
    $response = array("message" => "update unsuccessful");
}

$conn->close();
header('Content-Type: application/json');
echo json_encode($response);
?>