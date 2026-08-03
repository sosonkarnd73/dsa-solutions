package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	//fmt.Print("Enter w: ")

	// Scan reads a line of input
	if scanner.Scan() {
		inputStr := scanner.Text()
		inputStr = strings.TrimSpace(inputStr)
		convertedUint, err := strconv.ParseUint(inputStr, 10, 64)
		if err != nil {
			fmt.Println("Error converting to uint:", err)
			return
		}

		if convertedUint%2 == 0 && convertedUint > 2 {
			fmt.Println("YES")
		} else {
			fmt.Println("NO")
		}
		//fmt.Printf("Successfully converted! Value: %d, Type: %T\n", convertedUint, convertedUint)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading input:", err)
	}
}
