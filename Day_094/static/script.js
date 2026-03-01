const cells = document.querySelectorAll('.cell');
const resultText = document.getElementById('resultText');
const status = document.querySelector('.status');

let board = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";
let gameActive = true;

const winPatterns = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
];

cells.forEach(cell => {
    cell.addEventListener('click', handleClick);
});

function handleClick(e) {
    const index = e.target.dataset.index;

    if (board[index] !== "" || !gameActive) return;

    board[index] = currentPlayer;
    e.target.textContent = currentPlayer;

    checkWinner();

    currentPlayer = currentPlayer === "X" ? "O" : "X";
    status.textContent = `TURN: ${currentPlayer}`;
}

function checkWinner() {
    for (let pattern of winPatterns) {
        const [a,b,c] = pattern;

        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            resultText.textContent = `WINNER: ${board[a]}`;
            gameActive = false;
            return;
        }
    }

    if (!board.includes("")) {
        resultText.textContent = "DRAW";
        gameActive = false;
    }
}

function restartGame() {
    board = ["", "", "", "", "", "", "", "", ""];
    currentPlayer = "X";
    gameActive = true;
    resultText.textContent = "";
    status.textContent = "SYSTEM READY";

    cells.forEach(cell => cell.textContent = "");
}