function addOne(num) {
    return num + 1
}

function getNum() {
    return addOne(10)
}

function c() {
    console.log(getNum() + getNum())
}

c()