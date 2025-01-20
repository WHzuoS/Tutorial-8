# Graph = (Vertices, Edges)
# Vertices = [a,b,c,d]
# Edges = [(a,b),(a,c),(a,d),(b,c),(d,a),(d,b),(d,c)]

adjacencyMatrix = [[0,1,1,1],
                   [0,0,1,0],
                   [0,0,0,0],
                   [1,1,1,0]]

adjacencyList = [["b","c","d"],["c"],[],["a","b","c"]]

def matrixEdges(adjacencyMatrix):
    
    numVertices = len(adjacencyMatrix)
    
    for i in range(numVertices):
        numEdges = len(adjacencyMatrix[i])
        
        for j in range(numEdges):
            
            if bool(adjacencyMatrix[i][j]):
                print(f"{chr(97+i)} -> {chr(97+j)}", end=" ")
           
        if adjacencyMatrix[i] == [0,0,0,0]:
            print(f"{chr(97+i)} has no edges")
        
        else:
            print()
    
    print()
        
        
def listEdges(adjacencyList):
    
    numVertices = len(adjacencyList)
    
    for i in range(numVertices):
        
        if len(adjacencyList[i]) == 0:
            print(f"{chr(97+i)} has no edges")

        else:
            for j in adjacencyList[i]:
                print(f"{chr(97+i)} -> {j}", end=" ") 
        
            print()

def main():
    matrixEdges(adjacencyMatrix)
    listEdges(adjacencyList)
    
main()