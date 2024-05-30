<?php

$conn = mysqli_connect("localhost","root","","book_store_angular");
if(!$conn)
    die("Failed to connect..." . mysqli_error($conn));

?>