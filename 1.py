from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import mcpi.block as block

import keyboard
import time

x = 128
y = 65
z = 193
size = 20

mainBlock = block.OBSIDIAN.id
entranceBlock = block.SANDSTONE.id
exitBlock = block.LAPIS_LAZULI_BLOCK.id
pointerBlock = block.GLOWSTONE_BLOCK.id

mc.setBlocks(x,y,z,x+size,y,z+size, mainBlock)
mc.setBlocks(x+1,y,z+1,x+size-1,y,z+size-1, 0)
mc.setBlocks(x,y-1,z,x+size,y-1,z+size, 1)
mc.setBlock(x+1,y-1,z+1, block.SANDSTONE.id)
mc.setBlock(x+size-1,y-1,z+size-1,block.LAPIS_LAZULI_BLOCK.id)

x += 2
z += 1
mc.setBlock(x,y,z,pointerBlock)

while True:
    if keyboard.is_pressed('up'):
        mc.setBlock(x,y,z,mainBlock)
        x +=1
        mc.setBlock(x,y,z,pointerBlock)
        time.sleep(0.5)
    elif keyboard.is_pressed('down'):
        mc.setBlock(x,y,z,mainBlock)
        x -= 1
        mc.setBlock(x,y,z,pointerBlock)
        time.sleep(0.5)
    elif keyboard.is_pressed('left'):
        mc.setBlock(x,y,z,mainBlock)
        z -= 1
        mc.setBlock(x,y,z,pointerBlock)
        time.sleep(0.5)
    elif keyboard.is_pressed('right'):
        mc.setBlock(x,y,z,mainBlock)
        z += 1
        mc.setBlock(x,y,z,pointerBlock)
        time.sleep(0.5)
