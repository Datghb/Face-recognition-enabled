import face_recognition
import cv2
import pickle
from utils import save_face

def register():
    cam = cv2.VideoCapture(0)
    print("Đưa mặt vào camera...")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Đăng ký khuôn mặt - Nhấn 's' để lưu", frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            face_locations = face_recognition.face_locations(frame)
            if face_locations:
                face_encoding = face_recognition.face_encodings(frame, face_locations)[0]
                save_face(face_encoding)
                print("✅ Khuôn mặt đã được lưu!")
            else:
                print("❌ Không tìm thấy khuôn mặt. Thử lại.")
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    register()
