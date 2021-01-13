function calculateBBM(input) {
  let totalBBM = 0

  function recursionVehicle(passenger) {
    let newPassenger = passenger > 20 ? passenger % 20 : passenger

    if (passenger > 0 && passenger <= 6) {
      totalBBM += 50
      return totalBBM
    } else if (passenger > 6 && passenger <= 10) {
      totalBBM += 70
      return totalBBM
    } else if (passenger > 11 && passenger <= 20) {
      totalBBM += 120
      return totalBBM
    } else {
      totalBBM += 120
      return recursionVehicle(newPassenger)
    }
  }

  input.forEach((v) => {
    if (v > 20) {
      recursionVehicle(v)
    } else if (v <= 6) {
      totalBBM += 50
    } else if (v > 6 && v <= 10) {
      totalBBM += 70
    } else if (v > 10 && v <= 20) {
      totalBBM += 120
    }
  })

  console.log(totalBBM)
}

// calculateBBM([20, 5, 9, 3, 35, 30, 12])
calculateBBM([10, 9, 3, 35])
calculateBBM([20, 5, 30, 12])
