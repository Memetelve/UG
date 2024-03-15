package main

import (
	"fmt"
	"math"
)


func main() {
  var a int
  var b int 
  var c int

  leng, err := fmt.Scan(&a, &b, &c)

  if err != nil {
    fmt.Print(err, leng)
    return 
  }

  delta := int(math.Pow(float64(b), float64(2))) - 4*a*c

  if delta < 0 {
    fmt.Print("Delta jest mniejsza od zera, nie ma pierwsiatków")
  } else if delta == 0 {
    x1 := (-1 * b - int(math.Sqrt(float64(delta)))) / 2 * a
    fmt.Print(x1)
  } else {
    x1 := (-1 * b - int(math.Sqrt(float64(delta)))) / 2 * a
    x2 := (-1 * b + int(math.Sqrt(float64(delta)))) / 2 * a

    fmt.Println(x1, x2)
  }

}
