function palindrome(str) {
    let regex = /\W+|\s+|_/g;
    let newStr = str.replace(regex, "").toLowerCase();
    let arrNewStr = newStr.split("");
    let arrBackward = [];


    for (let i = arrNewStr.length - 1; i >= 0; i--) {
        arrBackward.push(arrNewStr[i]);
    };

    if (newStr === arrBackward.join("")) {
        return true;
    }
    else return false;

}



palindrome("eye");