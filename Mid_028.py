import heapq

Graph = {
    "S": [("A", 3), ("B",6)],
    "A": [("W", 4), ("C",8)],
    "B": [("W", 3), ("G",9)],
    "W": [("C", 2), ("G",10)],
    "C": [("G", 5)],
    "G": []       
}

A_MAX = 18+8
ID_Parity = "EVEN"

def Tmax(node,time):
    for nb,cost in Graph[node]:
        if node == "B" and nb == "G" and time >= 11:
            continue 
        yield nb,cost 

def heuristic(node):
    to_W ={"S":7,"A":4,"B":3,"W":0,"C":2,"G":999}
    to_G ={"S":15,"A":14,"B":9,"W":10,"C":5,"G":0}
    return to_G[node]
   
def a_star():
    heap = [(0, 0, "S", False, ["S"], A_MAX)]
    visited = set()

    while heap:
        f, g, node, has_water, path, armor = heapq.heappop(heap)

        if (node, has_water) in visited:
            continue
        visited.add((node, has_water))

        if node == "G" and has_water:
            print("Final Path:", " -> ".join(path))
            print("Total Time:", g)
            print("Remaining Armor:", armor)
            return

        for nb, cost in Graph[node]:
            if node == "B" and nb == "G" and g >= 11:
                continue

            new_g = g + cost
            new_armor = armor - cost

            if new_armor <= 0:
                continue

            new_has_water = has_water or (nb == "W")
            if nb == "B":
                new_armor = A_MAX

            new_f = new_g + heuristic(nb)

            heapq.heappush(heap,
                (new_f, new_g, nb, new_has_water, path + [nb], new_armor)
            )
    print("No path found.")

a_star()