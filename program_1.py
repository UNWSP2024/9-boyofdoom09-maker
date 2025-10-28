# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    names = open('names.txt', 'w')
    names.write("Alice\n")
    names.write("Bob\n")
    names.close() 

    
    names_read = open('names.txt', 'r')
    content = names_read.readlines()
    print(len(content))
    names_read.close()
    ######################
    print('In the count_file_lines function')



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
