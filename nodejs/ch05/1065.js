const fs = require('fs');
const [input] = fs.readFileSync("../dev/stdin").toString().trim().split(" ").map(Number);

let count = 0;

for (let i = 1; i <= input; i++) {
    if (i < 100) {
        count++
        continue
    }

    if (String(i)[0] - String(i)[1] == String(i)[1] - String(i)[2]) {
        count++
    }
}
console.log(count);