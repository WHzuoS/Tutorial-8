def listToDisctionary(aList):
    dictionary = {}
    objectList = []
    sum = 0
    
    for i in range(len(aList)):
        
        key = aList[i][0]
        
        for j in range(len(aList)):
            
            if (aList[i][0] == aList[j][0]):
                objectList.append(aList[j][1])
                sum += aList[j][2]

        if key not in dictionary:
            dictionary[key] = [objectList, sum]
        
        objectList = []
        sum = 0
    
    return dictionary
            
def display(aDictionary):
    
    for key in aDictionary:
        print(f"{key} : {aDictionary[key]}")

def main():
    
    sales = [["customer1", "bread", 5], ["customer2", "bread", 4.5], ["customer1", "egg", 6.75], 
             ["customer2", "milk", 4.35], ["customer3", "egg", 3.6], ["customer4", "bread", 4.5], 
             ["customer1", "milk", 4.35], ["customer2", "egg", 3.6], ["customer4", "milk", 4.35]]
    
    record = listToDisctionary(sales)
    
    display(record)
    
main()
    