from dyn import partition_dyn
from bnb import partition_bnb
from gendata import read_data
from pathlib import Path
import time
import gc
from pympler import asizeof 
import psutil
import tracemalloc
import humanize

# process = psutil.Process()

iters = 3

for func in [partition_dyn, partition_bnb]:
	for type in ['random']:
		for num in [10, 40, 80]:
			
			print(f"{func.__name__} {type} {num}:")
			total_time = 0
			total_size = 0

			for i in range(0, iters):
				data = None
				gc.collect()
				data = read_data(Path('data', f'{type}_{num}.txt'))

				start_time = time.time()
				# start_size = process.memory_info().rss
				tracemalloc.start()

				print(func(data), end='\t')

				# iter_size = process.memory_info().rss - start_size
				iter_size = tracemalloc.get_traced_memory()[1]
				tracemalloc.stop()
				iter_time = time.time() - start_time
				total_time += iter_time
				total_size += iter_size
				
				print(f'{round(iter_time * 1000, 4)} ms\t{iter_size / 1000} kB\t{humanize.naturaldelta(iter_time, minimum_unit="milliseconds")}\t{humanize.naturalsize(iter_size)}')
				# print(f'{round(iter_time * 1000, 4)}ms')

				time.sleep(0.5)
			
			print(f'Avg  \t{round(total_time / iters * 1000, 4)} ms\t{total_size / iters / 1000} kB\t{humanize.naturaldelta(total_time / iters, minimum_unit="milliseconds")}\t{humanize.naturalsize(total_size / iters)}')
			# print(f'{round((total_time/iters) * 1000, 4)}ms')
