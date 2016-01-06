<?php
  session_start();
  ini_set('display_errors','On');
  // include 'pdo.php';
  require_once 'mandrill-api-php/src/Mandrill.php';

  if(
    isset($_POST['sender_name']) &&
    isset($_POST['sender_email']) && 
    isset($_POST['message'])){

    $sender_name=htmlentities($_POST["sender_name"]);
    $sender_email=htmlentities($_POST["sender_email"]);
    $receiver="kuzijie@umich.edu";
    $msg=htmlentities($_POST["message"]);
  
    try {
        $mandrill = new Mandrill('aP99qLqMhOu61e4orFub1w');

        $message = array(
            'html' => "<p>Dear "."Zijie Ku"."</p>".'Your Email is Sent<br>'.$msg,
            'text' => 'Your Email is Sent<br>'.$msg,
            'subject' => 'Registration Confirmation',
            'from_email' => "$sender_email",
            'from_name' => "$sender_name",
            'to' => array(
                array(
                    'email' => "$receiver",
                    'name' => "$Zijie Ku",
                    'type' => 'to'
                )
            ),  
            'headers' => array('Reply-To' => "$receiver"),
        );
        $async = false;
        $result = $mandrill->messages->send($message, $async);
        // print_r($result);
        /*
        Array
        (
            [0] => Array
                (
                    [email] => recipient.email@example.com
                    [status] => sent
                    [reject_reason] => hard-bounce
                    [_id] => abc123abc123abc123abc123abc123
                )
        
        )
        */

        $message = array(
            'html' => "<p>Dear "."$sender_name"."</p>".'I have received your email.<br>'."I will get back to you ASAP.<br><br>Thank you<br>Zijie",
            'text' => 'Your Email is Sent<br>',
            'subject' => 'Registration Confirmation',
            'from_email' => "$sender_email",
            'from_name' => "$sender_name",
            'to' => array(
                array(
                    'email' => "$sender_email",
                    'name' => "$sender_name",
                    'type' => 'cc'
                )
            ),  
            'headers' => array('Reply-To' => "$receiver"),
        );
        $async = false;
        $result = $mandrill->messages->send($message, $async);

    } catch(Mandrill_Error $e) {
    // Mandrill errors are thrown as exceptions
    echo 'A mandrill error occurred: ' . get_class($e) . ' - ' . $e->getMessage();
    $_SESSION['email_status'] = "error";
    // A mandrill error occurred: Mandrill_Unknown_Subaccount - No subaccount exists with the id 'customer-123'
        throw $e;
    }
}
    $_SESSION['email_status'] = "sent";
    header( 'Location: contact.php' ) ;
    return;

?>
