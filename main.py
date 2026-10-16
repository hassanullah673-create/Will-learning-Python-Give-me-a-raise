data = pd.read_csv('data.csv')
X = data[['hours']]
y = data['raise']
model = LogisticRegression()
model.fit(X, y)
print(f"Accuracy: {model.score(X,y)*100:.1f}%")
print(f"Prob at 70 hours: {model.predict_proba([[70]])[0][1]*100:.1f}%")
