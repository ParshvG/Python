list = ["apple", "orange", "banana", 1, 2, 3.50, 1, 2]
print(list)
print(list[0])
#TO CHECK LENGTH OF LIST
print(len(list))
#TO CHECK TYPE
print(type(list))
#TO ACCESS ELEMENT OF THE LIST
print(list[2])
print(list[-6])
#USING RANGE
print(list[1:6])
print(list[2:])
print(list[:2])
#USING IN
if ("banana" in list):
    print("elements is present in list")
else:
    print("element is not present in list")
list[2] = "orange"
print(list)
list[:5] = ["how are you"]
print(list)
list[0] = "apple1"
print(list)
#append
list2 = [100, 1, 2, "hi"]
list2.append("apple1")
print(list2)
#insert value
list2.insert(1,"banana")
print(list2)
#adding list
print(list + list2)
print(list)
#putting list2 elements in list by extend function
list.extend(list2)
print(list)
#del(list)
#removing variables present in the list
list.remove(3.5)
print(list)
#pop using
list.pop(0)
print(list)
#if pop() used without putting input will remove last variable
list.pop()
print(list)
#del using
del(list[0])
print(list)
del(list)
print(list)
#clear elements using
list.clear()
print(list)
#using sort elements it uses to put in its's order ascending order
list1 = ["a", "z", "hi", "hello", "apple", "abble", "b", "c", "d", "e", "f"]
list2 = [1, 100, 0, 1000, 2, 3, 4, 5 , 6, 7]
list1.sort()
list2.sort()
print(list1)
print(list2)
#for desending order reverse
list1.sort(reverse=True)
print(list1)
list2.sort(reverse=True)
print(list2)
#for copying other list
list3 = list2.copy()
print(list3)