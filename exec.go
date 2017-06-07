// Sometimes our Go programs need to spawn other, non-Go
// processes. For example, the syntax highlighting on this
// site is [implemented](https://github.com/mmcgrana/gobyexample/blob/master/tools/generate.go)
// by spawning a [`pygmentize`](http://pygments.org/)
// process from a Go program. Let's look at a few examples
// of spawning processes from Go.

package main

import "fmt"
import "os/exec"

func main() {

    // We'll start with a simple command that takes no
    // arguments or input and just prints something to
    // stdout. The `exec.Command` helper creates an object
    // to represent this external process.
    dateCmd := exec.Command("date")

    // `.Output` is another helper that handles the common
    // case of running a command, waiting for it to finish,
    // and collecting its output. If there were no errors,
    // `dateOut` will hold bytes with the date info.
    dateOut, err := dateCmd.Output()
    if err != nil {
        panic(err)
    }
    fmt.Println("> date")
    fmt.Println(string(dateOut))
}
