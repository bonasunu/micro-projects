function checkCashRegister(price, cash, cid) {
    let change = cash - price;
    let totalCid = 0;
    let closed = {status: "CLOSED"};
<<<<<<< HEAD
    let newCid = [
        ["PENNY", 0],
        ["NICKEL", 0],
        ["DIME", 0],
        ["QUARTER", 0],
        ["ONE", 0],
        ["FIVE", 0],
        ["TEN", 0],
        ["TWENTY", 0],
        ["ONE HUNDRED", 0]
    ];
    let totalNewCid = 0;
    let open = {status: "OPEN", change: []};

    // Recursion function
    function money(change, usd, currency){
        change -= usd;
        newCid[currency][1] += usd; 
        if (change >= usd && newCid[currency][1] < cid[currency][1]){
            money(change, usd, currency);
        }
    }
=======
>>>>>>> parent of a264ef6... implement change < cid

    // Sum money in drawer
    for (let i = 0; i < cid.length; i++) {
        totalCid += cid[i][1];
    }

    // Fix totalCid to 2 decimals
    totalCid = totalCid.toFixed(2);

    if (change > totalCid) {
        return { status: "INSUFFICIENT_FUNDS", change: [] };
    }
    else if (change == totalCid) {
        closed.change = cid.slice();
        console.log(closed);
    }

<<<<<<< HEAD
    // Algorithm for changeand status: open
    for (let k = 0; k < newCid.length; k++){
        totalNewCid += newCid[k][1];
    };

    if (totalNewCid != 0){
        console.log(totalCid);
        console.log(change);
        
    }

    console.log(newCid);
=======
    console.log(totalCid);
    console.log(change);
>>>>>>> parent of a264ef6... implement change < cid
    
}

checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
