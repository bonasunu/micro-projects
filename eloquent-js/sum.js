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
function stepArray(start, end, step = 1){
    let arr = [];
    if (step > 0){
        for (let i = start; i <= end; i += step) {
            arr.push(i);
        }
    }
    else if (step < 0){
        for (let i = start; i >= end; i += step) {
            arr.push(i);
        }
    }
    else {
        for (let i = start; i <= end; i++) {
            arr.push(i);
        }
    }
    console.log(arr);
}

stepArray(5, 2, -1);