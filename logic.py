LIFE_STAGES = [
    ("Puppy", "1"),
    ("Adult", "2"),
    ("Senior", "3")
]

def calculate_dog_years(human_years):
    return human_years * 7


def determine_life_stage_from_radio(selection):
    stage = "Unknown"

    for name, value in LIFE_STAGES:
        if selection == value:
            stage = name

    return stage


def validate_inputs(owner, dog_name, dog_age_text, selection):
    owner = owner.strip()
    dog_name = dog_name.strip()

    if owner == "" or dog_name == "":
        return False, "Please complete the owner name and dog name fields.", None

    try:
        dog_age = int(dog_age_text)
    except ValueError:
        return False, "Enter a valid whole number for the dog's age.", None

    if dog_age < 0:
        return False, "Dog age cannot be negative.", None

    if selection == "":
        return False, "Please select a life stage.", None

    return True, "", dog_age


def process_information(owner, dog_name, dog_age, selection):
    dog_years = calculate_dog_years(dog_age)
    stage = determine_life_stage_from_radio(selection)

    return {
        "owner": owner,
        "dog_name": dog_name,
        "dog_age": dog_age,
        "dog_years": dog_years,
        "life_stage": stage
    }
