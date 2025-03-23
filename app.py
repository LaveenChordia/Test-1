from flask import Flask, request, jsonify, render_template
import heapq
import copy

app = Flask(__name__)

def print_sudoku(board):
    return "\n".join(" ".join(str(num) if num != 0 else "." for num in row) for row in board)

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def get_heuristic(board):
    return sum(row.count(0) for row in board)

def get_neighbors(board, row, col):
    neighbors = []
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            new_board = copy.deepcopy(board)
            new_board[row][col] = num
            neighbors.append(new_board)
    return neighbors

def best_first_search_sudoku(board):
    priority_queue = []
    heapq.heappush(priority_queue, (get_heuristic(board), board))

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        empty = find_empty(current)
        if not empty:
            return {"solution": print_sudoku(current)}
        row, col = empty
        for neighbor in get_neighbors(current, row, col):
            heapq.heappush(priority_queue, (get_heuristic(neighbor), neighbor))

    return {"message": "No solution found"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    board = [[int(data[f'cell{i}{j}']) for j in range(9)] for i in range(9)]
    result = best_first_search_sudoku(board)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
