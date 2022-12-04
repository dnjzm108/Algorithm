const fs = require("fs");
const [num] = fs.readFileSync("../dev/stdin").toString().trim().split(" ").map(Number);

let star = ""
let answer = ""

for (let i = 1; i <= num; i++) {
    for (let a = 0; a < num - i; a++) {
        star += " "
    }
    for (let b = 0; b < i; b++) {
        star += "*"
    }
    answer += star + "\n"
    star = ""
}

console.log(answer)