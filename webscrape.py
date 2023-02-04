# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 10:23:44 2023

@author: HP
"""
#importing modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager   
import time
import pandas as pd

#paper link
link="https://www.nature.com/articles/s41598-023-28880-x"


#setupChrome
websetup=webdriver.Chrome(ChromeDriverManager().install())
websetup.get(link)
time.sleep(5)

#title
title=websetup.find_element_by_xpath("/html/body/div[2]/main/article/div[2]/header/h1")
title_as_str=title.text
print(title_as_str)
print("\n")
    

#abs
abs_title=websetup.find_element_by_xpath("/html/body/div[2]/main/article/div[3]/section[1]/div/h2")
abs_title_as_str=abs_title.text
print(abs_title_as_str)
    
    
#abs_content
abst=websetup.find_element_by_id("Abs1-content")
abstract=abst.text
print(abstract)
abst_len=len(abstract.split())
print('\n Number of words in the abstract :',abst_len)
abst_len=str(abst_len)
    

#body_count
content=websetup.find_element_by_class_name("main-content")
content=content.text
spl_content=content.split()
print('\n Number of words in the body :',len(spl_content))
body_len=str(len(spl_content))
        
    
#img count
img=websetup.find_elements_by_tag_name('img')
print('\nNumber of images in the paper :',len(img))
img_len=str(len(img))
    
    
#references
l=[]
for i in range(1,40):
    id="ref-CR"
    i=str(i)
    id=id+''.join(i)
    ref=websetup.find_element_by_id(id)
    ref=ref.text
    l+=[ref]
    print('\n',ref)


#dictionary
dictionary={'Title':(title_as_str),'Abstract':(abstract),'Abs_count':(abst_len),'Bdy_count':(body_len)}


file1=pd.DataFrame(data=dictionary,index=[1])
print(file1)
file1.to_csv('.\paper_stats.csv')

file2=pd.DataFrame(l,columns=['references'])
file2.to_csv('./references.csv')
print(file2)





