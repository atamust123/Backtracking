import sys


def start(maze_input_file, current_health):
    # if health input is not given make operations according to that
    maze = []
    for i in maze_input_file:
        maze.append(list(i.split()[0]))  # maze
    sol = [[0 for j in range(len(maze[i]))] for i in range(len(maze))]  # output file
    x, y = 0, 0
    for i in maze:
        if "S" in i:
            x, y = (maze.index(i), i.index("S"))  # start x,y coordinates
            break
    sol[x][y] = "S"
    recursion(maze, sol, x, y, current_health)
    return


def recursion(maze, sol, x, y, current_health):
    if 0 <= x < len(maze) and 0 <= y < len(maze[x]) and maze[x][y] != "W" and sol[x][y] != 1:
        if type(current_health) == int:  # if health input is given decrease
            if current_health >= 0:
                current_health -= 1
            else:
                if sol[x][y] != "S":
                    sol[x][y] = 0
                    return False
        if sol[x][y] != "S":
            sol[x][y] = 1
        if maze[x][y] == "H" and current_health != "Without Health":  # take health
            current_health = health
        if maze[x][y] == "F":  # we are out of maze so print
            sol[x][y] = "F"
            for i in range(len(sol)):
                for j in range(len(sol[i]) - 1):
                    output.write(str(sol[i][j]) + ", ")
                output.write(str(sol[i][-1]) + "\n")
            return True
        elif recursion(maze, sol, x, y - 1, current_health):  # go left
            return True
        elif recursion(maze, sol, x - 1, y, current_health):  # go up
            return True
        elif recursion(maze, sol, x, y + 1, current_health):  # go right
            return True
        elif recursion(maze, sol, x + 1, y, current_health):  # go go down
            return True
        else:
            if type(current_health) == int:
                current_health += 1
            if sol[x][y] != "S":
                sol[x][y] = 0  # unsigned coordinates by the rule of backtracking
            return False
    else:
        return False


try:
    maze_input = open(sys.argv[1], "r")  # first argument without health
    maze__health_input = open(sys.argv[2], "r")  # second argument with healt
    health = int(sys.argv[3])  #
    output = open(sys.argv[4], "w")
    start(maze_input, "Without Health")  # start for maze without health command
    output.write("\n")
    start(maze__health_input, health)  # start for maze with health
    output.close()
    maze__health_input.close()  # close files.
    maze_input.close()
except:
    print("An error occurred")
    exit(-1)
