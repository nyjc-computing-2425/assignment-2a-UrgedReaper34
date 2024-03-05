num = input('Enter a number (decimal or integer): ')
# type your code here
newtext = num.replace("-", "").replace(".", "").lstrip("0")

sf = len(newtext)





# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
