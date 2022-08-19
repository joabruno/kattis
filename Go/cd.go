package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for {
		var jack_val, jill_val int
		scanner.Scan()
		fmt.Sscanf(scanner.Text(), "%d %d", &jack_val, &jill_val)

		if jack_val == 0 && jill_val == 0 {
			break
		}
		jack_set := make([]bool, 2000001)
		largest := 0
		for i := 0; i < jack_val; i++ {
			var j int
			scanner.Scan()
			j, _ = strconv.Atoi(scanner.Text())
			jack_set[j] = true
			largest = j
		}
		counter := 0
		for i := 0; i < jill_val; i++ {
			var i int
			scanner.Scan()

			i, _ = strconv.Atoi(scanner.Text())
			if largest < i {
				continue
			}
			if jack_set[i] {
				counter++
			}
		}
		fmt.Println(counter)
	}
}
