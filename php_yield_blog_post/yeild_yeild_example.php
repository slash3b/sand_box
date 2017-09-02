<?php
    function secondGen()
    {
        yield 9;
    }
    function getGen()
    {
        yield 1;
        yield from [2,3];
        yield from secondGen();
    }

    foreach(getGen() as $f ) {
        print $f . PHP_EOL;
    }
