import numpy as np

theta = 0
epoch = 3


class Perceptron:
    def __init__(self, input_size, learning_rate=1):
        self.learning_rate = learning_rate
        self.weights = np.zeros(input_size + 1)

    def train(self, x, y):
        for inputs, label in zip(x, y):
            net_in = np.dot(inputs, self.weights[1:]) + self.weights[0]
            y_out = 1 if net_in > theta else -1 if net_in < -theta else 0

            if y_out != label:
                self.weights[1:] += self.learning_rate * label * inputs
                self.weights[0] += self.learning_rate * label

            print(inputs, net_in, y_out, label, self.weights)


if __name__ == "__main__":
    x = [np.array([1, 1]), np.array([-1, 1]), np.array([1, -1]), np.array([-1, -1])]
    y = np.array([1, -1, -1, -1])

    perceptron = Perceptron(2)

    for i in range(epoch):
        print("Epoch", i)
        print("X1 X2 ", " Net ", " Y ", " T ", " B Weights")

        print("Initial Weights", perceptron.weights)
        perceptron.train(x, y)