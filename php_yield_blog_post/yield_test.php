<?php
ini_set('memory_limit', -1);

function yieldArray() {
    $arr = [];
    for($i = 0; $i <= 100000000; $i++) {
        yield $i; 
    }
}

yieldArray();
print number_format(memory_get_peak_usage(true) / 1024 / 1024, 2, '.', '') . 'Mb'. PHP_EOL;
