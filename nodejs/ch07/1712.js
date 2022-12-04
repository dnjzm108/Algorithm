const fs = require('fs');
const input = fs.readFileSync("../dev/stdin").toString().trim().split(" ").map(Number);

let one = input[0]
let two = input[1]
let three = input[2]
let result;

if (two >= three) {
    result = -1
} else {
    let tum = three - two

    result = Math.ceil(one / tum)
    if (one % tum == 0) {
        result += 1
    }
}

console.log(result);