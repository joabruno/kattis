while True:
    try:
        case = input()
    except EOFError:
        break
    if case == "0 0 0 0":
                break
    case_args = case.split()
    vertices = int(case_args[0])
    edges = int(case_args[1])
    queries = int(case_args[2])
    source = int(case_args[3])

    graph2 = []
    visited = []
    dist = []
    for _ in range(vertices):
        graph2.append([])
        visited.append(False)
        dist.append(float('inf'))

    for _ in range(edges):
        edge = input().split()
        graph2[int(edge[0])].append((int(edge[1]), int(edge[2])))
    
    dist[source] = 0
    current_set = {source}
    current_list = [source]
    while len(current_set) > 0:
        curr_closest = current_list[0]
        for i in current_list:
            if dist[i] < dist[curr_closest]:
                curr_closest = i


        #curr_closest = current_list[0]
        out_edges2 = graph2[curr_closest]
        for out in out_edges2:
            dest, weight = out
            if dist[curr_closest] + weight < dist[dest]:
                dist[dest] = dist[curr_closest] + weight
            if not visited[dest] and dest not in current_set:
                current_set.add(dest)
                current_list.append(dest)
        current_set.remove(curr_closest)
        current_list.remove(curr_closest)
        visited[curr_closest] = True
    for _ in range(queries):
        q = int(input())
        print(dist[q]) if dist[q] != float('inf') else print("Impossible")
    print("")