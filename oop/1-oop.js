class Person {
  constructor(first, last, age, gender) {
    this.name = {
      first,
      last
    }
    this.age = age
    this.gender = gender
  }

  greeting() {
    console.log(`Hi! My name is ${this.name.first}`)
  }
}

class Teacher extends Person { 
  constructor(first, last, age, gender, subject) { 
    super(first, last, age, gender)
    this.subject = subject
  }
}

class Student extends Person { 
  constructor(first, last, age, gender, house) {
    super(first, last, age, gender)
    this.house = house
  }
}

let dumbledore = new Teacher('Albus', 'Dumbledore', 70, 'Male', 'Potion') 
let ronald = new Student('Ronald', 'Weasley', 18, 'Male', 'Gryffindor') 
let hermione = new Student('Hermione', 'Granger', 18, 'Female', 'Gryffindor') 

console.log(dumbledore.constructor) 
console.log(ronald.age)