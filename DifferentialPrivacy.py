import numpy as np
from Utility import numlist
import time

diff_start_time = time.perf_counter()

def laplace_mechanism(numlist, epsilon):
    """
    Apply the Laplace mechanism to add noise to the query result.
    
    Args:
        query_result (float): The original query result.
        sensitivity (float): The sensitivity of the query (maximum difference in query result when data changes one unit).
        epsilon (float): Privacy parameter that controls the privacy guarantee.
    
    Returns:
        float: Noisy query result.
    """

    noise_count = np.random.laplace(1 / epsilon)
    noise_sum = np.random.laplace(max(numlist) / epsilon)

    count_D = len(numlist) + noise_count
    sum_D = sum(numlist) + noise_sum

    average = sum_D / count_D

    return average


# Your dataset (you can replace this with your actual data)
data = numlist

# Privacy budget
privacy_budget = 1.0

# Perform the private counting query
diffAverage = laplace_mechanism(data, privacy_budget)

diff_end_time = time.perf_counter()
