from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2


def beach_images_filter(image_name):
    np.set_printoptions(suppress=True)
    model = load_model("models/beach_model/keras_Model.h5", compile=False)
    class_names = open("models/beach_model/labels.txt", "r").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_name).convert("RGB")

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.LANCZOS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return confidence_score, class_name[2:-1]


def indoor_images_filter(image_name):
    np.set_printoptions(suppress=True)
    model = load_model("models/indoor_model/keras_Model.h5", compile=False)
    class_names = open("models/indoor_model/labels.txt", "r").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_name).convert("RGB")

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.LANCZOS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return confidence_score, class_name[2:-1]


def seasons_filter(image_name):
    np.set_printoptions(suppress=True)
    model = load_model("models/seasons_model/keras_model.h5", compile=False)
    class_names = open("models/seasons_model/labels.txt", "r").readlines()

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_name).convert("RGB")

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.LANCZOS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return confidence_score, class_name[2:-1]


def glasses_filter(image_name):
    np.set_printoptions(suppress=True)
    model = load_model("models/glasses_model/keras_model.h5", compile=False)
    class_names = open("models/glasses_model/labels.txt", "r").readlines()

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_name).convert("RGB")

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.LANCZOS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return confidence_score, class_name[2:-1]


def face_detection(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, width, height) in faces:
        cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 3)

    if isinstance(faces, tuple):
        return img, False
    else:
        return img, faces.size>0,


def show_image(image):
    cv2.imshow("Faces Detected", image)
    cv2.waitKey(0)


def classify_given_image(image):
    is_winter = True if seasons_filter(image)[1] == 'Zima' else False
    is_beach = True if beach_images_filter(image)[1] == 'beach' else False
    is_indoor = True if indoor_images_filter(image)[1] == 'indoor_photo' else False
    contains_glasses = True if glasses_filter(image)[1] == 'Z okularami' else False
    has_faces = face_detection(image)[1]
    image_classification = {'isWinter': is_winter, 'isBeach': is_beach, 'isIndoor': is_indoor, 'hasFaced': has_faces, 'glasses': contains_glasses}

    return image_classification

if __name__ == "__main__":
    print(classify_given_image("baza/10011-07.jpg"))
    show_image(face_detection("resources/test_photos/beach_people.png")[0])
