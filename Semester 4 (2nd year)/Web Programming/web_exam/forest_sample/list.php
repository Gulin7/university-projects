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
    <p>Current user: <?php echo htmlspecialchars($_SESSION['name']); ?>!</p>
    <button id="seefiles">My Projects</button>
    <ul id="lista"></ul>
    <script src="list.js"></script>
    <h2>All projects</h2>
    <table id="projectstable">
        <tr>
            <th>Id</th>
            <th>Name</th>
        </tr>
    </table>
    <a href="logout.php">Logout</a>
</body>
</html>