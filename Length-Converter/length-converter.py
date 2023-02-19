Input_length = input("length(◯ mm, ◯ cm, ◯ m, ◯ km): ")
Input_unit = input("unit(mm, cm, m, km): ")

def converter(length, unit):
    if length [-1] == 'm':
        if length[-2] == 'm':
            value = str(length).strip('mm')
            value = int(value)
            if unit == "mm":
                return value / 1
            
            elif unit == "cm":
                return value / 10
            
            elif unit == "m":
                return value / 1000
            
            elif unit == "km":
                return value / 1e+6
            
        elif length[-2] == 'k':
            value = str(length).strip('km')
            value = int(value)
            if unit == "mm":
                return value * 1e+6
            
            elif unit == "cm":
                return value * 100000
            
            elif unit == "m":
                return value * 1000
            
            elif unit == "km":
                return value * 1
        
        elif length[-2] == 'c':
            value = str(length).strip('cm')
            value = int(value)
            if unit == "mm":
                return value / 10
            
            elif unit == "cm":
                return value / 1
            
            elif unit == "m":
                return value / 100
            
            elif unit == "km":
                return value / 100000
        
        else:
            value = str(length).strip('m')
            value = int(value)
            if unit == "mm":
                return value * 1000
            
            elif unit == "cm":
                return value * 100
            
            elif unit == "m":
                return value * 1
            
            elif unit == "km":
                return value * 1000
