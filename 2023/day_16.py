from collections import defaultdict, deque
from typing import TYPE_CHECKING
import copy

import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
    decode_text,
    extract_ints,
    extract_iranges,
    extract_ranges,
    extract_uints,
    frange,
    irange,
    iter,
    list,
    map,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(16, 2023)


def parse_raw(raw: str):
    data = [list(r) for r in raw.splitlines()]
    return data


data = parse_raw(raw)

def count(table):
    return sum(t.count("#") for t in table)

# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    start_pos = ((0, 0), ">")
    scotty = [['.' for j in range(len(data[i]))] for i in range(len(data))]
    splitted = []
    through = []
    queue = [start_pos]
    changed = 0
    valami = []
    while queue:
        current, curr_dir = queue.pop(0)
        if (current, curr_dir) in valami:
            continue
        valami.append((current, curr_dir))
        if current[0] < 0 or current[0] >= len(data) or current[1] < 0 or current[1] >= len(data[0]):
            continue
        current_val = data[current[0]][current[1]]
        scotty[current[0]][current[1]] = '#'
        new_pos = (0, 0)
        if curr_dir == ">":
            new_pos = (current[0], current[1]+1)
        elif curr_dir == "<":
            new_pos = (current[0], current[1]-1)
        elif curr_dir == "^":
            new_pos = (current[0]-1, current[1])
        elif curr_dir == "v":
            new_pos = (current[0]+1, current[1])
        if current_val =='.':
            queue.append((new_pos, curr_dir))
        elif current_val =='|':
            if curr_dir == ">" or curr_dir == "<" and current not in splitted:
                splitted.append(current)
                queue.append(((current[0]+1, current[1]), "v"))
                queue.append(((current[0]-1, current[1]), "^"))
            elif curr_dir == "^" or curr_dir == "v" and current not in through:
                through.append(current)
                queue.append((new_pos, curr_dir))
        elif current_val =='-':
            if curr_dir == "^" or curr_dir == "v" and current not in splitted:
                splitted.append(current)
                queue.append(((current[0], current[1]-1), "<"))
                queue.append(((current[0], current[1]+1), ">"))
            elif curr_dir == ">" or curr_dir == "<" and current not in through:
                through.append(current)
                queue.append((new_pos, curr_dir))
        elif current_val =='\\':
            if curr_dir == ">":
                queue.append(((current[0]+1, current[1]), "v"))
            elif curr_dir == "<":
                queue.append(((current[0]-1, current[1]), "^"))
            elif curr_dir == "^":
                queue.append(((current[0], current[1]-1), "<"))
            elif curr_dir == "v":
                queue.append(((current[0], current[1]+1), ">"))
        elif current_val =='/':
            if curr_dir == ">":
                queue.append(((current[0]-1, current[1]), "^")) 
            elif curr_dir == "<":
                queue.append(((current[0]+1, current[1]), "v"))
            elif curr_dir == "^":
                queue.append(((current[0], current[1]+1), ">"))
            elif curr_dir == "v":
                queue.append(((current[0], current[1]-1), "<"))
    return count(scotty)


aoc_helper.lazy_test(day=16, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    max_eng = 0
    start_pos = []
    for i in range(len(data)):
        start_pos.append(((i, 0), ">"))
        start_pos.append(((i, len(data[i])-1), "<"))
    for i in range(len(data[i])):
        start_pos.append(((0, i), "v"))
        start_pos.append(((i, len(data)-1), "^"))
    for s in start_pos:
        scotty = [['.' for j in range(len(data[i]))] for i in range(len(data))]
        splitted = []
        through = []
        queue = [s]
        changed = 0
        valami = []
        while queue:
            current, curr_dir = queue.pop(0)
            if (current, curr_dir) in valami:
                continue
            valami.append((current, curr_dir))
            if current[0] < 0 or current[0] >= len(data) or current[1] < 0 or current[1] >= len(data[0]):
                continue
            current_val = data[current[0]][current[1]]
            scotty[current[0]][current[1]] = '#'
            new_pos = (0, 0)
            if curr_dir == ">":
                new_pos = (current[0], current[1]+1)
            elif curr_dir == "<":
                new_pos = (current[0], current[1]-1)
            elif curr_dir == "^":
                new_pos = (current[0]-1, current[1])
            elif curr_dir == "v":
                new_pos = (current[0]+1, current[1])
            if current_val =='.':
                queue.append((new_pos, curr_dir))
            elif current_val =='|':
                if curr_dir == ">" or curr_dir == "<" and current not in splitted:
                    splitted.append(current)
                    queue.append(((current[0]+1, current[1]), "v"))
                    queue.append(((current[0]-1, current[1]), "^"))
                elif curr_dir == "^" or curr_dir == "v" and current not in through:
                    through.append(current)
                    queue.append((new_pos, curr_dir))
            elif current_val =='-':
                if curr_dir == "^" or curr_dir == "v" and current not in splitted:
                    splitted.append(current)
                    queue.append(((current[0], current[1]-1), "<"))
                    queue.append(((current[0], current[1]+1), ">"))
                elif curr_dir == ">" or curr_dir == "<" and current not in through:
                    through.append(current)
                    queue.append((new_pos, curr_dir))
            elif current_val =='\\':
                if curr_dir == ">":
                    queue.append(((current[0]+1, current[1]), "v"))
                elif curr_dir == "<":
                    queue.append(((current[0]-1, current[1]), "^"))
                elif curr_dir == "^":
                    queue.append(((current[0], current[1]-1), "<"))
                elif curr_dir == "v":
                    queue.append(((current[0], current[1]+1), ">"))
            elif current_val =='/':
                if curr_dir == ">":
                    queue.append(((current[0]-1, current[1]), "^")) 
                elif curr_dir == "<":
                    queue.append(((current[0]+1, current[1]), "v"))
                elif curr_dir == "^":
                    queue.append(((current[0], current[1]+1), ">"))
                elif curr_dir == "v":
                    queue.append(((current[0], current[1]-1), "<"))
        max_eng = max(max_eng, count(scotty))
    return max_eng


aoc_helper.lazy_test(day=16, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=16, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=16, year=2023, solution=part_two, data=data)