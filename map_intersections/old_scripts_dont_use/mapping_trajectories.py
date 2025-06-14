import cv2


street_image_path = '/Users/digital_drifting/Documents/sensor_test2/map/empty_intersection.jpg' 
street_image = cv2.imread(street_image_path)

# Example trajectories
past_trajectory = [(50, 100), (55, 115), (60, 130)]
ground_truth_trajectory = [(60, 130), (65, 145), (70, 160)]
predicted_trajectory = [(70, 160), (75, 175), (80, 190)]


# Draw trajectories on the image
for i in range(len(past_trajectory)-1):
    cv2.line(street_image, past_trajectory[i], past_trajectory[i+1], (255, 0, 0), 2)  # Blue for past trajectory

for i in range(len(ground_truth_trajectory)-1):
    cv2.line(street_image, ground_truth_trajectory[i], ground_truth_trajectory[i+1], (0, 255, 0), 2)  # Green for ground truth

for i in range(len(predicted_trajectory)-1):
    cv2.line(street_image, predicted_trajectory[i], predicted_trajectory[i+1], (0, 0, 255), 2)  # Red for predicted trajectory

# Add a key to the image
cv2.putText(street_image, 'Past Trajectory', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 2)
cv2.putText(street_image, 'Ground Truth', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 255, 0), 2)
cv2.putText(street_image, 'Predicted Trajectory', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 0, 255), 2)

# Display the image with trajectories
cv2.imshow('Street with Trajectories', street_image)
cv2.waitKey(0)  # Wait for a key press to close
cv2.destroyAllWindows()

# Or save the image to a file
cv2.imwrite('street_with_trajectories.jpeg', street_image)