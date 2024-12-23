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


def resolve():
    graph = read_from_file()
    # print(graph)
    already_in_set = set()
    for key, connections in graph.items():
        if not key.startswith("t"):
            continue
        for connect_2 in connections:
            for connect_3 in graph[connect_2]:
                if connect_3 in graph[key] and connect_3 != key and tuple(sorted([key, connect_2, connect_3])) not in already_in_set:
                    already_in_set.add(tuple(sorted([key, connect_2, connect_3])))

    # for item in sorted(already_in_set):
    #     print(item)
    return len(already_in_set)

if __name__ == "__main__":
    start_time = time.time()
    result = resolve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")





