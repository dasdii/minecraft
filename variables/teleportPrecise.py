from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x = -11.1
y = 122.4
z = -13.6

time.sleep(1)

mc.player.setPos(x, y, z)


