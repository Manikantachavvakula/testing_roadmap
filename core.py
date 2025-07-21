class solution():
    def listss(self,n,target):
        n.append(23)
        print(f"List after appending 23 : {n}")
        n.insert(2,3)
        print(f"List after inserting 3 at index 2 : {n}")
        if target in n :
            n.remove(target)
            print(f"List after removing {target} : {n}")
        else : 
            print(f"No {target} found in the list")
        n.pop()
        print(f"List after popping : {n}")
        for i in n :
            print (i)

    def tuplee(self,n):
        try :
            n.append(2)
        except AttributeError :
            print("Tuples are immutable")

    def setss(self,n):
        b=set(n)
        b.add(5)
        print(f"Set after adding 5 : {b}")
        if 4 in n :
             b.remove(4)
             print(f"Set after removing 4 : {b}")
        else :
            print("No 4 is found")
        print(f"Set after no duplicates : {b} ")
        for i in b :
            print (i)


a= solution()
n = list(map(int,input("Enter list with space seperated : ").split()))
target = int(input("Enter a number to remove : "))
a.listss(n,target)

b=tuple(map(int,input("Enter tuple : ").split()))
a.tuplee(b)
        
f = list(map(int,input('Enter Set : ').split()))
a.setss(f)