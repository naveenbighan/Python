class person:
    
    
    def __init__(self,name,age):
        self.name = name
        self.age= age
    def __str__(self,name,age):
        self.name = name
        self.age= age
        return f"my name is {self.name} age is {self.age}"
    @staticmethod
    def hello():
        print("hello naven")
    
p1=person("naveen",25)

print("jasii",28)
p1.hello()




   

        
    