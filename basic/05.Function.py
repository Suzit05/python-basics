# py 05.Function.py

def check_usage(usage):   #"{}" k jhg use ":"
    if(usage)>75:          #keep notice to the line of the code
        return "High memory usage"
    return "Memory is normal"
print(check_usage(85))