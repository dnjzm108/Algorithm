const fs = require("fs");
const input = fs.readFileSync("../dev/stdin").toString().trim().split("\n");

let [count, num] = input[0].split(" ");
let check = input[1].split(" ").map(Number);

let answer = "";

for (let i = 0; i < count; i++) {
    if (check[i] < parseInt(num)) {
        answer += `${check[i]} `
    }
}

console.log(answer);