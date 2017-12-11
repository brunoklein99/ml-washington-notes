import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

frame = pd.read_csv('home_data.csv')
print('len', len(frame))
# plt.scatter(frame['sqft_living'], frame['price'])
# plt.show()

prices = frame.groupby(['zipcode'])['price'].mean()
prices = pd.DataFrame(prices)
prices = prices.sort_values(by=['price'], ascending=False)

# print(prices)

between = frame[(frame['sqft_living'] > 2000) & (frame['sqft_living'] < 4000)]


# print(between.size / frame.size)

def get_datasets(frame, features, target):
    train, test = train_test_split(frame, test_size=.2)
    train_x = train[features].values
    train_y = train[target].values
    test_x = test[features].values
    test_y = test[target].values
    print('train_x.shape', train_x.shape)
    return train_x, train_y, test_x, test_y


def evaluate(model, x, y):
    return sqrt(mean_squared_error(y, model.predict(x)))


def plot_model(model, x, y):
    plt.plot(x, y, '.', x, model.predict(x), '-')
    plt.show()


train_x, train_y, test_x, test_y = get_datasets(frame, ['sqft_living'], 'price')

sqft_model = LinearRegression()
sqft_model.fit(train_x, train_y)

print('sqft rmse:', evaluate(sqft_model, test_x, test_y))

#plot_model(sqft_model, train_x, train_y)

my_features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode']

train_x, train_y, test_x, test_y = get_datasets(frame, my_features, 'price')

my_features_model = LinearRegression()
my_features_model.fit(train_x, train_y)

print('my_features rmse:', evaluate(my_features_model, test_x, test_y))

#plot_model(my_features_model, train_x, train_y)

advanced_features = [
    'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode',
    'condition',  # condition of house
    'grade',  # measure of quality of construction
    'waterfront',  # waterfront property
    'view',  # type of view
    'sqft_above',  # square feet above ground
    'sqft_basement',  # square feet in basement
    'yr_built',  # the year built
    'yr_renovated',  # the year renovated
    'lat', 'long',  # the lat-long of the parcel
    'sqft_living15',  # average sq.ft. of 15 nearest neighbors
    'sqft_lot15',  # average lot size of 15 nearest neighbors
]

train_x, train_y, test_x, test_y = get_datasets(frame, advanced_features, 'price')

advanced_model = LinearRegression()
advanced_model.fit(train_x, train_y)

print('advanced rmse:', evaluate(advanced_model, test_x, test_y))
