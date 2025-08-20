# Email: 22f2000757@ds.study.iitm.ac.in

# ------------------------------
# Cell 1: Base Variables
# ------------------------------
# This cell defines the base values for analysis
base_value = 10
multiplier = 5  # Initial multiplier

# ------------------------------
# Cell 2: Dependent Calculation
# ------------------------------
# This cell calculates the result based on base_value and multiplier
# It automatically updates if base_value or multiplier changes
result = base_value * multiplier

# ------------------------------
# Cell 3: Interactive Slider
# ------------------------------
import mo

# Create a slider to adjust the multiplier interactively
slider = mo.ui.slider(1, 20, value=multiplier)

# Update multiplier based on slider value
multiplier = slider.value

# ------------------------------
# Cell 4: Dynamic Markdown Output
# ------------------------------
# This cell shows the current multiplier and result dynamically
# The number of green circles represents the multiplier
mo.md(f"""
### Interactive Result
- Multiplier: {multiplier}
- Base Value: {base_value}
- Result (base_value * multiplier): {result}

{'🟢' * multiplier}
""")
