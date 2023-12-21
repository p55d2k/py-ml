from sklearn.ensemble import GradientBoostingRegressor as GBR
from sklearn.model_selection import train_test_split


class Bot:
    def __init__(self, data):
        self.data = data
        self.model = GBR()

    def train(self, df):
        """
        This function will train the model.
        :return: The trained model.
        """
        x = df.drop(['Close'], axis=1)
        y = df['Close']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)

        # Training the model
        self.model.fit(x_train, y_train)

        # Predicting the values
        self.test(x_test, y_test)

    def test(self, testx, texty):
        """
        test the model
        :param testx: Input data
        :param texty: Actual results
        :return: print the results
        """
        for index, item in enumerate(testx):
            print(f"Predicted: {self.model.predict(item)}, Actual: {texty[index]}")
