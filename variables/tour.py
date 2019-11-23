import time
from mcpi.minecraft import Minecraft


mc = Minecraft.create()

x = -11.1
y = 122.4
z = -13.6

mc.player.setPos(x, y, z)

time.sleep(1)

x = 0
y = 121
z = 0

mc.player.setTilePos(x, y, z)

time.sleep(1)

x = 10
y = 120
z = 10

mc.player.setTilePos(x, y, z)

time.sleep(1)


