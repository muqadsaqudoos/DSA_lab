def solve_maze(maze):
     
    def is_valid(row, col):
        if (0<=row<len(maze)) and (0<=col<len(maze[0])) and maze[row][col] != "*":
           return True
        return False
        
    def is_finish(row,col):
        if maze[row][col] == "T":
            return True
        return False
      
    def explore(row,col,path):
        if is_finish(row,col):
           return True
        
        maze[row][col] = "Visited"
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for dr,dc in directions:
            if is_valid(row+dr,col+dc) and maze[row+dr][col+dc] != "Visited":
                path.append((row+dr,col+dc))
                if explore(row+dr,col+dc,path):
                    return True
                path.pop()
        return False
             
    row, col = None,None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "P":
                row, col = i,j
                break
    path = [(row,col)]
    if explore(row,col,path):
        return "solved",path
    else:
        return "unsolved",[]
        
def main():  
    maze = [
    [" ", "*", " ", "*", " ", " "],
    [" ", "*", " ", "*", " ", " "],
    ["P", " ", " ", " ", "*", " "],
    ["*", " ", "*", "*", "*", " "],
    [" ", " ", " ", " ", "*", "T"],
    ["*", " ", " ", " ", " ", " "]
    ]
    status, path = solve_maze(maze)
    print(status)
    if status == "solved":
        print("Path:", path)
    maze = [
    [" ", "*", " ", "*", " ", " "],
    [" ", "*", " ", "*", " ", " "],
    ["P", " ", " ", " ", "*", " "],
    ["*", " ", "*", "*", "*", " "],
    [" ", " ", " ", " ", "*", "T"],
    ["*", " ", " ", " ", " ", "*"]
    ]
    status, path = solve_maze(maze)
    print(status)
    if status == "solved":
        print("Path:", path)

main()
