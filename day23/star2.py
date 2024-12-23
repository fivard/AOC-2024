import time


test = False


if test:
    file_name = "simple_example.txt"
else:
    file_name = "example.txt"


def read_from_file():
    graph = {}
    with open(file_name, "r") as file:
        list_of_connections = []
        for line in file:
            splitted = line.strip().split("-")
            list_of_connections.append(splitted)

        for connect in list_of_connections:
            if connect[0] not in graph:
                graph[connect[0]] = set()
            if connect[1] not in graph:
                graph[connect[1]] = set()
            graph[connect[0]].add(connect[1])
            graph[connect[1]].add(connect[0])
    return graph


def bron_kerbosch(R, P, X, graph, largest_clique):
    if not P and not X:
        if len(R) > len(largest_clique[0]):
            largest_clique[0] = R
        return

    for vertex in list(P):
        bron_kerbosch(
            R | {vertex},
            P & graph[vertex],
            X & graph[vertex],
            graph,
            largest_clique
        )
        P.remove(vertex)
        X.add(vertex)


def resolve():
    graph = read_from_file()
    R = set()
    P = set(graph.keys())
    X = set()
    largest_clique = [set()]

    # Виклик алгоритму
    bron_kerbosch(R, P, X, graph, largest_clique)

    return ",".join(sorted(largest_clique[0]))


if __name__ == "__main__":
    start_time = time.time()
    result = resolve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")





