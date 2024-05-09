import pybamm
import matplotlib.pyplot as plt
from custom_plot import CustomPlot
from tqdm import tqdm

# Define parameters
parameter_values = pybamm.ParameterValues("Chen2020")

# Define cathode sizes to simulate
concentrations = [1000., 5000., 20000.]  # in meters

# Initialize a list to store simulation solutions
solutions = []

# Loop through cathode sizes and solve DFN model
for conc in tqdm(concentrations):
    # Update the parameter values for cathode thickness
    parameter_values.update(
        {"Initial concentration in electrolyte [mol.m-3]": conc})

    # Create the model
    model = pybamm.lithium_ion.DFN()

    # Create a simulation
    sim = pybamm.Simulation(model, parameter_values=parameter_values)

    # Solve the simulation
    solution = sim.solve([0, 3600])

    # Store the solution
    solutions.append(solution)

labels = ["1M", "5M", "20M"]
yaxis = "X-averaged battery reaction overpotential [V]"
cp = CustomPlot(solutions, labels, yaxis=yaxis)

# Show the plot
plt.show()
