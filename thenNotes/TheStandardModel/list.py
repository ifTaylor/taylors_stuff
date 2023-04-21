from flask import Flask, request, render_template
from flask_cors import CORS
...
app = Flask(__name__)
CORS(app)
...

# Set the path to the file where the list items will be stored
data_file = "./list.txt"

@app.route("/get_items", methods=["GET"])
def get_items():
    with open(data_file, "r") as file:
        items = file.read()
    return items

@app.route("/add_item", methods=["POST"])
def add_item():
    # Get the new item text from the request data
    data = request.get_json()
    text = data.get("text")
    
    # Check if the text is None
    if text is None:
        return "No text provided!"
    
    # Open the file in append mode and write the new item to it
    with open(data_file, "a") as file:
        file.write(text + "\n")

    # Return a success message
    return "Item added to list!"


if __name__ == "__main__":
    app.run()
