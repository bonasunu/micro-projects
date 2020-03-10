function largestPalindromeProduct(n) {
    let num = Math.pow((Math.pow(10, n) - 1), 2);
    let reverseNum = "";
    for (let i = num; i < 0; i--) {

        for (let j = i.toString().length - 1; j >= 0; j--) {
            reverseNum += i.toString()[j];
        }
        if (num == reverseNum) {
            console.log(parseInt(num));
            break;
        }
    }
    
    console.log(reverseNum);
}

largestPalindromeProduct(2);