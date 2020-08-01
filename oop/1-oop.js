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

let dumbledore = new Teacher('Albus', 'Dumbledore', 70, 'Male', 'Potion')

console.log(dumbledore)
dumbledore.greeting()
