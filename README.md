# BipartiteGraph
Python Script to determine graph "Bipartite-ness" for Algos course.
Reads from standard input where first line represents number of vertices and edges in graph respectively.
Following lines represent vertices. Returns immediately if graph has two edges or less. Otherwise, creates
an adjancey list to represent the graph and by use of a queue, an array to keep track of visted nodes,
and a level count determines if an odd cycle exists in graph which dictates that it is non bipartite.
