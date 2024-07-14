# Week 1 - Getting Familiar with Scribble and Python

In this project, we will be training and building an AI model that is able to detect scribbles and be able to tell what object the scribble represents. 

## A Brief Project Overview

In general, scribble is a game where every member of a group that is playing take turns to draw (or scribble) something on a canvas, and every other non-scribbling member has to guess what that object is. 

Take a look at: https://skribbl.io/. This is the game. Play a little to get familiar with it. It's always best to play with a couple of friends so you get the idea of the entire game. 

This project will be pretty similar to the game. The players should be able to choose a word randomly from a list of words that the AI will not know of. Afterwards, every player will be required to scribble the word as best as they can and the AI will try and predict what the word is. Simple idea. There will be no scribble-drawing AI, however. 

## Setting up Python Environment

What we will be using to complete this project will be Python for our base programming language, as well as Streamlit, which is a Python library that allows us to build web-ready apps without writing any web dev code. This will allow us to focus solely on Python and the AI. Since this project focuses on learning some foundational AI, we will be making use of Neural Networks to train the AI model, as opposed to using something like OpenAI API to have GPT recognize the image for us. We will be using scikit-learn for the AI.

1) If on Windows, install Python from https://www.python.org/ and download the latest version.
2) On Windows, make sure to check the box that says "Set Python to PATH" while installing.
3) On MacOS or Linux, Python should be pre-installed, so update it using Homebrew: [Insert MacOS instructions]

Install streamlit using pip inside a terminal or command prompt:
```bash
pip install streamlit
```

## Writing Basic Streamlit Code

Now, we get our feet a little wet by writing some basic Python code that uses the streamlit library to display content on a webpage. After creating a new .py file, write the following code:

```python
import streamlit as st

st.write("Hello World")
```

Then, it can easily be run from the terminal using the command:

```bash
streamlit run your-file-name.py
```

## Understanding the code

At first, we import the library. As we progress, you will come across this `import` statement a lot of times as we need to import external modules and libraries to help us achieve our goal. 

Secondly, the `st.write()` function takes whatever is put inside the parentheses and then displays them on the browser. This is a really simple approach where you do not have to deal with HTML, CSS or JS code and jump straight into Python while also having a web app to display your project. Just like `st.write()`, there are a plethora of other streamlit functions and programming styles that we will look at in the future weeks. 

## Farewell
Until next time, keep going over the things learned today, namely:

1) What Scribble is
2) 