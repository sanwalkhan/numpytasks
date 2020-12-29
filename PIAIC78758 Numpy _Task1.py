#!/usr/bin/env python
# coding: utf-8

# # Reading Recipes 
# 
# Note: Data file is recipes.csv Attached with jupyter notebook
1. Start by importing NumPy as np
# In[1]:


import numpy as np


# 2. All of Alize’s recipes call for milk, eggs, sugar, flour, and butter. For example, her cupcake recipe calls for:
# 
# Flour Sugar Eggs Milk Butter 2 cups 0.75 cups 2 eggs 1 cups 0.5 cups Create a NumPy array that represents this data. Each element should be a number (i.e., 2 for “2 cups”). Save this array as cupcakes.

# In[3]:


arr = np.array([2,0.75,2,1,0.5])
arr


# 3. Alize’s assistant has compiled all of her recipes into a csv (comma-separated variable) file called recipes.csv. Load this file into a variable called recipes.
# 
# ###########Explore yourselves how to load a csv file in numpy#######

# In[5]:


file = open("recipes.csv")
numpy_array = np.loadtxt(file, delimiter=",")
numpy_array


# 4.Display recipes using print.
# Display recipes using print.
# 
# 
# Each row represents a different recipe. Each column represents a different ingredient.
# 
# Recipe	       Cups of Flour	Cups of Sugar	Eggs	Cups of Milk	Cups of Butter
# 
# Cupcakes	         …	              …	          …	         …	              …
# 
# Pancake	             …                …	          …	         …	              …
# 
# Cookie	             …	              …	          …	         …	              …
# 
# Bread	             …	              …	          …	         …	              …

# In[6]:


numpy_array#type your code here


# 5.The 3rd column represents the number of eggs that each recipe needs.
# 
# Select all elements from the 3rd column and save them to the variable eggs.

# In[54]:


eggs =  print(numpy_array[:,[3]])
eggs #type your code here


# 6.Which recipes require exactly 1 egg? Use a logical statement to get True or False for each value of eggs.

# In[68]:


arr = print(numpy_array[:,[3]])
arr1 = arr.astype(np.bool)  #type your code here


# 7.Alize is going to make 2 batches of cupcakes (1st row) and 1 batch of cookies (3rd row).
# 
# You already have a variable for cupcakes. Create a variable for cookies with the data from the 3rd row.
# 

# In[95]:


cookies = print(numpy_array[3])   #type your code here
a = cookies
a


# 8.
# Get the number of ingredients for a double batch of cupcakes by using multiplication on cupcakes. Save your new variable to double_batch.

# In[96]:


double_batch = print(numpy_array[1]*numpy_array[1]) #type your code here


# 9.
# Create a new variable called grocery_list by adding cookies and double_batch.

# In[93]:


#type your code here


# In[107]:


cookies = np.array([4.  ,0.5  ,2.  ,2.  ,0.5])
double_batch = np.array([1.       ,0.015625 ,1.       ,1.       ,0.015625])
print(double_batch)
print(cookies)


# In[108]:


grocery_list = cookies + double_batch


# In[109]:


grocery_list


# In[ ]:




