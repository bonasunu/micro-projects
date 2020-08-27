const solution = (relation) => {
  let answer = 0
  let arr = [...relation]

  let checkKey = arr
    .map((i) => i[5])
    .sort()
    .reduce(
      (unique, item) => (unique.includes(item) ? unique : [...unique, item]),
      []
    ).length

  checkKey === arr.length ? answer++ : ''
  console.log(checkKey)
  console.log(answer)
}

let relation = [
  [100, 'ryan', 'music', 2],
  [200, 'apeach', 'math', 2],
  [300, 'tube', 'computer', 3],
  [400, 'con', 'computer', 4],
  [500, 'muzi', 'music', 3],
  [600, 'apeach', 'music', 2],
]

// answer: 2
solution(relation)
