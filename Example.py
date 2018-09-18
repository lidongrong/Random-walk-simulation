from RW import*


while 1:
    length=input("Please input the length of the line: ")
    length=int(length)

    original_pos=input("Please input the original position: ")
    original_pos=int(original_pos)

    num_of_step=input("Please input the number of steps: ")
    num_of_step=int(num_of_step)

    Walk(original_pos,length,num_of_step)
