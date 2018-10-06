# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    # Try counting the children. If the subtree has even number of nodes then the edge leading to 
    #this subtree can be removed. Otherwise, you have to keep on searching until you find a suitable
    #edge or the entire tree exhausted. As it always can be decomposed into forests of even number of nodes, 
    #you will always end up with an answer greater than 1.
    cnt=0
    adjList = collections.defaultdict(list)
    for child,parent in zip(t_from,t_to):
        adjList[parent].append(child)
    
    def bfs(adjList,root):
        stack=[root]
        visited=[]
        while stack:
            node=stack.pop()
            visited.append(node)
            for child in adjList[node]:
                if child not in visited:
                    stack.append(child)
        return visited
    
    b=[]
    for a in adjList:
        b.append(a)
    
    for node in b:
        if len(bfs(adjList,node))%2==0:
            cnt+=1
    return cnt-1