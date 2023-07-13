// https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/javascript
function persistence(num) {
    let counter = 0;
    let newNum = num;
    while (newNum >= 10) {
        const numStr = [...newNum.toString()];
        newNum = numStr.reduce((total, numChar) => total * parseInt(numChar))
        counter += 1;
    }
    return counter;
}


const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Persistent Bugger.", () => {
  it("Fixed tests", () => {
    assert.strictEqual(persistence(39),3);
    assert.strictEqual(persistence(4),0);
    assert.strictEqual(persistence(25),2);
    assert.strictEqual(persistence(999),4);
  });
});