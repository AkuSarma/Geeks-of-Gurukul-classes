let n = 5

for(let i=1; i<=n; i++){
    for(let j=1; j<=i; j++){
        process.stdout.write(j + " ")
    }
    console.log("")
}

for (let i = n; i >= 1; i--) {
  for (let j = i; j >= 1; j--) {
    process.stdout.write(j + " ");
  }
  console.log("");
}
console.log("-------------------")
for(let i = 1; i<=n; i++){
    for(let j=1; j<=n-i;j++){
        process.stdout.write(" ");
    }
    for(let j=1; j<=i; j++){
        process.stdout.write("* ");
    }
    console.log("")
}

for(let i=n; i>=1; i--){
    for(let j=1; j<=n-i; j++){
        process.stdout.write(" ");
    }
    for(let j=i; j>=1; j--){
        process.stdout.write("* ");
    }
    console.log("")
}
