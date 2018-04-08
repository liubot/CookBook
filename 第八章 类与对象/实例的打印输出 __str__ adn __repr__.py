class Pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair repr ( {0.x} {0.y})'.format(self)
    def __str__(self):
        return 'Pair str ({0.x} {0.y})'.format(self)


p=Pair(1,2)
print (p)

