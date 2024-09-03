              #BACKTRACKING


#pbm1:N Queen pbm

def isSafe1(self,row,col,board,n):
        duprow=row
        dupcol=col

        while row>=0 and col>=0:
            if board[row][col]=='Q':
                return False
            row-=1
            col-=1
        col=dupcol
        row=duprow
        while col>=0:
            if board[row][col]=='Q':
                return False
            col-=1
        row=duprow
        col=dupcol
        while row<n and col>=0:
            if board[row][col]=='Q':
                return False
            row+=1
            col-=1
        return True
    def solve(self,col,board,ans,n):
        if col ==n:
            ans.append(list(board))
            return
        for row in range(n):
            if self.isSafe1(row,col,board,n):
                board[row]=board[row][:col]+'Q'+board[row][col+1:]
                self.solve(col+1,board,ans,n)
                board[row]=board[row][:col]+'.'+board[row][col+1:]#backtracking

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=['.'*n for _ in range(n)]
        self.solve(0,board,ans,n)
        return ans


#pbm2:Solve Sudoku

class Solution:
    def isValid(self,board:List[List[str]],row:int,col:int,c:str):
        for i in range(9):
            if board[i][col]==c:
                return False
            if board[row][i]==c:
                return False
            #checking subgrid each subgrid also contains unique elmnts
            if board[3*(row//3)+i//3][3*(col//3)+i%3]==c: 
                return False
        return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    for c in "123456789":
                        if self.isValid(board,i,j,c):
                            board[i][j]=c
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j]="."
                    return False
        return True
        self.solveSudoku(board)

#pbm3:Rat in a maze pbm
        
#movmnt will bw in lexicographical order
from typing import List

class Solution:
    def findpathHelper(self,i:int,j:int,a:List[List[int]],n:int,ans:List[str],move:str,vis:List[List[int]]):
        if i==n-1 and j==n-1:
            ans.append(move)
            return
        
        #downward
        if i+1<n and not vis[i+1][j] and a[i+1][j]==1:
            vis[i][j]=1
            self.findpathHelper(i+1,j,a,n,ans,move+'D',vis)
            vis[i][j]=0
        #left
        if j-1>=0 and not vis[i][j-1] and a[i][j-1]==1:
            vis[i][j]=1
            self.findpathHelper(i,j-1,a,n,ans,move+'L',vis)
            vis[i][j]=0
        #right
        if j+1<n and not vis[i][j+1] and a[i][j+1]==1:
            vis[i][j]=1
            self.findpathHelper(i,j+1,a,n,ans,move+'R',vis)
            vis[i][j]=0
        #upward
        if i-1>=0 and not vis[i-1][j] and a[i-1][j]==1:
            vis[i][j]=1
            self.findpathHelper(i-1,j,a,n,ans,move+'U',vis)
            vis[i][j]=0
        
    
    def findPath(self, m, n):
        ans=[]
        if not m or not m[0] or m[0][0]!=1:
            return ans
        vis=[[0 for _ in range(n)] for _ in range(n)]
        if m[0][0]==1:
            self.findpathHelper(0,0,m,n,ans,'',vis)
        return ans

#binary representation upto N digits with no consecutive ones


from typing import List
def generateString(N: int) -> List[str]:
    def backtrack(current_str):
        if len(current_str)==N:
            result.append(current_str)
            return
        
        backtrack(current_str+'0')
        if not current_str or current_str[-1]!='1':
            backtrack(current_str+'1')
    result=[]
    backtrack('')
    return result

        
