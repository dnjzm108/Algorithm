const fs = require("fs");
const input = fs.readFileSync("../dev/stdin").toString().trim().split(" ").map(Number);

const a = input[0];

if (a < 60) {
    console.log("F")
} else if (a < 70) {
    console.log("D");
} else if (a < 80) {
    console.log("C");
} else if (a < 90) {
    console.log("B")
} else {
    console.log("A");
}