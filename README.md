# Automated-Biological-Dynamical-Systems-Simulator

DESCRIPTION AND MOTIVATION:

The software was developed to automate proccess of visualiztion of mathematically described dynamical systems. Primary focus is for biological systems (like prey-predetory models), but can be used for non-biological systems as well. Additionally software allows to visualize the vector field of the system - the direction of the evoution of the system.

USAGE:
1) User needs to input derivatives of two functions that depend on each other.
2) User needs to input the step size (dt), meaning the time difference between each calculation
3) Starting values of system x and system y must also be included.
4) Number of points indicates for how long user wants to analyze the system
5) Inclusion of vector field. User selects to include or not to include the vector field of the system. Due to the unpredictability of the dynamical systems, inclusion of the vector field can result in "messy" simulation. In some instances, vector fields should be avoided.

User has possibility of looking on example dynamical system of predetory-prey model by clicking "Example functions" button, which will fill all the necessary inputs.
By clicking the "Run" button, graphical visualiztion will be returned by the user, which can be saved. 

