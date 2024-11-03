<?php
$hostname = "localhost";
$username = "root";
$password = "";
$database = "websitesdocumentsphp";

$conn = new mysqli($hostname, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM websites";
$result = $conn->query($sql);

$webData = array();

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $webData[] = $row;
    }
}

$conn->close();
header('Content-Type: application/json');
echo json_encode($webData);
?>