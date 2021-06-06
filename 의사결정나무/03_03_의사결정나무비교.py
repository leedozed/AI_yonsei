import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('loan.csv')
df['job'] = df['job'].replace({'Office':0, 'ProfExe':1, 'Other':2, 'Mgr':3, 'Self':4, 'Sales':5})
X = df.drop(['y'], axis=1)
y = df['y']
xname = X.columns
yname = ['Normal','Bad']

#train과 test data로 구분
from sklearn.model_selection import train_test_split
#test data 40%, 층화추출 stratify = y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0, stratify=y)

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

#가지치기
from sklearn.model_selection import GridSearchCV
np.random.seed(0)
g_cv = GridSearchCV(DecisionTreeClassifier(random_state=0),
              param_grid={'ccp_alpha': np.arange(0.000, 0.005, 0.0001)}, cv=10)
g_cv.fit(X_train, y_train)

# print('selected:',g_cv.best_params_)
# print('score   :',g_cv.best_score_)

c1_tree = DecisionTreeClassifier(ccp_alpha=0.0008,random_state=0) 
c1_tree.fit(X_train, y_train)

c2_tree = DecisionTreeClassifier(ccp_alpha=0.0,min_impurity_decrease=0.0005,min_samples_split=2,random_state=0)
c2_tree.fit(X_train, y_train)

c3_tree = DecisionTreeClassifier(min_impurity_decrease=0.0003,random_state=0) 
c3_tree.fit(X_train, y_train)

c4_tree = DecisionTreeClassifier(random_state=0) 
c4_tree.fit(X_train, y_train)

from sklearn.metrics import plot_roc_curve
roc_tree=plot_roc_curve(c1_tree, X_test, y_test)
plot_roc_curve(c2_tree, X_test, y_test, ax = roc_tree.ax_)
plot_roc_curve(c3_tree, X_test, y_test, ax = roc_tree.ax_)
plot_roc_curve(c4_tree, X_test, y_test, ax = roc_tree.ax_)
plt.title("ROC curve comparison")
plt.show()

from sklearn.linear_model import LogisticRegression
c_logit = LogisticRegression(random_state=0, max_iter = 1000)
c_logit.fit(X_train, y_train)

from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
c_nn = MLPClassifier(hidden_layer_sizes=(5),random_state=0, max_iter = 1000)
c_nn.fit(X_train_scaled, y_train)

from sklearn import svm
c_svm = svm.SVC(kernel='rbf', random_state=0)
c_svm.fit(X_train_scaled,y_train)

from sklearn.ensemble import RandomForestClassifier
c_rf = RandomForestClassifier(random_state=0)
c_rf.fit(X_train,y_train)

roc_tree=plot_roc_curve(c2_tree, X_test, y_test)
plot_roc_curve(c_logit, X_test, y_test, ax = roc_tree.ax_)
plot_roc_curve(c_nn, X_test_scaled, y_test, ax = roc_tree.ax_)
plot_roc_curve(c_svm, X_test_scaled, y_test, ax = roc_tree.ax_)
plot_roc_curve(c_rf, X_test, y_test, ax = roc_tree.ax_)
plt.title("ROC curve comparison")
plt.show()

