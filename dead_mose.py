# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:25:47 2018

@author: Tarena
"""

import random

poison_bottle = random.randint(1,1001)

find_bottle = 0
dead_mouse = []

p_b = poison_bottle

for i in range(1,11):
    dp = p_b %2
    if dp == 1:
        dead_mouse.insert(0,i)
    p_b -=dp
    p_b /= 2
for n in dead_mouse:
    find_bottle += 2 **(n-1)
    
    
print(dead_mouse)
print(find_bottle)
print(poison_bottle)