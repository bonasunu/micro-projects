const o = {
    a: 'a',
    b: 'b',
    obj: {
        key: {
            nestedVal: 'val'
        }
    }
}

const o2 = Object.assign({}, o.obj)

//o2.obj.key = 'new value'

console.log(o2)

const num = 53

console.log(num.toString())