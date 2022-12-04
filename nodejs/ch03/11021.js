const fs = require("fs");
const input = fs.readFileSync("../dev/stdin").toString().trim().split("\n");

const count = parseInt(input[0]);

let answer = ""

for (let i = 1; i <= count; i++) {
   let [a, b] = input[i].split(" ");

   answer += `Case #${i}: ${parseInt(a) + parseInt(b)} \n`
}

console.log(answer);