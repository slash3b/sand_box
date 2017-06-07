package main

import(
    "fmt"
    "flag"
    "io/ioutil"
    "os"
//    "os/exec"
    "strings"
    "path/filepath"
)

func main() {
    dir := flag.String("dir", "./", "Folder that needs to be searched for repositories. Defaults to current directory")
    branch := flag.String("br", "develop", "Branch that needs to be pulled")
    flag.Parse()

    // items, err := os.ReadDir(*dir)
    items, err := ioutil.ReadDir(*dir);
    if err != nil {
        fmt.Println(err)
        os.Exit(2)
    }
    for _, item := range items {
        if item.Mode().IsDir() && !isHidden(item.Name()) {
            update(item.Name(), *branch)
        }
    }
}

func update(path, branch string) {
    fmt.Println("Updating ...", path)
    realPath, _ := filepath.Abs(strings.Join([]string{"./", path},""))
    fmt.Println(realPath)
}

/*
Check if directory/file name contains dot(.)
*/

func isHidden(s string) bool {
    return strings.Contains(s, ".")
}
