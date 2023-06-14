class Algorithms:

    def find_resource(self, initial_node_id, resource_id, ttl: int, algo: str):
        match algo:
            case "flooding":
                return self.flooding(initial_node_id, resource_id, ttl)
            case "informed_flooding":
                return self.informed_flooding(initial_node_id, resource_id, ttl)
            case "random_walk":
                return self.random_walk(initial_node_id, resource_id, ttl)
            case "informed_random_walk":
                return self.informed_random_walk(initial_node_id, resource_id, ttl)

    def flooding(self, initial_node_id, resource_id, ttl, graph):
        visited = set()
        queue = [initial_node_id]

        while queue:
            node = queue.pop(0)
            visited.add(node)

            if graph.nodes[node]['value'] == resource_id:
                return node

            neighbors = graph.neighbors(node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

        pass

    def informed_flooding(self, initial_node_id, resource_id, ttl):
        pass

    def random_walk(self, initial_node_id, resource_id, ttl):
        pass

    def informed_random_walk(self, initial_node_id, resource_id, ttl):
        pass
