<?php

$input = [1,8,9,2,5,6,3,4,7];

function heapSort(&$a) {
    heapMake($a);
    die(print_r($a));
    $n = count($a);
    while ($n > 0) {
        [$a[0], $a[$n - 1]] = [$a[$n - 1], $a[0]];
        $n--;
        heapify($a, 0, $n);
    }
}

function heapMake(&$a) {
    $n = count($a);
    for ($i = ($n - 1); $i >= 0; $i--) {
        heapify($a, $i, $n);
    }
}

function heapify(&$a, $pos, $n) {
    while (2 * $pos + 1 < $n) {
        $t = 2 * $pos +1;
        if (2 * $pos + 2 < $n && $a[2 * $pos + 2] >= $a[$t]) {
            $t = 2 * $pos + 2;
        }
        if ($a[$pos] < $a[$t]) {
            [$a[$pos], $a[$t]] = [$a[$t], $a[$pos]];
            $pos = $t;
        }
        else break;
    }
}

heapSort($input);
print_r($input);
