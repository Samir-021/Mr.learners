<?php
    session_start();
    if($_SESSION['username']){
        echo "<script>alert('welcomes to dashboard'); window.location='loader.html'</script>";
    }
    else
    {
        "<script>alert('Please Login First');window.location='login.php'</script>";
    }
?>