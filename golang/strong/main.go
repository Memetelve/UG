package main

import (
	"fmt"
	"math"
	"math/big"
	"strconv"
	"strings"
	"time"
)

func convertToASCII(s string) []int {
	var ascii []int
	for _, c := range s {
		ascii = append(ascii, int(c))
	}
	return ascii
}

func stringContainsAll(s string, chars []string) bool {
	for _, c := range chars {
		if !strings.Contains(s, c) {
			return false
		}
	}
	return true
}

func factorial(n int64) *big.Int {
	if n == 0 {
		return big.NewInt(1)
	}
	bigN := big.NewInt(n)
	return bigN.Mul(bigN, factorial(n-1))
}

func reverse(a []int) []int {
	for i, j := 0, len(a)-1; i < j; i, j = i+1, j-1 {
		a[i], a[j] = a[j], a[i]
	}
	return a
}

func fibonacciWithCount(n int, count []int) (*big.Int, []int) {

	count[n] = count[n] + 1

	// fmt.Println("Fibonacci: ", n, count[n])

	if n == 0 {
		return big.NewInt(0), count
	} else if n == 1 {
		return big.NewInt(1), count
	}

	fib1, _ := fibonacciWithCount(n-1, count)
	fib2, _ := fibonacciWithCount(n-2, count)
	value := new(big.Int).Mul(fib1, fib2)

	return value, count
}

func fib(n int) (*big.Int, []int) {
	count := make([]int, n+1)
	count[0] = 0
	count[1] = 1

	return fibonacciWithCount(n, count)
}

func normalFactorial(n uint64) uint64 {
	if n == 0 {
		return 1
	}
	return n * normalFactorial(n-1)
}

func main() {
	nick := "staols"

	nickInAscii := convertToASCII(nick)

	nickInAsciiString := make([]string, len(nickInAscii))
	for i, c := range nickInAscii {
		nickInAsciiString[i] = strconv.Itoa(c)
	}

	fmt.Println("Nick in ASCII: ", nickInAscii)

	var i int64
	var strongNumber int64
	for i = 1; i > 0; i++ {
		factorialValue := factorial(i)

		if stringContainsAll(factorialValue.String(), nickInAsciiString) {
			strongNumber = i
			break
		}
	}

	fmt.Println("Strong number: ", strongNumber)

	_, count := fib(30)
	count = reverse(count)

	// for i, c := range count {
	// 	fmt.Println(30-i, c)
	// }

	weakNumber := 0
	weakNumberDifference := math.Abs(float64(strongNumber - int64(count[0])))

	for i, c := range count {
		diff := math.Abs(float64(strongNumber - int64(c)))
		if diff < weakNumberDifference {
			weakNumber = 30 - i
			weakNumberDifference = diff
		}
	}

	fmt.Println("Weak number: ", weakNumber)

	var z uint64
	for z = 0; z < 30; z++ {
		if new(big.Int).SetUint64(normalFactorial(z)).Cmp(factorial(int64(z))) != 0 {
			fmt.Println("Pure golang implementation fails at: ", z)
			break
		}
	}

	var times []time.Duration

	for g := 20; g < 40; g++ {
		start := time.Now()
		_, _ = fib(g)
		elapsed := time.Since(start)
		times = append(times, elapsed)
		fmt.Println("Fib of ", g, " took: ", elapsed)
	}

	var stepUp float64
	// var stepUps []float64
	for i := 1; i < len(times); i++ {

		if times[i] == 0 || times[i-1] == 0 {
			continue
		}

		stepUp = (stepUp*(float64(i)-1) + float64(times[i].Seconds()/times[i-1].Seconds())) / float64(i)
		// stepUps = append(stepUps, times[i].Seconds()/times[i-1].Seconds())
	}

	// fmt.Println("Step ups: ", stepUps)
	fmt.Println("Step up: ", stepUp)

	// canculate time for 145th fib number
	x := 40
	start := time.Now()
	_, _ = fib(x)
	elapsed := time.Since(start)

	finalTime := elapsed.Seconds() * math.Pow(stepUp, float64(145-x))

	fmt.Println("Time for 145th fib number: ", finalTime)

}
