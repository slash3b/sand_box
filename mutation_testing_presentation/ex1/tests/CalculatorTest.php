<?php
declare(strict_types=1);

use Ex1\WeirdCalculator;
use PHPUnit\Framework\TestCase;

class CalculatorTest extends TestCase
{

    public function test_adds()
    {
        $calc = new WeirdCalculator();
        $result = $calc->adds(1,2);
        $this->assertTrue(is_int($result));
        $this->assertEquals(3, $result);
    }

    public function test_subtracts()
    {
        $calc = new WeirdCalculator();
        $result = $calc->subtracts(1,2);
        $this->assertTrue(is_int($result));
        $this->assertEquals(-1, $result);
    }

    public function test_in_array()
    {
        $calc = new WeirdCalculator();
        $result = $calc->inArray(['a','b'], 'a');
        $this->assertTrue(is_string($result));
    }

    public function test_filter_array()
    {
        $calc = new WeirdCalculator();
        $result = $calc->filterArray([1,2,3,10,20,30]);
        $this->assertCount(2, $result);
    }

}

