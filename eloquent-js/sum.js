// Function takes 2 arguments and returns the sum of the numbers between num1 and num2
function sumArray(num1, num2){
    let total = 0;
    for (let i = num1; i <= num2; i++){
        total += i;
    }
    console.log(total);
}

sumArray(1, 10);

// Function that takes 3 arguments and returns array. 