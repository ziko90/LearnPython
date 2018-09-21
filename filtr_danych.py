
def filter_input(input_list, n):
    print(len(input_list))
    signal_output = []

    for i, j in enumerate(input_list):
        if i - n < 0:
            signal_output.append(sum(input_list[:i + n+1]) / len(input_list[:i + n+1]))
        elif i + n > len(input_list):
            signal_output.append(sum(input_list[i - n:-1]) / len(input_list[i - n:-1]))
        #elif i - n < 0 and i + n > len(input_list):
        #    signal_output.append(sum(input_list[:]) / len(input_list[:]))
        else:
            signal_output.append(sum(input_list[i - n:i + n+1]) / len(input_list[i - n:i + n+1]))
    return signal_output

signal_input = [1, -0.2, 54, 3, 6, 7, 10, 20, 34, 50, 1, 2]
n = 1

x = filter_input(signal_input, n)
print(x)

if len(signal_input) == len(x):
    print(True)