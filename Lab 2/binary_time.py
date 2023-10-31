import time

def binary_time_conversion():
    current_time = time.localtime()
    hour_binary = bin(current_time.tm_hour)[2:].zfill(6)
    minute_binary = bin(current_time.tm_min)[2:].zfill(6)
    second_binary = bin(current_time.tm_sec)[2:].zfill(6)
    return current_time, minute_binary, second_binary, hour_binary

def print_time(current_time):
    time_print = f"{current_time.tm_mon:02}/{current_time.tm_mday:02}/{current_time.tm_year} {current_time.tm_hour:02}:{current_time.tm_min:02}:{current_time.tm_sec:02}"
    print("Current time:", time_print)
    
def convert_binary_to_2d():
    current_time, minute_binary, second_binary, hour_binary = binary_time_conversion()
    current_time = time.strftime("%m/%d/%Y \n %H:%M:%S")
    return current_time, [[int(m) for m in minute_binary], [int(s) for s in second_binary], [int(h) for h in hour_binary]]


