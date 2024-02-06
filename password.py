import random                       
def generate_password(len):   
    list_of_chars ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"   
    pass_str = ""   
    for i in range(len):   
        pass_str = pass_str + random.choice(list_of_chars)   
    return pass_str   
if __name__ == "__main__":   
    len = 8   
    pass_str = generate_password(len)   
    print("A randomly generated Password is:", pass_str)
