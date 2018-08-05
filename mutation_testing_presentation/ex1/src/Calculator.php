<?php
declare(strict_types=1);

namespace Ex1;

class WeirdCalculator
{
    public function adds(int $x, int $y)
    {
        return $x + $y;
    }

    public function subtracts(int $x, int $y)
    {
        return $x + $y;
    }

    public function inArray($arr, $needle)
    {
        foreach ($arr as $elem){
            if($elem == $needle) {
                $result = $elem;
                break;
            }
        }
        return $result;
    }

    public function filterArray($array)
    {
        return array_filter($array, function($elem) {
            return $elem > 10;
        });

    }


}
