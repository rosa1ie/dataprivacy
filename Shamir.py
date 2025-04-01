from Utility import numlist, n
import random as rand
import time

shamir_start_time = time.perf_counter()

def polynomialValue(coefficients, x):
    """
    This function evaluates the polynomial by getting sum of the function.
    
    Args:
    - coefficients (list): Coefficients of the polynomial.
    - x (int): Point at which the polynomial is to be evaluated.
    
    Returns:
    - int: Value of the polynomial at point x.
    """
    polynomial_value = 0

    for degree, coef in enumerate(coefficients):
        polynomial_value += coef * (x ** degree)

    return polynomial_value

def shamir_share(numbers, k):
    """
    This function generates shares using Shamir's Secret Sharing.
    
    Args:
    - numbers (list): List of secrets.
    - k (int): The threshold number of shares needed to reconstruct the secret.
    
    Returns:
    - list: Shares for each secret.
    """
    shares = []

    for s in numbers:
        poly = [s] + [rand.randint(0, 100) for _ in range(k-1)]    # create polynomial by concatenating secret value and list of k-1 random integers.

        for i in range(1, k+1):
            shares.append(polynomialValue(poly, i))
    
    return shares

def l_formula(i, k):
    """
    Using formula, this function calculates the product for a specific index `i` based on all other indices in the range [1, k].
    
    Args:
    - i (int): The specific index for which l(i) is to be computed.
    - k (int): The threshold number of shares.
    
    Returns:
    - float: The value of l(i).
    """
    product = 1

    for j in range(1, k+1):
        if (j != i):    # exclude the current index 'i' from the product computation
            product *= (-j) / (i - j)

    return product

def averageOfSecrets(shares, k):
    """
    This function calculates the average of the sum of secret numbers reconstructed from the provided shares.
    
    Args:
    - shares (list of lists): A list containing k shares for each secret.
    - k (int): The threshold number of shares needed to reconstruct each secret.
    
    Returns:
    - int: The sum of the reconstructed secrets.
    """
    num_secrets = len(shares) // k
    
    secret_sum = 0
    
    # For each secret, reconstruct it from its k shares and add to the sum
    for j in range(num_secrets):
        secret_reconstructed = 0
        for i in range(1, k+1):
            secret_reconstructed += shares[j*k + i - 1] * l_formula(i, k)
        secret_sum += secret_reconstructed
    return secret_sum / num_secrets


# Example usage
secrets = numlist

k = n // 2

shares = shamir_share(numlist, k)
shamirAverage = averageOfSecrets(shares, k)

shamir_end_time = time.perf_counter()

print(f"The average of Shamir: {shamirAverage}")
