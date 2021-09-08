import graphviz


class Graph:
    def __init__(self, filename="graph.dot"):
        self.nodes = {}
        self.edges = {}
        if (filename.endswith('.dot')):
            self.parsing_dot_file(filename=filename)

    def __str__(self):
        chaine = ""
        return chaine

    def parsing_dot_file(self, filename):
        replace = ["\n", "{", "}", ';']
        file = open("graph/graph.dot", "r")
        lines = file.readlines()
        for elt in replace:
            lines = [line.replace(elt, '') for line in lines]
        lines = [line.split(' ') for line in lines]
        lines = [[elt for elt in line if elt] for line in lines]
        lines = [line for line in lines if line]

        self.type = lines[0][0]
        self.name = lines[0][1]
        for line in lines[1:]:
            print(lines)
