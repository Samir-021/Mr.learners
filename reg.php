<?php
    error_reporting(E_ALL);
    ini_set('display_errors', 1);
    
    if(isset($_POST['register'])){
        $email = $_POST['email'];
        $username = $_POST['username'];
        $password = $_POST["pass"];
        $con = mysqli_connect('localhost', 'root','', 'register_form');
        $sql = "INSERT INTO info (email, username, password) VALUES ('$email', '$username', '$password')";
        if(mysqli_query($con, $sql)){
            echo "<script>alert('Register is succesfull!!'); window.location='Panda-login.html'</script>";
        }
        else
        {
            echo 'error';
        }
    }
?>