// coro_test.go
package main

import (
	"fmt"
)

func main() {
	a := 1
	b := 2

	go func() {
		b = a * b
	}()

	a = b * b

	fmt.Println("Hit Enter to see the answer")
	fmt.Scanln()

	fmt.Printf("a = %d, b = %d\n", a, b)
}
