class Ingredients():
    _name : ""
    _stock = 1
    
    def __init__(self, name, stock):
        self._name = name
        self._stock = stock
        
    @property
    def stock(self):
        return self._stock
    @property
    def name(self):
        return self._name

class Drinks() : 
    _name : ""
    _ingredients = [{"Quantity" : 0, "nameDrink" : ""}]
    
    _price = 1
    
    def __init__(self, name, ingredients, price):
        self._name = name
        self._ingredients = ingredients
        self._price = price
    
    @property
    def name(self):
        return self._name
        
    @property
    def ingredients(self):
        return self._ingredients
    
    @property
    def price(self):
        return self._price
        
class Barmaid() : 
    _ListDrinks = list()
    _Command = [{"nameDrink" : "", "size" : ""}]
    _listIngr = list()
    _finalPrice = 0
    _paid = False
    
    def __init__(self, ListDrinks, listIngr):
        self._ListDrinks = ListDrinks
        self._listIngr = listIngr
        
    def showPrice(self) : 
        total =0
        for i in self._Command :
            for j in self._ListDrinks:
                if i["nameDrink"] == j.name :
                    if i["size"] == "Large" :
                        total = total + 1
                    if i["size"] == "Medium" :
                        total = total + 0.5
                    total = total +j.price
        print("le total de votre commande s'élève à %s" %(total))
        return total
    
    def showMenu(self) :
        tab = []
        for i in self._ListDrinks : 
            tab.append(i.name)
        print(tab)
        return tab
        
    def showIngredients(self, nameDrink):
        tab = []
        for i in self._ListDrinks :
            if i.name == nameDrink:
                for j in i.ingredients : 
                    tab.append(j["nameIngr"])
        print(tab)
        return tab
        
    def selectDrink(self, nameDrink, size):
        print("vous venez de selectionner %s en taille %s" %(nameDrink, size))
        self._Command.append({"nameDrink" : nameDrink, "size" : size})
        self._finalPrice = barmaid.showPrice()
        return True
    
    def showCommand(self) :
        print(self._Command)
        return self._Command
    
    def validate(self) : 
        print("vous venez de valider votre commande dont le prix s'élève à %s" %(self._finalPrice))
    
    def pay(self) :
        print("vous venez de payer %s" %(self._finalPrice))
        self._paid = True
    
    def Print(self) : 
        if self._paid == True : 
            print("impression en cours")
        else :
            print("il faut payer !")
        
    
banana = Ingredients("banana", 18)
mango = Ingredients("mango", 20)
orange = Ingredients("orange", 14)
guajana = Ingredients("guajana", 5)
apple = Ingredients("apple", 14)
ginger = Ingredients("ginger", 23)
lemon = Ingredients("lemon", 14)
guava = Ingredients("guava", 17)
pineapple = Ingredients("pineapple", 18)
carrots = Ingredients("carrots", 30)
celery = Ingredients("celery", 25)
beetroot = Ingredients("beetroot", 41)
 
listIngr = [banana,mango, orange, guajana, apple, ginger, lemon, guava, pineapple, carrots, celery, beetroot]
 
TheBoost = Drinks("the_boost", [{"nameIngr" : "mango", "Quantity" : 0.5}, {"nameIngr" : "orange", "Quantity" : 2}, {"nameIngr" : "guajana", "Quantity" : 1}], 5)
TheFresh = Drinks("the_fresh", [{"nameIngr" : "apple", "Quantity" : 3},{"nameIngr" : "ginger", "Quantity" : 1}, {"nameIngr" : "lemon", "Quantity" : 1}], 4)
TheFusion = Drinks("the_fusion", [{"nameIngr" : "guava", "Quantity" : 1},{"nameIngr" : "pineapple", "Quantity" : 0.25}, {"nameIngr" : "banana", "Quantity" : 0.5}], 5)
TheDetox= Drinks("the_detox", [{"nameIngr" : "carrots", "Quantity" : 3},{"nameIngr" : "celery", "Quantity" : 1}, {"nameIngr" : "beetroot", "Quantity" : 1}], 3.5)

ListDrinks = [TheBoost, TheFresh, TheFusion, TheDetox]


CommandDone = [{"nameDrink":"the_detox", "size" : "Large"}]
barmaid = Barmaid(ListDrinks, listIngr)

barmaid.showMenu()
barmaid.showIngredients("the_detox")
barmaid.selectDrink("the_detox", "Large")
barmaid.selectDrink("the_detox", "Medium")
barmaid.selectDrink("the_fusion", "Small")
barmaid.showCommand()
barmaid.validate()
barmaid.showPrice()
barmaid.Print()
barmaid.pay()
barmaid.Print()

print(carrots.stock)





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    