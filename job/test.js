let item_list = [1, 2, 3, 4, 5, 5, 5, 7, 8, 2, 3, 4, 4, 4, 4, 4]

let duplicate = item_list.reduce((acc, currentValue, index, array) => {
  if (array.indexOf(currentValue) != index && !acc.includes(currentValue))
    acc.push(currentValue)
  return acc
}, [])

console.log('Duplicate items are ' + duplicate.join(','))
