import queue
import numpy as np
from rich import print as rprint
from typing import TypeAlias, Optional
import numpy as np
from rich import print as rprint

from aocd.models import Puzzle
from aocd.examples import Example

example = Puzzle(year=2022, day=12).examples[0]
exampleData= Example(example).input_data[0]
puzzleA = Puzzle(year=2022, day=12).input_data

data = [[l for l in line] for line in exampleData.splitlines()]

def get_height(r, c):
    s = data[r][c]
    if s == "S":
        return 0
    if s == "E":
        return 25
    return ord(s) - 97

def get_neightbors(r, c):
    h = get_height(r, c)
    neighbors = []
    for dis_r, dis_c in ([-1, 0], [1, 0], [0, -1], [0, 1]):
        r1, c1 = r + dis_r, c + dis_c
        if r1 >= 0 and r1 < len(data) and c1 >= 0 and c1 < len(data[0]):
            if get_height(r1, c1) <= h + 1:
                neighbors.append((r1, c1))
    return neighbors

rprint(data)

def findSandE(grid):
    y = 0
    SCoord = ()
    ECoord = ()
    for a in grid:
        if 'S' in a:
            SCoord = (y,a.index('S'))
        if 'E' in a:
            ECoord = (y,a.index('E'))
        y += 1
    return [SCoord,ECoord]

def runpath(data,S,E):
    visited = []
    paths = []
    q = []
    visited.append(S)
    
    while True:
        for n in get_neightbors(S[0],S[1]):
            if data[n[0]][n[1]] == 'E':
                visited.append((n[0],n[1]))
                break
            else:
                visited.append((n[0],n[1]))
                

rprint(get_neightbors(0,0))
rprint(findSandE(data))
