import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time

for i in range(10):
    mc.postToChat ("Your name")
