# Graph-Theory-Project

This project is a solution to three classic combinatorial problems: the Traveling Salesman Problem (TSP), the Knight’s Tour Problem and the Chinese Postman Problem, implemented in Python and C/C++, respectively.

# Traveling Salesman Problem (TSP)
The TSP involves finding the shortest possible route that visits a given set of cities (nodes) exactly once and returns to the starting city. Our implementation models the cities as nodes and the roads connecting them as edges with associated travel costs. By utilizing permutations and a cost calculation function, the program evaluates all possible routes to determine the one with the lowest cost. Additionally, it identifies the specific roads used in the optimal route.

# Knight's Tour Problem
The Knight's Tour is a famous problem in chess where the knight, starting from any given square on a chessboard, must visit each square exactly once. Our C-based implementation uses a backtracking algorithm to explore all possible knight moves and finds a solution for a board of any size. If a solution exists, the program outputs the coordinates of the knight's path in the order of their visit.

Both algorithms demonstrate the power of brute-force approaches and the challenges they present in terms of computational complexity, making them excellent examples for educational purposes in combinatorial optimization and graph theory.

# Chinese Postman Problem
The Chinese Postman Problem (also known as the Route Inspection Problem) focuses on finding the shortest possible route that covers all edges of a graph at least once. It is often compared to the TSP but differs in that every edge (or road) must be traversed, making it highly applicable to real-world scenarios like postal delivery routes or street inspections. Our implementation computes the optimal path by first identifying odd-degree vertices and then finding a minimal-cost way to traverse all edges while ensuring all roads are covered at least once. The result is an efficient route that minimizes travel costs and satisfies the requirements of the problem.

## Traveling Salesman Problem (TSP) Solution
Code's Credit to: Matteo
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
