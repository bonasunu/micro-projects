function telephoneCheck(str) {
    if (str.length === 12) {
        if (str.match(/\d{3}-\d{3}-\d{4}/g)) {
            return true;
        }
        else if (str.match(/\d{3}\s\d{3}\s\d{4}/g)) {
            return true;
        }
        else return false;
    }
    else if (str.length === 13) {
        if (str.match(/\(\d{3}\)\d{3}-\d{4}/g)) {
            return true;
        }
        else return false;
    }
    else if (str.length === 14) {
        if (str.match(/^\(\d{3}\)\s\d{3}-\d{4}/g)) {
            return true;
        }
        else if (str.match(/1\s\d{3}\s\d{3}\s\d{4}/g)) {
            return true;
        }
        else if (str.match(/1\s\d{3}-\d{3}-\d{4}/g)) {
            return true;
        }
        else if (str.match(/^1\(\d{3}\)\d{3}-\d{4}/g)) {
            return true;
        }
        else return false;
    }
    else if (str.length === 10) {
        if (str.match(/\d+/g)) {
            return true;
        }
        return false;
    }
    else if (str.match(/^1\s\(\d{3}\)\s\d{3}-\d{4}/)) {
        return true;
    }
    else return false;
}

telephoneCheck("555-555-5555");