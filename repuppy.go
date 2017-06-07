package main

import(
    "fmt"
    "flag"
    "io/ioutil"
    "os"
    "os/exec"
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
    base, _ := filepath.Abs(".")
    fmt.Println(base)
    fmt.Println("----------------------")
    for _, item := range items {
        if item.Mode().IsDir() && !isHidden(item.Name()) {
            repoPath := strings.Join([]string{base, item.Name()}, "/")
            update(repoPath, *branch)
        }
    }
}

func update(path, branch string) {
    fmt.Println("Updating ...", path)
    os.Chdir(path)
    // this is just checking that we `cd` to proper directory
    pwd, _ := os.Getwd()
    fmt.Println(pwd)
    err := exec.Command("git", "pull", "origin")
    if err == nil {
        fmt.Println("Ooooops")
    }
}

/*
Check if directory/file name contains dot(.)
*/

func isHidden(s string) bool {
    return strings.Contains(s, ".")
}
