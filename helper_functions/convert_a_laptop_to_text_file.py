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

# Example JSON data
json_data = {
    "url": "https://www.flipkart.com/hp-255g9-amd-ryzen-3-dual-core-ryzen3-3250-8-gb-512-gb-ssd-windows-11-home-255-g8-notebook/p/itm77dde4dbe727e?pid=COMGFBK9A3Z2QD9H&lid=LSTCOMGFBK9A3Z2QD9HP2ST2L&marketplace=FLIPKART&fm=organic&iid=9cfa78d4-1307-46c0-8046-13de8d2e096b.COMGFBK9A3Z2QD9H.PRODUCTSUMMARY&ppt=pp&ppn=pp&ssid=bt5pv8zats0000001709727566595",
    "name": "HP 255 G9 AMD Ryzen 3 Dual Core AMD Ryzen3 3250 - (8 GB/512 GB SSD/Windows 11 Home) 255 G8 Notebook Notebook  (15.6 inch, Dark Ash, 1.78 kg)",
    "highlights": [
        "15.6 inch FHD SVA anti-glare WLED-backlit",
        "Light Laptop without Optical Disk Drive"
    ],
    "description": "HP 255 G8  62Y23PA (AMD Ryzen 3-3250U/ 8GB Ram/ 512 Gb SSD / 39.62 cm (15.6 inch) HD/Windows 11/AMD Radeon Vega 8 Graphics/ Dark Ash Silver/1.74Kg 1 Year Warranty",
    "features": [],
    "specifications": [
        {
            "category": "General",
            "properties": [
                {
                    "name": "Sales Package",
                    "content": "Laptop 1 ; Adapter 1 ; Power Cable 1"
                },
                {
                    "name": "Model Number",
                    "content": "255 G8 Notebook"
                },
                {
                    "name": "Part Number",
                    "content": "62y23pa"
                }
            ]
        },
        {
            "category": "Processor And Memory Features",
            "properties": [
                {
                    "name": "Processor Brand",
                    "content": "AMD"
                },
                {
                    "name": "Processor Name",
                    "content": "Ryzen 3 Dual Core"
                },
                {
                    "name": "SSD",
                    "content": "Yes"
                },
                {
                    "name": "SSD Capacity",
                    "content": "512 GB"
                }
            ]
        },
        {
            "category": "Operating System",
            "properties": [
                {
                    "name": "OS Architecture",
                    "content": "64 bit"
                },
                {
                    "name": "Operating System",
                    "content": "Windows 11 Home"
                },
                {
                    "name": "Supported Operating System",
                    "content": "Windows, Linux"
                },
                {
                    "name": "System Architecture",
                    "content": "64 bit"
                }
            ]
        }
    ],
    "ratings": {
        "Overall": "4.2",
        "Performance": "4.0",
        "Battery": "3.8",
        "Design": "4.2",
        "Display": "3.8",
        "Value for Money": "4.0"
    },
    "reviews": [
        {
            "rating": "1",
            "title": "Useless product",
            "content": "Issues coming after 15 days only regarding software",
            "writtenBy": "...",
            "numberOfLikes": "26",
            "numberOfDislikes": "6"
        },
        {
            "rating": "4",
            "title": "Delightful",
            "content": "Very useful product.",
            "writtenBy": "...",
            "numberOfLikes": "56",
            "numberOfDislikes": "19"
        }
    ],
    "customer_questions": [
        {
            "question": "Is this with md office",
            "answers": [
                {
                    "content": "NO",
                    "answeredBy": "...",
                    "answererRole": "Flipkart Seller",
                    "numberOfLikes": "15",
                    "numberOfDislikes": "7"
                }
            ]
        },
        {
            "question": "Can I use AutoCAD software?",
            "answers": [
                {
                    "content": "Yes",
                    "answeredBy": "...",
                    "answererRole": "Flipkart Seller",
                    "numberOfLikes": "4",
                    "numberOfDislikes": "2"
                }
            ]
        }
    ]
}

# Create a directory for laptops if it doesn't exist
laptops_directory = os.path.join(".", "laptops/laptop_text_files")
os.makedirs(laptops_directory, exist_ok=True)

# Create a directory with a unique ID inside the laptops directory
unique_id = "laptop_1"
laptop_directory = os.path.join(laptops_directory, unique_id)
os.makedirs(laptop_directory, exist_ok=True)

# Write product info to file
product_info_file = os.path.join(laptop_directory, "product_info.txt")
convert_product_info(json_data, product_info_file)

# Write reviews to file
reviews_file = os.path.join(laptop_directory, "reviews.txt")
convert_reviews_to_file(json_data["reviews"], reviews_file)

# Write customer questions to file
customer_questions_file = os.path.join(laptop_directory, "customer_questions.txt")
convert_customer_questions_to_file(json_data["customer_questions"], customer_questions_file)

# Print the path to the created directory
print("Laptop directory created at:", laptop_directory)