const solution = (relation) => {
  let answer = [...relation]

  let id, name, major, grade
  let arr = []

  id = answer.map((item) => item[3]).sort()

  console.log(id)
  // console.log(name)
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
