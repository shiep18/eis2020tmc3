import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
import numpy as np
import time
from mcpi.minecraft import Minecraft

mc=Minecraft.create('47.100.46.95',4783)
SIZE=10
reader = csv.reader(open('house.csv'))
data=[]
for r in reader:
    data.append(r)
for name in data:
    if name[0] == 'clancenter':
        cx=int(name[1])
        cy=int(name[2])
        cz=int(name[3])
    elif name[0] == 'cjy':
        sx=int(name[1])
        sy=int(name[2])
        sz=int(name[3])
x=cx+sx
y=cy+sy
z=cz+sz
midx = x+SIZE/2
midy = y+SIZE/2
mc.setBlocks(x,y,z,x+SIZE,y+SIZE,z+SIZE,block.COBBLESTONE.id)
mc.setBlocks(x+1,y,z+1,x+SIZE-2,y+SIZE-1,z+SIZE-2,block.AIR.id)
mc.setBlocks(midx-1,y,z,midx+1,y+3,z,block.AIR.id)
mc.setBlocks(x+3,y+SIZE-3,z,midx-3,midy+3,z,block.GLASS.id)
mc.setBlocks(midx+3,y+SIZE-3,z,x+SIZE-3,midy+3,z,block.GLASS.id)
mc.setBlocks(x,y+SIZE-1,z,x+SIZE,y+SIZE-1,z+SIZE,block.WOOD.id)
mc.setBlocks(x+1,y-1,z+1,x+SIZE-2,y-1,z+SIZE-2,block.WOOL.id,14)
#on
