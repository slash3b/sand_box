<?php

declare(strict_types=1);

$input = [6,9,1,4,0];

$n = count($input);

for($i = 0; $i < $n; $i++) {
    for($a = 0; $a < $n-$i; $a++) {
        if(isset($input[$a+1]) && $input[$a] > $input[$a+1]) {
            [$input[$a], $input[$a+1]] = [$input[$a+1],$input[$a]];
        }
    }
}

print_r($input);
