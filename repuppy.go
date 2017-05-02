package main

import(
    "fmt"
    "flag"
    "io/ioutil"
    "os"
    "os/exec"
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
        if item.Mode().IsDir() && !isHidden(item.Name()) {
            path := strings.Join([]string{*dir, item.Name()}, "")
            go update(path, *branch)
            // go update(item, branch)
            // launch process that will
            // go into this folder
            // will launch bash command
            // that will update repo
        }
    }
}

func update(path, branch string) {
    os.Chdir(path)
    cmd := exec.Command("git", "pull", "origin", branch)
    err := cmd.Run()
    if err != nil {
        fmt.Println(err)
    }
}

/*
Check if directory/file name contains dot(.)
*/

func isHidden(s string) bool {
    return strings.Contains(s, ".")
}
