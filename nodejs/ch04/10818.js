const fs = require('fs');
const input = fs.readFileSync('../dev/stdin').toString().trim().split("\n");

const count = parseInt(input[0]);
const arr = input[1].split(" ").map(Number);

let up = arr[0];
let down = arr[0];

for (let i = 1; i < count; i++) {
    if (up < arr[i]) { up = arr[i] }
    if (down > arr[i]) { down = arr[i] }
}

console.log(`${down} ${up}`);