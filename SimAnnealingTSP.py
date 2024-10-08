import random
import math

# Function to calculate the cost of a road
def calculate_cost(graph, route):
    cost = 0
    for i in range(len(route) - 1):
        cost += graph[route[i]][route[i+1]]  # We recover the cost between two nodes using the graph matrice initialized in the "main" part
    cost += graph[route[-1]][route[0]]  # Don't forget to go back to the start point
    return cost

# Function to perform a random swap between two cities
def swap_cities(route):
    new_route = route[:]
    i, j = random.sample(range(1, len(route)), 2)  # Randomly swap two cities, keeping the start city fixed
    new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route

# Simulated Annealing TSP
def tsp_simulated_annealing(graph, start, max_iterations=1000, initial_temp=1000, cooling_rate=0.995):
    n = len(graph)
    current_route = [start] + [i for i in range(n) if i != start]
    currentEnergy = calculate_cost(graph, current_route)
    
    best_route = current_route[:]
    best_cost = currentEnergy
    
    temperature = initial_temp
    
    while temperature > 0.01:
        #generate a neighboring solution by swapping two citiesw
        new_route = swap_cities(current_route)
        nextEnergy = calculate_cost(graph, new_route)
        
        deltaEnergy = currentEnergy - nextEnergy
        #accept the new solution based on probability (Simulated Annealing Acceptance Criterion)
        if nextEnergy < currentEnergy or random.uniform(0, 1) < math.exp((deltaEnergy) / temperature):
            current_route = new_route[:]
            currentEnergy = nextEnergy
            
            if currentEnergy < best_cost: #update the best solution found
                best_route = current_route[:]
                best_cost = currentEnergy
        
        #cool down the temperature
        temperature *= cooling_rate 
    
    return best_cost, best_route

# Recover the edge names involved in the best route.
def get_edge_names_from_route(route, edge_names):
    edge_list = []  # Initialization of the edge list
    for i in range(len(route) - 1):
        u, v = route[i], route[i+1]  # We will run through the best route and the nodes involved by using 'u' and 'v'
        edge_list.append(edge_names[(u, v)] if (u, v) in edge_names else edge_names[(v, u)])  # We add to edge_list the number of the edge listed the 'edge_names' array
    
    # We have to add the edge to come back to the start point
    u, v = route[-1], route[0]  # So we take 'u' and 'v' as the last and start point.
    edge_list.append(edge_names[(u, v)] if (u, v) in edge_names else edge_names[(v, u)])  # And we add this last edge number to the edge list.
    return edge_list

# Main
if __name__ == "__main__":
    # We recover the number of nodes and edges
    n = int(input("Enter the number of nodes: "))
    e = int(input("Enter the number of edges: "))
    
    graph = [[float('inf') for _ in range(n)] for _ in range(n)]  # Initialization of the cost matrix.
    edge_names = {}  # Initialization of the edge names list.

    print("Enter the edges informations in the form of: edge_number node1 node2 cost")
    for _ in range(e):
        edge_info = input().split()  # This function '.split' allows you to recover data in an array
        edge_num = int(edge_info[0])  # Edge number
        u = int(edge_info[1]) - 1  # Node 1 connected to the edge (adjusted to 0-based index)
        v = int(edge_info[2]) - 1  # Node 2 connected to the edge (adjusted to 0-based index)
        cost = int(edge_info[3])  # Cost of the edge
        if graph[u][v] != 0:
            if graph[u][v] >= cost:  # If 2 edges connect 2 same nodes, we have to compare the cost of the edges to keep the lowest cost.
                graph[u][v] = cost  # We suppose here that we are not in a digraph...
                graph[v][u] = cost  # ... so u->v cost is the same as v->u.
                edge_names[(u, v)] = edge_num  # We recover the number of the edges.
                edge_names[(v, u)] = edge_num  # As we suppose that we are not in a digraph. The number of (u,v) is the same as (v,u)

    start = int(input("Enter the start point: ")) - 1  # Recover the start point (adjusted to 0-based index)
    
    print(edge_names)
    
    # Traveling Salesman Problem solving with Simulated Annealing
    min_cost, best_route = tsp_simulated_annealing(graph, start)

    # We have to check if a route has been found
    if best_route:
        print("Cost:", min_cost)
        
        # Print the best route (node path)
        node_path = [node + 1 for node in best_route]  # Convert node indices back to 1-based
        print("Node Path:", ' -> '.join(map(str, node_path)))

        # Recover and print the edge names along the route
        edge_route = get_edge_names_from_route(best_route, edge_names)  # We recover the number of the edges by using the best route and all the edge names used
        print("Edges Route:", ', '.join(map(str, edge_route)))
    else:
        print("No valid route found.")
