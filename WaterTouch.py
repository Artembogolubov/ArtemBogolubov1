from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import mcpi.block as block
import keyboard

waterId = block.WATER_BLOCK.id
distance = 1

while True:
    if keyboard.is_pressed('w'):
        direction = mc.player.getDirection()
        pos = mc.player.getPos()
        x = round(pos.x + distance*direction.x)
        y = round(pos.y + distance*direction.y)
        z = round(pos.x + distance*direction.z)

        if mc.getBlock(x,y,z,) != 0:
            mc.setBlock(x, y, z, waterId)
