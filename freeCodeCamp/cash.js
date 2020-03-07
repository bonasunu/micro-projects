function checkCashRegister(price, cash, cid) {
    let change = cash - price;
    change = change.toFixed(2);
    let totalCid = 0;
    let closed = { status: "CLOSED" };
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

    // Recursion function
    function money(change, usd, currency) {
        change -= usd;
        newCid[currency][1] += usd;
        if (change >= usd) {
            money(change, usd, currency);
        }
    }

    // Sum money in drawer
    for (let i = 0; i < cid.length; i++) {
        totalCid += cid[i][1];
    }

    // Fix totalCid to 2 decimals
    totalCid = totalCid.toFixed(2);

    // Check money algorithm
    if (change > totalCid) {
        return { status: "INSUFFICIENT_FUNDS", change: [] };
    }
    else if (change == totalCid) {
        closed.change = cid.slice();
        return closed;
    }
    else if (change < totalCid) {
        if (change >= 100 && cid[8][1] != 0) {
            money(change, 100, 8);
        }
        else if (change < 100 && change >= 20 && cid[7][1] != 0) {
            money(change, 20, 7);
        }
        else if (change < 20 && change >= 10 && cid[6][1] != 0) {
            money(change, 10, 6);
        }
        else if (change < 10 && change >= 5 && cid[5][1] != 0) {
            money(change, 5, 5);
        }
        else if (change < 5 && change >= 1 && cid[4][1] != 0) {
            money(change, 1, 4);
        }
        else if (change < 1 && change >= 0.25 && cid[3][1] != 0) {
            money(change, 0.25, 3);
        }
        else if (change < 0.25 && change >= 0.1 && cid[2][1] != 0) {
            money(change, 0.1, 2);
        }
        else if (change < 0.1 && change >= 0.05 && cid[1][1] != 0) {
            money(change, 0.05, 1);
        }
        else if (change < 0.05 && change >= 0.01 && cid[0][1] != 0) {
            money(change, 0.01, 0);
        }
        else return { status: "INSUFFICIENT_FUNDS", change: [] };

    }

}

checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);
