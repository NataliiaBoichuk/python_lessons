class Female_Grandparent:
    def __init__(self):
        self.grandma_name = 'Grandma'


class Male_Grandparent:
    def __init__(self):
        self.grandpa_name = 'Grandpa'


class Parent(Female_Grandparent, Male_Grandparent):
    def __init__(self):
        Female_Grandparent.__init__(self)
        Male_Grandparent.__init__(self)
        self.parent_name = 'Parent Class'


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)


# for cls in Parent.__bases__:
# This block grabs the classes of the child cls.__init__(self)
# class (which is named 'Parent' in this case),
# and iterates through them, initiating each one.
# The result is that each parent, of each child,
# is automatically handled upon initiation of the
# dependent class. WOOT WOOT! :D

g = Female_Grandparent()
print(g.grandma_name)
p = Parent()
print(p.grandma_name)
child = Child()
print(child.grandma_name)
