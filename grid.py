size = 7

for i in range(size):
	for j in range(size):
		if j == 0 or j == size - 1 or i == j:
			print("*", end=" ")
		else:
			print(" ", end=" ")
	print()
