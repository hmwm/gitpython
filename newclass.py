class CuteCat:
    def __init__(self, cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

    def cry(self):
        print("喵" * self.age)

    def think(self, ate_something):
        print(f"{self.name}在想{ate_something}..")


cat1 = CuteCat("daHua", 2, "black")
print(cat1.name, str(cat1.age), cat1.color)
cat1.cry()
cat1.think("今天吃啥？")

