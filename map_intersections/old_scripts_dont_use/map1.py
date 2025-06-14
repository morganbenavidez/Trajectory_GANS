import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the street image
image_path = '/Users/digital_drifting/Documents/sensor_test2/map/empty_intersection.jpg'  # Make sure to use your actual image path here
image = mpimg.imread(image_path)

# Example trajectories (replace these with your actual data)
past_trajectory = [(50, 100), (55, 115), (60, 130)]
ground_truth_trajectory = [(50, 100), (55, 110), (60, 140)]
predicted_trajectory = [(50, 100), (55, 105), (60, 150)]

# Unzip the coordinates for plotting
past_x, past_y = zip(*past_trajectory)
ground_truth_x, ground_truth_y = zip(*ground_truth_trajectory)
predicted_x, predicted_y = zip(*predicted_trajectory)

# Plotting
fig, ax = plt.subplots()
ax.imshow(image)
ax.plot(past_x, past_y, '-o', color='blue', label='Past Trajectory')
ax.plot(ground_truth_x, ground_truth_y, '-o', color='green', label='Ground Truth')
ax.plot(predicted_x, predicted_y, '-o', color='red', label='Predicted Trajectory')

# Adding a legend
ax.legend()

# Remove axes and white space
ax.axis('off')  # Turn off the axes
plt.tight_layout(pad=0)  # Remove white space (adjust pad as needed)

# Show the plot
#plt.show()
plt.savefig('/Users/digital_drifting/Documents/sensor_test2/map/empty_intersection_traj.jpg', bbox_inches='tight', pad_inches=0)