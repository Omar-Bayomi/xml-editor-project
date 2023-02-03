import re


class TreeNode:
    def __init__(self):
        self.__Children = []
        self.__TagData = None
        self.__TagName = None
        self.__Depth = 0
        self.__Parent = None

    @property
    def Children(self):
        return self.__Children

    @Children.setter
    def Children(self, value):
        self.__Children.append(value)

    def getAllChildren(self):
        return self.__Children

    @property
    def TagData(self):
        return self.__TagData

    @TagData.setter
    def TagData(self, value):
        self.__TagData = value

    @property
    def TagName(self):
        return self.__TagName

    @TagName.setter
    def TagName(self, value):
        self.__TagName = value

    @property
    def Depth(self):
        return self.__Depth

    @Depth.setter
    def Depth(self, value):
        self.__Depth = value

    @property
    def Parent(self):
        return self.__Parent

    @Parent.setter
    def Parent(self, value):
        self.__Parent = value
"""
    "ParseXml function 
    Time complexity     = O(n)
    space complexity    = O(n) 
"""
    @staticmethod
    def ParseXml(FilePath):
        xmlstring = ""
        with open(FilePath, 'r') as f:
            xmlstring = f.read()
            xmlstring = re.sub('\s+', '', xmlstring)
        f.close()
        Root = TreeNode()

        TreeNode.ParseRecursiveXml(xmlstring, 0, Root, True)
        return Root.getAllChildren()[0]

    @staticmethod
    def ParseRecursiveXml(xmlstring, index, Node, flag=False):
        if (Node is None and flag is False) or index >= len(xmlstring):
            return
        char = ''
        while index < len(xmlstring):
            char = xmlstring[index]
            index += 1
            if index >= len(xmlstring):
                break

            # begining Tag
            if char == '<' and xmlstring[index] != '/':
                child = TreeNode()
                child.Depth = Node.Depth + 1
                child.Parent = Node
                Node.Children = child
                res = re.search("(<.[^(><.)]+>)", xmlstring[index - 1:])
                if xmlstring[index: index + res.end() - 2] == '/posts':
                    pass
                child.TagName = xmlstring[index: index + res.end() - 2]
                index += res.end() - 1
                if index > len(xmlstring):
                    break
                char = xmlstring[index]
                # Nested Nodes
                if char == '<':
                    TreeNode.ParseRecursiveXml(xmlstring, index, child)
                    return
                # has a Value
                # <id>1</id>
                else:
                    res = re.search("(<.[^(><.)]+>)", xmlstring[index:])
                    child.TagData = xmlstring[index: index + res.start()]
                    index += res.end()
                    TreeNode.ParseRecursiveXml(xmlstring, index, child.Parent)

                    return
            else:

                res = re.search("(<.[^(><.)]+>)", xmlstring[index - 2:])
                index += res.end() - 2
                TreeNode.ParseRecursiveXml(xmlstring, index, Node.Parent)
                return
