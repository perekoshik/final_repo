// logs
currentNum = 1

function resetLogs() {
    document.querySelector(".logs-rows").innerHTML = "";
    currentNum = 1
}

function createLogsRow() {
    let row = document.createElement('div');
    row.classList.add('logs-row')

    let num = document.createElement('span');
    num.classList.add('logs-num')
    num.innerHTML = `${currentNum}.`
    currentNum += 1;
    let text = document.createElement('span');
    text.classList.add('logs-rowText');
    text.innerHTML = 'Lor (uho gorlo nos)'

    row.append(num);
    row.append(text);

    document.querySelector('.logs-rows').append(row)
}