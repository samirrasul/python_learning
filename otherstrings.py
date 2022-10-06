'''
txt1 = 'Hello, '
txt2 = 'World!'

print(txt1 + txt2)
'''

age = 22
name = 'Yalchin is {} years old'
print(name.format(age))

date = 7
time = 11.40
formatted_time = '{:.2f}'.format(time)
number_of_test = 1
txt = 'I have {} test at {} am in {} October'
print(txt.format(number_of_test, formatted_time, date))