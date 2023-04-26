# Table of Contents

[toc]

# Tree

# Tree + Tab Generator

The two principally interact with the `consult_tree` and `generate_tab_dictionary` methods in tab\_generator.py

1. `generate_tab_dictionary` will be modified to first call `consult_tree` to analyze if any patterns can be applied to the notes provided. 
2. The effects of this are:
	1. the `notes` parameter that `generate_tab_dictionary` takes will now be a mix of instances of the `Note` class and FretboardPositions
	2. one of these 2 will have to be modified as such:
		1. `generate_tab_dictionary` will use the `continue` keyword to skip over `FretboardPosition` instances 
		2. OR `get_best_next_position` will be modified to return the `FretboardPosition` instance passed to it (thus making no changes)
