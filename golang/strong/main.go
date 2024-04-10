package main

import (
	"fmt"
	"strconv"
	"strings"
)

func stringContains(s string, c string) bool {
  return strings.Contains(s, c)
}

func factorial(n int) int {
  if n == 0 {
    return 1
  }
  return n * factorial(n-1)
}

func convertToASCII(s string) []int {
	var ascii []int
	for _, c := range s {
		ascii = append(ascii, int(c))
	}
	return ascii
}

func main() {
	nick := "macmar"

	nickInAscii := convertToASCII(nick)
  
  var fakeNumber string
  for _, i := range nickInAscii {
    fakeNumber += strconv

  fmt.Println(fakeNumber)

  var i int
  for {
    factorialValue := factorial(i)
    if
    i++
  }
}
