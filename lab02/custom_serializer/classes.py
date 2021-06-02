class simple:
    @classmethod
    def func(self,a,b):
        return a*b

class complex(simple):
    def __init__(self):
        pass
    
    @classmethod
    def method(self,a):
        return super().func(a, a + 5)


        
