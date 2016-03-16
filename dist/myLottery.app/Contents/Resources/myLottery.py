#-*- coding:UTF-8 -*-

from Tkinter import *
import random
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#shuffle balls
def shuffle(aList):
	new_list = random.shuffle(aList)
	return new_list

#pick the ball
def getIndex(length):
	return length / 2 

def getNumList(original, length, n):
	num_list = []
	new_list = original
	for i in range(n):
		for j in range(1000):
			shuffle(new_list)
		index = getIndex(length - i)
		num_list.append(new_list[index])
		new_list.pop(index)
	return num_list

original_top = [i for i in range(1, 36)]
original_bottom = [i for i in range(1, 13)]

num_top_list = getNumList(original_top, 35, 5)
num_bottom_list = getNumList(original_bottom, 12, 2)

root = Tk()
listb = Listbox(root)
listb2 = Listbox(root)

for item in num_top_list:
	listb.insert(0, item)

for item in num_bottom_list:
	listb2.insert(0, item)

listb.insert(0, '前区号码:  ')
listb2.insert(0, '后区号码:  ')

listb.pack()
listb2.pack()
root.mainloop()
















	
