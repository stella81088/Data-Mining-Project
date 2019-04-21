import numpy as np
import pandas as pd
import math as mth
import os

#x1 = pd.read_csv("AmazonFriends.txt")
#x = np.loadtxt(fname= ("AmazonFriends.txt"),dtype='str' )




          
filepath = 'AmazonFriends.txt'  



with open(filepath) as textFile:
    lines = [line.split() for line in textFile]
    #print(lines)




string = "movies"
string.count("movies")

path="C:/Users/zclou/Desktop/CSC 498/data/CoLinAdapt/Amazon/Users"


for i in range (1):
#for i in range (len(lines)):
    for j in range(15):
    #for j in range(len(lines[i])):
        temp = lines[i][j]
        for m in os.listdir(path):
            if os.path.isfile(os.path.join(path,m)) and temp in m:
                with open("C:/Users/zclou/Desktop/CSC 498/data/CoLinAdapt/Amazon/Users/"+m) as f:
                    templ=f.read().replace('\n', '')
                #print(templ)
                print(m)
                
                print("Movies & TV: ",templ.count('Movies & TV'))
                print("Video Games: ",templ.count('Video Games'))
                print("Books: ",templ.count('Books'))
                print("Music: ",templ.count('Music'))
                print("Pet Supplies: ",templ.count('Pet Supplies'))
               
                
            
