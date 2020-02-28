function grid(string, lines) {
    let str = '';
    for (let i = 0; i < lines; i++){
        str += string + ' ';
    }

    // print lines
    for (let j = 0; j < lines; j++){
        console.log(str);
    }
};

grid('#', 5);