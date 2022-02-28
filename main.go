package main

import (
	"fmt"
	"strings"
	"time"
)

func main() {
	//fmt.Println("Hello World")
	start := time.Now()
	words := [9]string{"Adele", "Elaine", "Elizabeth", "Harriet", "Ingrid", "Michelle", "Isabella", "BELLAA", "Ella"}
	search := "Ella"
	count := [9]int{0}

	s := strings.ToLower(search)
	for i, word := range words {
		w := strings.ToLower(word)

		//count := make([]int, len(words))
		if strings.Contains(w, s) {
			if w == s {
				count[i] = 0
			} else {
				count[i] = 1
			}
		} else {
			count = contained_in_words(s, w, count, i)
			indexes := find_indexes(w, s)
			count = consecutive(indexes, count, i)
			count = right_order(indexes, count, i)

		}
	}
	for i, word := range words {
		fmt.Println(word, count[i])
	}
	end := time.Now()
	fmt.Println(end.Sub(start))
}

func contained_in_words(search string, word string, count [9]int, ind int) [9]int {
	search_list := word_to_list(search)
	for _, b := range search_list {
		if strings.Contains(word, b) {
			word = strings.Replace(word, b, "", 1)
		} else {
			count[ind] += 1
		}
	}
	return count
}
func find_indexes(word string, search string) [4]int {
	indexes := [4]int{0}
	letters := word_to_list(search)
	for i, letter := range letters {
		index := strings.Index(word, letter)
		if index != -1 {
			word = strings.Replace(word, letter, "1", 1)
			indexes[i] = index
		} else {
			indexes[i] = -2
		}
	}
	return indexes
}

func consecutive(indexes [4]int, count [9]int, ind int) [9]int {
	for j := 0; j < len(indexes)-1; j++ {
		if indexes[j+1]-indexes[j] != 1 {
			count[ind] += 1
		}
	}
	return count
}
func right_order(indexes [4]int, count [9]int, ind int) [9]int {
	temp := -1
	for j := 0; j < len(indexes)-1; j++ {
		if temp == -1 {
			if indexes[j] >= indexes[j+1] {
				count[ind] += 1
				if indexes[j+1] == -2 {
					temp = j
				} else {
					temp = j + 1
				}
			}
		} else {
			if indexes[temp] >= indexes[j+1] {
				count[ind] += 1
				if indexes[j+1] == -2 && indexes[j] != -2 {
					temp = j
				} else if indexes[j+1] == -2 && indexes[j] == -2 {
					continue
				} else {
					temp = j + 1
				}
			} else {
				temp = j + 1
			}
		}
	}
	return count
}

func word_to_list(word string) []string {
	word_list := []rune(word)
	list := []string{}
	for i := 0; i < len(word); i++ {
		char := string(word_list[i])
		list = append(list, char)
	}
	return list
}
