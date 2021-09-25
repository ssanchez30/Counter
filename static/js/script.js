
let increaseByTwoBtn = document.querySelector('.increaseByTwo');
let btnReset = document.querySelector('.btnReset');

function resetear() {

    let URL = '/destroy_session';
    let settings = {
        method: 'GET'
    }

    fetch(URL, settings)
        .then(response => {
            if (response.ok) {
                return response.json()
            }
        })
        .then(data => {
            window.location.href = '/';
        });
}

function increaseByTwo() {

    let URL = '/ByTwo';
    let settings = {
        method: 'GET'
    }

    fetch(URL, settings)
        .then(response => {
            if (response.ok) {
                return response.json()
            }
        })
        .then(data => {
            window.location.href = '/';
        });
}

increaseByTwoBtn.addEventListener('click', increaseByTwo)
btnReset.addEventListener('click', resetear)