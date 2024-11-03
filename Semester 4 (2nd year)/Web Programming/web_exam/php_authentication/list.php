<?php
include('session_check.php');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Files</title>
</head>
<body>
    <p>Logged successfully as <?php echo htmlspecialchars($_SESSION['username']); ?>!</p>
    <button id="seefiles">My files</button>
    <ul id="lista"></ul>
    <script src="list.js"></script>
    <a href="logout.php">Logout</a>
</body>
</html>