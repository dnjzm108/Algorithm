const fs = require('fs');
const input = fs.readFileSync("../dev/stdin").toString().trim().split("\n")

let num = Number(input[0])
let count = 0;


for (let i = 1; i <= num; i++) {
    let word = input[i];
    let state = true;
    let con = [];

    for (let v = 0; v < word.length; v++) {

        if (con.indexOf(word[v]) == -1) {
            con.push(word[v])
        } else {
            if (con.indexOf(word[v]) !== con.length - 1) {
                state = false
            }
        }
    }

    if (state) {
        count += 1
    }

}

console.log(count);
