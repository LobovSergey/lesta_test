from random import randint


def is_even(value):            
    return not bool(value & 1)  



if __name__ == "__main__":
    picked_value = randint(0, 256)  
    
    value = is_even(value=picked_value)
    print(f"picked num is {picked_value}. Even - {bool(value)}")
    


