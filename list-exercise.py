avengers=["Iron Man","Captain America","Black Widow","Hulk","Thor","Hawkeye"]
print(len(avengers))
avengers.append("Spider Man")
print(avengers)
avengers.remove("Captain America")
avengers.insert(0,"Captain America")
print(avengers)
avengers.remove("Hawkeye")
avengers.insert(4,"Hawkeye")
print(avengers)
avengers.pop(0)
avengers.pop(0)
avengers.pop(0)
avengers.pop(0)
avengers.pop(0)
avengers.pop(0)
print(avengers)
new_superheroes=["Doctor Strange","Vision","Wanda","Kate Bishop","Ant-Man"]
print(new_superheroes)
avengers.extend(new_superheroes)
# new_superheroes.sort()
# print(new_superheroes)
print(avengers)
avengers.sort()
print(avengers)



