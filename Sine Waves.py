import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 200)

frames = [0, 5, 10, 15] # phase shifts for multiple frames
single_frame = 10   # frame for the single updated line

# Create figure with 2 subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))


# --- Left subplot: multiple static waves ---
for frame in frames:
    y = np.sin(x + frame/10)
    axes[0].plot(x, y, label=f'Frame {frame}')

axes[0].set_title("Multiple Sine Waves (Static Frames)")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[0].legend()
axes[0].grid()
axes[0].set_ylim(-1.5, 1.5)


# --- Right sublot: single sine wave update ---
y_single = np.sin(x + single_frame/10)
line, = axes[1].plot(x, y_single)
axes[1].set_title(f"Single Updated Sine Wave (Frame {single_frame})")
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")
axes[1].set_ylim(-1.5, 1.5)
axes[1].grid()

plt.tight_layout()
plt.show()


