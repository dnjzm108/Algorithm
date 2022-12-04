const fs = require("fs");
const input = fs.readFileSync("../dev/stdin").toString().trim().split("\n");

const a = Number(input[0]);
const b = input[1];

let answer = 0;
for (let i = 0; i < a; i++) {
    answer += Number(b[i]);
}
console.log(answer);