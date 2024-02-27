#!/usr/bin/env python3

# Import necessary modules
from multiprocessing import Pool
import multiprocessing
import subprocess
import os

# Expand '~' to the full home directory path
home_path = os.path.expanduser('~')

# Define source and destination paths for backup
src = home_path + "/data/prod/"
dest = home_path + "/data/prod_backup/"

# This block will only be executed if the script is run directly (not imported as a module)
if __name__ == "__main__":
    # Create a pool of worker processes equal to the number of CPU cores
    pool = Pool(multiprocessing.cpu_count())
    
    # Use multiprocessing to run rsync in parallel for efficient directory sync
    # Rsync options '-arq' archive data, preserve attributes, and quiet non-errors
    pool.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))
