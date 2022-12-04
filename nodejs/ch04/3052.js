const fs = require("fs");
const input = fs.readFileSync("../dev/stdin").toString().trim().split("\n").map(Number);

let arr = [];

for (let i of input) {
    arr.push(i % 42)
}

console.log([...new Set(arr)].length);