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

a= solution()
n = list(map(int,input("Enter list with space seperated : ").split()))
target = int(input("Enter a number to remove : "))
a.listss(n,target)
        