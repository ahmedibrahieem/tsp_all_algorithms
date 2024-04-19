import random
import numpy as np


class NodeGenerator:
    def __init__(self, width, height, nodesNumber):
        self.width = width
        self.height = height
        self.nodesNumber = nodesNumber

    def generate(self):
        #xs = np.random.randint(self.width, size=self.nodesNumber)
        #ys = np.random.randint(self.height, size=self.nodesNumber)
        filename = ('x.txt')
        xs=[]
        file = open('x.txt', 'r')
        read = file.readline()
        for line in file:
            xs.append(int(line.strip()))
        file.close()
        
        filename = ('y.txt')
        ys=[]
        file = open('y.txt', 'r')
        read = file.readline()
        for line in file:
            ys.append(int(line.strip()))
        file.close()
        np.array(xs)
        np.array(ys)
        #return np.column_stack((xs, ys))

        return np.column_stack((xs, ys))
