#!/usr/local/bin/node

let mAgera = {
	name: "Agera",
	manufacturer: {
		name: "Koenigsegg",
		loaction: "Sweden"
	},
	topSpeed: 429,
	color: "Black",
	spoilers: false,
}

console.log(mAgera.name)
console.log(mAgera.topSpeed)
console.log(mAgera.manufacturer)
console.log(mAgera.manufacturer.name)

let newArray = ['blue', 'green', 'white']
console.log(newArray)
console.log(typeof newArray)

console.log(newArray[2])

// update values
newArray[0] = 'red'
console.log(newArray)

// add more items

newArray[3] = 'gold'
console.log(newArray)

newArray[newArray.length - 1] = 'Fuxia'
console.log(newArray)
//adds news items to the end of an array
newArray.push("gray")
console.log(newArray)

// delete a value
newArray.pop(newArray)
console.log(newArray)

let secondNew = newArray.pop(newArray)
console.log(secondNew)
console.log(newArray)

let newArrays = ['blue', 'green', 'white', 'grey', 'red']
newArrays.splice(1, 1, 'fuxia', 'skyblue')
//the first element is to indicate where to start
// the second is to indicate how many deleted
// the others are to add to the array
console.log(newArrays)

newArrays.sort()
console.log(newArrays)