function reverseArray(arr){
    console.log(arr);
}

reverseArray([1, 2, 3, 4, 5]);

function reverseArrayInPlace(arr){
    let newArr = [];
    for (let item in arr){
        newArr.unshift(arr[item]);
    }
    console.log(newArr);
}

reverseArrayInPlace([1, 2, 3, 4, 5]);