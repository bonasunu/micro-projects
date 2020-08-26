const solution = (record) => {
  let nickname = {}

  const newRecord = record.map((item) => {
    let newItem = item.split(' ')
    let arr = [newItem[1], newItem[0]]
    newItem[0] !== 'Leave'
      ? newItem[2].length <= 10 // assign userid when nickname more than 10 characters
        ? (nickname[newItem[1]] = newItem[2])
        : (nickname[newItem[1]] = newItem[1])
      : ''
    return arr
  })

  const answer = newRecord
    .map((item) => {
      switch (item[1]) {
        case 'Enter':
          return `${nickname[item[0]]} came in.`
        case 'Leave':
          return `${nickname[item[0]]} has left.`
        case 'Change':
          return 'Change'
      }
    })
    .filter((item) => item !== 'Change')

  console.log(answer)
}

let input = [
  'Enter uid1234 Muzi',
  'Enter uid4567 Prodo',
  'Leave uid1234',
  'Enter uid1234 Prodo',
  'Change uid4567 Ryan',
]
// output ["Prodo came in.", "Ryan came in.", "Prodo has left.", "Prodo came in."]

solution(input)
