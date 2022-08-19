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
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	if n != 1 {
		stringMap := make([]string, n)
		for i := 0; i < n; i++ {
			scanner.Scan()
			stringMap[i] = scanner.Text()
		}
		var last int
		for i := 0; i < n-1; i++ {
			scanner.Scan()
			text := strings.Fields(scanner.Text())
			t0, _ := strconv.Atoi(text[0])
			t1, _ := strconv.Atoi(text[1])
			stringMap[t0-1] += stringMap[t1-1]
			stringMap[t1-1] = ""
			last = t0 - 1
		}
		fmt.Println(stringMap[last])
	} else {
		scanner.Scan()

		fmt.Println(scanner.Text())
	}

}
