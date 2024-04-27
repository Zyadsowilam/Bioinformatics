import numpy as np
import matplotlib.pyplot as plt

def plot_grid(seq1, seq2, window_size=1):
    """
    Generate a grid plot to visualize relationships between two DNA sequences.

    Args:
    - seq1 (str): The first DNA sequence.
    - seq2 (str): The second DNA sequence.
    - window_size (int): The window size for comparing nucleotides. Default is 1.

    Returns:
    - None (Displays the grid plot using matplotlib)
    """
 
    grid = np.zeros((len(seq1), len(seq2)), dtype=str)

  
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i:i+window_size] == seq2[j:j+window_size]:
                grid[i][j] = 'o'

  
    fig, ax = plt.subplots(figsize=(len(seq2), len(seq1)))
    
    
    ax.imshow([[0, 0], [0, 0]], cmap='Greys', interpolation='nearest', extent=(-0.5, len(seq2) - 0.5, -0.5, len(seq1) - 0.5))

    # Draw vertical and horizontal lines to create borders
    for i in range(len(seq1) + 1):
        ax.axhline(y=i - 0.5, color='black', linewidth=1)
    for j in range(len(seq2) + 1):
        ax.axvline(x=j - 0.5, color='black', linewidth=1)

    ax.set_xticks(np.arange(len(seq2)))
    ax.set_yticks(np.arange(len(seq1)))
    ax.set_xticklabels(seq2)
    ax.set_yticklabels(seq1)

 
    ax.xaxis.tick_top()
   
    ax.yaxis.tick_left()

    ax.tick_params(axis='both', which='both', length=0)

    # Add dots for matches
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if grid[i][j] == 'o':
                ax.text(j, i, grid[i][j], ha='center', va='center', color='blue')

   
    plt.savefig('grid_plot.png')
    
    plt.show()

