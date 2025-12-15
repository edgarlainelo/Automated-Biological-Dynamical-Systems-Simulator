import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
from sympy import symbols, lambdify, sympify
import pandas as pd
import math



class App:


    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("570x380")


        self.frame = tk.Frame(self.root)
        self.frame.grid(sticky = "nsew")

        self.button_run = tk.Button(self.frame, text = 'Run', font = ('Arial',10), command = self.run)
        self.button_run.grid(row=7, column=2, pady =10, padx=300, sticky ='w')

        self.btn_example = tk.Button(self.frame, text = 'Example functions', font = ('Arial',10), command = self.example)
        self.btn_example.grid(row = 7, column = 2, pady= 10, padx = 100, sticky = 'w')


        
        self.first_fun_label = tk.Label(self.frame, text = 'Derivative of function 1:', font = ('Arial', 12))
        self.first_fun_label.grid(row=0, column = 2, pady = 10, padx=10, sticky = 'w')
        self.first_fun = tk.Text(self.frame, height=1, width=45)
        self.first_fun.grid(row=0, column=2, pady=10, padx=180, sticky='w')


        self.second_fun_label = tk.Label(self.frame, text = 'Derivative of function 2:', font = ('Arial', 12))
        self.second_fun_label.grid(row=1, column = 2, pady = 10, padx=10, sticky = 'w')
        self.second_fun = tk.Text(self.frame, height =1, width=45)
        self.second_fun.grid(row=1, column=2, pady=10, padx=180, sticky='w')

        self.step_label = tk.Label(self.frame, text = 'Step size (dt):', font = ('Arial',12))
        self.step_label.grid(row= 2, column=2, pady = 10, padx=10, sticky='w')
        self.step_input = tk.Text(self.frame, height = 1, width = 10)
        self.step_input.grid(row=2, column= 2, pady =10, padx=120, sticky='w')

        self.start_x_label = tk.Label(self.frame, text = 'x starting value:', font = ('Arial',12))
        self.start_x_label.grid(row=3, column=2,pady=10, padx= 10, sticky='w')
        self.start_x = tk.Text(self.frame, height=1, width = 20)
        self.start_x.grid(row= 3, column = 2, pady = 10, padx = 130, sticky='w')

        self.start_y_label = tk.Label(self.frame, text = 'y starting value:', font = ('Arial',12))
        self.start_y_label.grid(row=4, column=2,pady=10, padx= 10, sticky='w')
        self.start_y = tk.Text(self.frame, height=1, width = 20)
        self.start_y.grid(row= 4, column = 2, pady = 10, padx = 130, sticky='w')

        self.vector_label = tk.Label(self.frame, text ='Include vector field:', font = ('Arial',12))
        self.vector_label.grid(row=6, column=2, pady = 10, padx = 10, sticky='w')
        self.vector_chose = ttk.Combobox(self.frame, width = 20, height = 10)
        self.vector_chose.grid(row = 6, column=2, pady=10, padx=160, sticky='w')
        self.vector_chose['values'] = ['No', 'Yes (may be hard to read)']
        self.vector_chose.current(0)


        self.num_steps = tk.Label(self.frame, text = 'Number of points:', font = ('Arial',12))
        self.num_steps.grid(row = 5, column=2, pady = 10, padx=10, sticky='w')
        self.num_steps_input = tk.Text(self.frame, height=1, width = 20)
        self.num_steps_input.grid(row = 5, column=2, pady = 10, padx = 150, sticky='w')

        self.root.mainloop()

    
    def run(self):
        #Converting function input into a function
        self.dx_input = self.first_fun.get('1.0',END)
        self.dy_input = self.second_fun.get('1.0', END)
        self.x, self.y = symbols('x y')
        self.dx_expr = sympify(self.dx_input)
        self.dy_expr = sympify(self.dy_input)
        self.dx_fun = lambdify((self.x, self.y), self.dx_expr)
        self.dy_fun = lambdify((self.x, self.y), self.dy_expr)
        

        #Getting starting values
        self.dt = float(self.step_input.get('1.0', END))
        self.x = int(self.start_x.get('1.0', END))
        self.y = int(self.start_y.get('1.0', END))
        self.points = int(self.num_steps_input.get('1.0', END))

        #Creating dataframe with starting values
        self.df = pd.DataFrame({'x':[self.x],
                                'y':[self.y]})
        
        #Getting values for the plot
        for i in range(0,self.points):
            self.dx = self.dx_fun(self.x, self.y) * self.dt
            self.dy = self.dy_fun(self.x, self.y) * self.dt

            self.x += self.dx
            self.y += self.dy

            self.df.loc[len(self.df)] = [self.x, self.y]


        plt.scatter(self.df['x'], self.df['y'])
        self.x_range = plt.xlim()[1] - plt.xlim()[0]
        self.y_range = plt.ylim()[1] - plt.ylim()[0]

        self.arrow_size = 0.00025 * max(self.x_range, self.y_range)
        
        if self.vector_chose.get() == 'Yes (may be hard to read)':
            self.min_x, self.max_x = min(self.df['x']), max(self.df['x'])
            self.min_y, self.max_y = min(self.df['y']), max(self.df['y'])

            for i in range(math.floor(self.min_x), math.ceil(self.max_x), math.floor((self.max_x-self.min_x)/10)):
                for j in range(math.floor(self.min_y), math.ceil(self.max_y), math.floor((self.max_y-self.min_y)/10)):
                    self.pointer_x = self.dx_fun(i,j) * self.dt
                    self.pointer_y = self.dy_fun(i,j) * self.dt
                
                    plt.arrow(i,j, self.pointer_x, self.pointer_y, head_width = self.arrow_size, head_length = self.arrow_size*10)
            plt.show()
                    
            
        else:
            plt.show()




    def example(self):
        
        if len(self.first_fun.get('1.0', END)) > 0:
            self.first_fun.delete('1.0', END)
            self.first_fun.insert(INSERT,'0.1*x*(1-(x/10000))-0.005*x*y')
        else:
            self.first_fun.insert(INSERT,'0.1*x*(1-(x/10000))-0.005*x*y')

        if len(self.second_fun.get('1.0', END)) >0:
            self.second_fun.delete('1.0', END)
            self.second_fun.insert(INSERT, '0.00004*x*y-0.04*y')
        else:
            self.second_fun.insert(INSERT, '0.00004*x*y-0.04*y')

        if len(self.step_input.get('1.0', END)) > 0:
            self.step_input.delete('1.0', END)
            self.step_input.insert(INSERT, '1')
        else:
            self.step_input.insert(INSERT, '1')

        if len(self.start_x.get('1.0', END)) > 0:
            self.start_x.delete('1.0', END)
            self.start_x.insert(INSERT, '2000')
        else:
            self.start_x.insert(INSERT, '2000')
        
        if len(self.start_y.get('1.0', END)) > 0:
            self.start_y.delete('1.0', END)
            self.start_y.insert(INSERT, '10')
        else:
            self.start_y.insert(INSERT, '10')

        if len(self.num_steps_input.get('1.0', END)) > 0:
            self.num_steps_input.delete('1.0', END)
            self.num_steps_input.insert(INSERT, '1000')
        else:
            self.num_steps_input.insert(INSERT, '1000')

        


if __name__ == "__main__":
    App()