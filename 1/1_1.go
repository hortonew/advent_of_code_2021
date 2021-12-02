package main

import (
	"fmt" // print
	"os" // read file
	"bufio" // file scanner
	"strconv" // string to int
)

func main() {
	current_reading := 0
	previous_reading := 0
	increases := 0

	// load file
	f, _ := os.Open("1.txt")
	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		line := scanner.Text()
		previous_reading = current_reading

		// convert line to integer
		current_reading, _ = strconv.Atoi(line)

		// only increase if there was a positive change
		if previous_reading != 0 && current_reading > previous_reading {
			increases += 1 
		}
	}
	fmt.Println(increases)
}