<?php
   /*$pdo = new \PDO(
        'mysql:host=db;dbname=demoName',
        'demoUser',
        'demoPass'
    );
    var_dump($pdo);*/
try {
    $dbh = new PDO('mysql:host=db;dbname=demoDb', 'demoUser', 'demoPass');
    print gettype($dbh);
    $dbh = null;
} catch (PDOException $e) {
    print "Error!: " . $e->getMessage() . "<br/>";
    die();
}
    // var_dump(mysqli("db", "demoUser", "demoPass", "demoDb"));
    phpinfo();
