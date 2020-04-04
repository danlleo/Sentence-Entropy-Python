import math

def char_frequency(string):
    sorted_string = sorted(set(string))
    char_counter = []
    frequency_value = []
    entropy = 0

    for i in range(0, len(sorted_string)):
        char_counter.append(string.count(sorted_string[i]))

    diagram = dict(zip(sorted_string, char_counter))

    for i in range(0, len(sorted_string)):
        frequency_value.append(round(diagram[sorted_string[i]] / len(string), 3))
        

    frequency = dict(zip(sorted_string, frequency_value))

    for i in range(0, len(frequency_value)):
        entropy -= frequency_value[i] * math.log2(frequency_value[i])
    
    
    return round(entropy, 3)


print(char_frequency("entropy"))
