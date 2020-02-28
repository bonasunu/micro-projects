function grid(string, lines) {
    let str = string + ' ';
    for (let i = 1; i < lines; i++){
        str += str;
    }

    // print lines
    for (let j = 0; j < lines; j++){
        console.log(str);
    }
};

grid('#', 5);