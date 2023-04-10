import bpy
import random

for i in range(10):
    # 随机选择立方体或球
    if random.random() < 0.5:
        bpy.ops.mesh.primitive_cube_add(location=(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)))
    else:
        bpy.ops.mesh.primitive_uv_sphere_add(location=(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5)))
    
    # 随机调整大小
    bpy.context.object.scale = (random.uniform(0.5, 2), random.uniform(0.5, 2), random.uniform(0.5, 2))
