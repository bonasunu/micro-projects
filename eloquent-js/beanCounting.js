function countBs(str, char) {
    let countB = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i] === char) {
            countB++;
        }
    }
    return countB;
}

countBs('BonaBonbonasunu', 'o');