class test1:
    def __init__(self,value):
        self.value=value

    # @staticmethod
    def static_add_one(value):
        return value+1

    # @property
    def new_val(self):
        self.value=self.static_add_one(self.value)
        return self.value


a=test1(3)
print(a.new_val)



class test2:
    def __init__(self,value):
        self.value=value

    def static_add_one(self,value):
        return value+1

    @property
    def new_val(self):
        self.value=self.static_add_one(self.value)
        return self.value


b=test2(3)
print(b.new_val) ## >>> 4