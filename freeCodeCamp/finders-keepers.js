function findElement(arr, func) {
    let i = 0;
    let newFunc = func;
    while (newFunc(arr[i]) === false) {
        i++;
    }

    if (newFunc(arr[i]) === true) {
        return arr[i];
    }
    return undefined;
}

findElement([1, 2, 3, 4], num => num % 2 === 0);