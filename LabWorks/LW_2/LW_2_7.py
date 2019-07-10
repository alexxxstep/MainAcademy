

# new_file = open('myfily.txt', 'w')
#
# new_file.write('Hello file world!')
# new_file.read()
# new_file.close()

# new_file = open('somefile.txt', 'w')

# with open('somefile.txt', 'rt') as f:
#     data = f.read()
#     print(data)


# read files
# with open('somefile.txt', 'rt') as f:
#     for line in f:
#         print(line)


# перезаписываем
# with open('somefile.txt', 'wt') as f:
#     f.write('text1')
#     f.write('text2')
# try:
#     with open('somefile.txt', 'r') as f:
#         contents = f.read()
#     print(contents)
# except:
#     print('Error opening file')


# with open('somefile.txt', 'r') as f:
#         lines = f.readlines()
#
# for i in  lines:
#     print(i)

# with open('planets.txt', 'r') as f:
#     for line in f:
#         print(line)
#         print(len(line.strip()))


with open('top.txt', 'w') as output_file:
    output_file.write('Hello!\n')


with open('top.txt', 'a') as output_file:
    output_file.write('Hello!\n')





