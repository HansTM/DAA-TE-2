import random

def generate_sorted(start: int, end: int, qty: int) -> list:
	if start > end:
		start, end = end, start
	return list(range(start, end, (end-start)//qty))

def generate_random(start: int, end: int, qty: int) -> list:
	arr = []
	for i in range(0, qty):
		arr.append(random.randint(start, end))
	if sum(arr) % 2:
		return generate_random(start, end, qty)
	return arr

def write_data(arr, filename):
	for i in range(0, len(arr)):
		arr[i] = str(arr[i]) + '\n'
	with open(filename, 'w') as file:
		file.writelines(arr)

def read_data(filename):
	with open(filename, 'r') as file:
		arr = file.readlines()
	for i in range(0, len(arr)):
		arr[i] = int(arr[i])
	return arr

from pathlib import Path

if __name__ == "__main__":

	Path('data').mkdir(exist_ok=True)

	for i in [10, 40, 80]:
		write_data(generate_sorted(0, 80, i), Path('data', f'sorted_{i}.txt'))
		write_data(generate_random(0, 80, i), Path('data', f'random_{i}.txt'))
		
	for i in [10, 40, 80]:
		print(len(read_data(Path('data', f'sorted_{i}.txt'))))
		print(len(read_data(Path('data', f'random_{i}.txt'))))