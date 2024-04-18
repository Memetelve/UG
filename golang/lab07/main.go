package main

import "fmt"

type Human struct {
  name string
}
func giveBirth(name string) Human {
  return Human{name: name}
}

func (human Human) say(message string) {
  fmt.Println(human.name + " says " + message)
}

type Student struct {
  Human
  age int8
}
func enroll(name string) Student {
  return Student{Human: giveBirth(name), age: 1}
}

type Master struct {
  Human
  title string
}
func (master Master) sayTitle() {
  fmt.Println(master.name + " is a master of " + master.title)
}


type Doctor struct {
  Master
  title string
}
func (doctor Doctor) sayTitle() {
  fmt.Println(doctor.name + " is a doctor of " + doctor.title)
  fmt.Println(doctor.name + " is a master of " + doctor.Master.title)
}



type Someone interface {
  sayTitle()
}

func main()  {
  var student Student = enroll("John") 
  
  var master Master = Master{Human: giveBirth("Jane"), title: "Mathematics"}
  
  var doctor Doctor = Doctor{Master: Master{Human: giveBirth("Alice"), title: "Mathematics"}, title: "Physics"}
  
  say(student, master, doctor)
}


func say(someone ...Someone) {
  for _, theOne := range someone {
    if hasTitle(theOne) {
      theOne.sayTitle()
    }
  }
}

func hasTitle(someone interface{}) bool {
  _, ok := someone.(Someone)
  return ok
}
