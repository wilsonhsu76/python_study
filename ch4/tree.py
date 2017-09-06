class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    def __str__(self, level=0):
        ret = ''
        if self.left:
            ret += self.left.__str__(level+1)
        ret += "\t"*level+repr(self.data)+"\n"
        if self.right:
            ret += self.right.__str__(level+1)
        return ret
