const fs = require("fs");
const input = fs.readFileSync("../dev/stdin").toString().trim().split("\n");

const answer = parseInt(input[0])
const count = parseInt(input[1])

let total = 0;

for (let i = 2; i < 2 + count; i++) {
  let [a, b] = input[i].split(" ");
  total += parseInt(a) * parseInt(b)
}

if (answer == total) {
  console.log("Yes")
} else {
  console.log("No")
}