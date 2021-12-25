import qrcode
import cv2

#trying out the git add/status function

in1 = input("Enter a URL ")
in2 = input("Give it a name ")
img = qrcode.make(in1)
x = img.save(str(in2)+".jpg")

d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread(str(in2)+".jpg"))
print("the link is " + val + ".")
