import os
import json

def convert_laptop_to_string(data):
    laptop_info = "Product Name: {}".format(data["name"])
    laptop_info += " Description: {}".format(data["description"])
    laptop_info += " Highlights:"
    for highlight in data["highlights"]:
        laptop_info += " - {}".format(highlight)

    laptop_info += "start of General Information:"
    for spec in data["specifications"]:
        laptop_info += " - {}".format(spec["category"])
        for prop in spec["properties"]:
            laptop_info += " {}: {}".format(prop["name"], prop["content"])
    laptop_info += "end of General Information:"

    laptop_info += "start of Overall Ratings:"
    for key, value in data["ratings"].items():
        laptop_info += " - {}: {}".format(key, value)
    laptop_info += "end of Overall Ratings:"

    laptop_info += "start of Reviews:"
    for review in data["reviews"]:
        laptop_info += "-start of a review-"
        laptop_info += " Title: {}".format(review["title"])
        laptop_info += " Content: {}".format(review["content"])
        laptop_info += " Rating: {}".format(review["rating"])
        laptop_info += " Likes: {}".format(review["numberOfLikes"])
        laptop_info += " Dislikes: {}".format(review["numberOfDislikes"])
        laptop_info += "-end of a review-"
    laptop_info += "end of Reviews:"

    laptop_info += "start of Customer Questions:"
    for question in data["customer_questions"]:
        laptop_info += "-start of a customer question-"
        laptop_info += " Question: {}".format(question["question"])
        for answer in question["answers"]:
            laptop_info += " Answer: {}".format(answer["content"])
            laptop_info += " Likes: {}".format(answer["numberOfLikes"])
            laptop_info += " Dislikes: {}".format(answer["numberOfDislikes"])
        laptop_info += "-end of a customer question-"
    laptop_info += "end of Customer Questions:"
    
    return laptop_info

# Opening JSON file
f = open(os.path.join(".", "laptops/laptop_details.json"))

# returns JSON object as 
# a dictionary
data = json.load(f)

# Closing file
f.close()

# Create a directory for laptops if it doesn't exist
laptops_directory = os.path.join(".", "laptops")
os.makedirs(laptops_directory, exist_ok=True)

# Example JSON data
laptop_data_list = []
for laptop_json in data:
    # Create a dictionary with all the laptop info
    laptop_dict = {}
    laptop_dict["text"] = convert_laptop_to_string(laptop_json)

    # Add the laptop dictionary to the list
    laptop_data_list.append(laptop_dict)

# Write the list of laptop dictionaries to a JSON file
with open(os.path.join(laptops_directory, "laptop_text_data.json"), 'w') as json_file:
    json.dump(laptop_data_list, json_file, indent=4)

print("Laptop data written to JSON file.")
