const fs = require('fs');
const input = fs.readFileSync("../dev/stdin").toString().trim().split(/\s+/).map(Number);

let a = input[0]
let b = input[1] + input[2]



if (b >= 60) {
    a = a + Math.floor(b / 60)
    b = b % 60
    if (a >= 24) {
        a = a - 24
    }
    console.log(a, b);
} else {
    if (a >= 24) {
        a = a - 24
    }
    console.log(a, b)
}