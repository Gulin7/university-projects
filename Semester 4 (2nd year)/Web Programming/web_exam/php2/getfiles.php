<?php
session_start();
$hostname = "localhost";
$username = "root";
$password = "";
$database = "authenticationphp";

$conn = new mysqli($hostname, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$userId = $_SESSION['id'];
$sql = "select * from files where userid = '$userId'";
$result = $conn->query($sql);

$response = array();
if($result->num_rows > 0)
{
    while($row = $result->fetch_assoc())
        $response[] = $row;
}
$conn->close();
header('Content-Type: application/json');
echo json_encode($response);
?>