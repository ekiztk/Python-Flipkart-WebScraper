import os
import json

def convert_product_info(data, file_path):
    with open(file_path, 'w') as file:
        file.write("Product Name: {}\n".format(data["name"]))
        file.write("Description: {}\n".format(data["description"]))
        file.write("Highlights:\n")
        for highlight in data["highlights"]:
            file.write("- {}\n".format(highlight))
        file.write("\n")

        file.write("General Information:\n")
        for spec in data["specifications"]:
            file.write("- {}\n".format(spec["category"]))
            for prop in spec["properties"]:
                file.write("  {}: {}\n".format(prop["name"], prop["content"]))
            file.write("\n")

        file.write("Overall Ratings:\n")
        for key, value in data["ratings"].items():
            file.write("- {}: {}\n".format(key, value))

def convert_reviews_to_file(reviews, file_path):
    with open(file_path, 'w') as file:
        for review in reviews:
            file.write("Title: {}\n".format(review["title"]))
            file.write("Content: {}\n".format(review["content"]))
            file.write("Rating: {}\n".format(review["rating"]))
            file.write("Likes: {}\n".format(review["numberOfLikes"]))
            file.write("Dislikes: {}\n".format(review["numberOfDislikes"]))
            file.write("\n")

def convert_customer_questions_to_file(questions, file_path):
    with open(file_path, 'w') as file:
        for question in questions:
            file.write("Question: {}\n".format(question["question"]))
            for answer in question["answers"]:
                file.write("Answer: {}\n".format(answer["content"]))
                file.write("Likes: {}\n".format(answer["numberOfLikes"]))
                file.write("Dislikes: {}\n".format(answer["numberOfDislikes"]))
                file.write("\n")

# Opening JSON file
f = open(os.path.join(".", "laptops/laptop_details.json"))

# returns JSON object as 
# a dictionary
data = json.load(f)

# Closing file
f.close()

# Create a directory for laptops if it doesn't exist
laptops_directory = os.path.join(".", "laptops/laptop_text_files")
os.makedirs(laptops_directory, exist_ok=True)

# Example JSON data

index = 1
for laptop_json in data:
    # Create a directory with a unique ID inside the laptops directory
    unique_id = "laptop_" + index.__str__()
    laptop_directory = os.path.join(laptops_directory, unique_id)
    os.makedirs(laptop_directory, exist_ok=True)

    # Write product info to file
    product_info_file = os.path.join(laptop_directory, "product_info.txt")
    convert_product_info(laptop_json, product_info_file)

    # Write reviews to file
    reviews_file = os.path.join(laptop_directory, "reviews.txt")
    convert_reviews_to_file(laptop_json["reviews"], reviews_file)

    # Write customer questions to file
    customer_questions_file = os.path.join(laptop_directory, "customer_questions.txt")
    convert_customer_questions_to_file(laptop_json["customer_questions"], customer_questions_file)

    # Print the path to the created directory
    print("Laptop directory created at:", laptop_directory)
    index+=1
    pass


