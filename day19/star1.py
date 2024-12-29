import time

test = False


if test:
    file_name = "simple_example.txt"
else:
    file_name = "example.txt"


def read_from_file():
    with open(file_name, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    available_strips = [item.strip() for item in lines[0].split(",")]
    to_solve = lines[1:]
    print("available_strips_hash: ", len(available_strips), ", ", available_strips)
    print("Other lines array: ",  len(to_solve), ", ", to_solve)
    return available_strips, to_solve


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, s, start, memo):
        if start == len(s):
            return True
        if start in memo:
            return memo[start]

        node = self.root
        for i in range(start, len(s)):
            char = s[i]
            if char not in node.children:
                break
            node = node.children[char]
            if node.is_end_of_word and self.search(s, i + 1, memo):
                memo[start] = True
                return True

        memo[start] = False
        return False


def resolve():
    available_strips, to_solve = read_from_file()
    trie = Trie()
    for strip in available_strips:
        trie.insert(strip)

    result = 0
    for strip in to_solve:
        print(strip, to_solve.index(strip))
        if trie.search(strip, 0, {}):
            result += 1
    return result


if __name__ == "__main__":
    start_time = time.time()
    result = resolve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
