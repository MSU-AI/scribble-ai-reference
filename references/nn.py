
import numpy as np

def categorical_cross_entropy(predicted, actual):
    predicted = np.array(predicted)
    actual = np.array(actual)
    return -np.sum(actual * np.log(predicted))

class Neuron:
    def __init__(self, num_inputs, activation_function):
        self.num_inputs = num_inputs
        self.activation_function = activation_function
        self.weights = np.random.randn(num_inputs)
        self.bias = np.random.randn()
        self.output = 0
        self.delta = 0

    def relu(self, x):
        return x if x > 0 else 0

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def calc_output(self, inputs):
        self.output = np.dot(self.weights, inputs) + self.bias

        # Applying activation function
        if self.activation_function == "relu":
            self.output = self.relu(self.output)

        return self.output

class Layer:
    def __init__(self, num_inputs, num_neurons, activation_function):
        self.num_inputs = num_inputs
        self.num_neurons = num_neurons
        self.activation_function = activation_function

        # Creating the neurons
        self.neurons = []
        for _ in range(self.num_neurons):
            neuron = Neuron(self.num_inputs, activation_function=self.activation_function)
            self.neurons.append(neuron)

        self.outputs = []

    def gen_outputs(self, inputs):
        self.outputs = [neuron.calc_output(inputs) for neuron in self.neurons]

        if self.activation_function == "softmax":
            exp_values = np.exp(self.outputs - np.max(self.outputs))
            self.outputs = exp_values / np.sum(exp_values)

        return self.outputs
    
class NeuralNetwork:
    def __init__(self, num_inputs, num_hidden_layers, num_hidden_layer_neurons, num_output_layer_neurons):
        self.num_inputs = num_inputs
        self.num_hidden_layers = num_hidden_layers
        self.num_hidden_layer_neurons = num_hidden_layer_neurons
        self.num_output_layer_neurons = num_output_layer_neurons
        self.loss = None

        # Creating the hidden layers
        self.layers = []
        input_size = num_inputs

        for _ in range(num_hidden_layers):
            layer = Layer(input_size, self.num_hidden_layer_neurons, activation_function="relu")
            self.layers.append(layer)
            input_size = self.num_hidden_layer_neurons

        # Create and add the output layer, the last layer
        output_layer = Layer(num_inputs=input_size, num_neurons=num_output_layer_neurons,
                            activation_function="softmax")
        self.layers.append(output_layer)

    def forward(self, inputs, outputs):

        layer_inputs = inputs
        for layer in self.layers:
            layer_output = layer.gen_outputs(layer_inputs)
            layer_inputs = layer_output


        self.loss = categorical_cross_entropy(layer_inputs, outputs)

        print(F"PREDICTED {layer_inputs}")
        print(f"ACTUAL: {outputs}")
        print(f"DELTA: {self.calc_loss_delta(layer_inputs, outputs)}")
        print(f"LOSS: {self.loss}")

        return layer_inputs

    def calc_loss_delta(self, predicted_outputs, actual_outputs):
        # Calculate the delta for the output layer
        delta = predicted_outputs - actual_outputs
        return delta

    def backward(self, inputs, outputs, learning_rate):
        # Forward pass to get the predicted outputs
        predicted_outputs = self.forward(inputs, outputs)

        # Calculate the delta for the output layer
        delta = self.calc_loss_delta(predicted_outputs, outputs)

        # Update the output layer weights and biases
        output_layer: Layer = self.layers[-1]

        for i, neuron in enumerate(output_layer.neurons):
            new_weights = neuron.weights - ( delta[i] * learning_rate * self.layers[-2].outputs[i] )
            new_bias = neuron.bias - (learning_rate * delta[i])

            neuron.weights = new_weights
            neuron.bias = new_bias

            neuron.delta = delta[i]

inputs = [4, 3, 7]
outputs = [0, 1, 0]

nn = NeuralNetwork(3, 2, 4, 3)
nn.backward(inputs, outputs, 0.1)