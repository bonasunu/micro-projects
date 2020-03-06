function rot13(str) {
    let decoded = [];
    for (let item in str){
        if (str.charCodeAt(item) > 64 && str.charCodeAt(item) < 91){
            if ((str.charCodeAt(item) - 13) < 65){
                decoded.push(String.fromCharCode(str.charCodeAt(item) - 13 + 26));
            }
            else {decoded.push(String.fromCharCode(str.charCodeAt(item) - 13))}
        }
        else {decoded.push(str[item])}
    }
    
    console.log(decoded.join(""));
}

rot13("SERR PBQR PNZC");
