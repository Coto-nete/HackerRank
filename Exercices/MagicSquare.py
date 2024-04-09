def main():
    magic(0)
    print(resp)
    

def magic(pos):
    if pos==9:
        check(grid)
        return
    for c in range(1,10):
        if ref[c]==-0:
            ref[c]=1
            grid[pos]=c
            magic(pos+1)
            ref[c]=0

def check(grid):
    for c in range(0,9,3):
        soma = grid[c]+grid[c+1]+grid[c+2]   #linha
        if soma !=15:
            return
    for c in range(3):
        soma = grid[c]+grid[c+3]+grid[c+6]   #coluna
        if soma !=15:
            return
    if grid[0]+grid[4]+grid[8]!=15: #diagonal
        return
    if grid[2]+grid[4]+grid[6]!=15: #diagonal
        return
    soma=0
    global resp
    global comprare
    for x, item in enumerate(grid):
        if item!=compare[x]:
            soma += abs(item-compare[x])
    if soma<=resp:
        resp = soma



resp = 999
inputformat = []
compare = []
for c in range(3):
    inputformat.append(list(map(int,input().rstrip().split())))
for c in range(3):
    for j in range(3):
        compare.append(inputformat[c][j])
grid = [0]*9
ref = [0]*10
main()