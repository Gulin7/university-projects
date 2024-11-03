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
$input = file_get_contents("php://input");
$data = json_decode($input, true);

$username = $data['username'];
$givenPassword = $data['password'];

$sql = "select * from users where username = '$username'";
$result = $conn->query($sql);

$response = array();
if($result->num_rows > 0)
{
    $user = $result->fetch_assoc();
    if($user['password'] === $givenPassword)
    {
        $_SESSION['username'] = $user['username'];
        $_SESSION['id'] = $user['id'];
        $response = array("message" => "success");
    }
    else
    {
        $response = array("message" => "fail");
    }
    $conn->close();
    header('Content-Type: application/json');
    echo json_encode($response);
}
