//Javascript interview qquestion

//! Datatypes in JS
//Primitive  +  Non Primitive datatypes
//1.String  2.Number  3.BigInt  4.Boolean  5.undefined 6.null  7.Symbol
//Object is a non-primitve datatype in JS
/* var name = "Manas";
var age = 21;
var count = true;
var rollno;
var phoneNumber = null;
console.log(name);
console.log(age);
console.log(count);
console.log(rollno);
console.log(phoneNumber);
console.log(typeof count);
 */

//!Function in JS (traditional vs fat arrow function)
/* function print() {
  console.log("Hello manas");
} */
/* const print = () => console.log("manas"); */

//! Hoisting in JS
//Hoisting works with only 'var', 'let' and 'const' doesn't support hoisting
//Hoisting is a default behaviour of JS where all the variable and function declaration are moved to the top
//Only variable declaration are hoisted not the initialization
/* console.log(a);
var a = 10; */

//! '===' is more strict than '=='

//!Dynamically Typed vs Static Typed Language
//JS is a dynamically(loosely) typed language
//In a dynamically typed language, the type of a variable is checked during run-time in contrast to statically typed language, where the type of a variable is checked during compile-time.
//For example =>  let x=100 (type NUmber )   x='Manas' (type is string)

//!NaN in JS stands for Not A Number
// console.log(isNaN("23"));

//!Pass by value AND Pass by reference in JS
//Primitive datatypes are passed by value
//Non primitive datatypes are passed by reference
// var a = 10;
// var b = a;
// console.log(a, b);
// a = 100;
// console.log(a, b);

// var a = { name: "manas", age: 22 };
// var b = a;
// console.log(a, b);
// a.age = 21;
// console.log(a, b);

//!IIFE (Immediately Innovked function ) in JS
/*( () => {
    console.log("hello manas");
  }
)();
 */

//! High order function in JS
//A high order function is a function that takes another function as a argument or return another function
//Inbuilt high order functions are map(),forEach() etc...
/* fruits = ["mango", "orange", "apple"];
fruits.forEach((item) => console.log(item)); */

//! var vs let vs const

//!Temporal Dead zone
//The let and const variables exist in the TDZ from the start of their enclosing scope until they are declared.
// a = 23;
// let a;
// console.log(a);

//! We can redeclare variable created using var keyword
/* var b = 100;
var b = 10;
console.log(b); */

//!Array destructuring or unpacking
/* let nums = [100, 200, 300, 400];
let a = nums[0];
let b = nums[1];
let c = nums[2];
let d = nums[3];
let [a, b, c, d] = nums;
console.log(a, b, c, d);
 */

//! Object destructuring
/* let myBio = {
  name: "Jack",
  age: 52,
  profession: "US Army",
};
const name = myBio.name;
const age = myBio.age;
const profession = myBio.profession;
const { age: myAge, profession: myProfession, name: myName } = myBio;
console.log(myName, myAge, myProfession); */

//!Class in JS was introduced in ES6
//this keyword refers to the current instance of the class
/* class Student {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  display() {
    console.log(this.name, this.age);
  }
}

s1 = new Student("Jack", 52);
s2 = new Student("John Wick", 45);
s1.display();
s2.display();
console.log(s2.age); */

//!Promises in JS
//Promises is used with asynchronous operations
//Before promises, callbacks were used to handle asynchronous operations. But due to limited functionality of callback, using multiple callbacks to handle asynchronous code can lead to unmanageable code.
//Promise in JS has 4 states => Pending , Rejected , Fullfilled , Settled
//Before promises we use callbacks to perform asyn operations

//!this keyword behaviour in traditional vs fat arrow function
//this keyword in traditional function refers to the object calling the function
//While this keyword in fat arrow function does not refers to the object calling it , it refers to the object parent's object

//!DOM in JS
//Dom stands for document object model, when the brower pareses the html document ,it creates a object of it called as DOM, with this object we can directly manipulate the document
