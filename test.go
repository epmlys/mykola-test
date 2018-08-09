package main

import (
	"fmt"
	"io"
	"math/rand"
	"os"
	"runtime"
	"runtime/debug"
	"sort"
	"strconv"
	"sync"
	"time"
)

type Add func(a int, b int) int

var (
	counter = 0
	lock    sync.Mutex
)

func main() {
	// channels producer-consumer
	ch := make(chan int)
	for i := 0; i < 5; i++ {
		worker := &Worker{id: i}
		go worker.process(ch)
	}

	for {
		select {
		case ch <- rand.Int():
			fmt.Println(len(ch))
		case <-time.After(5000):
			fmt.Println("timeout")
			//default:
			//	fmt.Println("dropped")
		}
		time.Sleep(500)
	}

	/*
		// deadlock
		go func() { lock.Lock() }()
		time.Sleep(10000)
		lock.Lock()

		// synchronization
		for i := 0; i < 20; i++ {
			go incr()
		}
		time.Sleep(10000)
	*/
	// gorountine
	fmt.Println("start")
	go func() {
		fmt.Println("processing...")
	}()
	time.Sleep(10000)
	fmt.Println("done.")

	// function type, func as first-class type/object
	fmt.Print("Sum is: ")
	fmt.Println(process(func(a int, b int) int {
		return a + b
	}))
	// strings and byte arrays
	// sa := "the spice must flow"
	// ba := []byte(sa)
	// fmt.Println(len(ba))
	// fmt.Println(len(sa))
	// sb := string(ba)
	// fmt.Println(sb)
	// fmt.Println(len(""))

	// error handling
	if len(os.Args) != 2 {
		fmt.Println("Args should be 2, Exiting..")
		os.Exit(1)
	}
	checkType(os.Args[1])

	// defer
	file, err := os.Open("file")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	// package error variable
	var input int
	_, er := fmt.Scan(&input)
	if er == io.EOF {
		fmt.Println("No more input!")
	}

	num, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println("not a valid number")
	} else {
		fmt.Println(num)
	}

	// slices
	scores := make([]int, 0, 10)
	scores = scores[0:8]
	scores[7] = 9090
	fmt.Println("Scores len:", len(scores))

	scor := make([]int, 0, 5)
	c := cap(scor)
	fmt.Println("cap c: ", c)

	for i := 0; i < 25; i++ {
		scor = append(scor, i)

		if cap(scor) != c {
			c = cap(scor)
			fmt.Println("cap c: ", c)
		}
	}

	slice := scor[2:4]
	slice[0] = 9999
	scor = removeAtIndex(scor, 3)
	fmt.Println("scor:", scor)

	scor = make([]int, 100)
	for i := 0; i < 100; i++ {
		scor[i] = int(rand.Int31n(100))
	}
	sort.Ints(scor)
	worst := make([]int, 3)
	copy(worst, scor)
	fmt.Println("Worst:", worst)
	//------- maps -----------------------------
	look := map[string]int{
		"one": 9001,
		"two": 2039,
		"fuc": 1,
	}

	for key, val := range look {
		fmt.Println(key, val)
	}
	//------------------------------------------
	power, is_value := getPower()
	// name, power := "Mykola", 8999
	fmt.Println("Running", os.Args[0])
	fmt.Printf("%v's power Is over %v\n", is_value, power)

	n := &Ninja{
		Person: &Person{"Makamutu"},
		power:  90,
	}
	n.super()
	n.Introduce()
	fmt.Println(n.power)

	var memStats runtime.MemStats
	runtime.ReadMemStats(&memStats)
	fmt.Println(memStats.NumGC)
	fmt.Println(runtime.NumGoroutine())

	var stats debug.GCStats
	debug.ReadGCStats(&stats)
	fmt.Printf("%d", stats.PauseTotal)
}

// channels producer-consumer
type Worker struct {
	id int
}

func (w *Worker) process(c chan int) {
	for {
		data := <-c
		fmt.Printf("worker %d got %d\n", w.id, data)
		time.Sleep(500000)
	}
}

// synchronization concurency
func incr() {
	lock.Lock()
	defer lock.Unlock()
	counter++
	fmt.Println(counter)
}

// func as first-class type
func process(adder Add) int {
	return adder(2, 3)
}

func checkType(a interface{}) {
	// empty interface and conversion
	switch a.(type) {
	case int:
		fmt.Println("this is integer!")
	case bool, string:
		fmt.Println("This is string!")
	}
}

func removeAtIndex(source []int, index int) []int {
	lastIndex := len(source) - 1
	//swap the walue with last to return slice without it
	source[index], source[lastIndex] = source[lastIndex], source[index]
	return source[:lastIndex]
}

func (n *Ninja) super() {
	n.power += 1000
}

func getPower() (int, bool) {
	return 9002, false
}

type Person struct {
	name string
}

func (p *Person) Introduce() {
	fmt.Printf("Hi, I'am %v\n", p.name)
}

type Ninja struct {
	*Person
	power int
}

func (n *Ninja) Introduce() {
	fmt.Printf("Hi, I'am ninja %s\n ", n.name)
}

//func newNinja(name string, power int) *Ninja {
//	return &Ninja{
//		name:  name,
//		power: power,
//	}
//}
