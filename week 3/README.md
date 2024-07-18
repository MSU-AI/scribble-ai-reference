# Week 3 - Learn to Draw on a Canvas!

Welcome back. I hope the last week's lessons were helpful. The primary purpose of giving a sneak peek at Google Quickdraw at the end was to give not only an idea of what the completed project would look like, but also to give you guys a little bit of time to think what things are needed from a technical standpoint.

The very first thing you might have noticed on Google Quickdraw is the big white canvas where you have to draw the doodles. To build a project similar to that, our first task, hence, should be to get a canvas up and running. And not any canvas would do, we need a drawable canvas!

## Installing streamlit drawable canvas

Luckily for us, we don't need to code out a drawable canvas ourselves. There exists lots of external libraries for streamlit - called streamlit "components" - and one of them is a drawable canvas! This should give us a head start so that we can put all of our focus onto the AI features of this project.

We'll install it right away:

```bash
pip install streamlit-drawable-canvas
```

After we install it, we are free to get started. To begin, we will use the starter code provided by this library to get a canvas up and running:

```python
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Specify canvas parameters in application

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")

realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    update_streamlit=realtime_update,
    height=500,
    drawing_mode="freedraw",
    point_display_radius=0,
    key="canvas",
)

# Do something interesting with the image data and paths
# The image from the canvas is available as an ndarray and can be accessed via "canvas_result.image_data"
if canvas_result.image_data is not None:
    # Do something here
```

That is a lot of code! Fear not!!

We'll go through them together. Let's look at the imports first

```python
import streamlit as st
from streamlit_drawable_canvas import st_canvas
```

So, we are importing streamlit as before, but now we are also importing the drawable canvas that we just installed.

Let's look at the first three lines:

```python
stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
```

In these lines, we are making use of the `.sidebar()` functionality of streamlit. It is just like `.write()` or any other streamlit function we have looked at before. It is used to control the sidebar of our webapp. Then, with the sliders and color pickers we are setting the stroke width and color, and the background color.

Now:

```python
realtime_update = st.sidebar.checkbox("Update in realtime", True)
```

This line dictates whether the canvas is updated in real time or not. It is a checkbox in the sidebar. By default, it is set to true. For our purposes, we will always want this to be true.

At the very end:

```python
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    update_streamlit=realtime_update,
    height=500,
    drawing_mode="freedraw",
    point_display_radius=0,
    key="canvas",
)
```

This is the code that draws the canvas on the webpage. You can see the various options it is taking, the stroke width and color, the background color, whether to update in realtime or not, everything we did before is now passed to this function to dictate how the canvas will look like.

Pretty much all the code we have covered till now should remain the same and will only give you a canvas. The main task (and challenge) now lies in **doing** something with the image produced by the canvas.

The image by the canvas is available in `canvas_result.image_data`. We can do whatever we want with the image right now.

## Wrapping up

For this week, we feel like this should be enough. This week we learned:

1) We learned about the need of a canvas
2) We installed the streamlit drawable canvas
3) We looked at the streamlit sidebar
4) We went through the canvas code and tried to comprehend what it does
5) We now can advance to actually doing something with the canvas image

## References

- https://github.com/andfanilo/streamlit-drawable-canvas
