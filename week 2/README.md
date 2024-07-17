# Week 2 - Playing Around with Streamlit (and Sneak Peek at Google QuickDraw)

Welcome to the 2nd week! For this week, we would be exploring some commands of streamlit and the various components that it offers.

## Text functions

Streamlit has lots of ways to display text on the webpage, and you are free to choose whichever one is best suited for the situation.

`st.title()` - Display text is title formatting

`st.heading()` and `st.subheading()` are used for heading and subheading formatting

## More functions

`st.table()` allows you to display a table on the webpage. Most easily, a Python dictionary can be passed to the function. Let's take a cook at the code block:

```python
data_table = {
    "Days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Temperature": [20, 21, 22, 23, 24]
}

st.table(data_table)
```

This will display a nicely formatted table of temperature data on the webpage

## Displaying Images

We can use the `st.image()` function and pass it any image object to have it displayed on the website. For simplicity, we will use a local image on our computer and simply call the function with the name of the image.

```python
st.image("cat.jpg")
```

## A Simple Mini Program

Go ahead and try to run this streamlit code, but before you do, try to guess what will happen.

```python
import streamlit as st

st.title("Hello ! Welcome to the number guessing game")

st.write("Enter any number and we will display a different image depending on whether the number is odd or even")

num = st.number_input("Enter a number", min_value=0)

if num % 2 == 0 and num != 0:
    st.subheader("You win a cat!")
    st.image("cat.jpg")
elif num % 2 != 0 and num != 0:
    st.subheader("You win a dog!")
    st.image("dog.jpg")
else:
    pass
```

Let us decipher the code:

In the first two lines, we making use of the simple `.title()` and `.write()` functions to display some text and let the user know what the program is about. Then:
```python
num = st.number_input("Enter a number", min_value=0)
```
with this line, we are using `st.number_input()` to take a number input from the user and store it in a variable called `num`. Note that we set the min_value to be 0, this serves as both the minimum value and the starting value. Up next,

```python
if num % 2 == 0 and num != 0:
    st.subheader("You win a cat!")
    st.image("cat.jpg")
elif num % 2 != 0 and num != 0:
    st.subheader("You win a dog!")
    st.image("dog.jpg")
else:
    pass
```
Here, we are using a bunch of if statements to see if the number is odd or even. If it is even, we show a picture of a cat, and if it is odd, we show a picture of a dog.

On each conditions, we are also requiring that the number not be zero since that is our default value and Python considers zero to be an even number, so can you guess what would have happened if we hadn't put in the extra conditional?

## One More Thing - Google Quickdraw

For your final project, you’ll be creating an interactive web application inspired by Google’s Quick, Draw!. This is an engaging game where an AI tries to recognize your doodles in real time. You’ll be using Streamlit, a powerful tool you’ve been learning about, to build this application. The goal is to design an app that can interpret the user’s doodles and make accurate guesses about what they represent. It’s a fantastic opportunity to apply your coding skills, explore AI, and create something fun and interactive. I encourage you to visit Google’s Quick, Draw! to get a feel for what you’ll be building.

Check it out at: https://quickdraw.withgoogle.com/

## Wrapping Up

With that, we conclude our week 2 of this project. In this, we learned about:

- Various streamlit text functions
- The `.table()` function to display a nicely formatted table of data
- The `.image()` function to display images
- A mini program to show some control flow while using streamlit

## Try for yourself

Before next week, challenge yourself by scouting the streamlit API docs and edit the code to:

1) Play a "meow" cat sound alongside displaying the cat image
2) Play a "woof woof" dog sound alongside displaying the dog image
3) Keep everything else the same

## References:

- https://docs.streamlit.io/develop/api-reference
- [Cat Image](https://www.freepik.com/free-photo/red-white-cat-i-white-studio_9405869.htm#query=cat&position=0&from_view=keyword&track=sph&uuid=a21038ba-a8e9-42b8-a9ea-003d5f36f9e5)
