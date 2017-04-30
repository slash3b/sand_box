<?php

require_once __DIR__ . '/vendor/autoload.php';

use Enqueue\AmqpExt\AmqpConnectionFactory;
use Enqueue\AmqpExt\AmqpContext;

// launch RabbitMQ with this command
// docker run -d --hostname my-rabbit --name some-rabbit3 -P rabbitmq:3-management
// NOTE: with -P argument all ports are going to be exposed at random
// local ports so $options should be adjusted
$options = [
  'host'      => '0.0.0.0',
  'port'      => 32771,
  'vhost'     => '/',
  'login'     => 'guest',
  'password'  => 'guest',
  'persisted' => FALSE,
];
$context = (new AmqpConnectionFactory($options))->createContext();

/** @var AmqpContext $context */
$queue = $context->createQueue('process_image');
$context->declareQueue($queue);
$consumer = $context->createConsumer($queue);
while (TRUE) {
  $message   = $consumer->receive($timeout = 10);
  if ($message) {
    print_r($message);
    $imagePath = $message->getBody();
    // image processing logic here
    $consumer->acknowledge($message);
  }
}
