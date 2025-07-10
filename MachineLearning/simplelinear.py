import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv(r"C:\Users\hp\OneDrive\Documents\Salary_Data.csv")
df
df.head(12)
x=df.iloc[:,:-1]
y=df.iloc[:,1]
x
y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=9)


from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)


print("Intercept",model.intercept_)
print("Cofficient",model.coef_)



# visualize the data in training set
plt.scatter(x_train,y_train,c='r')
plt.plot(x_train,model.predict(x_train),c='b')
plt.title('Salary vs Experience (Training _set)')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

# visualize the plot in testset
plt.scatter(x_test,y_test,c='r')
plt.plot(x_test,model.predict(x_test),c='b')
plt.title('Salary vs Experience (Testing _set)')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

from sklearn.metrics import mean_squared_error
print("MSE FOR TRAIN DATA",mean_squared_error(y_train,model.predict(x_train)))
print("MSE FOR TEST DATA",mean_squared_error(y_test,y_pred))


print("RMSE FOR TEST",np.sqrt(mean_squared_error(y_test,y_pred)))

print("Train R2",model.score(x_train,y_train))

from sklearn.model_selection import cross_val_score
score = cross_val_score(model, x, y, cv=5)
print(score)
print("Cross Validation Score:", score.mean())

import pickle  # ✅ Required to use pickle

filename = 'linear_regression_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)

print("Model has been pickled and saved as linear_regression_model.pkl")
