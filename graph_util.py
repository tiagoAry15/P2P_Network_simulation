import networkx as nx


class GraphBuilder:
    def __init__(self):
        self.G = nx.Graph()
        self.resources = {}
        self.edges = []
        self.min_neighbors = 0
        self.max_neighbors = 0
        self.num_nodes = 0
        self.is_connected = False
        self.valid_neighbors = False
        self.no_empty_resources = False

    def build(self, file_content):
        lines = file_content.split("\n")
        self.num_nodes = int(lines[0].split(":")[1].strip())
        self.min_neighbors = int(lines[1].split(":")[1].strip())
        self.max_neighbors = int(lines[2].split(":")[1].strip())

        is_resources_section = False
        for line in lines[3:]:
            if line.strip() == "":
                break
            if line.strip() == "resources:":
                is_resources_section = True
            elif line.strip() == "edges:":
                is_resources_section = False
            elif is_resources_section:
                node, resource_str = line.strip().split(":")
                self.resources[node.strip()] = [r.strip() for r in resource_str.split(",")]
            else:
                node1, node2 = line.strip().split(",")
                self.edges.append((node1.strip(), node2.strip()))

        # Adicionar nós com recursos
        for node, node_resources in self.resources.items():
            self.G.add_node(node, resources=node_resources)

        # Adicionar arestas
        for edge in self.edges:
            node1, node2 = edge
            if node1 != node2 and node1 in self.G and node2 in self.G:
                self.G.add_edge(node1, node2)

        # Verificar se a rede é conexa
        self.is_connected = nx.is_connected(self.G)

        # Verificar os limites de vizinhos para cada nó
        self.valid_neighbors = all(self.min_neighbors <= self.G.degree[node] <= self.max_neighbors for node in self.G.nodes)

        # Verificar se não há nós sem recursos
        self.no_empty_resources = all(len(self.G.nodes[node]["resources"]) > 0 for node in self.G.nodes)
        if not self.is_connected:
            print("A rede não é conexa")
        if not self.valid_neighbors:
            print("A rede não possui o número de vizinhos válido")
        if not self.no_empty_resources:
            print("A rede possui nós sem recursos")

        if self.is_connected and self.valid_neighbors and self.no_empty_resources:
            return self.G
        else:
            return None


