import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
from mcpi.minecraft import Minecraft
mc = minecraft.Minecraft.create("47.100.46.95",4783)
entityId= mc.getPlayerEntityId("cjy")
#pos=mc.entity.getPos(entityId)

def house(pos.x,pos.y,pos.z):
   
mc. setBlocks (pos.x, pos.y-155, pos.z,pos.x+8, pos.y+4, pos.z+8,5)



mc. setBlocks (pos.x+1, pos.y+1, pos.z+1,pos.x+7, pos.y+4, pos.z+7,0)


for i in range(6):
    mc.setBlocks(pos.x-1+i, pos.y+5+i, pos.z-1+i,pos.x+9-i, pos.y+5+i, pos.z+9-i,5)

for ii in range(18):
    mc. setBlocks (pos.x+1, pos.y-5-6*ii, pos.z+1,pos.x+7, pos.y-1-6*ii, pos.z+7,0)
    mc. setBlock(pos.x+7, pos.y-1-6*ii, pos.z,50)
    mc. setBlock(pos.x, pos.y-1-6*ii, pos.z+7,50)
    mc. setBlock(pos.x+1, pos.y-1-6*ii, pos.z,50)    
    for i in range(6):
        mc. setBlock(pos.x+7-i, pos.y-i-6*ii, pos.z+7,53,0)
    mc. setBlock(pos.x+6, pos.y-6*ii, pos.z+7,0)
    mc. setBlock(pos.x+5, pos.y-6*ii, pos.z+7,0)
    mc. setBlock(pos.x+4, pos.y-6*ii, pos.z+7,0)

mc. setBlock(pos.x, pos.y+1, pos.z+4, 194, 4)
mc. setBlock(pos.x, pos.y+2, pos.z+4, 194, 8)
mc. setBlock(pos.x, pos.y+19, pos.z+6, 26)
#mc. setBlock(pos.x, pos.y+19, pos.z+7, 26,4)
#台阶

mc. setBlock(pos.x-1, pos.y, pos.z+3, 53, 2)
mc. setBlock(pos.x-1, pos.y, pos.z+4, 53, 0)
mc. setBlock(pos.x-1, pos.y, pos.z+5, 53, 3)
mc. setBlocks (pos.x+8, pos.y+2, pos.z+2,pos.x+8, pos.y+3, pos.z+6,160, 3)

mc. setBlocks (pos.x+3, pos.y+2, pos.z,pos.x+5,pos.y+3,pos.z,160, 3)
mc. setBlocks (pos.x+3, pos.y+2,pos. z+8,pos.x+5, pos.y+3,pos. z+8,160, 3)
mc. setBlocks (pos.x, pos.y+2,pos. z+1,pos.x, pos.y+3,pos. z+2,160, 3)
mc. setBlocks(pos.x, pos.y+2, pos. z+6,pos.x, pos.y+3, pos. z+7,160, 3)

mc. setBlocks (pos.x+3, pos.y+5,pos.z+3,pos.x+5, pos.y+5,pos.z+5,169)
#mc. setBlocks (pos.x+3, pos.y-1,pos.z+3,pos.x+5, pos.y-1,pos.z+5,169)
mc. setBlock(pos.x-15, pos.y, pos.z+3, 355)
    
reader = csv.reader(open('1.csv'))
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

house(cx+sx,cy+sy,cz+sz)
