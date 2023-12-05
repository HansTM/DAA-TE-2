# from memory_profiler import profile

best_err = None

# Partition the values. Return an array with entry i = true if
# value i belongs in the first set of the partition.
# @profile(precision=6)
def partition_bnb(values):
	global best_err

	# test_assignment = [False] * len(values)

	# Get the total of all values.
	total_value = sum(values)

	if total_value % 2 != 0:
		return False
	
	# Partition the values starting with index 0.
	best_err = total_value
	partition_values_from_index(values, 0, total_value, total_value, 0)
	
	# Return the result.
	return best_err == 0

# Partition the values keeping those before index start_index fixed.
# test_assignment is the test assignment so far.
# test_value is the total value of the first set in the test assignment.
# Initially best assignment and its error are in best_assignment and best_err.
# Update those to reflect any improved solution we find.
# @profile(precision=6)
def partition_values_from_index(values, start_index, total_value, unassigned_value, test_value, tabs = ''):

	print(f'{tabs}CALL {start_index, unassigned_value, test_value}')
	
	global best_err
	if best_err == 0:
		return
	
	# print(start_index, unassigned_value, best_err, test_assignment1)

	# If start_index is beyond the end of the array,
	# then all entries have been assigned.
	if start_index >= len(values):

		# print(start_index)
		# We're done. See if this assignment is better than what we have so far.

		test_err = abs(2 * test_value - total_value)
		# print(f'test_err: {test_err}')
		# print(f'best_err: {best_err}')
		if test_err < best_err:
			# This is an improvement. Save it.
			best_err = test_err

			# print(f'best_err: {best_err}')
	
	else:
	
		# See if there's any way we can assign
		# the remaining items to improve the solution.
		test_err = abs(2 * test_value - total_value)
		potential_err = test_err - unassigned_value

		if potential_err < best_err:
			# print(f'potential_err: {potential_err}')

			# There's a chance we can make an improvement.
			# We will now assign the next item.

			unassigned_value -= values[start_index]
			
			# Try adding values[start_index] to set 1.
			# test_assignment[start_index] = True

			partition_values_from_index(values, start_index + 1, total_value, unassigned_value, test_value + values[start_index], tabs + '   ')
			
			# Try adding values[start_index] to set 2.
			# test_assignment[start_index] = False

			partition_values_from_index(values, start_index + 1, total_value, unassigned_value, test_value, tabs + '   ')

	print(f'{tabs}CALL {start_index, unassigned_value, test_value} END')