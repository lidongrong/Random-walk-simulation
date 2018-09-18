#Random walk
#随机游动模拟

import numpy as np
import time

#两侧为吸收壁的普通随机游动
def Walk(original_pos,length,num_of_step,p=50):
    pos=original_pos
    for i in range(0,num_of_step):
        '''
        Then generate a bernoulli distribution with
        p(x=0)=p ,p(x=1)=1-p
        if x=0, we draw back
        else we move forward
'''
        probability=np.random.uniform(0,100)
        if probability<=p: 
  

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

#有反射壁（一侧）的随机游动，用于炉石传说上分模拟

def HearthStone(original_pos,length,p=50):
    pos=original_pos
    step=0
    while pos<length-1:
        probability=np.random.uniform(0,100)

        if probability<=p:
            pos=pos+1

        else:
            pos=pos-1
            if pos<0:
                pos=pos+1

        print(pos)
        step=step+1

    return step

                




    



