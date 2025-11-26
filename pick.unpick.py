#Pickling and unplicking in python.....

import seaborn as sns

df=sns.load_dataset('tips')
print(df)
o=df.head()
print(o)
import pickle
filename='file.pkl'

#serialize process
pickle.dump(df,open(filename,'wb'))

#unserialize process
pickle.load(open(filename,'rb'))

type(df)

dic_example={'first_name':'Nabin','last_name':'Dhakal'}
pickle.dump(dic_example,open('test.pkl','wb'))
pickle.load(open('test.pkl','rb'))



