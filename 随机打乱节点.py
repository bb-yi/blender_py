import bpy
import random

# 获取名为 "MyMaterial" 的材质
mat = bpy.data.materials["MyMaterial"]

# 获取节点树和所有节点
nodes = mat.node_tree.nodes
node_list = list(nodes)

a = 2000

# 将所有节点的位置随机化
for node in node_list:
    x = random.uniform(-a, a)
    y = random.uniform(-a, a)
    node.location = (x, y)

# 对每个节点，微调它的位置
for i, node1 in enumerate(node_list):
    for node2 in node_list[i+1:]:
        while (node1.location - node2.location).length < 200:
            dx, dy = random.uniform(-50, 50), random.uniform(-50, 50)
            node1.location = (node1.location[0] + dx, node1.location[1] + dy)

# 更新节点树
mat.node_tree.nodes.update()
