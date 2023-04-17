# DESCRIPTION:

# Introduction
# Welcome Adventurer. Your aim is to navigate the maze and reach the finish point without touching any walls.
# Doing so will kill you instantly!

# Task
# You will be given a 2D array of the maze and an array of directions. Your task is to follow the directions given.
# If you reach the end point before all your moves have gone, you should return Finish.
# If you hit any walls or go outside the maze border, you should return Dead.
# If you find yourself still in the maze after using all the moves, you should return Lost.

def maze_runner(maze, directions):
    row, col = 0, 0
    for row in maze:
        if 2 in row:
            row, col = maze.index(row), row.index(2)
            break
    for direction in directions:
        if direction == 'N':
            row -= 1
        if direction == 'E':
            col += 1
        if direction == 'W':
            col -= 1
        if direction == 'S':
            row += 1
        if row < 0 or col < 0 or col >= len(maze) or row >= len(maze):
            return 'Dead'
        if maze[row][col] == 0:
            continue
        if maze[row][col] == 1:
            return 'Dead'
        if maze[row][col] == 3:
            return 'Finish'
    return 'Lost'
