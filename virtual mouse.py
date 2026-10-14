import cv2
import mediapipe as mp
import pyautogui
import math
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Screen dimensions
screen_w, screen_h = pyautogui.size()

# Variables for smoothing cursor movement
prev_x, prev_y = 0, 0
curr_x, curr_y = 0, 0

# Variables for click detection
click_threshold = 30
left_clicked = False
right_clicked = False

# Variables for zoom
zoom_threshold = 40
zoom_active = False
initial_distance = 0


def distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # If one hand detected - cursor movement and clicks
        if len(results.multi_hand_landmarks) == 1:
            hand_landmarks = results.multi_hand_landmarks[0]

            # Get index, thumb, and middle fingertips
            index_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]
            middle_tip = hand_landmarks.landmark[12]

            index_x, index_y = int(index_tip.x * frame.shape[1]), int(index_tip.y * frame.shape[0])
            thumb_x, thumb_y = int(thumb_tip.x * frame.shape[1]), int(thumb_tip.y * frame.shape[0])
            middle_x, middle_y = int(middle_tip.x * frame.shape[1]), int(middle_tip.y * frame.shape[0])

            # Draw circles
            cv2.circle(frame, (index_x, index_y), 10, (0, 255, 0), cv2.FILLED)
            cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(frame, (middle_x, middle_y), 10, (255, 0, 0), cv2.FILLED)

            # Move cursor based on index finger
            cursor_x = np.interp(index_x, (0, frame.shape[1]), (0, screen_w))
            cursor_y = np.interp(index_y, (0, frame.shape[0]), (0, screen_h))

            # Smooth cursor movement
            curr_x = prev_x + (cursor_x - prev_x) / 5
            curr_y = prev_y + (cursor_y - prev_y) / 5
            pyautogui.moveTo(screen_w - curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y

            # Left click (thumb & index pinch)
            thumb_index_dist = distance((thumb_x, thumb_y), (index_x, index_y))
            if thumb_index_dist < click_threshold:
                if not left_clicked:
                    pyautogui.click()
                    left_clicked = True
                    cv2.putText(frame, "Left Click", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                left_clicked = False

            # Right click (thumb & middle pinch)
            thumb_middle_dist = distance((thumb_x, thumb_y), (middle_x, middle_y))
            if thumb_middle_dist < click_threshold:
                if not right_clicked:
                    pyautogui.rightClick()
                    right_clicked = True
                    cv2.putText(frame, "Right Click", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                right_clicked = False

        # If two hands detected - zoom functionality
        elif len(results.multi_hand_landmarks) == 2:
            hand1 = results.multi_hand_landmarks[0]
            hand2 = results.multi_hand_landmarks[1]

            thumb1 = (int(hand1.landmark[4].x * frame.shape[1]), int(hand1.landmark[4].y * frame.shape[0]))
            index1 = (int(hand1.landmark[8].x * frame.shape[1]), int(hand1.landmark[8].y * frame.shape[0]))
            thumb2 = (int(hand2.landmark[4].x * frame.shape[1]), int(hand2.landmark[4].y * frame.shape[0]))
            index2 = (int(hand2.landmark[8].x * frame.shape[1]), int(hand2.landmark[8].y * frame.shape[0]))

            # Draw circles
            for pt in [thumb1, index1, thumb2, index2]:
                cv2.circle(frame, pt, 10, (0, 255, 0), cv2.FILLED)

            dist1 = distance(thumb1, index1)
            dist2 = distance(thumb2, index2)

            if dist1 < click_threshold and dist2 < click_threshold:
                if not zoom_active:
                    initial_distance = distance(thumb1, thumb2)
                    zoom_active = True
                else:
                    current_distance = distance(thumb1, thumb2)
                    if current_distance > initial_distance + zoom_threshold:
                        pyautogui.hotkey('ctrl', '+')
                        cv2.putText(frame, "Zoom In", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        initial_distance = current_distance
                    elif current_distance < initial_distance - zoom_threshold:
                        pyautogui.hotkey('ctrl', '-')
                        cv2.putText(frame, "Zoom Out", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        initial_distance = current_distance
            else:
                zoom_active = False

    # Display frame
    cv2.imshow("Virtual Mouse", frame)

    # Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
