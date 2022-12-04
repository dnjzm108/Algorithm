const fs = require("fs");
const input = fs.readFileSync("../dev/stdin").toString().trim().split(" ");

let first = Number(input[0].split("").reverse("").join(""));
let second = Number(input[1].split("").reverse("").join(""));

console.log(first > second ? first : second);

