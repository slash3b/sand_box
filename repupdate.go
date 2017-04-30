package main

import(
    "fmt"
    "flag"
)



func main() {
    folder := flag.String("dir", "./", "Folder that needs to be searched for repositories. Defaults to current directory")
    branch := flag.String("br", "develop", "Branch that needs to be pulled")
    flag.Parse()

    fmt.Println(*folder)
    fmt.Println(*branch)
}
