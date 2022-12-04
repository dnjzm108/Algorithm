const fs = require("fs");
const [num] = fs.readFileSync("../dev/stdin").toString().trim().split(" ").map(Number);

let star = ""
let answer = ""

for (let i = 1; i <= num; i++) {
    star += "*"
    answer += star + "\n"
}

console.log(answer)