import pybamm
import matplotlib.pyplot as plt
from custom_plot import CustomPlot
from tqdm import tqdm

# Various kinds of chemistries
chem_map = {
    "LFP": "Prada2013",
    "Lithium": "Chen2020"
}
# Initialize a list to store simulation solutions
solutions = []

# Loop through discharge rates and solve DFN model
for chem in tqdm(chem_map.values()):
    # Create the model
    model = pybamm.lithium_ion.DFN()
    parameter_values = pybamm.ParameterValues(chem)

    # Create a simulation
    sim = pybamm.Simulation(
        model, parameter_values=parameter_values)

    # Solve the simulation
    solution = sim.solve([0, 3000])

    # Store the solution
    solutions.append(solution)

labels = chem_map.keys()
yaxis = "Terminal voltage [V]"

# Create a custom plot using the CustomPlot class (assuming it's defined)
cp = CustomPlot(solutions, labels, yaxis=yaxis)
cp.ax.legend(loc="lower left")
cp.ax.set_xlim([0, 0.8])

# Show the plot
plt.show()
