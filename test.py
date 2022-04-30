
class test() :
    def __init__(self,texte) :
        self.texte = texte
        

    def bonjour(self) :
        return self.texte

text = test("bonjour")
print(text.bonjour())