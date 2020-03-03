function largestPrimeFactor(number) {
    let num = number;
    let div = 2;
    while (num >= div) {
        if (num % div === 0) {
            num = num / div;
        }
        else {
            div++;
        }
    }
    return div;
}

largestPrimeFactor(13195);