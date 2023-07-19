// https://www.codewars.com/kata/54e6533c92449cc251001667/javascript

var uniqueInOrder = function (iterable) {
    return [...iterable].filter((char, index) => char != iterable[index - 1]);
}

const result = uniqueInOrder('AAAABBBCCDAABBB') // ['A', 'B', 'C', 'D', 'A', 'B']
console.log(result)
