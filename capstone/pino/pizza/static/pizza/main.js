let totalPrice;

function addItem() {
    let input = document.querySelectorAll('td > input');
    let price = document.querySelectorAll('td > input').dataset.price;

    for (let i = 0; i < input.length; i++) {
        let li = document.createElement('th');
        li.innerHTML = input[i];
        document.querySelector('#total_price').append(li);
    }
};