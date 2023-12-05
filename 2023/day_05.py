from collections import defaultdict, deque
from typing import TYPE_CHECKING

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

class SeedData:    
    def __init__(self):
        self.seeds = []
        self.seedToSoil = []
        self.soilToFertilizer = []
        self.fertilizerToWater = []
        self.waterToLight = []
        self.lightToTemp = []
        self.tempToHumidity = []
        self.humidtityToLoc = []
        
    def helper(self, inp, l):
        ret = -1
        for d, s, r in l:
            if inp >= s and inp < s+r:
                ret = d + (inp-s)
        if ret == -1:
            ret = inp
        return ret
        
    def helper2(self, inp, l):
        ret = -1
        for d, s, r in l:
            if inp >= d and inp < d+r:
                ret = s + (inp-d)
        if ret == -1:
            ret = inp
        return ret
    
    def getSeedToSoil(self, seed):
        return self.helper(seed, self.seedToSoil)
        
    def getSoilFert(self, soil):
        return self.helper(soil, self.soilToFertilizer)
    
    def getFertToWater(self, fert):
        return self.helper(fert, self.fertilizerToWater)
        
    def getWaterToLight(self, water):
        return self.helper(water, self.waterToLight)
        
    def getLigthToTemp(self, light):
        return self.helper(light, self.lightToTemp)
        
    def getTempToHumi(self, temp):
        return self.helper(temp, self.tempToHumidity)
    
    def getHumiToLoc(self, humi):
        return self.helper(humi, self.humidtityToLoc)
        
    def getLoc(self, seed):
        return self.getHumiToLoc(self.getTempToHumi(self.getLigthToTemp(self.getWaterToLight(self.getFertToWater(self.getSoilFert(self.getSeedToSoil(seed)))))))
        
    def getLocToSeed(self, loc):
        return self.helper2(self.helper2(self.helper2(self.helper2(self.helper2(self.helper2(self.helper2(loc, self.humidtityToLoc), self.tempToHumidity), self.lightToTemp), self.waterToLight), self.fertilizerToWater), self.soilToFertilizer), self.seedToSoil)
    

raw = aoc_helper.fetch(5, 2023)


def parse_raw(raw: str):
    raw = raw.split("\n\n")
    seed_info = SeedData()
    for r in raw:
        if "seeds" in r:
            r = r.split(": ")[1]
            seed_info.seeds = list(map(int, r.split()))
        elif "seed-to-soil" in r:
            r = r.splitlines()[1:]
            for l in r:
                seed_info.seedToSoil.append(list(map(int, l.split())))
        elif "soil-to-fertilize" in r:
            r = r.splitlines()[1:]
            for l in r:
                seed_info.soilToFertilizer.append(list(map(int, l.split())))
        elif "fertilizer-to-water" in r:
            r = r.splitlines()[1:]
            for l in r:
                seed_info.fertilizerToWater.append(list(map(int, l.split())))
        elif "water-to-light" in r:
            r = r.splitlines()[1:]
            for l in r:
                seed_info.waterToLight.append(list(map(int, l.split())))
        elif "light-to-temperature" in r:
            r = r.splitlines()[1:]
            for l in r:
                seed_info.lightToTemp.append(list(map(int, l.split())))
        elif "temperature-to-humidity" in r:
            r = r.splitlines()[1:]
            for l in r:
                seed_info.tempToHumidity.append(list(map(int, l.split())))
        elif "humidity-to-location" in r:
            r = r.splitlines()[1:]
            for l in r:
                seed_info.humidtityToLoc.append(list(map(int, l.split())))
    return seed_info


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    min_loc = 1000000000000
    for s in data.seeds:
        loc = data.getLoc(s)
        if loc < min_loc:
            min_loc = loc
    return min_loc


aoc_helper.lazy_test(day=5, year=2023, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    min_loc = 1000000000000
    i = 0
    locs = []
    while i < len(data.humidtityToLoc):
        locs.append(data.humidtityToLoc[i][0]+data.humidtityToLoc[i][2])
        i +=1
    m = max(locs)
    i = 0
    while i<m:
        seed = data.getLocToSeed(i)
        j = 0
        found = False
        while j<len(data.seeds):
            if seed >= data.seeds[j] and seed < data.seeds[j]+data.seeds[j+1]:
                found = True
                break
            j += 2
        if found:
            break
        i += 100000
    for k in range(i-100000, i):
        seed = data.getLocToSeed(k)
        j = 0
        while j<len(data.seeds):
            if seed >= data.seeds[j] and seed < data.seeds[j]+data.seeds[j+1]:
                return k
            j += 2
        i += 1
    return 0


aoc_helper.lazy_test(day=5, year=2023, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=5, year=2023, solution=part_one, data=data)
aoc_helper.lazy_submit(day=5, year=2023, solution=part_two, data=data)
