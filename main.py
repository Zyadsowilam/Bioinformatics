from orfs import find_orfs
from dot import plot_grid
from test import stress_test_find_orfs
dna_sequence = "ATGGTACCTTGAAATGTTGAGCTAGCTAG"
# default test min_orf_length=0, start_codons=["ATG"], stop_codons=[ "TAA", "TGA"]
print(find_orfs(dna_sequence))
# test for start and stop codon from user
modified_start_stop=find_orfs(dna_sequence, start_codons=["ATG", "CTG"], stop_codons=["TGA"])
print(modified_start_stop)
# test for minmum value
modified_min=find_orfs(dna_sequence="ATGTAA",min_orf_length=9)
print(modified_min)
#test dot plot
seq1 = "ATCGATCG"
seq2 = "CGATCGAT"
plot_grid(seq1, seq2)
#stress test run it multiple of times or increase num of tests
stress_test_find_orfs(num_tests=10, max_sequence_length=50, min_orf_length=3)