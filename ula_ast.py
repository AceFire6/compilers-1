
class UlaAst(object):
    def __init__(self):
        self.root = Node('Program', 1)

    def get_tree_str(self):
        return ''


class Node(object):
    def __init__(self, tag, depth, parent=None, children=list()):
        self.tag = tag
        self.depth = depth
        self.children = []
        self.parent = parent
        for child in children:
            self.children.append(Node(child, depth+1))

    def get_str(self, depth):
        return ('\t' * depth) + self.tag

    def add_child(self, child, grandchildren=None):
        child_node = Node(child, self.depth+1, self)
        self.children.append(child_node)
        for grandchild in grandchildren:
            child_node.add_child(Node(grandchild, self.depth+2, child_node))
        return child_node

