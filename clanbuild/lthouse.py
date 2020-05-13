from mcpi.minecraft import Minecraft
import time

reader = csv.reader(open('house.csv'))
data=[]
for r in reader:
    data.append(r)
for name in data:
    if name[0] == 'clancenter':
        cx=int(name[1])
        cy=int(name[2])
        cz=int(name[3])
    elif name[0] == 'hjn':
        sx=int(name[1])
        sy=int(name[2])
        sz=int(name[3])

x=cx+sx
y=cy+sy
z=cz+sz

mc.setBlocks(x,y,z,x+7,y+7,z+5,57)
mc.setBlocks(x+1,y+1,z+1,x+6,y+6,z+4,0)