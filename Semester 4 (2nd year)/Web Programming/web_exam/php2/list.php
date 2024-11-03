<?php 
include('session_check.php');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Logged in as <?php echo htmlspecialchars($_SESSION['username']); ?></h1>
    <a href="logout.php">Logout</a>
    <button id="seefiles">My files</button>
    <ul id="lista"></ul>
    <script src="list.js"></script>
</body>
</html>