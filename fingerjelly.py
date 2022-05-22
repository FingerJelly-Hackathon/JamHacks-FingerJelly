# ==== SETUP ====
import cv2
import mediapipe as mp
from tkinter import *
from PIL import Image, ImageTk

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

# Base variables for UI
points = 0 
lives = 3 
xShift = 0

# Default vector positions
pointerDown = False
middleDown = False
ringDown = False
pinkyDown = False
thumbCrossed = False

root = Tk()
s = Canvas(root)
imag = s.create_image(0,0,image = None)


# ==== IDENTIFIES ASL FINGERSPELLING ALPHABET ====
def aslRecognition():
    def setLetter(x):
        cv2.putText(img, x, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3) # Provides translation immediately on webcam
        currentLetter = x   # Compares with falling fruit

    while True:
        ret, img = cap.read()
        if ret:
            photo = ImageTk.PhotoImage(image = Image.fromarray(img))
            s.imgtk = photo
            s.itemconfig(img,image = photo)
        img = cv2.flip(img, 1)
        h, w, c = img.shape
        results = hands.process(img)

        if results.multi_hand_landmarks: 
            for hand_landmark in results.multi_hand_landmarks:
                lm_list = []
                for id, lm in enumerate(hand_landmark.landmark):
                    lm_list.append(lm)

                x, y = int(lm_list[8].x * w), int(lm_list[8].y * h)
                # print(x, y)

                # Defines shortcuts for hand positions
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

                # "Neutral hand"
                if pointerDown == False and middleDown == False and ringDown == False and pinkyDown == False and thumbCrossed == False:
                    setLetter("...")

                # A
                elif pointerDown == True and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == False \
                    and lm_list[4].x > lm_list[5].x and lm_list[4].y < lm_list[7].y:
                    setLetter("A")

                # B
                if pointerDown == False and middleDown == False and ringDown == False and pinkyDown == False and thumbCrossed == True:
                    setLetter("B")

                # C
                elif pointerDown == True and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == False \
                    and lm_list[4].x > lm_list[2].x and lm_list[8].x > lm_list[6].x and lm_list[12].x > lm_list[10].x and \
                    lm_list[16].x > lm_list[14].x and lm_list[20].x > lm_list[18].x and lm_list[4].y > lm_list[12].y:
                    setLetter("C")
                
                # D
                elif pointerDown == False and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == True \
                    and lm_list[4].x >= lm_list[12].x and lm_list[8].x > lm_list[0].x:
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
                    lm_list[20].x < lm_list[18].x and lm_list[4].x > lm_list[2].x and lm_list[0].x < lm_list[17].x and \
                    lm_list[0].x < lm_list[5].x and lm_list[5].y < lm_list[17].y and lm_list[4].y < lm_list[0].y:
                    setLetter("G")
                
                # H
                elif lm_list[8].x > lm_list[6].x and lm_list[12].x > lm_list[10].x and lm_list[16].x < lm_list[14].x and \
                    lm_list[20].x < lm_list[18].x and lm_list[4].x > lm_list[2].x and lm_list[0].x < lm_list[17].x and \
                    lm_list[0].x < lm_list[5].x and lm_list[5].y < lm_list[17].y and lm_list[4].y < lm_list[17].y:
                    setLetter("H")
                    

                # I
                elif pointerDown == True and middleDown == True and ringDown == True and pinkyDown == False and thumbCrossed == True \
                    and lm_list[0].x < lm_list[10].x:
                    setLetter("I")
                
                # J
                elif pointerDown == True and middleDown == True and ringDown == True and pinkyDown == False and thumbCrossed == True:
                    setLetter("J")
                
                #K 
                elif pointerDown == False and middleDown == False and ringDown == True and pinkyDown == True and thumbCrossed == True \
                    and lm_list[4].x > lm_list[10].x:
                    setLetter("K")

                # L
                elif pointerDown == False and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == False:
                    setLetter("L")
                
                # M
                elif pointerDown == True and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == True \
                    and lm_list[4].x < lm_list[14].x and lm_list[4].y < lm_list[18].y:
                    setLetter("M")

                # N
                elif pointerDown == True and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == True \
                    and lm_list[4].x < lm_list[12].x and lm_list[4].y < lm_list[14].y:
                    setLetter("N")

                # O
                elif pointerDown == True and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == False \
                    and lm_list[4].x > lm_list[2].x and lm_list[8].x > lm_list[6].x and lm_list[12].x > lm_list[10].x and \
                    lm_list[16].x > lm_list[14].x and lm_list[20].x > lm_list[18].x and lm_list[4].y < lm_list[12].y:
                    setLetter("O")

                # P
                elif pointerDown == True and middleDown == True and ringDown == False and pinkyDown == False and thumbCrossed == False \
                    and lm_list[4].x > lm_list[10].x and lm_list[0].x < lm_list[5].x:
                    setLetter("P")

                # Q
                elif pointerDown == True and middleDown == False and ringDown == False and pinkyDown == False and thumbCrossed == False \
                    and lm_list[4].x > lm_list[10].x and lm_list[0].x < lm_list[5].x:
                    setLetter("Q")

                # R
                elif pointerDown == False and middleDown == False and ringDown == True and pinkyDown == True and thumbCrossed == True \
                    and lm_list[8].x < lm_list[12].x:
                    setLetter("R")

                # S
                elif pointerDown == True and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == True \
                    and lm_list[4].y > lm_list[14].y and lm_list[4].x < lm_list[16].x:
                    setLetter("S")

                # T
                elif pointerDown == True and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == True \
                    and lm_list[4].y < lm_list[7].y:
                    setLetter("T")

                # U
                elif pointerDown == False and middleDown == False and ringDown == True and pinkyDown == True and thumbCrossed == True \
                    and lm_list[8].x < lm_list[1].x:
                    setLetter("U")

                # V
                elif pointerDown == False and middleDown == False and ringDown == True and pinkyDown == True and thumbCrossed == True \
                    and lm_list[8].x > lm_list[1].x:
                    setLetter("V")
                
                # W
                elif pointerDown == False and middleDown == False and ringDown == False and pinkyDown == True and thumbCrossed == True:
                    setLetter("W")

                # X
                elif pointerDown == False and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == True \
                    and lm_list[8].y > lm_list[7].y:
                    setLetter("X")

                # Y
                elif pointerDown == True and middleDown == True and ringDown == True and pinkyDown == False and thumbCrossed == False:
                    setLetter("Y")

                # Z
                elif pointerDown == False and middleDown == True and ringDown == True and pinkyDown == True and thumbCrossed == True \
                    and lm_list[4].x >= lm_list[12].x and lm_list[8].x < lm_list[0].x:
                    setLetter("Z")


                # Draws mesh on hand
                mp_draw.draw_landmarks(img, hand_landmark,
                                    mp_hands.HAND_CONNECTIONS,
                                    mp_draw.DrawingSpec((0, 0, 255), 6, 3),
                                    mp_draw.DrawingSpec((0, 255, 0), 4, 2)
                                    )

        s.update()
        cv2.imshow("Hand Sign Detection", img)
        cv2.waitKey(1)


# ==== DRAW GUI ELEMENTS ====
root.after(0,aslRecognition)
s.pack()
s.focus_set()

# Background
s.configure(bg="MediumPurple1")
s.create_rectangle(340,0, 390,270, fill="MediumPurple4", outline="MediumPurple4")
s.create_polygon(341,-20, 340,-20, 330,10, 320,40, 330,70, 340,100, 330,130, 320,160, 330,190, 340,220, 330,250, 340,280, 341,280, fill="MediumPurple4", smooth=1)

# Points
s.create_text(370, 10, text=str(points), fill="white", justify='right')

# Lives
for i in range(lives):
    s.create_oval(375-xShift, 30, 365-xShift, 20, fill="white", outline = "white")
    xShift += 15

# Current translation
#s.create_text()

root.mainloop()