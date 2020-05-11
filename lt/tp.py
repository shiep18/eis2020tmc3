from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create("47.100.46.95",4783)
entityId= mc.getPlayerEntityId("LT")
pos=mc.entity.getTilePos(entityId)
print("player pos is",pos)

def tp(x,y,z):                              #传送
    mc.entity.setTilePos(entityId,x,y,z)