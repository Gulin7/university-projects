<?php
// Allow from any origin
if (isset($_SERVER['HTTP_ORIGIN'])) {
    header("Access-Control-Allow-Origin: {$_SERVER['HTTP_ORIGIN']}");
    header('Access-Control-Allow-Credentials: true');
    header('Access-Control-Max-Age: 86400');    // cache for 1 day
}

// Access-Control headers are received during OPTIONS requests
if ($_SERVER['REQUEST_METHOD'] == 'OPTIONS') {

    if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_METHOD']))
        header("Access-Control-Allow-Methods: GET, POST, PUT, OPTIONS");

    if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']))
        header("Access-Control-Allow-Headers: {$_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']}");

    exit(0);
}

include("connect.php");

$json_data = json_decode(file_get_contents('php://input'), true);

if (isset($json_data['idSend']) && isset($json_data['updateAuthor']) && isset($json_data['updateTitle']) && isset($json_data['updatePages']) && isset($json_data['updateGenre'])) {
    $bookId = $json_data['idSend'];

    $author = $json_data['updateAuthor'];
    $title = $json_data['updateTitle'];
    $pages = intval($json_data['updatePages']);
    $genre = $json_data['updateGenre'];

    $sql = "UPDATE book SET author=?, title=?, pages=?, genre=? WHERE id=?";
    $stmt = mysqli_stmt_init($conn);

    if (mysqli_stmt_prepare($stmt, $sql)) {
        mysqli_stmt_bind_param($stmt, "ssisi", $author, $title, $pages, $genre, $bookId);

        $result = mysqli_stmt_execute($stmt);

        if ($result) {
            // Return a JSON response indicating success
            echo json_encode(["message" => "Record updated successfully"]);
        } else {
            // Return a JSON response indicating error
            echo json_encode(["error" => "Error updating record: " . mysqli_error($conn)]);
        }
    }
} else {
    $response['status'] = 400;
    $response['message'] = 'Bad Request: Missing or invalid data';
    echo json_encode($response);
}
?>
