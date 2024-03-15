package main

import (
	"fmt"
)

func collatz(x int, s []int) ([]int, int ) {
  s = append(s, x) 

  if x == 1 {
    return s, len(s) - 1
  }

  if x % 2 == 0 {
    return collatz(x / 2, s)
  } else {
    return collatz(3 * x + 1, s)
  }

}

func main() {

  

  var all []int
  var longest_number int
  var longest_operations int

  longest_operations = 0

  for i := 1; i <= 1000; i++ {
    _, number_of_operations := collatz(i, []int{})
    all = append(all, number_of_operations)

    if number_of_operations > longest_operations {
      longest_operations = number_of_operations
      longest_number = i
    }
  }
  
  fmt.Printf("Logest calculation for %d of %d operations\n", longest_number, longest_operations)

  var sum int 
  for i := 0; i <= 999; i++ {
    sum += all[i]
  }

  fmt.Println(float64(sum) / float64(len(all)))
}
