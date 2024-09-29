import os
import json

def convert_all_to_file(data, file_path):
    with open(file_path, 'w', encoding="utf-8") as file:
        for laptop_json in data:
            file.write("Product Name: {}\n".format(laptop_json["name"]))
            file.write("Description: {}\n".format(laptop_json["description"]))
            file.write("Highlights:\n")
            for highlight in laptop_json["highlights"]:
                file.write("- {}\n".format(highlight))
            file.write("\n")

            file.write("General Information:\n")
            for spec in laptop_json["specifications"]:
                file.write("- {}\n".format(spec["category"]))
                for prop in spec["properties"]:
                    file.write("  {}: {}\n".format(prop["name"], prop["content"]))
                file.write("\n")

            file.write("Overall Ratings:\n")
            for key, value in laptop_json["ratings"].items():
                file.write("- {}: {}\n".format(key, value))
            
            file.write("\nReviews:\n")
            for review in laptop_json["reviews"]:
                file.write("Title: {}\n".format(review["title"]))
                file.write("Content: {}\n".format(review["content"]))
                file.write("Rating: {}\n".format(review["rating"]))
                file.write("Likes: {}\n".format(review["numberOfLikes"]))
                file.write("Dislikes: {}\n".format(review["numberOfDislikes"]))
                file.write("\n")
            
            file.write("\nCustomer Questions:\n")
            for question in laptop_json["customer_questions"]:
                file.write("Question: {}\n".format(question["question"]))
                for answer in question["answers"]:
                    file.write("Answer: {}\n".format(answer["content"]))
                    file.write("Likes: {}\n".format(answer["numberOfLikes"]))
                    file.write("Dislikes: {}\n".format(answer["numberOfDislikes"]))
                    file.write("\n")
            
            file.write("\n\n")

def read_text_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        return file.read()

# Opening JSON file
f = open(os.path.join(".", "laptops/laptop_details.json"),encoding="utf-8")

# returns JSON object as 
# a dictionary
data = json.load(f)

# Closing file
f.close()

# Create a directory for laptops if it doesn't exist
laptops_directory = os.path.join(".", "laptops/laptop_text_files")
os.makedirs(laptops_directory, exist_ok=True)

# Write each laptop's information to separate files
index = 1
for laptop_json in data:
    # Create a directory with a unique ID inside the laptops directory
    unique_id = "laptop_" + str(index)
    laptop_directory = os.path.join(laptops_directory, unique_id)
    os.makedirs(laptop_directory, exist_ok=True)

    # Write all information to a single file for this laptop
    laptop_info_file = os.path.join(laptop_directory, "laptop_info.txt")
    convert_all_to_file([laptop_json], laptop_info_file)

    print("Laptop information has been written to:", laptop_info_file)

    # Read the text file and save its content as a JSON object
    text_content = read_text_file(laptop_info_file)
    json_content = {"text": text_content}

    # Write the JSON object to a JSON file
    json_file_path = os.path.join(laptops_directory, "laptop_text_data.json")
    with open(json_file_path, 'w', encoding="utf-8") as json_file:
        json.dump(json_content, json_file, ensure_ascii=False, indent=4)

    print("Laptop information has been written to:", json_file_path)
    index += 1

print("All laptop information has been written to separate files in:", laptops_directory)