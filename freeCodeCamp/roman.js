function convertToRoman(num) {
    // Define Roman Symbol
    let romanSym = [
     {sym: "I", num: 1},
     {sym: "V", num: 5},
     {sym: "X", num: 10},
     {sym: "L", num: 50},
     {sym: "C", num: 100},
     {sym: "D", num: 500},
     {sym: "M", num: 1000}
 ];

    // Check num where it stay between Roman Symbol
    let minSym = [];
    let maxSym = [];
    
    for (let i = 1; i < romanSym.length; i++){
        if (num >= romanSym[i - 1].num && num <= romanSym[i].num) {
            minSym.push(romanSym[i - 1].num);
            minSym.push(i - 1);
            maxSym.push(romanSym[i].num);
            maxSym.push(i);
        }
    };
    

}

convertToRoman(36);