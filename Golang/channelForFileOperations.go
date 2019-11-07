package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"

	"github.com/labstack/echo"
)

type FileData struct {
	filePath string
	fileData []byte
}

func main() {
	go getFiles()
	e := echo.New()
	e.Logger.Fatal(e.Start(":1323"))
}

func getFiles() {

	files, err := ioutil.ReadDir("files")
	if err != nil {
		log.Fatal(err)
	}
	filePathsChan := make(chan string)
	fileDataChan := make(chan FileData)
	processedFileDataChan := make(chan FileData)

	go worker(filePathsChan, fileDataChan, processedFileDataChan)
	go worker(filePathsChan, fileDataChan, processedFileDataChan)
	go worker(filePathsChan, fileDataChan, processedFileDataChan)

	for i := 0; i < len(files); i++ {
		filePathsChan <- files[i].Name()
	}
	close(filePathsChan)
}

func worker(filePathsChan chan string, fileDataChan chan FileData, processedFileDataChan chan FileData) {
	go processFiles(fileDataChan, processedFileDataChan)
	go readFile(filePathsChan, fileDataChan)
	go writeFiles(processedFileDataChan)
}

func readFile(filePathsChan chan string, fileDataChannel chan FileData) {

	for {
		filePath := <-filePathsChan
		contents, err := ioutil.ReadFile("files/" + filePath)
		if err != nil {
			fmt.Println(err)
		}
		fd := FileData{}
		fd.fileData = contents
		fd.filePath = filePath
		fileDataChannel <- fd
	}
}
func processFiles(fileWriteDataChan, processedFileDataChan chan FileData) {
	for {
		fd := <-fileWriteDataChan
		fd.fileData = append(fd.fileData, []byte(" Processed successfully..!")...)
		processedFileDataChan <- fd
	}
}
func writeFiles(processedFileDataChan chan FileData) {
	for {
		fd := <-processedFileDataChan
		err := ioutil.WriteFile("processedFiles/"+fd.filePath, fd.fileData, 0644)
		if err != nil {
			fmt.Println(err)
		}
		fmt.Println(fd.filePath)
	}
}

func genFiles() {
	for i := 0; i < 10000; i++ {
		idStr := strconv.Itoa(i)
		fileContents := "Hey, hi. This is sandeep. My roll number is : " + idStr
		filePath := "files/" + idStr
		err := ioutil.WriteFile(filePath, []byte(fileContents), 0644)
		if err != nil {
			fmt.Println(err)
		}
	}
}
