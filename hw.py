
# coding: utf-8

# In[ ]:


# functions used in the hw_target_customer project 


# In[1]:


# to get the session/spend/purchase days since the installment date 
import pandas as pd
import numpy as np
from pylab import *
import re
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from collections import Counter
import warnings
warnings.filterwarnings('ignore')
from datetime import datetime, timedelta
from sklearn.metrics import roc_auc_score,roc_curve

def get_time_delta(ts, install_ts):
    try: 
        np.isnan(ts)
        delta = np.nan 
    except TypeError: 
        c = pd.DataFrame(columns=['start','stop'])
        c.stop=pd.to_datetime(ts) 
        c.start=install_ts
        delta = np.array((c.stop-c.start).dt.days+(c.stop-c.start).dt.seconds/(24*3600))
        #    delta = [x for x in delta if x < purchase_ts[0]]
    return delta 

def retention(data,threshold):
    # retention 
    if any([data > threshold]):
        return 1
    else:
        return 0
    
def outliers(x): 
    Q1 = x.quantile(0.25)
    Q3 = x.quantile(0.75)
    IQR = Q3 - Q1
    out={'lower':(x < (Q1 - 3.0 * IQR)), 'higher':(x > (Q3 + 3.0 * IQR))}
    return out

def spend_iap(data):
    if 'IAP' in data:
        return 1
    else:
        return 0
    
def plot_ROC(model, X_test,Y_test):
    Y_prob = model.predict_proba(X_test)[:,1]
    fpr, tpr, thresh = roc_curve(Y_test, Y_prob, pos_label=1)
    roc_auc = roc_auc_score(Y_test, Y_prob)
    fig = plt.figure()
    plt.plot(fpr, tpr, color='r', lw=2)
    plt.plot([0, 1], [0, 1], color='b', lw=2, linestyle='--')
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve (Area = {:.2f})'.format(roc_auc))
    plt.legend(loc="lower right")
    plt.show()

def increased_rev(p,alpha,N):
    return (p-alpha*(p+1))*N

def session_before_break_iaps(date,iaps_date):
    # find all the session activity during continuous sessions 
    try:
        array1 = np.diff(pd.to_datetime(date)).astype('timedelta64[D]') >= np.timedelta64(1, 'D')
        index1 = np.argmax(array1)
        array2 = pd.to_datetime(date) > pd.to_datetime(iaps_date[0])
        index2 = np.argmax(array2)
        if index1 ==0 and not array1[index1]:
            index1 = len(date)
        if index2 ==0 and not array2[index2]:
            try:
                index2 = len(date)
            except TypeError:
                pass
        index = min(index1,index2)
    except (TypeError,ValueError):
        index = 0
        pass
    return index 



def session_before_break(date):
    # find all the session activity during continuous sessions 
    try:
        array = np.diff(pd.to_datetime(date)).astype('timedelta64[D]') >= np.timedelta64(1, 'D')
        index = np.argmax(array)
        if (index ==0) and not array[index]:
            index = len(date)
    except (TypeError,ValueError):
        index = 0
        pass
    return index 



def spend_before_break(col,break_date):
    # find all the spend activity during continuous sessions 
    try: 
        array = pd.to_datetime(col) > pd.to_datetime(break_date[-1])
        index = np.argmax(array)
        if index == 0 and not array[index]:
            try:
                index = len(col)
            except TypeError:
                pass
    except (TypeError,ValueError):
        index = 0
        pass
    return index