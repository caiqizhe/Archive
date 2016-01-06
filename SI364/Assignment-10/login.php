<?php
/**
 * Copyright (C) 2013 peredur.net
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
include_once 'includes/db_connect.php';
include_once 'includes/functions.php';

sec_session_start();

if (login_check($pdo) == true) {
    $logged = 'in';
} else {
    $logged = 'out';
}
?>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
        <title>Secure Login: Log In</title>
        <link rel="stylesheet" href="styles/style.css" />
        <script type="text/JavaScript" src="js/sha512.js"></script> 
        <script type="text/JavaScript" src="js/forms.js"></script> 
    </head>
    <body>

        
        <div id = "content">
        <h1>Welcome to the Secured Login!</h1>
        <p> Please sign in to access your account.</p>
        <form action="includes/process_login.php" method="post" name="login_form">                      
            <fieldset>
                <?php
                  if (isset($_SESSION['error'])) {
                      echo '<p class="error">'.$_SESSION['error'].'</p>';
                  }
                  unset($_SESSION['error']);
                ?> 
                <label>Email: <br/><input type="email" name="email" /></label><br/>
                <label>Password: <br/><input type="password" 
                             name="password" 
                             id="password"/></label><br/>
                 <input type="button" 
                   value="Login" 
                   onclick="formhash(this.form, this.form.password);" /> 
        

        </fieldset>
        </form>
        <p>If you don't have a login, please <a href="register.php">register</a></p>
        <p>If you are done, please <a href="includes/logout.php">log out</a>.</p>
        <p>You are currently logged <?php echo $logged ?>.</p>
    </div>
    </body>
</html>