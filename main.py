from dyn_view import partition_dyn
from bnb_view import partition_bnb
from gendata import read_data
from pathlib import Path
import time
import gc

# A = [5,4,3,2,1]
# B = [46, 24, 25, 71, 72, 84, 60, 87, 91, 96, 45, 20, 61, 48, 22, 21]

print(partition_dyn([1, 4, 3]))
print(partition_bnb([1, 4, 3]))
