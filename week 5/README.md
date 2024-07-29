# Week 5 - Neural Network from Scratch!

Today, we implement a simple neural network from scratch using Python and NumPy. The code is structured into three main components: Neuron, Layer, and NeuralNetwork. Below, we will break down each part and explain how it works.

## Neuron
A neuron is the basic unit of a neural network. It takes multiple inputs, applies weights to them, adds a bias, and produces an output. The dot product we learned about last week will be handy here.

```python
class Neuron:
    def __init__(self, num_inputs):
        self.num_inputs = num_inputs
        self.weights = np.random.random(num_inputs)
        self.bias = np.random.random()
        self.output = 0

    def calc_output(self, inputs):
        self.output = np.dot(self.weights, inputs) + self.bias
        return self.output
```

### Explanation of Neuron code

**Initialization (`__init__` method):**

- **`num_inputs`**: Number of inputs to the neuron.
- **`weights`**: Randomly initialized weights for each input.
- **`bias`**: Randomly initialized bias.
- **`output`**: The output of the neuron, initialized to 0.

**Calculate Output (`calc_output` method):**

- Takes `inputs` as an argument.
- Computes the dot product of `weights` and `inputs`, adds the `bias`, and stores the result in `output`.

## Layer

A layer consists of multiple neurons. It takes inputs, passes them through each neuron, and produces outputs.

```python
class Layer:
    def __init__(self, num_inputs, num_neurons):
        self.num_inputs = num_inputs
        self.num_neurons = num_neurons

        # Creating the neurons
        self.neurons = []
        for _ in range(self.num_neurons):
            neuron = Neuron(self.num_inputs)
            self.neurons.append(neuron)

        # Storing the neurons outputs
        self.outputs = []

    def gen_outputs(self, inputs):
        self.outputs = [neuron.calc_output(inputs) for neuron in self.neurons]
        return self.outputs
```

### Explanation of Layer code

**Initialization (`__init__` method):**

- **`num_inputs`**: Number of inputs to each neuron in the layer.
- **`num_neurons`**: Number of neurons in the layer.
- **`neurons`**: List of neurons in the layer, each initialized with `num_inputs`.
- **`outputs`**: List to store the outputs of each neuron.

**Generate Outputs (`gen_outputs` method):**

- Takes `inputs` as an argument.
- Computes the output for each neuron and stores it in `outputs`.


## NeuralNetwork

A neural network consists of multiple layers. It takes inputs, passes them through each layer, and produces final outputs.

```python
class NeuralNetwork:
    def __init__(self, num_inputs, num_hidden_layers, num_hidden_layer_neurons, num_output_layer_neurons):
        self.num_inputs = num_inputs
        self.num_hidden_layers = num_hidden_layers
        self.num_hidden_layer_neurons = num_hidden_layer_neurons
        self.num_output_layer_neurons = num_output_layer_neurons

        # Creating hidden layers
        self.hidden_layers = []
        for _ in range(self.num_hidden_layers):
            layer = Layer(self.num_inputs, self.num_hidden_layer_neurons)
            self.hidden_layers.append(layer)

        # Creating output layer
        self.output_layer = Layer(self.num_hidden_layer_neurons, self.num_output_layer_neurons)

    def forward(self, inputs):
        for layer in self.hidden_layers:
            inputs = layer.gen_outputs(inputs)
        outputs = self.output_layer.gen_outputs(inputs)
        return outputs
```

### Explaining the Network Code

**Initialization (`__init__` method):**

- **`num_inputs`**: Number of inputs to the network.
- **`num_hidden_layers`**: Number of hidden layers.
- **`num_hidden_layer_neurons`**: Number of neurons in each hidden layer.
- **`num_output_layer_neurons`**: Number of neurons in the output layer.
- **`hidden_layers`**: List of hidden layers, each initialized with `num_inputs` and `num_hidden_layer_neurons`.
- **`output_layer`**: The output layer, initialized with `num_hidden_layer_neurons` and `num_output_layer_neurons`.

**Forward Pass (`forward` method):**

- Takes `inputs` as an argument.
- Passes `inputs` through each hidden layer and then through the output layer.
- Returns the final outputs.

## Full Code

```python
import numpy as np 

np.random.seed(0)

class Neuron:
    def __init__(self, num_inputs):
        self.num_inputs = num_inputs
        self.weights = np.random.random(num_inputs)
        self.bias = np.random.random()
        self.output = 0

    def calc_output(self, inputs):
        self.output = np.dot(self.weights, inputs) + self.bias
        return self.output
    
class Layer:
    def __init__(self, num_inputs, num_neurons):
        self.num_inputs = num_inputs
        self.num_neurons = num_neurons

        # Creating the neurons
        self.neurons = []
        for _ in range(self.num_neurons):
            neuron = Neuron(self.num_inputs)
            self.neurons.append(neuron)

        self.outputs = []

    def gen_outputs(self, inputs):
        self.outputs = [neuron.calc_output(inputs) for neuron in self.neurons]
        return self.outputs
    
class NeuralNetwork:
    def __init__(self, num_inputs, num_hidden_layers, num_hidden_layer_neurons, num_output_layer_neurons):
        self.num_inputs = num_inputs
        self.num_hidden_layers = num_hidden_layers
        self.num_hidden_layer_neurons = num_hidden_layer_neurons
        self.num_output_layer_neurons = num_output_layer_neurons

        # Creating hidden layers
        self.hidden_layers = []
        for _ in range(self.num_hidden_layers):
            layer = Layer(self.num_inputs, self.num_hidden_layer_neurons)
            self.hidden_layers.append(layer)

        # Creating output layer
        self.output_layer = Layer(self.num_hidden_layer_neurons, self.num_output_layer_neurons)

    def forward(self, inputs):
        for layer in self.hidden_layers:
            inputs = layer.gen_outputs(inputs)
        outputs = self.output_layer.gen_outputs(inputs)
        return outputs
```

## Summary

In this guide, we explored the implementation of a basic neural network in Python:

1. **Neuron Class**: 
   - Initializes with random weights and bias.
   - Computes output using dot product and bias.

2. **Layer Class**: 
   - Contains a list of neurons.
   - Computes outputs for each neuron and stores them.

3. **Neural Network Class**: 
   - Composes multiple layers, including hidden and output layers.
   - Passes data through layers to generate final outputs.

This implementation showcases the fundamental components and data flow in a feedforward neural network. Experiment with the code to see how different configurations affect the network's output.

## Upcoming

There is a lot more to learn about neural network as we proceed. We will soon cover:

- Activation functions and why we need them
- Types of activation functions
- Calculating loss using categorical cross entropy
- Backpropagation
- Updating our weights and biases on the fly to cater to the training dataset
- And more!
