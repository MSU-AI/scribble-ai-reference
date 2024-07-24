# Week 4 - Cool Stuff - AI!

Over the previous weeks, we have looked at Python and Streamlit and also setup a drawable canvas on the webpage. But, what about all the cool AI Stuff? That's where we will get into now!

## Machine Learning - A Primer

Let us start with a little bit on Machine Learning. It is a subfield of Artificial Intelligence, and you can do all sorts of cool stuff with it. It's a buzzword nowadays. Facial recognition, fingerprint recognition, object detection in images, etc. are all powered by machine learning. But what is it?

To understand ML from scratch, we would need lots of math, which is out of the scope of this project. But, we will still try and understand the concept as much as we can. In ML, we basically have three types of learning:

1) Supervised
2) Unsupervised
3) Reinforcement

**Supervised**: A supervised learning algorithm includes regression and classification algorithms. Here, we provide a mathematical model with some existing data points and then make use of mathematical functions and equations to predict where an unknown data point should lie. For example, For example, let’s say we have a dataset of house prices along with their sizes. In supervised learning, we can train a model on this data, where the size is the input feature and the price is the output we want to predict. Once the model is trained, we can input the size of a new house, and the model will predict its price.

**Unsupervised**: Unsupervised learning algorithms include clustering and association algorithms. Unlike supervised learning, unsupervised learning does not rely on labeled output data. Instead, it finds patterns and relationships in the input data. For example, let’s say we have a dataset of customers with their shopping habits but no specific output variable. An unsupervised learning algorithm can group these customers into clusters based on their shopping habits, helping us understand our customer base better.

**Reinforcement**: Reinforcement learning is a type of machine learning where an agent learns to make decisions by taking actions in an environment to maximize a reward. A classic example is a chess game. The agent makes a move (action), the environment (the chessboard) changes, and the agent gets a reward if it eventually wins the game.

In our project, we will mostly learn about and utilize Neural Networks, which can be considered a Supervised Learning Algorithm.

## What is a Neural Network?

A Neural Network is a computational model inspired by the human brain. It consists of interconnected nodes, or “neurons”, which work together to solve specific problems. NNs are particularly effective at processing complex data such as images, audio, and text.

### Structure of a Neural Network

A typical Neural Network consists of three types of layers:

**Input Layer**: This is where the network receives input from your dataset. Each neuron in this layer represents a unique feature from your dataset.

**Hidden Layer(s)**: These are the layers between the input and output layers. The neurons in these layers perform computations and transfer information from the input nodes to the output nodes.

**Output Layer**: The final layer in the network. It translates the computations from the hidden layers into the final output.

![nn](nn.jpg)

