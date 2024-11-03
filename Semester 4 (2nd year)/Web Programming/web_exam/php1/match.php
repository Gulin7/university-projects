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

$keys = $data['keywords'];
$keywords = explode(',', $keys);

$sql = "SELECT * FROM documents";
$result = $conn->query($sql);
$documentsData = array();

if($result->num_rows > 0){
    while($row = $result->fetch_assoc())
        $documentsData[] = $row;
}

$response = array();

foreach ($documentsData as $document) {
    $cnt = 0;
    foreach($keywords as $k){
        if($document['keyword1'] === $k)
            $cnt++;
        if($document['keyword2'] === $k)
            $cnt++;
        if($document['keyword3'] === $k)
            $cnt++;
        if($document['keyword4'] === $k)
            $cnt++;
        if($document['keyword5'] === $k)
            $cnt++;
    }
    if($cnt === 3)
        $response[] = $document;
}


$conn->close();
header('Content-Type: application/json');
echo json_encode($response);
?>