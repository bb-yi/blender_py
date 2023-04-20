import bpy
import os
#r'D:\mmd_project\amoQ版MMD\wj\alembic_file.mtl'


file_path =r'D:\mmd_project\amoQ版MMD\wj\alembic_file.mtl'



materials = {}
with open(file_path, 'r') as f:
    current_material = None
    for line in f:
        if line.startswith("newmtl"):
            current_material = line.split()[1]
            materials[current_material] = {}
        elif line.startswith("map_Kd"):
            materials[current_material]["map_Kd"] = line.split()[1]

new_materials_dict = {}
for i, (key, value) in enumerate(materials.items()):
    new_key = f'xform_0_material_{i}'
    new_materials_dict[new_key] = value

materials = {k: v['map_Kd'] for k, v in new_materials_dict.items()}
# 输出新字典
#print(materials)
#print(new_materials_dict['xform_0_material_0']['map_Kd'])


for key, value in materials.items():
    obj = bpy.data.objects[key]

    mat = bpy.data.materials.new(name=value)
    
    # 设置该材质使用节点
    mat.use_nodes = True

    # 创建一个新的Image纹理节点
    tex = mat.node_tree.nodes.new('ShaderNodeTexImage')
    tex.location = (-300,300)

    new_name = value
    new_path = file_path.replace(file_path.split('\\')[-1], new_name)
    
    print(new_path)
    # 设置纹理图片路径
    tex.image = bpy.data.images.load(new_path)

    # 获取Diffuse BSDF节点
    bsdf = mat.node_tree.nodes.get('Principled BSDF')

    # 将Image纹理节点连接到Diffuse BSDF节点的Base Color输入
    mat.node_tree.links.new(tex.outputs['Color'], bsdf.inputs['Base Color'])
    mat.node_tree.links.new(tex.outputs['Alpha'], bsdf.inputs['Alpha'])

    #赋予材质
    obj.data.materials.append(mat)

'''
file_path = '/path/to/myfile.png'
new_name = 'newfile.png'

# 使用字符串的 replace 方法来替换文件名
new_path = file_path.replace(file_path.split('/')[-1], new_name)
print(new_path)
'''



'''
# 创建一个新的Image纹理节点
tex = mat.node_tree.nodes.new('ShaderNodeTexImage')

# 设置纹理图片路径
tex.image = bpy.data.images.load('path/to/texture/image.png')

# 获取Diffuse BSDF节点
bsdf = mat.node_tree.nodes.get('Principled BSDF')

# 将Image纹理节点连接到Diffuse BSDF节点的Base Color输入
mat.node_tree.links.new(tex.outputs['Color'], bsdf.inputs['Base Color'])

'''

'''
# 获取当前场景
scene = bpy.context.scene

# 新建一个材质
mat = bpy.data.materials.new(name="MyMaterial")

# 设置该材质使用节点
mat.use_nodes = True

# 获取该材质的节点树
tree = mat.node_tree

# 获取节点树中的节点
nodes = tree.nodes

# 新建一个漫反射节点
diffuse_node = nodes.new(type='ShaderNodeBsdfDiffuse')

# 新建一个输出节点
output_node = nodes.new(type='ShaderNodeOutputMaterial')

# 将漫反射节点连接到输出节点
links = tree.links
link = links.new(diffuse_node.outputs['BSDF'], output_node.inputs['Surface'])
'''


'''
# 获取场景中名称为 "Cube" 的物体
obj = bpy.data.objects["Cube"]

new_mat = bpy.data.materials.new(name="New Material")
if obj.data.materials:
    # 如果物体已经有材质，添加新材质到现有材质的末尾
    obj.data.materials[-1] = new_mat
else:
    # 如果物体没有材质，添加新材质到物体的材质列表中
    obj.data.materials.append(new_mat)
    '''