# -*- coding: utf-8 -*-
"""
programma Raccomandation Engine 

Doc pandas dataframe
https://note.nkmk.me/en/python-pandas-set-index/

Author: Alessandra
Date: 1/05/2020


"""
import argparse
import pandas as pd 
import math 


def raccomandation(filename):
    
    name = []
    scorecolumn = []
        
    #read file
    articlelist = pd.read_csv(filename)      
    print (articlelist)  
    
    nrow, ncol = articlelist.shape
    print ('nrow = ',nrow,'ncol = ', ncol)
    
    #element al quale propore i prodotti
    last = nrow - 1
    
    # assign the name of the column
    for j in range(ncol) :
        name.append (articlelist.columns[j])
    print  (name)


    #compute minimum distance 
    for i in range(nrow-1) :
        score = 0
        for j in range(1,ncol) :
              score = score + (pow ((articlelist.loc[last,name[j]] -  articlelist.loc[i,name[j]]),2))  
    
        #print ('score = ',score, ' e sqrt score = ', math.sqrt (score))
        scorecolumn.append(math.sqrt (score))
        
    #add last value in score column
    scorecolumn.append(10000)
    #print (score)
    print (scorecolumn)  
    
    # add column
    articlelist['score'] = scorecolumn
    print (articlelist) 
    

    # find minimum score     
    minValue = articlelist['score'].min()
    idrowmin = articlelist.index[articlelist['score']== minValue].tolist()
    
    print ('minvalue = ',minValue,'idrowmin= ', idrowmin)
    
   
    #propose product not in list
    for i in range(len(idrowmin)) :
        for j in range(3,ncol) :
            if (articlelist.loc[idrowmin[i],name[j]] == 1) and  (articlelist.loc[last,name[j]]  == 0 ) :  
                print ('user = ', articlelist.loc[idrowmin[i],articlelist.columns[0]]  , ' proposed article = ', articlelist.columns[j])


    
           
## main        
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-t", "--text", required=True, help="path to text file")

args = vars(ap.parse_args())  

raccomandation(args["text"])





