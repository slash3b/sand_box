<?php
declare(strict_types=1);

class LinkedNode
{
    public $data;
    public $next;

    public function __construct(){
        $this->data = null;
        $this->next = null;
    }
}

$a = new LinkedNode;
$a->data = 50;

$b = new LinkedNode;
$b->data = 33;

$c = new LinkedNode;
$c->data = 12;

$d = new LinkedNode;
$d->data = 66;

$a->next = $b;
$b->next = $c;
$c->next = $d;



function dumpLinkedList($node) {
    if ($node->next instanceof LinkedNode && $node->next->data == 12){
        var_dump($node->next);
        return;
    }
    if ($node->next instanceof LinkedNode) {
        dumpLinkedList($node->next);
    }
}

dumpLinkedList($a);

var_dump($a);


