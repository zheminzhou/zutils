import re

class Phylogeny:
    edges = []
    tip_label = []
    node_label = []
    root_lenght = 0.0
    def __init__ (self, tree = None) :
	if tree != None:
	    readTree(tree)
    
    def readTree (self, tree, tip_names) :
        tree2 = tree.strip()
        if tree2[-1] != ';': return (-1)
        
        open_edge = []
        i = len(tree2)-1
        while i >= 0 :
            if tree2[i] == ':' :
                edge_len = 0
                annote = ''
                for j in range(i+1, len(tree2)) :
                    if tree2[j] in (',', ';', ')') :
                        edge_len = float(tree2[(i+1):j])
                        break
                for j in range(i-1, -1, -1) :
                    if tree2[j] in (',', '(', ')') :
                        annote = tree2[(j+1):i]
                        i = j + 1
                        break
                if tree2[j] == ')' :
                    # internal node
                    self.node_label.append(annote)
		    if len(open_edge) > 0 :
			self.edges.append([-open_edge[-1], -len(self.tip_label), edge_len])
		    else :
			self.root_lenght = edge_len
		    open_edge.append(len(self.node_label))
                else :
                    # tip node
                    self.tip_label.append(annote)
                    self.edges.append([-open_edge[-1], len(self.tip_label), edge_len])
            
            elif tree2[i] == '(' :
                del open_edge[-1]
                if len(open_edge) < 1:
                    break
	    i -= 1
	
        for e in self.edges :
	    e[0] = len(self.tip_label) - e[0]
            if e[1] < 0:
                e[1] = len(self.tip_label) - e[1]
	    else :
		e[1] = len(self.tip_label) - e[1] + 1
	self.tip_label = self.tip_label[::-1]
        return (0)

    def readNexus (self, treefile) :
	with open(treefile, 'r') as fin:
	    for line in fin:
		
    def readNewick (self, treefile) :
	tree = []
	with open(treefile, 'r') as fin:
	    for line in fin:
		tree.append(line.strip())
	return readTree(tree)
if __name__ == '__main__':
    import sys
    tr = Phylogeny()
    tree = open(sys.argv[1], 'r').readline().strip()
    tr.readTree(tree)
    print tr.edges
	