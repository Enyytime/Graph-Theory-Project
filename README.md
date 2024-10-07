# Graph-Theory-Project
| Name | NRP |
|-----------------|-----------------|
| Matteo, Alain, Jean-marie, Joseph, Dennequin | 5999241043 | 
| Fadhil Revinno Hairiman    | 5025231002 |
| R. Rafif Aqil Aabid Hermawan     | 5025231069 | 
| Rogelio Kenny Arisandi | 5025231074 | 

This project is a solution to three classic combinatorial problems: the Traveling Salesman Problem (TSP), the Knight’s Tour Problem and the Chinese Postman Problem, implemented in Python and C/C++, respectively.

# Traveling Salesman Problem (TSP)
The TSP involves finding the shortest possible route that visits a given set of cities (nodes) exactly once and returns to the starting city. Our implementation models the cities as nodes and the roads connecting them as edges with associated travel costs. By utilizing permutations and a cost calculation function, the program evaluates all possible routes to determine the one with the lowest cost. Additionally, it identifies the specific roads used in the optimal route.

# Knight's Tour Problem
The Knight's Tour is a famous problem in chess where the knight, starting from any given square on a chessboard, must visit each square exactly once. Our C-based implementation uses a backtracking algorithm to explore all possible knight moves and finds a solution for a board of any size. If a solution exists, the program outputs the coordinates of the knight's path in the order of their visit.

Both algorithms demonstrate the power of brute-force approaches and the challenges they present in terms of computational complexity, making them excellent examples for educational purposes in combinatorial optimization and graph theory.

# Chinese Postman Problem
The Chinese Postman Problem (also known as the Route Inspection Problem) focuses on finding the shortest possible route that covers all edges of a graph at least once. It is often compared to the TSP but differs in that every edge (or road) must be traversed, making it highly applicable to real-world scenarios like postal delivery routes or street inspections. Our implementation computes the optimal path by first identifying odd-degree vertices and then finding a minimal-cost way to traverse all edges while ensuring all roads are covered at least once. The result is an efficient route that minimizes travel costs and satisfies the requirements of the problem.

## Traveling Salesman Problem (TSP) Solution
Code's Credit to: Mattéo
### Brief explanation on the main function
```python
if __name__ == "__main__":
    # We recover the number of nodes and edges
    n = int(input("Enter the number of nodes: "))
    e = int(input("Enter the number of edges: "))
    
    graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)] # Initialization of the cost matrice.
    edge_names = {} #Initialization of the edge names list.

    print("Enter theedges informations in the form of : edge_number node1 node2 cost")
    for _ in range(e):
        edge_info = input().split() # This funtion '.split' allows you to recover data in an array
        edge_num = int(edge_info[0])  # Edge number
        u = int(edge_info[1]) # Node 1 connected to the edge
        v = int(edge_info[2]) # Node 2 connected to the edge
        cost = int(edge_info[3]) # Cost of the edge
        if graph[u][v] != 0 :
            if graph[u][v] >= cost : #If 2 edges connect 2 same nodes, we have to compare the cost of the edges to keep the lowest cost.
                graph[u][v]=cost #We suppose here that we are not in a digraph...
                graph[v][u]=cost # ... so u->v cost is the same as v->u.
                edge_names[(u, v)] = edge_num # We recover the number of  the edges.
                edge_names[(v, u)] = edge_num # As we suppose that we are not in a digraph. The number of (u,v) is the same as (v,u)
        
    start = int(input("Enter the start point: ")) #Recover the start point
    print(edge_names )
    # Traveling Salesman Problem solving
    min_cost, best_route = tsp(graph, start)

    # We have to check if a route has been find
    if best_route:
        print("Cost:", min_cost)
        edge_route = get_edge_names_from_route(best_route, edge_names) #We recover the number of the edges by using the best route and all the edge names used
        print("Route :", ', '.join(map(str, edge_route)))
    else:
        print("None valide route found.")
```
* input by the number of edges and and the number of nodes
```python
n = int(input("Enter the number of nodes: "))
e = int(input("Enter the number of edges: "))
```
* and ofcourse we are going to need to store the graph and the edges for solving a tsp problem, so we can use this way as a way to store it
```python
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)] # Initialization of the cost matrice.
edge_names = {} #Initialization of the edge names list.
```
* here is for the inputting the graph part, we will give an explanation on the important part
* since we're assuming that its an undirected graph so we are going with this way of inputting the graph `graph[u][v]=cost ` and `graph[v][u]=cost`
* we are using adjacency matrix as a way to represent the graph
```python
if graph[u][v] >= cost : #If 2 edges connect 2 same nodes, we have to compare the cost of the edges to keep the lowest cost.
    graph[u][v]=cost #We suppose here that we are not in a digraph...
    graph[v][u]=cost # ... so u->v cost is the same as v->u.
    edge_names[(u, v)] = edge_num # We recover the number of  the edges.
    edge_names[(v, u)] = edge_num # As we suppose that we are not in a digraph. The number of (u,v) is the same as (v,u)
```
### TSP Function explanation
#### Function Overview:
The function `tsp(graph, start)` is designed to solve the Traveling Salesman Problem (TSP) using a brute-force approach by trying all possible routes (permutations) between the nodes of a graph. The goal of the function is to find the minimum cost path (route) that visits all nodes exactly once and returns to the starting point.

```python
def tsp(graph, start):
    n = len(graph)
    vertices = [i+1 for i in range(n-1) if i+1 != start] #Initialization of an arry which contains all the number of the nodes except the start point.
    min_cost = 999 #Initialization of a minimum cost which will be compared later.
    best_route = []
    
    for perm in permutations(vertices): # the  function "permutations" from itertools library gives us all the permutations of the vertices array.
        current_route = [start] + list(perm) # Because we initialized the vertices array without the start point
        current_cost = calculate_cost(graph, current_route) #We use the function calculate_cost for each permutation.
        
        if current_cost < min_cost: #We compare the result obtained with 'min_cost'
            min_cost = current_cost # We keep the lowest cost in 'min_cost' ...
            best_route = current_route # ... and we keep the route associated in 'best_route'

    return min_cost, best_route
```
* the most important part of this code is of course the TSP Function
#### Parameters
* graph: This is an adjacency matrix representation of the graph. It is a 2D list where graph[i][j] represents the cost to travel from node i to node j.
* start: This is the node where the salesman starts and ends the journey. The route must begin and end at this node.
#### Some variables
* vertices: This is a list that contains all the nodes except the start node. These are the nodes the salesman will visit during the journey.
The expression `[i+1 for i in range(n-1) if i+1 != start]` generates a list of nodes from 1 to n-1 (assuming nodes are numbered starting from 1) excluding the start node.
```python
    for perm in permutations(vertices): # the  function "permutations" from itertools library gives us all the permutations of the vertices array.
        current_route = [start] + list(perm) # Because we initialized the vertices array without the start point
        current_cost = calculate_cost(graph, current_route) #We use the function calculate_cost for each permutation.
        
        if current_cost < min_cost: #We compare the result obtained with 'min_cost'
            min_cost = current_cost # We keep the lowest cost in 'min_cost' ...
            best_route = current_route # ... and we keep the route associated in 'best_route'
```
so we decided to use a permutation of all possible combination and finding the best one using `permutation` function in the itertools
* the `current_route` is for storing the current permutation combination
* after that `current_cost` is storing the current cost's route by calculating it with this function
```
# Function to calculate the cost of a road
def calculate_cost(graph, route):
    cost = 0
    for i in range(len(route) - 1):
        cost += graph[route[i]][route[i+1]] # We recover the cost between two nodes using the graph matrice initialized in the "main" part
    cost += graph[route[-1]][route[0]]  # Don't forget to go back to the start point
    return cost
```
* and then returns the total cost
* and after that minimum cost is found by this lines of code
```
if current_cost < min_cost: #We compare the result obtained with 'min_cost'
    min_cost = current_cost # We keep the lowest cost in 'min_cost' ...
    best_route = current_route # ... and we keep the route associated in 'best_route'
```
* then we can return the `min_cost, best_route`

## Knight's Tour Solution
Code's Credit to: Mattéo
For the Knight's Tour problem we employs a backtracking technique combined with recursive search. 
```c
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
```
* to represent the board we are going to use a 2-D Array `int board[N][N];`
* and then we can initialize it with a for loop
```c
for (int x = 0; x < n; x++)
    for (int y = 0; y < m; y++)
        board[x][y] = -1;
```
* and we can declare a movement vector that represent the movement of a knight 
```
int xMove[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int yMove[8] = {1, 2, 2, 1, -1, -2, -2, -1};
```
* then call the main part of the code, which is to solve the knights tour
### Algorithm's Explanation
```
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
```
so basically in this code we are using backtracking and recursive search
* we have a `next_x` and `next_y` for us to move to a new tile in the board by adding it with the movement vector we just implements
```
int isSafe(int x, int y, int board[N][N], int n, int m) {
    // We have to check if the next x and y are positive AND if they respect the chessboard size.
    // Moreover, the last condition verify that the (x,y) square has never been visited.
    return (x >= 0 && x < n && y >= 0 && y < m && board[x][y] == -1); 
}
```
* and if the board is safe (never been visited, and not outside the desired grid) we can move the knight and recursively call the function again
* if we're stuck at a deadend, we are gonna go back to previous steps that are have a lot of possible moves, hence it's called backtracking
* repeat this until all of the board has been visited
* the way we check it is by using this line of code
```
if (movei == n * m)  // If all the movements has been done, we go out from the recursivity.
        return 1;
```
