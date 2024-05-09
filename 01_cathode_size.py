import pybamm
import matplotlib.pyplot as plt
from custom_plot import CustomPlot
from tqdm import tqdm

# Define parameters
parameter_values = pybamm.ParameterValues("Chen2020")

# Define cathode sizes to simulate
cathode_sizes = [7.5e-5, 15e-5, 30e-5]  # in meters

# Initialize a list to store simulation solutions
solutions = []

# Loop through cathode sizes and solve DFN model
for size in tqdm(cathode_sizes):
    # Update the parameter values for cathode thickness
    parameter_values.update({"Positive electrode thickness [m]": size})

    # Create the model
    model = pybamm.lithium_ion.DFN()

    # Create a simulation
    sim = pybamm.Simulation(model, parameter_values=parameter_values)

    # Solve the simulation
    solution = sim.solve([0, 3600])

    # Store the solution
    solutions.append(solution)

labels = ["75 µm", "150 µm", "300µm"]
yaxis = "Terminal voltage [V]"
cp = CustomPlot(solutions, labels, yaxis=yaxis)

# Show the plot
plt.show()
