const fs = require('fs');
const input = fs.readFileSync('../dev/stdin').toString().trim().split(" ").map(Number);

const a = input[0]
let num = 0;

for (let i = 1; i <= a; i++) {
    num += i
}

console.log(num);