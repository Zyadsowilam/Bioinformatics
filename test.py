"""
Just random sequence
"""

import random
from orfs import find_orfs
import random

def generate_random_sequence(length):
    """
    Generate a random DNA sequence of specified length with at least one ORF.

    Args:
    - length (int): The length of the DNA sequence to generate.

    Returns:
    - sequence (str): The generated DNA sequence.
    """
    # Generate random DNA sequence
    sequence = ''.join(random.choices('ATGC', k=length))
    
    # Insert start codon "ATG" at random position with 50% probability
    if random.random() < 0.5:
        start_index = random.randint(0, length - 3)
        sequence = sequence[:start_index] + "ATG" + sequence[start_index + 3:]
    
    # Insert stop codon "TGA" at random position with 50% probability
    if random.random() < 0.5:
        stop_index = random.randint(0, length - 3)
        sequence = sequence[:stop_index] + "TGA" + sequence[stop_index + 3:]

    return sequence

# Test the modified function


def stress_test_find_orfs(num_tests, max_sequence_length, min_orf_length=0):
    """
    Stress test the find_orfs function with random DNA sequences.

    Args:
    - num_tests (int): The number of random DNA sequences to generate and test.
    - max_sequence_length (int): The maximum length of the random DNA sequences.
    - min_orf_length (int): The minimum length of ORFs to be considered. Default is 0.

    Returns:
    - None
    """
    for i in range(num_tests):
        sequence_length = random.randint(10, max_sequence_length)
        dna_sequence = generate_random_sequence(sequence_length)
        print(f"Test {i+1}: DNA Sequence - {dna_sequence}")
        orfs = find_orfs(dna_sequence, min_orf_length=min_orf_length)
        print("ORFs found:")
        for orf in orfs:
            print(orf)
        print("-" * 50)

