<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1><center>Register form</center></h1>
    <fieldset>
        <legend>Personal information</legend>
        <form action="reg.php" method="POST" enctype="">
            <label for="name">Full Name:</label>
            <input type="text" placeholder="first name">
            <input type="text" placeholder="middle name">
            <input type="text" placeholder="last name"> <br> <br>
            <label for="">E-mail</label>
            <input type="email" name="email"> <br> <br>
            <label for="">Usename</label>
            <input type="text" name="username"> <br> <br>
            <label for="">Password</label>
            <input type="password" name="pass"> <br> <br>
            <input type="submit" name="register">
            <input type="reset">
        </form>
    </fieldset>
</body>
</html>