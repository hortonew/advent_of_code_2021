package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	horizontal_pos := 0
	depth := 0

	f, _ := os.Open("2.txt")
	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		line := scanner.Text()
		reading := strings.Split(line, " ")
		movement_type := reading[0]
		movement_str := reading[1]
		movement, _ := strconv.Atoi(movement_str)

		// depth
		if movement_type == "down" {
			depth += movement
		} else if movement_type == "up" {
			depth -= movement
		} else {
			horizontal_pos += movement
		}
	}

	calculation := horizontal_pos * depth
	fmt.Println(calculation)
}
