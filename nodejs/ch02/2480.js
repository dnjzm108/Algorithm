const fs = require('fs');
let input = fs.readFileSync('../dev/stdin').toString().trim().split(" ").map(Number);

input.sort((a, b) => { return b - a })

const a = input[0]
const b = input[1]
const c = input[2]

if (a == b && b == c && a == c) {
    console.log(10000 + a * 1000);
} else if (a == b || b == c || a == c) {
    console.log(1000 + b * 100)
} else {
    console.log(a * 100)
}
