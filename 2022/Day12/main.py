import numpy as np
from rich import print as rprint

from aocd.models import Puzzle
from aocd.examples import Example

example = Puzzle(year=2022, day=12).examples[0]
puzzleA = Puzzle(year=2022, day=12).input_data


def getNeighbors(arr,coord):
    val = arr[coord[0],coord[1]]

    top = arr[coord[0]-1,coord[1]]
    bottom = arr[coord[0]+1,coord[1]]
    left = arr[coord[0],coord[1]-1]
    right = arr[coord[0],coord[1]+1]

    return (f"Val: {val}, Top: {top}, Bottom: {bottom}, left: {left}, right: {right}")

arr = np.arange(64).reshape(8,8)

ii = np.where(arr == 43)
coord = (ii[0][0],ii[1][0])
neighbors = getNeighbors(arr,coord)

rprint(neighbors)
