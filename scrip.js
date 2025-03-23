const form = document.getElementById('sudokuForm');
const output = document.getElementById('output');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const data = {};

    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const cellValue = formData.get(`cell${i}${j}`) || "0";
            data[`cell${i}${j}`] = cellValue;
        }
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/solve', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
        });


        const result = await response.json();

        if (result.status === "success") {
            output.textContent = "Sudoku Solved:\n" + result.solution;
        } else {
            output.textContent = "Error: " + result.message;
        }
    } catch (error) {
        output.textContent = "Error solving Sudoku. Please try again.";
        console.error("Error:", error);
    }
});
