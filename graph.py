#adjacency matrix

def add_edge(mat,i,j):
    mat[i][j]=1
    mat[j][i]=1

def display_matrix(mat):
    for row in mat:
        print("".join(map(str,row)))
if __name__=="__main__":
    v=5
    mat=[[0]*(v+1) for _ in range(v+1)]
adj=[[] for _ in range(v)]
add_edge(mat,1,2)
add_edge(mat,1,3)
add_edge(mat,2,4)
add_edge(mat,3,4)
add_edge(mat,3,5)
add_edge(mat,4,5)
display_matrix(mat)

#adjacency lists


def add_edge(adj,i,j):
    adj[i].append(j)
    adj[j].append(i)

def display_adj_list(adj):
    for i in range(len(adj)):
        print(f"{i}:",end="")
        for j in adj[i]:
            print(j,end=" ")
        print()
v=4
adj=[[] for _ in range(v)]
add_edge(adj,0,1)
add_edge(adj,0,2)
add_edge(adj,1,2)
add_edge(adj,2,3)
display_adj_list(adj)
