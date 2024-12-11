from collections import Counter

with open('example.txt', 'r') as file:
    content = file.read()
    stones = list(map(int, content.split()))


def split_number(num):
    num_str = str(num)
    mid = len(num_str) // 2
    return int(num_str[:mid]), int(num_str[mid:])


def blink(stone_counts):
    new_counts = Counter()
    for stone, count in stone_counts.items():
        if stone == 0:
            new_counts[1] += count
        elif len(str(stone)) % 2 == 0:
            left, right = split_number(stone)
            new_counts[left] += count
            new_counts[right] += count
        else:
            new_counts[stone * 2024] += count
    return new_counts


def stone_count_after_blinks_optimized(initial_stones, blinks):
    stone_counts = Counter(initial_stones)
    for _ in range(blinks):
        print(stone_counts)
        stone_counts = blink(stone_counts)
    return sum(stone_counts.values())


result = stone_count_after_blinks_optimized(stones, 75)
print(result)
