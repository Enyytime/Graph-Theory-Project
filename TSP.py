from itertools import permutations

# Function to calculate the cost of a road
def calculate_cost(graph, route):
    cost = 0
    for i in range(len(route) - 1):
        cost += graph[route[i]][route[i+1]] # We recover the cost between two nodes using the graph matrice initialized in the "main" part
    cost += graph[route[-1]][route[0]]  # Don't forget to go back to the start point
    return cost

# TSP function
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

#Recover the edge names involved in the best route.
def get_edge_names_from_route(route, edge_names):
    edge_list = [] # Initialization of the edge list
    for i in range(len(route) - 1):
        u, v = route[i], route[i+1] #We will run through the best route and the nodes involved by using 'u' and 'v'
        edge_list.append(edge_names[(u, v)] if (u, v) in edge_names else edge_names[(v, u)]) #We add to edge_list the number of the edge listed the 'edge_names' array
    
    # We have to add the edge to come back to the start point
    u, v = route[-1], route[0] # So we take 'u' and 'v' as the last and start point.
    edge_list.append(edge_names[(u, v)] if (u, v) in edge_names else edge_names[(v, u)]) # And we add this last edge number to the edge list.
    return edge_list

# Main
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
