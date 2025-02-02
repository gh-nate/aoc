.PHONY: run
run: main
	./main input

main: main.go
	go vet main.go
	gofmt -l -w -s main.go
	go build main.go
