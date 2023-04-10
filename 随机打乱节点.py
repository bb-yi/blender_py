import bpy
import random

# 获取名为 "MyMaterial" 的材质
mat = bpy.data.materials["MyMaterial"]

# 获取节点树和所有节点
nodes = mat.node_tree.nodes
node_list = list(nodes)

# 获取选中的节点
selected_nodes = [node for node in node_list if node.select]

a = 2000

# 将所有节点的位置随机化
for node in selected_nodes:
    x = random.uniform(-a, a)
    y = random.uniform(-a, a)
    node.location = (x, y)

# 对每个节点，微调它的位置
for i, node1 in enumerate(selected_nodes):
    for node2 in selected_nodes[i+1:]:
        while (node1.location - node2.location).length < 200:
            dx, dy = random.uniform(-50, 50), random.uniform(-50, 50)
            node1.location = (node1.location[0] + dx, node1.location[1] + dy)

# 更新节点树
mat.node_tree.nodes.update()

#测试1