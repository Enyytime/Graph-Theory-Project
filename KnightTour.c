#include <stdio.h>

#define N 8  // Mamximum size of the chessboard (editable)

// Function to check if the movement to (x,y) is a valid movement on the chessboard.
int isSafe(int x, int y, int board[N][N], int n, int m) {
    // We have to check if the next x and y are positive AND if they respect the chessboard size.
    // Moreover, the last condition verify that the (x,y) square has never been visited.
    return (x >= 0 && x < n && y >= 0 && y < m && board[x][y] == -1); 
}

// Function to display the coordinates of the square, in order of visit.
void printSolution(int board[N][N], int n, int m) {

    // Find and display the coordinates in order of visit.
    for (int move = 0; move < n * m; move++) {
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < m; y++) {
                if (board[x][y] == move) { //We recover the coordinates by searching the order of visit of each square.
                    printf("(%d, %d)\n", x, y); // Imprimer la coordonnée visitée
                }
            }
        }
    }
}

// Recursive function to solve the Knight Tour problem.
int solveKnightTourUtil(int x, int y, int movei, int board[N][N], int xMove[], int yMove[], int n, int m) {
    int next_x, next_y;
    if (movei == n * m)  // If all the movements has been done, we go out from the recursivity.
        return 1;

    // Try all the Knight movements possible
    for (int k = 0; k < 8; k++) {
        next_x = x + xMove[k]; // We run through the xMove...
        next_y = y + yMove[k]; //... and the yMove possible. 
        if (isSafe(next_x, next_y, board, n, m)) { // We check if the next position is possible or not.
            board[next_x][next_y] = movei; // If the square is safe, we move the knight to it.
            if (solveKnightTourUtil(next_x, next_y, movei + 1, board, xMove, yMove, n, m) == 1) // We call this recursive function with the new positions to see if we can find a way to go through all the squares.
                return 1;
            else
                board[next_x][next_y] = -1;  // Backtracking
        }
    }
    return 0;
}

// KnightTour function
int solveKnightTour(int n, int m, int startX, int startY) {
    int board[N][N]; //chessboard 

    // We initialize each square of the chessboard with -1
    for (int x = 0; x < n; x++)
        for (int y = 0; y < m; y++)
            board[x][y] = -1;

    // Just below, here are the 8 movements the knight can do on the chessboard by associating the 'xMove' index with the 'yMove' one.
    int xMove[8] = {2, 1, -1, -2, -2, -1, 1, 2};
    int yMove[8] = {1, 2, 2, 1, -1, -2, -2, -1};

    // We put the knight on the the starting point.
    board[startX][startY] = 0;

    // We have to call the recursive function to solve the problem.
    if (solveKnightTourUtil(startX, startY, 1, board, xMove, yMove, n, m) == 0) {
        printf("No solution found.\n");
        return 0;
    } else
        printSolution(board, n, m);

    return 1;
}

int main() {
    int n, m, startX, startY;

    // Recover the chessboard size.
    printf("Enter the size of the chessboard (n m): ");
    scanf("%d %d", &n, &m);
    
    printf("Enter the start position of the Knight (startX startY): ");
    scanf("%d %d", &startX, &startY);

    // Let's solve the Knight Tour problem.
    solveKnightTour(n, m, startX, startY);

    return 0;
}
