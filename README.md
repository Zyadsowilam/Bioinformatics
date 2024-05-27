# Bioinformatics

**README**

## Dot Plot

### Introduction

The Dot Plot program generates a visual representation of the relationship between two DNA sequences using a dot plot. Dot plots are widely used in bioinformatics to identify similarities, repeats, and other patterns in biological sequences.

### Usage

To use the Dot Plot program, you need to provide two DNA sequences as input. The program will then generate a dot plot to visualize the relationships between these sequences.

### Installation

No installation is required to use the Dot Plot program. Simply download the Python script and execute it using a Python interpreter.

### Example

```python 
from dot import plot_grid
 
# Define two DNA sequences
sequence1 = "ATCGATCGATCG"
sequence2 = "ATCGATAGCTAG"

# Generate dot plot
dot_plot.plot(sequence1, sequence2)
```

## ORFs (Open Reading Frames)

### Introduction

The ORFs program identifies and extracts Open Reading Frames (ORFs) from a given DNA sequence. ORFs are sequences of DNA that have the potential to encode proteins.

### Usage

To use the ORFs program, provide a DNA sequence as input. The program will then search for ORFs within the sequence and return their start and end positions, along with the ORF sequences.

### Installation

No installation is required to use the ORFs program. Simply download the Python script and execute it using a Python interpreter.

### Example

```python

from orfs import find_orfs

# Define DNA sequence
dna_sequence = "ATGAGCTAGCTAGTAA"

# Find ORFs
orfs = orfs_finder.find_orfs(dna_sequence)

# Print ORFs
for start, end, sequence in orfs:
    print(f"Start: {start}, End: {end}, Sequence: {sequence}")
```

## Testing

### Introduction

The Testing module contains stress tests /unit for ORFs programs to ensure their functionality and reliability.

### Usage

To run the tests, execute the test script provided for each program. The tests will verify that the programs produce the expected output for different input scenarios.Using random sequence of DNA

### Installation

No installation is required to run the tests. Simply download the test scripts and execute them using a Python interpreter.

### Example

```bash
from test import stress_test_find_orfs
stress_test_find_orfs(num_tests=10, max_sequence_length=50, min_orf_length=3)

```
# Neighbor Joining Algorithm

## Introduction

This Python script implements the Neighbor Joining algorithm, a method in bioinformatics for the construction of phylogenetic trees from a distance matrix representing the evolutionary distances between pairs of species or taxa.
## Without using BioPython ApplyNeighbourJoining.py
## Requirements

- pandas
- numpy
- matplotlib
- networkx

You can install the required packages via pip:

```bash
pip install pandas numpy matplotlib networkx
```
## Input
The input distance matrix should be a square matrix where each cell represents the evolutionary distance between two species or taxa. The distances should be symmetric, i.e., the distance from species A to species B should be the same as the distance from species B to species A.
Example input:

```python
distMatrix = pd.DataFrame(
    [
        [0, 0.17, 0.59, 0.59, 0.77, 0.81, 0.87],
        [0.17, 0, 0.6, 0.59, 0.77, 0.82, 0.86],
        [0.59, 0.6, 0, 0.13, 0.75, 0.73, 0.86],
        [0.59, 0.59, 0.13, 0, 0.75, 0.74, 0.88],
        [0.77, 0.77, 0.75, 0.75, 0, 0.8, 0.93],
        [0.81, 0.82, 0.73, 0.74, 0.8, 0, 0.9],
        [0.87, 0.86, 0.86, 0.88, 0.93, 0.9, 0]
    ]
)
```
## Output
The script will generate two files:

- joins.txt: Contains the details of each join made during the neighbor joining process.
- neighbor_joining_tree.png: Visual representation of the constructed neighbor joining tree.
- Additionally, during execution, the script will write the join details to joins_and_distances.txt.
## With using BioPython ApplyNeighbourJoiningBioPython.py

## Requirements

- Biopython

You can install Biopython via pip:

```bash
pip install biopython
```
## Input
The input distance matrix should be a square matrix where each cell represents the evolutionary distance between two species or taxa. The distances should be symmetric, i.e., the distance from species A to species B should be the same as the distance from species B to species A.
Example input:

```python
distance_matrix_data = [
    [0, 0.5, 0.2, 0.7],
    [0.5, 0, 0.4, 0.9],
    [0.2, 0.4, 0, 0.6],
    [0.7, 0.9, 0.6, 0]
]
```
## Output
The script will generate a file named tree_info.txt which contains the tree structure and branch lengths. Additionally, it will display the phylogenetic tree graphically.


