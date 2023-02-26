import cv2

# Iterate over camera indices until no camera is found
index = 0
while True:
    # Create a VideoCapture object for the current index
    cap = cv2.VideoCapture(index)

    # Check if the camera is available
    if not cap.read()[0]:
        break

    # Release the VideoCapture object
    cap.release()

    # Print the index of the available camera
    print('Camera with index {} is available'.format(index))

    # Increment the index to check the next camera
    index += 1
