from ucimlrepo import fetch_ucirepo 
import pandas as pd
import matplotlib.pyplot as plt
    
wine = fetch_ucirepo(id=109)   

X = wine.data.features 
y = wine.data.targets 
  

print(X.describe())

print(X.corr())

x_var = X['Proanthocyanins']
y_var = X['Flavanoids']
plt.scatter(x_var, y_var, color='blue', marker='o', label='Data Points')
plt.xlabel('X Variable')
plt.ylabel('Y Variable')
plt.title('Scatter Plot between X and Y')

plt.show()