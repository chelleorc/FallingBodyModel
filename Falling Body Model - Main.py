#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This is a falling body modeling project that takes air resistance 
#into account

#This is the main program that will call the 
#functions needed to model a falling ball


# In[4]:


#Function that calls the list of Python libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as ani
import pandas as pd
import seaborn as seb


# In[11]:


#Function that calculates the solution of a falling body 
# of the falling body differential equation
#dv/dt + (k/m)v = g
def model(v,t):
    k = 0.5
    m = 20
    g = 9.8
    dvdt = g - (k/m)*v
    return dvdt

#initial condition
v0 = 0

#time points
t = np.linspace(0,200)

#v is the velocity 
# v stores the solution of the ordinary differential equation
v = odeint(model,v0,t)


# In[19]:


#Function that creates the graph to plot the falling body
def plotFunction():
    plt.plot(t,v)
    plt.xlabel("time")
    plt.ylabel("v(t)")
    plt.title("Graph of Falling Body with Air Resistance")
    plt.show()
    display()
    
#Calls function to plot the falling body graph    
plotFunction()
    


# In[25]:


#Function that calls the dynamic plot to demonstrate the falling body
# Use this site to plot animation: https://towardsdatascience.com/intro-to-dynamic-visualization-with-python-animations-and-interactive-plots-f72a7fb69245 

# Change matplotlib backend
get_ipython().run_line_magic('matplotlib', 'notebook')
title = 'Falling Body'
t = np.array(time)
v = np.array(velocity)
fallingBody = pd.DataFrame(t,v)
#TN,VN = augment(t,v,10)
#augmented = pd.DataFrame(TN,VN)

#Initialize writer
Writer = ani.writers['ffmpeg']
writer = Writer(fps=20, metadata=dict(artist='Me'), bitrate=1800)

#Label and set limits for animation
fig = plt.figure(figsize=(10,6))
plt.tlim(0, 200)
plt.tlabel('Time', fontsize=20)

plt.vlim(np.min())


# In[ ]:


# From https://towardsdatascience.com/intro-to-dynamic-visualization-with-python-animations-and-interactive-plots-f72a7fb69245
#Function that calls the animation that demonstrates the falling body 
# Import animation package
from matplotlib.animation import FuncAnimation

# Change matplotlib backend to allow for interactive plots
get_ipython().run_line_magic('matplotlib', 'notebook')

# Create variable reference to plot
f_d, = ax.plot([], [], linewidth=2.5)

# Add text annotation and create variable reference for time
tp = ax.text(1, 1, '', ha='right', va='top', fontsize=24)

# Animation function
def animate(i):
    t = np.linspace(0,1,200)
    v = odeint(model,v0,t)
    f_d.set_data(t,v)
    f_d.set_color(colors(i))
    tp.set_text(str(int()))
    

