<?php
        error_reporting(E_ALL);
        ini_set('display_errors', 1);

    if(isset($_POST['login'])){
        $username = $_POST['username'];
        $password = $_POST["pass"];
        $con = mysqli_connect('localhost', 'root','', 'register_form');
        $sql = "SELECT * FROM info WHERE username='$username' AND password = '$password'";

        $result =mysqli_query($con, $sql);
        if(mysqli_num_rows($result)>0){
            session_start();
            $_SESSION['username']=$username;
                echo "<script>alert('login sucessfull!!'); window.location='dashboard.php'</script>";
            }
         else
            {
                echo "<script>alert('try again to log_in please check your username & password')</script>";
            }
        }
?>