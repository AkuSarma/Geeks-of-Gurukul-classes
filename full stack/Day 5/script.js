const reverseString = (s) => {
    s = s.split("")
    for(let i=0; i<s.length/2; i++){
        let temp = s[i];
        s[i] = s[s.length - i - 1]
        s[s.length - i - 1] = temp
    }
    s = s.join("")
    return s;
}

let string = "Sarmaji"

console.log(reverseString(string))


const duplicates = (a) => {
  let d = [];
  for (let i = 0; i < a.length; i++) {
    for (let j = i + 1; j < a.length; j++) {
      if (a[i] === a[j]) {
        d = d + a[i];
      }
    }
  }
  return d
}

let arr = [9,3,6,4,2,8,9,4,2,7];
console.log("Duplicate numbers are: " + duplicates(arr));



const countVowel = (s) => {
    let vowels = ['a', 'e', 'i', 'o', 'u']
    let count = 0
    for(let i = 0; i < s.length; i++){
        for(let j = 0; j < vowels.length; j++){
            if(s[i].toLowerCase() === vowels[j]){
                count++
            }
        }
    }
    return count
}

let s = "aku sarma"

console.log(countVowel(s))

const findFactorial = (n) => {
    if (n == 1) {
        return 1
    }

    return n * findFactorial(n-1)
}

console.log(findFactorial(5))