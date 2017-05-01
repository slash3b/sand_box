package main

import(
    "fmt"
    "flag"
    "io/ioutil"
    "os"
    // "os/exec"
    "strings"
)



func main() {
    dir := flag.String("dir", "./", "Folder that needs to be searched for repositories. Defaults to current directory")
    branch := flag.String("br", "develop", "Branch that needs to be pulled")
    flag.Parse()

    // items, err := os.ReadDir(*dir)
    items, err := ioutil.ReadDir(*dir)
    if err != nil {
        os.Exit(2)
    }
    for _, item := range items {
        // fmt.Printf("%T", item)
        // fmt.Println()
        // name := item.Name()
        if item.Mode().IsDir() && !isHidden(item.Name()) {
            path := strings.Join([]string{*dir, item.Name()}, "")
            fmt.Println(path)
            // cmd := exec.Command()
            // go update(item, branch)
            // launch process that will
            // go into this folder
            // will launch bash command
            // that will update repo
        }
    }
    fmt.Println(*branch)
}

/*
Check if directory/file name contains dot(.)
*/

func isHidden(s string) bool {
    return strings.Contains(s, ".")
}
