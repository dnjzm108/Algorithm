const fs = require('fs');
const input = fs.readFileSync("../dev/stdin").toString().trim().split("\n");

const a = parseInt(input[0]);

for (let i = 1; i <= a; i++) {
    let [b, c] = input[i].split(" ")
    console.log(parseInt(b) + parseInt(c));
}

