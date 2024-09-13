package main

import "fmt"

func main() {
	config1 := GetInstancia()
	config2 := GetInstancia()

	config1.URL = "http://exemplourl.com"
	fmt.Println(config2.URL)

	fmt.Println(config1 == config2) 
}