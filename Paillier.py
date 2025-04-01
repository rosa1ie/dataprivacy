from phe import paillier
from Utility import numlist
import time

paillier_start_time = time.perf_counter()

def encrypt_list(numbers, public_key):
    """
    This function encrypts a list of numbers using the provided public key.
    
    Args:
    - numbers (list of int): A list of numbers to be encrypted.
    - public_key (object): The public key object with an encrypt method for encryption.
    
    Returns:
    - list of encrypted values: A list containing the encrypted representation of each number.
    """
    return [public_key.encrypt(n) for n in numbers]

def decrypt_sum(encrypted_numbers, private_key):
    """
    This function ecrypts the sum of a list of encrypted numbers using the provided private key.
    
    Args:
    - encrypted_numbers (list): A list of encrypted numbers.
    - private_key (object): The private key object with a decrypt method for decryption.
    
    Returns:
    - int: The decrypted sum of the encrypted numbers.
    """
    return private_key.decrypt(encrypted_numbers)


public_key, private_key = paillier.generate_paillier_keypair()

encrypted_numbers = encrypt_list(numlist, public_key)

encrypted_sum = sum(encrypted_numbers)

decrypted_sum = decrypt_sum(encrypted_sum, private_key)

paillierAverage = decrypted_sum / len(numlist)

paillier_end_time = time.perf_counter()
