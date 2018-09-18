#Random walk
#This is a package that offers a function that stimulates the random walk

import numpy as np
import time


def Walk(original_pos,length,num_of_step,p=50):
    pos=original_pos
    for i in range(0,num_of_step):
        '''
        Then generate a bernoulli distribution with
        p(x=0)=0.5,p(x=1)=0.5
        if x=0, we draw back
        else we move forward
'''
        number=np.random.uniform(0,100)
        if number>=p: 
  

            pos=pos+1
            if pos==length-1:
                break
        else:
            pos=pos-1
            if pos==0:
                break

        print(pos)
       # time.sleep(0.1)

    return pos




    



