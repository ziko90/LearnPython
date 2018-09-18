
text = '12310980789349753484'

if isinstance(text, str) and text.isdigit():
    numb=text
else:
    numb = str(text)

print(numb)

while len(numb) > 1 and numb.isdigit():
    l_of_digits = [int(digit) for digit in numb]
   # l_b = l_of_digits[:]
   # print(l_b)
   # print(l_of_digits)
    numb = str(sum(l_of_digits))
    print(numb)
    if len(numb) == 1:
        print(numb)

