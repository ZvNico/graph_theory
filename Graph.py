import graphviz


class Graph:
    def __init__(self, filename: str = "graph.dot"):
        self.nodes = []
        self.edges = {}
        # self.options = {}
        if (filename.endswith('.dot')):
            self.parsing_dot_file(filename=filename)
        self.render()

    def __str__(self):
        chaine = ""
        return chaine

    def parents(self, node: str) -> list:
        parents = []
        for key, value in self.edges.items():
            if node in value:
                parents.append(key)
        return parents

    def children(self, node: str) -> list:
        return self.edges[node]

    def render(self, format: str = "png") -> None:
        if self.type == 'digraph':
            gv = graphviz.Digraph(format=format)
        else:
            gv = graphviz.Graph(format=format)
        gv.graph_attr['rankdir'] = 'LR'
        for start, value in self.edges.items():
            for node in value:
                gv.edge(start, node)
        gv.render(f'renders/{self.name}.gv')

    def parsing_dot_file(self, filename: str) -> None:
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
        del (lines[0])
        for line in lines:
            if line[0] not in self.nodes:
                self.nodes.append(line[0])
            self.edges[line[0]] = []
            for node in line[2:]:
                if node not in self.nodes:
                    self.nodes.append(node)
                if node not in self.edges[line[0]]:
                    self.edges[line[0]].append(node)
        for node in self.nodes:
            print(node)
