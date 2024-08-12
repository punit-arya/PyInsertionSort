"""PyInsertionSort: insertion sort implementation."""

import random

inputSequence = [random.randrange(10) for _ in range(10)]
print("inputSequence:", inputSequence)

# for i in range(len(inputSequence)):
# 	for j in range(i, len(inputSequence)):
# 		if inputSequence[i] > inputSequence[j]:
# 			# t = inputSequence[i]
# 			# inputSequence[i] = inputSequence[j]
# 			# inputSequence[j] = t
# 			inputSequence[i], inputSequence[j] = inputSequence[j], inputSequence[i]

# CLRS implementation:
for i in range(1, len(inputSequence)):
	key = inputSequence[i]
	j = i - 1
	while j >= 0 and inputSequence[j] > key:
		inputSequence[j + 1] = inputSequence[j]
		j -= 1
	inputSequence[j + 1] = key

print("inputSequence:", inputSequence)
