<?php
session_start();
$db_host = 'localhost';
$db_port = '3306';
$db_name = 'authenticationphp';
$db_user = 'root';
$db_pass = '';

$conn = new mysqli($db_host, $db_user, $db_pass, $db_name, $db_port);

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