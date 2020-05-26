def get_neighbours(namedGraph, node):
    neighbourNames = []
    nodePosition = get_node_position(namedGraph, node)
    y = nodePosition[0]
    x = nodePosition[1]
    try:
        if y - 1 < 0 or namedGraph[y - 1][x] == 0:
            pass
        else:
            neighbourNames.append(namedGraph[y - 1][x])
    except:
        pass
    try:
        if y - 1 < 0 or namedGraph[y - 1][x + 1] == 0:
            pass
        else:
            neighbourNames.append(namedGraph[y - 1][x + 1])
    except:
        pass
    try:
        if namedGraph[y][x + 1] == 0:
            pass
        else:
            neighbourNames.append(namedGraph[y][x + 1])
    except:
        pass
    try:
        if namedGraph[y + 1][x + 1] == 0:
            pass
        else:
            neighbourNames.append(namedGraph[y + 1][x + 1])
    except:
        pass
    try:
        if namedGraph[y + 1][x] == 0:
            pass
        else:
            neighbourNames.append(namedGraph[y + 1][x])
    except:
        pass
    try:
        if x - 1 < 0 or namedGraph[y + 1][x - 1] == 0:
            pass
        else:
            neighbourNames.append(namedGraph[y + 1][x - 1])
    except:
        pass
    try:
        if x - 1 < 0 or namedGraph[y][x - 1] == 0:
            pass
        else:
            neighbourNames.append(namedGraph[y][x - 1])
    except:
        pass
    try:
        if y - 1 < 0 or x - 1 < 0 or namedGraph[y - 1][x - 1] == 0:
            pass
        else:
            neighbourNames.append(namedGraph[y - 1][x - 1])
    except:
        pass
    return list(set(neighbourNames))


def print_board(board):
    for row in board:
        print(row)


def get_node_position(namedGraph, node):
    size = len(namedGraph)
    for y in range(size):
        for x in range(size):
            if namedGraph[y][x] == node:
                return [y, x]


def create_named_graph(graph):
    height = len(graph)
    width = len(graph[0])
    namedGraph = []
    namedRow = []
    number = 0
    for y in range(height):
        for x in range(width):
            if graph[y][x] != 1:
                namedRow.append(0)
                continue
            number += 1
            namedRow.append(number)
        namedGraph.append(namedRow)
        namedRow = []
    return namedGraph


def get_list_of_nodes_to_visit(graph):
    nodesList = []
    for row in graph:
        for number in row:
            if number != 0:
                nodesList.append(number)
    return nodesList


def get_unique_nodes_from_paths(pathsInCurrentIsland):
    uniqueNodes = []
    for path in pathsInCurrentIsland:
        for number in path:
            uniqueNodes.append(number)
    return set(uniqueNodes)


def remove_duplicate_sets(listName):
    uniqueList = []
    for sett in listName:
        if sett not in uniqueList:
            uniqueList.append(sett)
    return uniqueList


def traverse_from_node(startNode, visited, pathsInCurrentIsland):
    """this recursive/backtracking DFS function goes through all connected nodes on single island
        and when all nodes have been visited it appends those paths[sets] to pathsInCurrentIsland list

    Arguments:
        startNode {[int]} -- [traversing will start from this node]
        visited {[tuple]} -- [tuple with visited nodes]
        pathsInCurrentIsland {list} -- [empty list]
    """
    visited += (startNode,)

    neighbours = get_neighbours(namedMap, startNode)
    for neighbour in neighbours:
        if neighbour in visited:
            continue
        else:
            traverse_from_node(neighbour, visited, pathsInCurrentIsland)
            continue
        return

    pathsInCurrentIsland.append(set(visited))


def get_islands():
    """the function iterates over every possible starting node on the namedMap and uses
    recursive/backtracking DFS function -> traverse_from_node() to get all neighbours an paths 
    From every path only unique nodes are taken to "create an island"
    Current island (created from current startingNode) is appended to uniqueIslands
    pathsInCurrentIsland is cleared and function starts over with next node from toVisit list
    function returns allIslands visited (with duplicate islands)

    Returns:
        [list] -- [list of sets - ALL visited islands (with duplicates)]
    """

    pathsInCurrentIsland = []
    allIslands = []
    toVisit = get_list_of_nodes_to_visit(namedMap)

    for node in toVisit:
        visited = ()
        traverse_from_node(node, visited, pathsInCurrentIsland)
        island = get_unique_nodes_from_paths(pathsInCurrentIsland)
        allIslands.append(island)
        pathsInCurrentIsland.clear()

    return allIslands


if __name__ == "__main__":

    graph = [[1, 1, 1, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 1, 1]]

    namedMap = create_named_graph(graph)
    print("Named graph:")
    print_board(namedMap)

    toVisit = get_list_of_nodes_to_visit(namedMap)
    uniqueIslandsList = remove_duplicate_sets(get_islands())

    print("Unique islands nodees:")
    print(uniqueIslandsList)
    print("Number of islands:", len(uniqueIslandsList))
