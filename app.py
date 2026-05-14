from flask import Flask, render_template, request
from logic import LIFE_STAGES, validate_inputs, process_information

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    error_message = ""
    result = None

    form_data = {
        "owner": "",
        "dog_name": "",
        "dog_age": "",
        "life_stage": ""
    }

    if request.method == "POST":
        form_data["owner"] = request.form.get("owner", "")
        form_data["dog_name"] = request.form.get("dog_name", "")
        form_data["dog_age"] = request.form.get("dog_age", "")
        form_data["life_stage"] = request.form.get("life_stage", "")

        is_valid, message, dog_age = validate_inputs(
            form_data["owner"],
            form_data["dog_name"],
            form_data["dog_age"],
            form_data["life_stage"]
        )

        if not is_valid:
            error_message = message
        else:
            result = process_information(
                form_data["owner"].strip(),
                form_data["dog_name"].strip(),
                dog_age,
                form_data["life_stage"]
            )

    return render_template(
        "index.html",
        life_stages=LIFE_STAGES,
        error_message=error_message,
        result=result,
        form_data=form_data
    )

if __name__ == "__main__":
    app.run(debug=True)