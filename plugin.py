
#python imports
import bpy
from random import randint

#start of for loop with x times of loop
for i in range(100):
    #size of the particles between x and y
    randomScale = randint(0,3)
    #range of coordinates for variable x, y and z
    x = randint(-40, 40)
    y = randint(-40, 40)
    z = randint(-40, 40)
    #"Blender" code for a smooth sphere
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(x, y, z), scale=(1, 1, 1))
    bpy.ops.object.shade_smooth()
