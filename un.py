#def calculate_i_by_power(degree: int) -> int | str:
    # return = ['1', 'i', '-1', '-i'][power % 4]

#for number in range (5)
#print (calculate_i_by_power)


#2.1 

def shift(values: list, direction: str) -> list:
    steps = int(direction [1:]) % len(values)
    if direction[0] in ['B', 'b']:
       return values[:steps]
    elif direction[1].lower() == 'f':
        return values[steps:] + values[:steps]
    elif direction [1].lower() == 'f':
        return values[len(values)-steps:] + values[:len(values)-steps]

data = [1, 2, 3, 4]
print(shift(data, 'f1'))
print(shift(data, 'b1'))
    
    
   

    
    

