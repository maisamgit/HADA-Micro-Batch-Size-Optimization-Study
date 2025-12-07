import matplotlib.pyplot as plt
import numpy as np

# Coded by: Maisam Abbas
# Course: Advance Operating System
# Micro-Batch Sizes
batch_sizes = [1, 2, 4, 8, 16]

# Standard Strategy Data
# Note: At batch size 8, the table notes "(Peak)" which is just a label, the value is 78.90
std_throughput = [58.30, 66.92, 77.82, 78.90, 74.11]

# Checkpointing Strategy Data
chk_throughput = [37.71, 45.75, 53.26, 57.33, 53.89]

# --- Plotting the Graph ---
plt.figure(figsize=(10, 6))

# Plotting Standard Line
plt.plot(batch_sizes, std_throughput, marker='o', linestyle='-', color='#d62728', label='Standard Strategy', linewidth=2, markersize=8)

# Plotting Checkpointing Line
plt.plot(batch_sizes, chk_throughput, marker='s', linestyle='--', color='#1f77b4', label='Checkpointing Strategy', linewidth=2, markersize=8)

# Adding labels and title
plt.title('Throughput Comparison: Standard vs. Checkpointing', fontsize=16, fontweight='bold')
plt.xlabel('Micro-Batch Size', fontsize=12, fontweight='bold')
plt.ylabel('Throughput (samples/sec)', fontsize=12, fontweight='bold')

# Setting the x-axis ticks to match the specific batch sizes
plt.xticks(batch_sizes)

# Adding grid and legend
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# Annotating the Peak
peak_val = 78.90
peak_idx = 3 # Index of batch size 8
plt.annotate('Standard Peak\n(78.90 s/s)', xy=(8, 78.90), xytext=(8, 85),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center', color='#d62728')

# Show the plot
plt.tight_layout()
plt.show()