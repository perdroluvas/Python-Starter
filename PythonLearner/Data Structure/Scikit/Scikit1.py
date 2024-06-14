from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
X = [[0,0], [1,1], [2,2]]
y = [0,1,2]
reg = linear_model.LinearRegression()
reg.fit(X,y)
print(reg.coef_)
print(StandardScaler().fit(X).transform(X))
data = MinMaxScaler(feature_range=(0.,1)).fit_transform(X)
print(data)
pipe = make_pipeline(
    StandardScaler(),
    linear_model.LinearRegression()
)
print(pipe.fit(X,y))
print(pipe[1].coef_)

x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.1)
pipe.fit(x_train,y_train)
print(mean_squared_error(y_test, pipe.predict(x_test)))
