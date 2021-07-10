#!/usr/local/bin/node
// js variables use let and const
// execution is made one line at a time, from top to bottom
// increment -- and decrement ++ (depending what goes first)
/* += *= /= <= =>
 == the type does not matter 5 == '5'
 === type matters 5 !== '5'
 Ternary operator (expression) ? a : b
 */
// to clear the console:
console.clear()

let num1 = 3;
let num2 = 5;

let sum = num1 + num2;
console.log(typeof(sum))
// toString() number as input and returns a string
console.log(num1.toString())
console.log(num2.toString())

let strNum1 = "10";
let strNum2 = "11.5";
let strNum3 = "ABC";

// parseInt() string numeral as input and returns a number
console.log(parseInt(strNum1));
console.log(parseInt(strNum2));
console.log(parseInt(strNum3));

// parseFloat() string numeral as an input and returns a foating
console.log(parseFloat(strNum2))
console.log(parseFloat(strNum3))

// toFixed() takes floating number and rounds it off to given position

let strFloat = 87.987653;
console.log(strFloat.toFixed())
console.log(strFloat.toFixed(2))
console.log(strFloat.toFixed(5))
console.log(strFloat.toFixed(10))

let myFirstString = "This is a string for Javascript string functions, Javascript"
// Find index of a string inside another string
console.log(myFirstString.indexOf('Javascript'))
console.log(myFirstString.indexOf('This'))

// Find LAST index of a string inside another string
console.log(myFirstString.lastIndexOf('Javascript'))
console.log(myFirstString.lastIndexOf('This'))

// Get a part of our string slice(start, end)
console.log(myFirstString.slice(0, 4))
console.log(myFirstString.slice(21, 31))
//this goes from -10 to end
console.log(myFirstString.slice(-10))
//this goes from 5 to end
console.log(myFirstString.slice(5))

// Get sub string function - substr(startPos, length)
console.log(myFirstString.substr(0, 4))
console.log(myFirstString.substr(21, 10))
// from 21 to end
console.log(myFirstString.substr(21))

let withStrings = "this is my new project called \"new\""


console.log(sum);

console.log(withStrings.length);
// converts the whole string:
console.log(withStrings.toUpperCase());
console.log(myFirstString.toLowerCase());

let newString = "to add more words"
// to join strings:
console.log(withStrings.concat(myFirstString))
console.log(withStrings.concat(" ", myFirstString, newString))

// another way to concat strings:
console.log(withStrings + ' ' + myFirstString + newString)

// trim to remove extra spaces:
let seconString = 'new    function    for'
console.log(seconString.trim())
// to print a char in a given index 
console.log(newString.charAt(5))

//to split a string considering the arguments passed gives an array
console.log(newString.split(' '))

if (5 > 7) {
	console.log('5 > 7')
} else if(7 > 8){ 
	console.log('7 > 8')
} else {
	console.log('Nothing')
}

let length = 200;
let height = 200;
 
if (length === height){
    console.log('is a square')
} else {
    console.log('is a rectangle')
}

let grade = 77
if (grade > 60 && grade < 80){
    console.log( grade = 'B')
}