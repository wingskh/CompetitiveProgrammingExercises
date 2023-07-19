// https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/javascript

function openOrSenior(data) {
    return data.map((member) => member[0] >= 55 && member[1] > 7 ? 'Senior' : 'Open');
}

openOrSenior([[45, 12], [55, 21], [19, -2], [104, 20]]); // ['Open', 'Senior', 'Open', 'Senior']
openOrSenior([[3, 12], [55, 1], [91, -2], [53, 23]]); // ['Open', 'Open', 'Open', 'Open']
openOrSenior([[59, 12], [55, -1], [12, -2], [12, 12]]); // ['Senior', 'Open', 'Open', 'Open']
