package main

import(
    "fmt"
)

func main() {
    a := multiply([]int{1,2,3}...)
    fmt.Println(a)
}

func multiply(args ...int) int {
    result := 0

    for _, value := range args {
        result = result + value
    }

    return result
}
