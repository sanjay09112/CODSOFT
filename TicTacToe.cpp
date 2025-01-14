#include <iostream>
#include <string>
using namespace std;

void printBoard(char gameBoard[3][3]) {
    cout << "   |   |   " << endl;
    cout << " " << gameBoard[0][0] << " | " << gameBoard[0][1] << " | " << gameBoard[0][2] << endl;
    cout << "___|___|___" << endl;
    cout << "   |   |   " << endl;
    cout << " " << gameBoard[1][0] << " | " << gameBoard[1][1] << " | " << gameBoard[1][2] << endl;
    cout << "___|___|___" << endl;
    cout << "   |   |   " << endl;
    cout << " " << gameBoard[2][0] << " | " << gameBoard[2][1] << " | " << gameBoard[2][2] << endl;
    cout << "   |   |   " << endl;
}

char checkWinner(char gameBoard[3][3]) {
    // Check rows and columns
    for (int i = 0; i < 3; i++) {
        if (gameBoard[i][0] != ' ' && gameBoard[i][0] == gameBoard[i][1] && gameBoard[i][1] == gameBoard[i][2]) {
            return gameBoard[i][0];
        }
        if (gameBoard[0][i] != ' ' && gameBoard[0][i] == gameBoard[1][i] && gameBoard[1][i] == gameBoard[2][i]) {
            return gameBoard[0][i];
        }
    }
    // Check diagonals
    if (gameBoard[0][0] != ' ' && gameBoard[0][0] == gameBoard[1][1] && gameBoard[1][1] == gameBoard[2][2]) {
        return gameBoard[0][0];
    }
    if (gameBoard[0][2] != ' ' && gameBoard[0][2] == gameBoard[1][1] && gameBoard[1][1] == gameBoard[2][0]) {
        return gameBoard[0][2];
    }
    return ' ';
}

int main() {
    char gameBoard[3][3] = {
        {' ', ' ', ' '}, 
        {' ', ' ', ' '}, 
        {' ', ' ', ' '}
    };

    const char playerX = 'X';
    const char playerO = 'O';
    char currentPlayer = playerX;
    int row = -1;
    int col = -1;
    char gameWinner = ' ';

    for (int turn = 0; turn < 9; turn++) {
        printBoard(gameBoard);

        if (gameWinner != ' ') {
            break;
        }

        cout << "Current Player: " << currentPlayer << endl;
        while (true) {
            cout << "Enter row and column (0-2): ";
            cin >> row >> col;
            if (row < 0 || row > 2 || col < 0 || col > 2) {
                cout << "Invalid input, try again." << endl;
            }
            else if (gameBoard[row][col] != ' ') {
                cout << "Tile is already taken, try again." << endl;
            }
            else {
                break;
            }

            row = -1;
            col = -1;
            cin.clear();
            cin.ignore(10000, '\n');
        }

        gameBoard[row][col] = currentPlayer;
        currentPlayer = (currentPlayer == playerX) ? playerO : playerX;
        gameWinner = checkWinner(gameBoard);

    }

    printBoard(gameBoard);
    
    if (gameWinner != ' ') {
        cout << "Player " << gameWinner << " wins!" << endl;
    } else {
        cout << "It's a tie!" << endl;
    }

    return 0;
}