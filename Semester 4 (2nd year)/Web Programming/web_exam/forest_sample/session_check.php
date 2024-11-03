<?php
session_start();
if(!isset($_SESSION['name'])){
    header("Location: main.html");
    exit();
}