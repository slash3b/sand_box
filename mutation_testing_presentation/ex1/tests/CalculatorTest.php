<?php
declare(strict_types=1);

use Ex1\Calculator;
use PHPUnit\Framework\TestCase;

final class CalculatorTest extends TestCase
{

    public function test_adds()
    {
        $calc = new Calculator();
        $result = $calc->adds(1,2);
        $this->assertTrue(is_int($result));
    }

    public function test_subtracts()
    {
        $calc = new Calculator();
        $result = $calc->subtracts(1,2);
        $this->assertTrue(is_int($result));
    }

    public function test_in_array()
    {
        $calc = new Calculator();
        $result = $calc->inArray(['a','b'], 'a');
        $this->assertTrue(is_string($result));
    }

    public function test_filter_array()
    {
        $calc = new Calculator();
        $result = $calc->filterArray([1,2,3,10,20,30]);
        $this->assertCount(2, $result);
    }

}

