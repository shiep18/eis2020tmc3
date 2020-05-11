import binvox_rw
import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
mc = minecraft.Minecraft.create("47.100.46.95",4783)
reader = csv.reader(open('logo.csv'))
data=[]
for r in reader:
    data.append(r)
for name in data:
    if name[0] == 'clancenter':
        tx=int(name[1])
        ty=int(name[2])
        tz=int(name[3])
    elif name[0] == 'clanlogo':
        gx=int(name[1])
        gy=int(name[2])
        gz=int(name[3])
a=tx+gx
b=ty+gy
c=tz+gz
with open('aifeier.binvox', 'rb') as f:
    model = binvox_rw.read_as_3d_array(f)
print(model.dims)
print(model.scale)
print(model.translate)
#print(model.data)

for y in range(model.dims[1]):
    print("layer y=",y)
    layer_data=model.data[y]
    stringlayer=""
    for x in range(model.dims[0]):
        stringlayer=stringlayer+"\n"
        for z in range(model.dims[2]):
            if model.data[x][y][z] == True:
                stringlayer=stringlayer+'1'
                mc.setBlock(a+y,b+z,c+x,block.DIAMOND_BLOCK.id)
            else:
                stringlayer=stringlayer+'0'
                mc.setBlock(a+y,b+z,c+x,block.AIR.id)
    print(stringlayer)

