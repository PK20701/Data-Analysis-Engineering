#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('pip', 'install pdfplumber -q')


# In[4]:


import pdfplumber as pp

with pp.open(r'C:\Users\ADMIN\Desktop\Prasanna\Learning\Data Analyst\DataAnalysis-\PYModules\book.pdf') as book:
    for page_no, page in enumerate(book.pages, start=1):
        print(f'{page_no = }')
        data = page.extract_text()
        print(data.strip())
        print('-'*45)


# In[ ]:




