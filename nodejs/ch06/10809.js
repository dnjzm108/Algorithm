const fs = require('fs');
const input = fs.readFileSync("../dev/stdin").toString().trim();

const arr = Array.from({ length: 26 }, (v, i) => String.fromCharCode(i + 65).toLowerCase());

let answer = '';
for (let i = 0; i < arr.length; i++) {
    if (answer.length == 0) {
        answer += input.indexOf(arr[i]);
    } else {
        answer += ' ' + input.indexOf(arr[i]);
    }
}

console.log(answer);