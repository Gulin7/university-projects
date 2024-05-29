<?php
// Allow from any origin
if (isset($_SERVER['HTTP_ORIGIN'])) {
    header("Access-Control-Allow-Origin: {$_SERVER['HTTP_ORIGIN']}");
    header('Access-Control-Allow-Credentials: true');
    header('Access-Control-Max-Age: 86400');    // cache for 1 day
}

// Access-Control headers are received during OPTIONS requests
if ($_SERVER['REQUEST_METHOD'] == 'OPTIONS') {

    if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_METHOD'])) {
        header("Access-Control-Allow-Methods: GET, POST, DELETE, OPTIONS"); // Only allow POST method for insertion
    }

    if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS'])) {
        header("Access-Control-Allow-Headers: {$_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']}");
    }

    exit(0);
}

include("connect.php");

// Check if it's a POST request
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Get the data from the request body
    $data = json_decode(file_get_contents("php://input"), true);

    // Extract the data
    $author = $data['authorSend'];
    $title = $data['titleSend'];
    $pages = $data['pagesSend'];
    $genre = $data['genreSend'];

    
    $pagesNumber = intval($pages);
    if ($pagesNumber < 1 || $pagesNumber > 2000) {
        http_response_code(400);
        echo json_encode(array("message" => "Pages should range between 1 and 2000"));
        exit;
    }

    
    $sql = "INSERT INTO book (author, title, pages, genre) VALUES (?, ?, ?, ?)";
    if ($stmt = $conn->prepare($sql)) {
        // Bind params
        $stmt->bind_param("ssis", $author, $title, $pagesNumber, $genre);
        
        // Execute statement
        if ($stmt->execute()) {
            
            http_response_code(201); // Created
            echo json_encode(array("message" => "Book was added successfully."));
        } else {
            http_response_code(500); // Internal Server Error
            echo json_encode(array("message" => "Unable to add book."));
        }

        
        $stmt->close();
    } else {
        // Respond with error message if prepared statement fails
        http_response_code(500); 
        echo json_encode(array("message" => "Unable to prepare statement."));
    }
} else {
    // Respond with error message if it's not a POST request
    http_response_code(405); // Method Not Allowed
    echo json_encode(array("message" => "Only POST method is allowed."));
}
?>
