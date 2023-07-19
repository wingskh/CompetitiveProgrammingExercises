// https://www.codewars.com/kata/55f2b110f61eb01779000053/javascript

function getSum(a, b) {
    let smaller;
    let bigger;
    if (a < b) {
        smaller = a;
        bigger = b;
    } else {
        smaller = b;
        bigger = a;
    }
    const length = bigger - smaller + 1;
    return length === 1 ? a : Array.from({ length }, (_, i) => smaller + i).reduce((acc, num) => acc + num, 0);
}

let a = 5;
let b = -1
const result = getSum(a, b);
console.log(result);
// Incorrect answer for a=5, b=-1: expected 4 to equal 14
// Incorrect answer for a=415, b=-84: expected 331 to equal 82750
