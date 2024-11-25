import matplotlib.pyplot as plt
import pandas as pd

# Custom color mapping
colors_custom_cleaned = {
    "EDC": "#66c2a5",
    "EAC": "#fc8d62",
    "Fe": "#e78ac3",
    "EEC": "#8da0cb",
    "Mn": "#a6d854",
    "S": "#ffd92f"
}

# Depth values
depths_numeric = [10, 30, 50]

# Function to plot with SEM and circles
def plot_with_sem_circles(ax, data, cleaned_variables, colors, depths_numeric):
    for var, color in zip(cleaned_variables, colors):
        original_var = variable_name_mapping.get(var, var)
        means = data[original_var].values
        sems = data[f"{original_var} sem"].values
        ax.plot(means, depths_numeric, color=color, marker='o', label=var, linestyle=':', linewidth=3, markersize=8)
        ax.fill_betweenx(depths_numeric, means - sems, means + sems, color=color, alpha=0.2)

# Function to set subplot properties
def set_subplot_properties_with_custom_xticks(ax, title):
    ax.set_xlabel("mmol g⁻¹ soil", fontsize=10)
    ax.set_ylabel("Soil Depth (cm)", fontsize=10)
    ax.set_xlim(0, 0.75)
    ax.set_xticks([0, 0.25, 0.5, 0.75])
    ax.set_ylim(55, 5)
    ax.legend(loc='lower left', frameon=False, ncol=4, fontsize=8)
    ax.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('black')
        spine.set_linewidth(1.5)
    ax.text(0.95, 0.98, title, horizontalalignment='right', verticalalignment='top',
            transform=ax.transAxes, fontsize=12)

# variable orders
left_variables = ["EDC", "EAC"]
right_variables = ["EEC", "Fe", "S", "Mn"]

# dataset loading
file_path = "MEC_data.xlsx"
df = pd.read_excel(file_path)

# Separate data by location
floodplain_data = df[df['Unnamed: 1'] == 'Floodplain']
hillslope_data = df[df['Unnamed: 1'] == 'Hillslope']

# Final plot
fig, axs = plt.subplots(2, 2, figsize=(8, 8), constrained_layout=True)

# Plot Floodplain data
plot_with_sem_circles(axs[0, 0], floodplain_data, left_variables, 
                      [colors_custom_cleaned[var] for var in left_variables], depths_numeric)
set_subplot_properties_with_custom_xticks(axs[0, 0], "Floodplain")

plot_with_sem_circles(axs[0, 1], floodplain_data, right_variables_reordered_final, 
                      [colors_custom_cleaned[var] for var in right_variables_reordered_final], depths_numeric)
set_subplot_properties_with_custom_xticks(axs[0, 1], "Floodplain")

# Plot Hillslope data
plot_with_sem_circles(axs[1, 0], hillslope_data, left_variables, 
                      [colors_custom_cleaned[var] for var in left_variables], depths_numeric)
set_subplot_properties_with_custom_xticks(axs[1, 0], "Hillslope")

plot_with_sem_circles(axs[1, 1], hillslope_data, right_variables_reordered_final, 
                      [colors_custom_cleaned[var] for var in right_variables_reordered_final], depths_numeric)
set_subplot_properties_with_custom_xticks(axs[1, 1], "Hillslope")

plt.show()
