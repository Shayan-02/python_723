let a = prompt("enter a word");

let t = 1;

for (let i = 0; i <= a.length; i++){
    if (a[i] == "a") {
        t *= 2;
    }
}

alert(t)
