const solution = (N, users) => {
  let players = [...users]
  let totalPlayers = players.length
  let stages = []

  // make new array based on stages (N)
  for (let i = 1; i <= N; i++) {
    stages.push({
      level: i,
      fr: 0, //fr = failure rate
    })
  }

  let answer = stages
    .map((stage) => {
      let total = players.filter((i) => i === stage.level).length
      stage.fr = total / totalPlayers
      totalPlayers = totalPlayers - total
      return stage
    })
    .sort((a, b) => b.fr - a.fr)
    .map((item) => item.level)

  console.log(answer)
}

const N = 5
const N2 = 4
const users = [2, 1, 2, 6, 2, 4, 3, 3]
const users2 = [4, 4, 4, 4, 4]
solution(N, users)
solution(N2, users2)
// output [3,4,2,1,5]
