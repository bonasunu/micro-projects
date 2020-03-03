function frankenSplice(arr1, arr2, n) {
    let newArr1 = arr1.slice(0, arr1.length);

    const startIndex = n;
    const amountToDelete = 0;

    let newArr2 = arr2.slice(0, arr2.length);

    for (let i = arr1.length - 1; i >= 0; i--) {
        newArr2.splice(startIndex, amountToDelete, newArr1[i]);
    }

    return newArr2;
}


frankenSplice([1, 2, 3], [4, 5, 6], 1);