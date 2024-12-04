def calculateSimilarity(list_a, list_b):
    item_counts = itemCounts(list_a, list_b)
    similarity = 0
    for i in range(0, len(list_a)):
        i_similarity = int(list_a[i]) * item_counts[i]
        similarity += i_similarity
    return similarity

def itemCounts(list_a, list_b):
    list_a_counts = []
    for item in list_a:
        item_count = list_b.count(item)
        list_a_counts.append(item_count)
    return list_a_counts


path = r"C:\Users\Gamer\Documents\code\adventOfCode\day1\input"
f = open(path)

all_lines = f.readlines()

left = []
right = []

for line in all_lines:
    split_line = line.split()
    left.append(split_line[0])
    right.append(split_line[1])

print(left)
print(right)

left.sort()
right.sort()

print(left)
print(right)

print(calculateSimilarity(left, right))
