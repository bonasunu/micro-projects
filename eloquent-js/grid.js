function grid(string, lines) {
    let str = '';
    for (let i = 1; i < lines; i++){
        str += string + ' ';
    }

    // print lines
    for (let j = 0; j < lines; j++){
        console.log(str);
    }
};

grid('#', 3);