# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 12:34:32 2018

@author: DELL
"""

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return new_G

R = 'r'
G = 'g'
beliefs = [
        [R,G,G,G,R,R,R],
        [G,G,R,G,R,G,R],
        [G,R,G,G,G,G,R],
        [R,R,G,R,G,G,G],]

#for i, row in enumerate(beliefs):
#    print(i)
#    
#for i, row in enumerate(beliefs):
#    print(row)
# **/   
for i, row in enumerate(beliefs):
    for j, cell in enumerate(row):
      print(str(j) + ' ' + str(cell))

#m = 7
#for i in range(-8, 10 + 1):
#    print(str(i) + ' ' + str(i % 7))