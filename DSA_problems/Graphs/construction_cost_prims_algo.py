
class Pair:
    def __init__(self, node,  weight):
        self.node = node
        self.weight = weight
    
    def __lt__(self, other):
        return self.weight < other.weight
    
    def __gt__(self, other):
        return self.weight > other.weight
    
    def __repr__(self):
        return f"node:{self.node}-wt:{self.weight}"


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        import heapq
        if not len(B):
            return 0

        m = 10 ** 9 + 7

        graph = build_graph(A, B)
        print("graph",graph)
        visited = [False for _ in range(A + 1)]
        heap = []
        start = A
        visited[start] = True
        children = graph[start]

        for child in children:
            if not visited[child.node]:
                heapq.heappush(heap, child)

        min_cost = 0
        
        while len(heap):
            current = heapq.heappop(heap)
            curr_wt = current.weight
            curr_node = current.node
            print("current", current)

            if visited[curr_node]:
                # print("continued", current)
                continue
            
            visited[curr_node] = True
            min_cost += curr_wt

            children = graph[curr_node]
            # print("children", children)
            for child in children:
                if not visited[child.node]:
                    heapq.heappush(heap, child)
            
            print("min_cost", min_cost,"\n")
            print("heapppp", heap)

        
        return min_cost



        

def build_graph(nodes, edges):
    graph = [list() for i in range(nodes + 1)]
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        wt = edges[i][2]
        p = Pair(v, wt)
        graph[u].append(p)
        
    return graph



