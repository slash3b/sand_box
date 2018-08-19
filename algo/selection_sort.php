<?php

$input = [4, 5, 2, 1, 6, 8, 0, 3, 7, 9, 324, 23456, 12, -56, 111000003, 34, 1, -54];
$len = count($input);

for ($i = 0; $i < $len; $i++) {
    $minIndex = $i;
    for ($j = $i; $j < $len; $j++) {
        $nI = $j + 1;
        if(isset($input[$nI]) && $input[$j] > $input[$nI] && $input[$nI] < $input[$minIndex]) {
            $minIndex = $nI;
        }
    }
    $input[$i] !== $input[$minIndex] && ([$input[$i], $input[$minIndex]] = [$input[$minIndex], $input[$i]]);
}
print_r($input);