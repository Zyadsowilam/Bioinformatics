
from Bio.Phylo.TreeConstruction import DistanceMatrix
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor

def lower_triangular(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i] = matrix[i][:i+1]
    return matrix

def generate_species_names(num_species):
    species_names = [f"Species{i}" for i in range(1, num_species + 1)]
    return species_names

def save_tree_info(tree, filename):
    with open(filename, "w") as f:
        f.write("Tree Structure:\n")
        f.write(str(tree) + "\n\n")
        f.write("Branch Lengths:\n")
        for clade in tree.find_clades():
            f.write(f"{clade.name}: {clade.branch_length}\n")

distance_matrix_data = [
    [0, 0.5, 0.2, 0.7],
    [0.5, 0, 0.4, 0.9],
    [0.2, 0.4, 0, 0.6],
    [0.7, 0.9, 0.6, 0]
]

species_names = generate_species_names(len(distance_matrix_data))
transformed_matrix = lower_triangular(distance_matrix_data)

distance_matrix = DistanceMatrix(names=species_names, matrix=transformed_matrix)

calculator = DistanceCalculator('identity')
constructor = DistanceTreeConstructor(calculator)
tree = constructor.nj(distance_matrix)


save_tree_info(tree, "tree_info.txt")

Phylo.draw(tree)
