package main

import "fmt"

func main() {
	var l int8 = 127
	// var ll int8 = -128

	fmt.Printf("%T\n", l)
	fmt.Printf("%b\n", l)

	fmt.Println(l)
	fmt.Println(l + 1)

	// print type of variable
	fmt.Printf("%T\n", l)
	fmt.Printf("%b\n", l)

}
