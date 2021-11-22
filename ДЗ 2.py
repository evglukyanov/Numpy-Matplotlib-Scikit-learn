#!/usr/bin/env python
# coding: utf-8

# In[9]:


#1. Импортируйте библиотеку Numpy и дайте ей псевдоним np.
#Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов. 
#Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7.
#Будем считать, что каждый столбец - это признак, а строка - наблюдение. 
#Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy. 
#Результат запишите в массив mean_a, в нем должно быть 2 элемента.


# In[3]:


import numpy as np


# In[14]:


a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])

print(a)

print("Размерность a: {}".format(a.ndim))

print("Форма a: {}".format(a.shape))


# In[5]:


a.size


# In[8]:


mean_a = a.mean(axis = 0)
mean_a


# In[10]:


#2. Вычислите массив a_centered, отняв от значений массива а 
#средние значения соответствующих признаков, содержащиеся в массиве mean_a.
#Вычисление должно производиться в одно действие.
#Получившийся массив должен иметь размер 5x2.


# In[15]:


a_centered = np.subtract(a, mean_a)
a_centered


# In[16]:


#3. Найдите скалярное произведение столбцов массива a_centered.
#В результате должна получиться величина a_centered_sp. 


# In[17]:


a1=a_centered[:,0]
a2=a_centered[:,1]
a_centered_sp=np.dot(a1,a2)
a_centered_sp


# In[18]:


#4. поделите a_centered_sp на N-1, где N - число наблюдений


# In[19]:


N=a.shape[0]
N


# In[20]:


my_cov=a_centered_sp/(N-1)
my_cov


# In[1]:


#1. Импортируйте библиотеку Pandas и дайте ей псевдоним pd.


# In[2]:


import pandas as pd


# In[3]:


#1. Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: 
#[1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].


# In[5]:


authors = pd.DataFrame({'author_id':[1, 2, 3],
                      'author_name':['Тургенев', 'Чехов', 'Островский']}, columns=['author_id', 'author_name'])
authors


# In[6]:


#создайте датафрейм book cо столбцами author_id, book_title и price,
#в которых соответственно содержатся данные: [1, 1, 1, 2, 2, 3, 3], 
#['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
#[450, 300, 350, 500, 450, 370, 290].


# In[7]:


books = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
                     'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 
                     'price':[450, 300, 350, 500, 450, 370, 290]}, 
                      columns = ['author_id', 'book_title', 'price'])
books


# In[8]:


#2. Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.


# In[9]:


authors_price = pd.merge(authors, books, on = 'author_id', how = 'outer')
authors_price


# In[10]:


#3. Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.


# In[11]:


top5 = authors_price.nlargest(5, 'price')
top5


# In[12]:


#4. Создайте датафрейм authors_stat на основе информации из authors_price.
#В датафрейме authors_stat должны быть четыре столбца:
#author_name, min_price, max_price и mean_price,
#в которых должны содержаться соответственно имя автора,
#минимальная, максимальная и средняя цена на книги этого автора.


# In[14]:


df1 = authors_price.groupby('author_name').agg({'price': 'min'}).rename(columns={'price':'min_price'})
df2 = authors_price.groupby('author_name').agg({'price': 'max'}).rename(columns={'price':'max_price'})
df3 = authors_price.groupby('author_name').agg({'price': 'mean'}).rename(columns={'price':'mean_price'})
authors_stat=pd.concat([df1, df2, df3], axis = 1)
authors_stat


# In[ ]:




