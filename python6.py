"""
#
# Functions
#
"""
def myFullName(firstName = "Unknown", lastName= "Forger"):
    return firstName + " " + lastName

print(myFullName("dog","cat"))
print(myFullName(firstName="lion"))
print(myFullName())
print(myFullName(lastName="wolf"))
print(myFullName("fox","bear"))
print(myFullName("eagle","hawk"))
print(myFullName("shark","whale"))

def redPotion (hp):
    return hp + 50
def bluePotin (mp):
    return mp + 30
    
current_hp = 70
print("Current Hp: " , current_hp)
current_hp = redPotion(current_hp)
print("After using Red Potion , Hp : ", current_hp)