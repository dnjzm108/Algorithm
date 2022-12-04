const fs = require("fs");
const input = fs.readFileSync("../dev/stdin").toString().trim().toUpperCase();

let top;
let answer = {};

for (let i = 0; i < input.length; i++) {
    if (answer[input[i]] == undefined) {
        answer[input[i]] = 0
    }
    answer[input[i]] = answer[input[i]] + 1
}

let arr = Object.values(answer);
let max = Math.max(...arr);

let count = 0;
for (let i in answer) {
    if (max == answer[i]) {
        top = i
        count++
    }
    if (count > 1) {
        top = "?"
    }
}

console.log(top);
