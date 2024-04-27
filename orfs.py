

def find_orfs(dna_sequence, min_orf_length=0, start_codons=["ATG"], stop_codons=[ "TAA", "TGA"]):
    """
    Find all Open Reading Frames (ORFs) in a given DNA sequence.

    Args:
    - dna_sequence (str): The input DNA sequence.
    - min_orf_length (int): The minimum length of ORFs to be considered. Default is 0.
    - start_codons (list): The list of start codons to search for. Default is ["ATG"].
    - stop_codons (list): The list of stop codons to search for. Default is ["TAG", "TAA", "TGA"].

    Returns:
    - orfs (list): A list of tuples, where each tuple contains:
        - start_position (int): The start position of the ORF.
        - end_position (int): The end position of the ORF.
        - orf_sequence (str): The sequence of the ORF.
    """

    orfs = []

    for i in range(len(dna_sequence) - 2):
        if dna_sequence[i:i+3] in start_codons:
            for j in range(i+3, len(dna_sequence), 3):
                codon = dna_sequence[j:j+3]
                if codon in stop_codons:
                    
                    orf_sequence = dna_sequence[i:j+3]
                    if len(orf_sequence) >= min_orf_length:
                        orfs.append(dna_sequence[i:j+3])
                    break
                elif len(codon) < 3:
                    print("min")
                    break

    return orfs

