import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def plot_individual_trajectories(image_path, all_trajectory_sets):
    """
    Plots individual sets of trajectories (Past, Ground Truth, Prediction) on separate images of a background.
    Displays the images in rows of 3.
    
    Parameters:
    - image_path: Path to the background image.
    - all_trajectory_sets: A list of lists, where each inner list contains three sets of trajectories
      (Past Trajectory, Ground Truth, Prediction), with each set being a list of (x, y) tuples.
    """
    image = mpimg.imread(image_path)
    num_sets = len(all_trajectory_sets)
    cols = 3  # Columns for subplot arrangement
    rows = (num_sets + cols - 1) // cols  # Calculate rows needed
    
    # Creating subplots
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 5 * rows))
    if rows * cols > 1:  # If more than one subplot, flatten axes array
        axes = axes.flatten()
    else:
        axes = [axes]
    
    for idx, ax in enumerate(axes[:num_sets]):
        ax.imshow(image)
        # Plotting each trajectory type in a set with a different color
        colors = ['blue', 'green', 'red']  # Colors for Past, Ground Truth, Prediction
        labels = ['Past Trajectory', 'Ground Truth', 'Prediction']
        for traj, color, label in zip(all_trajectory_sets[idx], colors, labels):
            x, y = zip(*traj)
            ax.plot(x, y, '-o', color=color, label=label)
        ax.axis('off')
        ax.legend()

    # Hide any extra subplots
    for ax in axes[num_sets:]:
        ax.axis('off')

    plt.tight_layout(pad=0)
    
    # Define the location you want the image saved (absolute path)
    plt.savefig('/Users/digital_drifting/Documents/sensor_test2/map/empty_intersection_traj_multiple6.jpg', bbox_inches='tight', pad_inches=0)


# Define location of blank image for location (absolute path)
image_path = '/Users/digital_drifting/Documents/sensor_test2/map/blank_images/eth_hotel.jpeg'

trajectories1 = [
    [(50, 100), (100, 100), (150, 100)],  # Past Trajectory (Straight forward)
    [(50, 105), (100, 105), (150, 120)],  # Ground Truth (Slight upward angle)
    [(50, 105), (100, 105), (150, 140)]   # Prediction (Sharp upward angle)
]

trajectories2 = [
    [(50, 100), (100, 100), (150, 90)],   # Past Trajectory (Slight downward angle)
    [(50, 95), (100, 95), (150, 70)],     # Ground Truth (Sharp downward angle)
    [(50, 95), (100, 95), (150, 50)]      # Prediction (More sharp downward angle)
]

trajectories3 = [
    [(50, 100), (100, 110), (150, 120)],  # Past Trajectory (Slight right curve)
    [(50, 100), (100, 115), (150, 140)],  # Ground Truth (Moderate right curve)
    [(50, 100), (100, 120), (150, 160)]   # Prediction (Sharp right curve)
]

trajectories4 = [
    [(50, 100), (100, 90), (150, 80)],    # Past Trajectory (Slight left curve)
    [(50, 100), (100, 85), (150, 60)],    # Ground Truth (Moderate left curve)
    [(50, 100), (100, 80), (150, 40)]     # Prediction (Sharp left curve)
]

trajectories5 = [
    [(50, 100), (100, 100), (150, 110)],  # Past Trajectory (Gently up)
    [(50, 100), (100, 100), (150, 130)],  # Ground Truth (Upward)
    [(50, 100), (100, 100), (150, 150)]   # Prediction (Steeply up)
]

trajectories6 = [
    [(50, 100), (100, 100), (150, 90)],   # Past Trajectory (Gently down)
    [(50, 100), (100, 100), (150, 70)],   # Ground Truth (Downward)
    [(50, 100), (100, 100), (150, 50)]    # Prediction (Steeply down)
]


# Add more trajectory sets as needed
plot_individual_trajectories(image_path, [trajectories1, trajectories2, trajectories3, trajectories4, trajectories5, trajectories6])
    
"""
# Example usage with additional trajectories
image_path = '/Users/digital_drifting/Documents/sensor_test2/map/empty_intersection.jpg'
trajectories1 = [
    [(50, 100), (55, 115), (60, 130)],
    [(50, 100), (55, 110), (60, 140)],
    [(50, 100), (55, 105), (60, 150)]
]

trajectories2 = [
    [(70, 100), (75, 115), (80, 130)],
    [(70, 100), (75, 110), (80, 140)],
    [(70, 100), (75, 105), (80, 150)]
]

trajectories3 = [
    [(90, 100), (95, 115), (100, 130)],
    [(90, 100), (95, 110), (100, 140)],
    [(90, 100), (95, 105), (100, 150)]
]

# Assuming each of these lists is a set of trajectories to be plotted on separate images
plot_multiple_trajectories(image_path, [trajectories1, trajectories2, trajectories3])

"""