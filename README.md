 🧩 Sudoku Solver using Best-First Search

This project is a Sudoku Solver that uses the Best-First Search (BFS) algorithm to efficiently find the solution to a given Sudoku puzzle. It is built using Python for the algorithm and Flask for the web interface.

Features
- Solves 9x9 Sudoku puzzles using the Best-First Search algorithm.
- User-friendly web interface built with HTML, CSS, and Flask.
- Displays the input Sudoku puzzle and the solved puzzle.
- Validates user input and checks for solvability.


 Technologies Used
- Python: For implementing the BFS algorithm.
- Flask: Backend framework to run the server.
- HTML & CSS: Frontend for a simple and interactive UI.
- Heapq & Copy Modules: Efficient priority queue management.

 Project Structure
project_folder/
├── app.py                Flask backend server
├── templates/
│   └── index.html         Frontend HTML file
└── static/
    └── style.css          Styling for the UI


Installation and Setup

1. Clone the Repository
   bash
   git clone https://github.com/yourusername/sudoku-solver.git
   cd sudoku-solver
   

2. Install Required Libraries
   bash
   pip install flask
   

3. Run the Flask Server
   bash
   python3 app.py
   
   Open your browser and visit:
   
   http://127.0.0.1:5000/
   
 Usage
1. Enter the Sudoku puzzle in the text fields.
2. Click the "Solve" button.
3. The solved Sudoku puzzle will be displayed on the screen.


 Troubleshooting
- Make sure you have Python and Flask installed.
- If the server doesn't start, ensure the port is not occupied.
- Check for missing dependencies and install them with:
  bash
  pip install -r requirements.txt
  

License
This project is licensed under the MIT License.

Contributing
Feel free to submit a Pull Request or open an Issue if you find any bugs or want to improve the project!
