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

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def count_ways_to_form_word(self, word, memo={}):
        if word in memo:
            return memo[word]

        if not word:
            return 1

        ways = 0
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            if self.search(prefix):
                ways += self.count_ways_to_form_word(word[i:], memo)

        memo[word] = ways
        return ways


def resolve():
    available_strips, to_solve = read_from_file()
    trie = Trie()
    for strip in available_strips:
        trie.insert(strip)

    result = 0
    for strip in to_solve:
        result += trie.count_ways_to_form_word(strip)
    return result


if __name__ == "__main__":
    start_time = time.time()
    result = resolve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Result: {result}")
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
