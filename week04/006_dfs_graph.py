graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)
    for adjacent in adjacent_graph:
        if adjacent not in visited_array:
            dfs_recursion(adjacent_graph, adjacent, visited_array)
    if len(adjacent_graph.keys()) == len(visited_array):
        return visited_array


def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    discovered = []
    while True:
        node = stack.pop()
        discovered.append(node)
        for adj in adjacent_graph[node]:
            if adj not in discovered:
                stack.append(adj)
        if len(adjacent_graph) == len(discovered):
            return discovered


print(dfs_recursion(graph, 1, []))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!
print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!
