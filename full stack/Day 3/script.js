// for(let i=0; i<5; i++){
//     console.log("Good morning")
// }

// for(let i=1; i<=100; i++){
//     if (i%2===0){
//         console.log(i + " is even")
//     } else {
//         console.log(i + " is Odd")
//     }
// }

// for (let i = 100; i >= 1; i--) {
//   if (i % 2 === 0) {
//     console.log(i);
//   } else {
//     console.log(i);
//   }
// }
// sum = 0;
// for (let i = 1; i <= 151; i++) {
//   if (i % 2 === 0) {
//     console.log(i);
//     sum++;
//   }
// }
// console.log(sum + " total sum numbers between 1 and 151");
// psum = 0
// for(let i=1; i<=100; i++){
//     let primeNo = true;
//     for(let j=2; j<(i/2); j++){
//         if(i%j===0){
//             primeNo = false;
//         }
//     }
//     if(primeNo){
//         console.log(i)
//         psum++
//     }
// }
// console.log("total prime number between 1 to 151 is: " + psum)

// let n=5;
// let fsum = 1
// for(let i=n; i>=1; i--){
//   fsum *= i;
// }
// console.log(fsum)

let trafficLight = "Red"

if (trafficLight === "Green") {
  console.log("Can go");
} else if (trafficLight === "Yellow") {
  console.log("Wait");
} else {
  console.log("Stop");
}
