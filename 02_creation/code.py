import random

def fancy_forest(num_trees):
    # Generate random heights and random leaf characters
    heights = [random.randint(3, 6) for _ in range(num_trees)]
    leaves = [random.choice(['*', '^', 'o', '@',]) for _ in range(num_trees)]
    widths = [h * 2 - 1 for h in heights]
    
    max_height = max(heights)
    
    # Print the canopy
    for level in range(max_height):
        row = []
        for h, w, char in zip(heights, widths, leaves):
            depth = level - (max_height - h)
            if depth >= 0:
                char_count = 1 + (depth * 2)
                row.append((char * char_count).center(w))
            else:
                row.append(" " * w)
        print(" ".join(row))
        
    # Print the trunks
    for trunk_level in range(2):
        row = []
        for h, w in zip(heights, widths):
            # Only small trees skip the second trunk
            if trunk_level == 1 and h <= 4:
                row.append(" " * w)
            else:
                row.append("|".center(w))
        print(" ".join(row))

fancy_forest(6)

#  -------- OUTPUT ---------
'''

               o                       ^           @     
    *         ooo                     ^^^         @@@    
   ***       ooooo                   ^^^^^       @@@@@   
  *****     ooooooo     ^     ^     ^^^^^^^     @@@@@@@  
 *******   ooooooooo   ^^^   ^^^   ^^^^^^^^^   @@@@@@@@@ 
********* ooooooooooo ^^^^^ ^^^^^ ^^^^^^^^^^^ @@@@@@@@@@@
    |          |        |     |        |           |     
    |          |                       |           |     

'''