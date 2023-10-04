import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import GridSearchCV

dataframe = pd.read_excel('SUV_26 Nisan 2023.xlsx', sheet_name='Sınıflandırma İçin Veri Seti')

X = dataframe.iloc[:, [3,7]].values
y = dataframe.iloc[:, 18].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.24, random_state = 0)

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print(cm)


rf_params = {"max_depth": [2,5,8,10],"max_features": [2,5,8],"n_estimators": [10,500,1000],"min_samples_split": [2,5,10]}
classifier = RandomForestClassifier()
rf_cv_model = GridSearchCV(classifier,rf_params,cv = 10,n_jobs = -1,verbose = 2) 
rf_cv_model.fit(X_train, y_train)

print("En iyi parametreler: " + str(rf_cv_model.best_params_))

rf_tuned = RandomForestClassifier(max_depth = 2,max_features = 2,min_samples_split = 2,n_estimators = 10)
rf_tuned.fit(X_train, y_train)

y_pred = rf_tuned.predict(X_test)
accuracy_score(y_test, y_pred)
tcm = confusion_matrix(y_test, y_pred)
print(tcm)
