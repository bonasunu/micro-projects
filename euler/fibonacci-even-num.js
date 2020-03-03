function fiboEvenSum(n) {
    let n0 = 0;
    let n1 = 1;
    let n2 = 0;
    let sum = 0;
    for (let i = 0; i < n; i++) {
        n2 = n0 + n1;
        n0 = n1;
        n1 = n2;
        if (n2 % 2 === 0) {
            sum += n2;
        }
        else if (n2 >= n) {
            break;
        }
    }
    console.log(sum);
}

fiboEvenSum(1000);