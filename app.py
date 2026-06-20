from flask import Flask, render_template, request
from ultralytics import YOLO
from collections import Counter
import os
import shutil

app = Flask(__name__, static_folder="static")
print(os.getcwd())

model = YOLO("yolov8n.pt")


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        file = request.files["image"]

        filepath = os.path.join("uploads", file.filename)
        os.makedirs("uploads", exist_ok=True)

        file.save(filepath)

        original_path = "static/original.jpg"
        shutil.copy(filepath, original_path)

        results = model(filepath)

        results[0].save(filename="static/result.jpg")

        #to get ids to names
        class_ids=results[0].boxes.cls.tolist()
        #convert class_id to name
        names=[results[0].names[int (i)] for i in class_ids]
        #count object
        object_count=Counter(names)

        output_path = "result.jpg"

        return render_template("index.html", output="result.jpg",original="original.jpg",objects=object_count)

    return render_template("index.html", output=None,original=None,objects=None)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)