import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips = [8, 12, 16, 20]
thumb_tip = 4

pointerDown = False
middleDown = False
ringDown = False
pinkyDown = False
thumbCrossed = False

def setLetter(x):
    cv2.putText(img, x, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    currentLetter = x

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    results = hands.process(img)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)

            x, y = int(lm_list[8].x * w), int(lm_list[8].y * h)
            print(x, y)

            # Determine shortcuts
            if lm_list[4].x < lm_list[2].x:
                thumbCrossed = True
            else:
                thumbCrossed = False
                
            if lm_list[8].y > lm_list[6].y:
                pointerDown = True
            else:
                pointerDown = False
            
            if lm_list[12].y > lm_list[10].y:
                middleDown = True
            else:
                middleDown = False

            if lm_list[16].y > lm_list[14].y:
                ringDown = True
            else:
                ringDown = False

            if lm_list[20].y > lm_list[18].y:
                pinkyDown = True
            else:
                pinkyDown = False


            # A
            if pointerDown == True and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == False \
                and lm_list[4].x > lm_list[5].x and lm_list[4].y < lm_list[7].y:
                setLetter("A")

            # B
            if pointerDown == False and middleDown == False and ringDown == False and pinkyDown == False and thumbCrossed == True:
                setLetter("B")

            # C
            elif pointerDown == True and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == False \
                    and lm_list[4].x > lm_list[2].x and lm_list[8].x > lm_list[6].x and lm_list[12].x > lm_list[10].x and \
                    lm_list[16].x > lm_list[14].x and lm_list[20].x > lm_list[18].x:
                setLetter("C")
            
            # D
            elif pointerDown == False and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == True \
                and lm_list[4].x >= lm_list[12].x:
                setLetter("D")

            # E
            elif pointerDown == True and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == True \
                and lm_list[4].x <= lm_list[20].x and lm_list[4].y > lm_list[18].y:
                setLetter("E")

            # F
            elif pointerDown == True and middleDown == False and ringDown == False and pinkyDown == False and thumbCrossed == True:
                setLetter("F")

            # G
            elif lm_list[8].x > lm_list[6].x and lm_list[12].x < lm_list[10].x and lm_list[16].x < lm_list[14].x and \
                lm_list[20].x < lm_list[18].x and lm_list[4].x > lm_list[2].x:
                setLetter("G")

            mp_draw.draw_landmarks(img, hand_landmark,
                                   mp_hands.HAND_CONNECTIONS,
                                   mp_draw.DrawingSpec((0, 0, 255), 6, 3),
                                   mp_draw.DrawingSpec((0, 255, 0), 4, 2)
                                   )

    cv2.imshow("Hand Sign Detection", img)
    cv2.waitKey(1)
