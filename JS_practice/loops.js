#!/usr/local/bin/node

/* while (condition){
    code
}
*/

let number = 1

while (number < 10){
    console.log(number++)
}

while (number < 10){
    number++
}
console.log(number)

let numbers = [1, 2, 3, 4, 5]
let position = 0
for (position > 0; position < numbers.length; position++){
    if (position == 2){
        break
    }
    console.log('position -> ' + position + ' value -> ' + numbers[position]) 
}
console.log('=======================')

// like a mini break
let numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
let positions = 0
for (positions > 0; positions < numero.length; positions++){
    if (positions % 2 === 0){
        continue
    }
    console.log('position -> ' + positions + ' value -> ' + numero[positions]) 
}

let phrase = 'Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence.'
let newphrase = ''

let i = 0

for (i > 0; i < phrase.length-1; i++) {
        if (phrase[i] === 'a' || phrase[i] === 'e'){
       newphrase = phrase.replace(/a/g, '4').replace(/e/g, '5')
        }
       
}   
console.log(newphrase)
    

// find how many vowels are in a string

let newString2 = 'Good, better, best. Never let it rest. \'Til your good is better and your better isbest.'
let count = 0
for (let i = 0; i < newString2.length; i++) {
    if (newString2[i] === 'a' || newString2[i] === 'e' || newString2[i] === 'i' || newString2[i] === 'o' || newString2[i] === 'u'){
        count++
    }
}
console.log(count)

// swap uppercase and lowercase

let newString3 = 'The Quick Brown Fox'
let lower = 'abcdefghijklmnopqrstuvwxyz'
let upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
let newnew = []

for (let i = 0; i < newString3.length; i++) {
    if (upper.indexOf(newString3[i]) !== -1) {
        newnew.push(newString3[i].toLowerCase())
    }
    else if (lower.indexOf(newString3[i]) !== -1) {
        newnew.push(newString3[i].toUpperCase())
    }
    else {
        newnew.push(newString3[i])
    }
}
console.log(newnew.join(''))

function swap(str) {
    str = str.toString();
    let newStr = '';
    
    for(let i = 0; i < str.length; i++){
    if(str[i] === str[i].toUpperCase()){
    newStr += str[i].toLowerCase();
    }else{
    newStr += str[i].toUpperCase();
    
    }
    }
    return newStr;
    }
    
    console.log(swap('The Quick Brown Fox'));

// reverse words

let reverse = 'There is exactly one space between each word and no punctuation is used.'
let s = ''
//let newReverse = reverse.split(' ')
//let j = 0
for ( let i = reverse.length - 1; i >= 0; i--){
    
        s += reverse[i]

}
console.log(s)
// reverse only odd length words
let reversed = 'There is exactly one space between each word and no punctuation is used.'
let newReverse = reversed.split(' ')

let j = 0
for ( let i = 0; i < newReverse.length - 1; i++){
    if (newReverse[i].length % 2 !== 0){
    newReverse[i] = newReverse[i].split('').reverse().join('')
    }
    
    else {
        newReverse[i] = newReverse[i].split('').join('')
    }
   
}
console.log(newReverse.join(' '));