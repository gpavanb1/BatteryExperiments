import pybamm
import matplotlib.pyplot as plt
from custom_plot import CustomPlot
from tqdm import tqdm

# Define parameters
parameter_values = pybamm.ParameterValues("Chen2020")

# Define discharge rates to simulate (in C-rate)
discharge_rates = [0.1, 0.5, 1]  # in C

# Initialize a list to store simulation solutions
solutions = []

# Loop through discharge rates and solve DFN model
for rate in tqdm(discharge_rates):
    # Create the model
    model = pybamm.lithium_ion.DFN()

    # Create a simulation
    sim = pybamm.Simulation(
        model, parameter_values=parameter_values, C_rate=rate)

    # Solve the simulation
    solution = sim.solve([0, 3600])

    # Store the solution
    solutions.append(solution)

labels = ["0.1C", "1C", "10C"]
yaxis = "Terminal voltage [V]"

# Create a custom plot using the CustomPlot class (assuming it's defined)
cp = CustomPlot(solutions, labels, yaxis=yaxis)
cp.ax.legend(loc="lower left")

# Show the plot
plt.show()
