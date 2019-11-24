from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
mc.postToChat("Prosto Hello")
time.sleep(5)
pos = mc.player.getTilePos()
mc.postToChat(pos.x)
time.sleep(5)
mc.postToChat(pos.y)
time.sleep(5)
mc.postToChat(pos.z)
time.sleep(5)
