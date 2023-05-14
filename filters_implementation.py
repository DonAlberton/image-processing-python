from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2


def beach_images_filter(image_name):
    np.set_printoptions(suppress=True)
    model = load_model("beach_model/keras_Model.h5", compile=False)
    class_names = open("beach_model/labels.txt", "r").readlines()
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
    model = load_model("indoor_model/keras_Model.h5", compile=False)
    class_names = open("indoor_model/labels.txt", "r").readlines()
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
    model = load_model("seasons_model/keras_model.h5", compile=False)
    class_names = open("seasons_model/labels.txt", "r").readlines()

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

    has_faces = False
    if faces.size>0:
        has_faces = True

    return img, has_faces



#indoor_images_filter("resources/test_photos/indoor_photo.jpg")
#indoor_images_filter("resources/test_photos/Mountain-Valid.jpeg")
#beach_images_filter("resources/test_photos/beach_1.jpg")
#beach_images_filter("resources/test_photos/desert.jpeg")
#seasons_filter("resources/test_photos/test-zima.jpg")

def classify_given_image(image):
    is_winter = True if seasons_filter(image)[1] == 'zima' else False
    is_beach = True if beach_images_filter(image)[1] == 'beach' else False
    is_indoor = True if indoor_images_filter(image)[1] == 'indoor_photo' else False
    has_faces = face_detection(image)[1]
    image_classification = {'isWinter': is_winter, 'isBeach': is_beach, 'isIndoor': is_indoor, 'hasFaced': has_faces}

    return image_classification

if __name__ == "__main__":
    #print(classify_given_image("resources/test_photos/test-zima.jpg"))
    #face_detection("resources/test_photos/test-zima.jpg")
    print(classify_given_image("resources/test_photos/beach_people.png"))
