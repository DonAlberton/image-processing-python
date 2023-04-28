from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
def seasons_filter(image_name):
    np.set_printoptions(suppress=True)
    model = load_model("seasons_model/keras_Model.h5", compile=False)
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

    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)
    return confidence_score



seasons_filter("resources/test_photos/test-zima.jpg")
seasons_filter("resources/test_photos/test-lato.jpg")
seasons_filter("resources/test_photos/test-jesien.jpg")

