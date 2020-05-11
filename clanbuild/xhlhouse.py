from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create("47.100.46.95", 4783) 
entityId = mc.getPlayerEntityId("xhl") 
pos=mc.entity.getPos(entityId)

pos=mc.player.getTilePos()
print("player pos is",pos)

reader = csv.reader(open('house.csv'))
data=[]
for r in reader:
    data.append(r)
for name in data:
    if name[0] == 'clancenter':
        cx=int(name[1])
        cy=int(name[2])
        cz=int(name[3])
    elif name[0] == 'xhl':
        sx=int(name[1])
        sy=int(name[2])
        sz=int(name[3])
x=cx+sx
y=cy+sy
z=cz+sz

mc.setBlocks(x,y,z,x+10,y+20,z+30,3)
