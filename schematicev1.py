import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_schematic():
    fig, ax = plt.subplots()
    
    # Draw solar panel (SP)
    solar_panel = patches.Rectangle((0.1, 0.7), 0.2, 0.2, fill=True, edgecolor='black', facecolor='lightgray')
    ax.add_patch(solar_panel)
    ax.text(0.2, 0.8, 'SP', fontsize=12, ha='center')
    
    # Draw charge controller (CC)
    charge_controller = patches.Rectangle((0.4, 0.7), 0.2, 0.2, fill=True, edgecolor='black', facecolor='lightgray')
    ax.add_patch(charge_controller)
    ax.text(0.5, 0.8, 'CC', fontsize=12, ha='center')
    
    # Draw battery (B)
    battery = patches.Rectangle((0.7, 0.7), 0.2, 0.2, fill=True, edgecolor='black', facecolor='lightgray')
    ax.add_patch(battery)
    ax.text(0.8, 0.8, 'B', fontsize=12, ha='center')
    
    # Draw motor controller (MC)
    motor_controller = patches.Rectangle((0.4, 0.4), 0.2, 0.2, fill=True, edgecolor='black', facecolor='lightgray')
    ax.add_patch(motor_controller)
    ax.text(0.5, 0.5, 'MC', fontsize=12, ha='center')
    
    # Draw motor (M)
    motor = patches.Rectangle((0.4, 0.1), 0.2, 0.2, fill=True, edgecolor='black', facecolor='lightgray')
    ax.add_patch(motor)
    ax.text(0.5, 0.2, 'M', fontsize=12, ha='center')
    
    # Draw switches (S)
    switch1 = patches.Rectangle((0.1, 0.4), 0.2, 0.2, fill=True, edgecolor='black', facecolor='lightgray')
    ax.add_patch(switch1)
    ax.text(0.2, 0.5, 'S', fontsize=12, ha='center')
    
    switch2 = patches.Rectangle((0.7, 0.4), 0.2, 0.2, fill=True, edgecolor='black', facecolor='lightgray')
    ax.add_patch(switch2)
    ax.text(0.8, 0.5, 'S', fontsize=12, ha='center')
    
    # Draw connections (wires)
    plt.plot([0.3, 0.4], [0.8, 0.8], color='black')  # SP to CC
    plt.plot([0.6, 0.7], [0.8, 0.8], color='black')  # CC to B
    plt.plot([0.5, 0.5], [0.7, 0.6], color='black')  # CC to MC
    plt.plot([0.5, 0.5], [0.4, 0.3], color='black')  # MC to M
    plt.plot([0.3, 0.4], [0.5, 0.5], color='black')  # S1 to MC
    plt.plot([0.6, 0.7], [0.5, 0.5], color='black')  # S2 to MC
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    plt.axis('off')
    plt.show()

draw_schematic()
