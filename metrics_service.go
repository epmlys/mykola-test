// go metrics service
package main

import (
	"fmt"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "bx_space 2323\n bx_latency 100\n path %s", r.URL.Path[1:])
}

func main() {
	http.HandleFunc("/metrics", handler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
