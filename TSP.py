from sys import maxsize #maxsize is the maximum value of a variable of type int
v = 4 #number of vertices

def TSP(graph, s): #s is the starting vertex
    vertex = []
    for i in range(v):
        if i != s:
            vertex.append(i) #vertex is a list of vertices excluding s

    min_path = maxsize # 
    while True: #loop until all permutations are checked
        current_cost = 0
        k = s
        for i in range(len(vertex)):
            current_cost += graph[k][vertex[i]]
            k = vertex[i]
        current_cost += graph[k][s]
        min_path = min(min_path, current_cost)

        if not next_perm(vertex):
            break
    return min_path

def next_perm(l): #l is a list of vertices
    n = len(l)
    i = n-2

    while i >= 0 and l[i] > l[i+1]: #find the largest index i such that l[i] < l[i+1]
        i -= 1
    
    if i == -1: #if no such index exists, the permutation is the last permutation
        return False

    j = i+1
    while j < n and l[j] > l[i]: #find the smallest element greater than l[i]
        j += 1 #j is the index of the smallest element greater than l[i]

    j -= 1 #decrement j to get the index of the smallest element greater than l[i]

    l[i], l[j] = l[j], l[i] #swap l[i] and l[j]
    left = i+1
    right = n-1

    while left < right: #reverse the list
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return True

graph = [[0,10,15,20], [10,0,35,25], [15,35,0,30], [20,25,30,0]] #adjacency matrix of the graph
s = 0
res = TSP(graph,s) #s is the starting vertex of the graph and res is the minimum cost of the TSP
print("Minimun cost of TSP:",res) #print the result

