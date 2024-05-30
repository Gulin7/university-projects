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
        header("Access-Control-Allow-Methods: GET, POST, DELETE, OPTIONS");

    if (isset($_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']))
        header("Access-Control-Allow-Headers: {$_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']}");

    exit(0);
}

include("connect.php");

// Check if it's a DELETE request
if ($_SERVER['REQUEST_METHOD'] == 'DELETE') {
    // Get the book ID from the request
    $bookId = isset($_GET['id']) ? $_GET['id'] : null;

    if ($bookId) {
        // Use prepared statement to prevent SQL injection
        $sql = "DELETE FROM book WHERE id = ?";
        
        if ($stmt = $conn->prepare($sql)) {
            // Bind the book ID parameter
            $stmt->bind_param("i", $bookId);
            
            // Execute the statement
            if ($stmt->execute()) {
                // Respond with success message
                http_response_code(200);
                echo json_encode(array("message" => "Book was deleted successfully."));
            } else {
                // Respond with error message if deletion fails
                http_response_code(500);
                echo json_encode(array("message" => "Unable to delete book."));
            }

            // Close statement
            $stmt->close();
        } else {
            // Respond with error message if prepared statement fails
            http_response_code(500);
            echo json_encode(array("message" => "Unable to prepare statement."));
        }
    } else {
        // Respond with error message if book ID is not provided
        http_response_code(400);
        echo json_encode(array("message" => "Book ID is missing."));
    }
} else {
    // Respond with error message if it's not a DELETE request
    http_response_code(405); // Method Not Allowed
    echo json_encode(array("message" => "Only DELETE method is allowed."));
}
?>
