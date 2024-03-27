package main

import (
	"bytes"
	"fmt"
	"os"
	"os/exec"
)

func main()  {
  cmd := exec.Command("cat")
  var out bytes.Buffer
  var input bytes.Buffer
  cmd.Stdout = &out
  cmd.Stdin = os.Stdin

  err := cmd.Start()
  if err != nil {
    panic(err)
  }
  
  fmt.Println("Mamma mia")

  for {
    msg, err := out.ReadBytes('\n')
    fmt.Print(string(msg))


    if err != nil && err.Error() != "EOF"{
      fmt.Println("Error: ", err)
      break
    }

    // var my_input []byte
    // fmt.Scan(&my_input)
    // fmt.Println("Input: ", string(my_input))
    
    input = bytes.Buffer{}
    fmt.Scan(&input)
    cmd.Stdin = &input
  }
}
