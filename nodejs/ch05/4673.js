let arr = [];
function show(n) {
    let sel = n;

    while (true) {
        if (n === 0) break;
        sel += n % 10;
        n = parseInt(n / 10);    
    }

    arr[sel] = sel;
    return sel;
}

for (let i = 1; i < 50; i++) {
    show(i);
    if (arr[i] == undefined) {
        console.log(i);
    }
}
