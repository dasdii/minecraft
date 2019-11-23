from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 11
y = 122
z = 13

mc.player.setTilePos(x, y, z)
