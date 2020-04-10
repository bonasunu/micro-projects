document.addEventListener('DOMContetLoaded', () => {
    document.querySelector('#form').onsubmit = () => {

        // Initialize new request
        const request = new XMLHttpRequest();
        const currency = document.querySelector('#currency').nodeValue;
        request.open('POST', '/convert');

        // callback function for when request completes
        request.onload = () => {
            // extract json data from request
            const data = JSON.parse(request.responseText);

            // update result div
            if (data.success) {
                const contents = `1 USD is equal to ${data.rate} ${currency}.`;
                document.querySelector('#result').innerHTML = contents;
            }
            else {
                document.querySelector('#result').innerHTML = 'There was an error.';
            }
        }

        // add data to send with request
        const data = new FormData();
        data.append('currency', currency);

        // send request
        request.send(data);
        return false;
    }
});