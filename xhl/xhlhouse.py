from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create("47.100.46.95", 4783) 
entityId = mc.getPlayerEntityId("xhl") 
pos=mc.entity.getPos(entityId)

pos=mc.player.getTilePos()
print("player pos is",pos)


mc.setBlocks(pos.x,pos.y,pos.z,pos.x+10,pos.y+20,pos.z+30,3)
