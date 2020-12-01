h = open('input_day1.txt', 'r') 
myList = [] 

content = h.readlines() 
  

for line in content:   
    for i in line: 
        myList.append(int(line))

def twoNums(): 
    for num in myList: 
        a = 2020 - num 
        if a in myList:
            print(a * (2020 - a))
            return 

def threeNums(): 
    for num in myList: 
        a = 2020 - num
        for num2 in myList:
            if num2 < a and num2 in myList: 
                b = (a - num2)
                if b in myList:
                    print(str(num) + ", " + str(num2) + ", " + str(b) + ", ")
                    print(num * num2 * b)
                    return 




threeNums()