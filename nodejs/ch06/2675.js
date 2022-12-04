const fs = require('fs');
const input = fs.readFileSync("../dev/stdin").toString().trim().split("\n");

const count = Number(input[0]);

let answer = "";

for (let i = 1; i <= count; i++) {
    let str = input[i].split(" ");

    for (let a = 0; a < str[1].length; a++) {
        for (let b = 0; b < Number(str[0]); b++) {
            answer += str[1][a]
        }
    }
    if (i !== count) {
        answer += "\n"
    }
}

console.log(answer);