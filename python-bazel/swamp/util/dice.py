import random
import simplemath

def roll(rolls = 1, size = 6):
    return [random.randint(1, size) for i in range(rolls)]

def roll2d6():
    return simplemath.add(roll()[0], roll()[0])
