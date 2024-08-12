#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


dataset = pd.read_csv("loan-train.csv")


# In[3]:


dataset.head()


# In[4]:


dataset.shape


# In[5]:


dataset.info()


# In[6]:


dataset.describe()


# In[8]:


pd.crosstab(dataset['Credit_History'], dataset['Loan_Status'], margins=True)


# In[9]:


dataset.boxplot(column='ApplicantIncome')


# In[10]:


dataset['ApplicantIncome'].hist(bins=20)


# In[11]:


dataset['CoapplicantIncome'].hist(bins=20)


# In[12]:


dataset.boxplot(column='ApplicantIncome', by='Education')


# In[13]:


dataset.boxplot(column='LoanAmount')


# In[14]:


dataset['LoanAmount'].hist(bins=20)


# In[16]:


dataset['LoanAmount_log']=np.log(dataset['LoanAmount'])
dataset['LoanAmount_log'].hist(bins=20)


# In[17]:


dataset.isnull().sum()


# In[26]:


dataset['Gender'].fillna(dataset['Gender'].mode()[0],inplace=True)


# In[27]:


dataset['Married'].fillna(dataset['Married'].mode()[0],inplace=True)


# In[28]:


dataset['Dependents'].fillna(dataset['Dependents'].mode()[0],inplace=True)


# In[29]:


dataset['Self_Employed'].fillna(dataset['Self_Employed'].mode()[0],inplace=True)


# In[22]:


dataset.LoanAmount = dataset.LoanAmount.fillna(dataset.LoanAmount.mean())
dataset.LoanAmount_log = dataset.LoanAmount_log.fillna(dataset.LoanAmount_log.mean())


# In[30]:


dataset['Loan_Amount_Term'].fillna(dataset['Loan_Amount_Term'].mode()[0],inplace=True)


# In[31]:


dataset['Credit_History'].fillna(dataset['Credit_History'].mode()[0],inplace=True)


# In[32]:


dataset.isnull().sum()


# In[34]:


dataset['TotalIncome']= dataset['ApplicantIncome'] + dataset['CoapplicantIncome']
dataset['TotalIncome_log']= np.log(dataset['TotalIncome'])


# In[35]:


dataset['TotalIncome_log'].hist(bins=20)


# In[36]:


dataset.head()


# In[39]:


X = dataset.iloc[:,np.r_[1:5,9:11,13:15]].values
y = dataset.iloc[:,12].values


# In[40]:


X


# In[41]:


from sklearn.model_selection import train_test_split
X_train,X_test, y_train, y_test, = train_test_split(X,y,test_size = 0.2, random_state = 0)


# In[42]:


print(X_train)


# In[43]:


from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()


# In[44]:


for i in range(0,5):
    X_train[:,i]= labelencoder_X.fit_transform(X_train[:,i])


# In[45]:


X_train[:,7]= labelencoder_X.fit_transform(X_train[:,7])


# In[46]:


X_train


# In[47]:


labelencoder_y = LabelEncoder()
y_train= labelencoder_y.fit_transform(y_train)


# In[48]:


y_train


# In[49]:


for i in range(0,5):
    X_test[:,i]= labelencoder_X.fit_transform(X_test[:,i])


# In[50]:


X_test[:,7]= labelencoder_X.fit_transform(X_test[:,7])


# In[51]:


labelencoder_y = LabelEncoder()
y_test= labelencoder_y.fit_transform(y_test)


# In[52]:


X_test


# In[53]:


y_test


# In[55]:


from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
X_train=ss.fit_transform(X_train)
X_test=ss.fit_transform(X_test)


# In[56]:


from sklearn.tree import DecisionTreeClassifier
DTClassifier = DecisionTreeClassifier(criterion='entropy', random_state = 0)
DTClassifier.fit(X_train,y_train)


# In[57]:


y_pred= DTClassifier.predict(X_test)
y_pred


# In[58]:


from sklearn import metrics
print('The accuracy of decision tree is:', metrics.accuracy_score(y_pred,y_test))


# In[59]:


from sklearn.naive_bayes import GaussianNB
NBClassifier = GaussianNB()
NBClassifier.fit(X_train,y_train)


# In[60]:


y_pred= NBClassifier.predict(X_test)


# In[61]:


y_pred


# In[62]:


print('The accuracy of Naive Bayes is: ', metrics.accuracy_score(y_pred,y_test))


# In[65]:


testdata = pd.read_csv("loan-test.csv")


# In[66]:


testdata.head()


# In[68]:


testdata.info()


# In[69]:


testdata.isnull().sum()


# In[71]:


testdata['Gender'].fillna(testdata['Gender'].mode()[0],inplace=True)
testdata['Dependents'].fillna(testdata['Dependents'].mode()[0],inplace=True)
testdata['Self_Employed'].fillna(testdata['Self_Employed'].mode()[0],inplace=True)
testdata['Loan_Amount_Term'].fillna(testdata['Loan_Amount_Term'].mode()[0],inplace=True)
testdata['Credit_History'].fillna(testdata['Credit_History'].mode()[0],inplace=True)


# In[72]:


testdata.isnull().sum()


# In[74]:


testdata.boxplot(column='LoanAmount')


# In[75]:


testdata.boxplot(column='ApplicantIncome')


# In[76]:


testdata.LoanAmount= testdata.LoanAmount.fillna(testdata.LoanAmount.mean())


# In[78]:


testdata['LoanAmount_log']= np.log(testdata['LoanAmount'])


# In[79]:


testdata.isnull().sum()


# In[80]:


testdata['TotalIncome']= testdata['ApplicantIncome']+testdata['CoapplicantIncome']
testdata['TotalIncome_log']= np.log(testdata['TotalIncome'])


# In[81]:


testdata.head()


# In[82]:


test = testdata.iloc[:, np.r_[1:5,9:11,13:15]].values


# In[84]:


for i in range(0,5):
    test[:,i]=labelencoder_X.fit_tranform(test[:,i])


# In[ ]:




