function reverseArray(arr){
    let newArr = [];
    for (let item in arr){
        newArr.unshift(arr[item]);
    }
    return newArr;
}

console.log(reverseArray([1, 2, 3, 4, 5]));

function reverseArrayInPlace(arr){
    let newArr = [];
    for (let item in arr){
        newArr.unshift(arr[item]);
    }
    return newArr;
}

reverseArrayInPlace([1, 2, 3, 4, 5]);

