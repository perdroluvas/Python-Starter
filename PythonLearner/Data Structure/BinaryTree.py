class BinaryTreeNode(object):
    def __init__(self):
        self.data = '#'
        self.leftChild = None
        self.rightChild = None

class BinaryTree(object):
    #def __init__(self):
     #   self.data = '#'
      #  self.leftChild = None
       # self.rightChild = None
    def createBinaryTree(self,Root):
        data = input('==>')
        if data == '#': #Não adiciona mais
            Root = None
        else:
            Root.data = data
            Root.leftChild = BinaryTreeNode()
            self.createBinaryTree(Root.leftChild)
            Root.rightChild = BinaryTreeNode()
            self.createBinaryTree(Root.rightChild)
    def preOrder(self, Root):
        if Root is not None:
            self.visitBinaryTreeNode(Root)
            self.preOrder(Root.leftChild)
            self.preOrder(Root.rightChild)
    def inOrder(self,Root):
        if Root is not None:
            self.inOrder(Root.leftChild)
            self.visitBinaryTreeNode(Root)
            self.inOrder(Root.rightChild)
    def postOrder(self,Root):
        if Root is not None:
            self.postOrder(Root.leftChild)
            self.postOrder(Root.rightChild)
            self.visitBinaryTreeNode(Root)
    def visitBinaryTreeNode(self,BinaryTreeNode):
        if BinaryTreeNode.data is not '#':
            print(BinaryTreeNode.data, end="->")
    

bTN = BinaryTreeNode()
bT = BinaryTree()
bT.createBinaryTree(bTN)
print('pre order: ')
bT.preOrder(bTN)
print('\nin order: ')
bT.inOrder(bTN)
print('\npost order: ')
bT.postOrder(bTN)
