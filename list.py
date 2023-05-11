items=['Butter','Pasta','Fruits','Veggis']
items2=['Sugar','Pizza']
print(items)
#index
p=items[3] #positiveindexing 0,1,2,3,4,5.... from left to right
n=items[-3] #negetiveindexing -1,-2,-3,-4.....from right to left
print(p)
print(n)
#slicing
s=items[1:3]
print(s)
ni=items[-3:]
print(ni)
print(items[1::2])
print(items[-1::-1])
#append/add
items.append('Maggi')
print(items)
#extend
items.extend(items2)
print(items)
#insert
items.insert(2,'Butter')
print(items)
#remove
items.remove('Butter')
print(items)
#inoporators
ch="rice" not in items
print(ch)
hc="rice" in items
print(hc)
#num
expenses=[4536,10,20,20000,400]
print(expenses)
    #soring
expenses.sort()
print(expenses)

print("")

items.sort()
print(items)

print("")

items.sort(reverse=True)
print(items)

print("")
#listconcatinate
food_items=['Biscuit','sugar','pasta']
makup_items=['lipstick','eyeliner','powder']
new_item=food_items + makup_items
print(new_item)
#length
l=len(new_item)
print(l)
# d=dir(new_item)
# print(d)
#listcount
x=new_item.count("powder")
print(x)
#listpop
p=new_item.pop(0)
print(p)
print(type(items))
newl=[2,3,'Hello',[5,6,7]]
print(newl[3][0])
print(newl[-1::-2])








