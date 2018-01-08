import community
import networkx as nx

# load the edge list and create a directed Graph
fh = open("hamster.edgelist", 'rb')
G = nx.read_edgelist(fh)
fh.close()

# This method implements Louvain method using a greedy algorithm
# This is the partition of highest modularity, 
# i.e. the highest partition of the dendrogram generated by the Louvain algorithm
# more details: http://perso.crans.org/aynaud/communities/api.html#community.best_partition
partition = community.best_partition(G)

# partition is the returned results of best_partition
# it is a dict in Python
print partition