function checkCashRegister(price, cash, cid) {
    let change = cash - price;
    let totalCid = 0;
    let closed = {status: "CLOSED"};

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

    console.log(totalCid);
    console.log(change);
    
}

checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);
