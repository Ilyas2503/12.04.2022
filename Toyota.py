from factory import Factory
class Toyota(Factory):
    def wheels(self):
        return "Колёса готовы"
    def windows(self):
        return "Стекла готовы"

t = Toyota()
print (t.wheels())
print (t.windows())
a = []
a.append(t.wheels())
a.append(t.windows())
print (a)