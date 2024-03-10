# Python-Flipkart-WebScraper
Flipkart website scraper for 2024.
<h3>İf you like it please give it a ⭐.</h3>

<h2>Required Python Libraries:</h2>
<ul>
  <li>BeautifulSoup</li>
  
      pip install beautifulsoup4
</ul>
<ul>
  <li>Pandas</li>
  
      pip install pandas
</ul>
<ul>
  <li>Selenium</li>
  
      pip install selenium
</ul>
<ul>
  <li>Webdriver-manager</li>
  
     0 pip install webdriver-manager
</ul>

<h2>Products:</h2>
    <h3>1. Laptops:</h3>
        <ul>
            <li>Stores urls of laptops in laptop_urls.csv.</li>
            <li>Stores data of laptops in laptop_details.json.</li>
        </ul>
        <h4>Structure</h4>
        <pre lang="python">
        class Laptop:
            def __init__(self,url, name, highlights, features,specifications,ratings,reviews,customer_questions):
                self.url = url
                self.name = name
                self.highlights = highlights
                self.features = features
                self.specifications = specifications
                self.ratings = ratings
                self.reviews = reviews
                self.reviews = reviews
                self.customer_questions = customer_questions
        </pre>
        <h4>Sample Output</h4>
        <pre lang="json">[
    {
        "url":"https://www.flipkart.com/hp-255g9-amd-ryzen-3-dual-core-ryzen3-3250-8-gb-512-gb-ssd-windows-11-home-255-g8-notebook/p/itm77dde4dbe727e?pid=COMGFBK9A3Z2QD9H&lid=LSTCOMGFBK9A3Z2QD9HP2ST2L&marketplace=FLIPKART&fm=organic&iid=9cfa78d4-1307-46c0-8046-13de8d2e096b.COMGFBK9A3Z2QD9H.PRODUCTSUMMARY&ppt=pp&ppn=pp&ssid=bt5pv8zats0000001709727566595",
        "name":"HP 255 G9 AMD Ryzen 3 Dual Core AMD Ryzen3 3250 - (8 GB/512 GB SSD/Windows 11 Home) 255 G8 Notebook Notebook  (15.6 inch, Dark Ash, 1.78 kg)",
        "highlights":[
            "15.6 inch FHD SVA anti-glare WLED-backlit",
            "Light Laptop without Optical Disk Drive"
        ],
        "description":"HP 255 G8  62Y23PA (AMD Ryzen 3-3250U/ 8GB Ram/ 512 Gb SSD / 39.62 cm (15.6 inch) HD/Windows 11/AMD Radeon Vega 8 Graphics/ Dark Ash Silver/1.74Kg 1 Year Warranty",
        "features":[],
        "specifications":[
            {
                "category":"General",
                "properties":[
                    {
                        "name":"Sales Package",
                        "content":"Laptop 1 ; Adapter 1 ; Power Cable 1"
                    },
                    {
                        "name":"Model Number",
                        "content":"255 G8 Notebook"
                    },
                    {
                        "name":"Part Number",
                        "content":"62y23pa"
                    },
                    ...
                ]
            },
            {
                "category":"Processor And Memory Features",
                "properties":[
                    {
                        "name":"Processor Brand",
                        "content":"AMD"
                    },
                    {
                        "name":"Processor Name",
                        "content":"Ryzen 3 Dual Core"
                    },
                    {
                        "name":"SSD",
                        "content":"Yes"
                    },
                    {
                        "name":"SSD Capacity",
                        "content":"512 GB"
                    },
                    ...
                ]
            },
            {
                "category":"Operating System",
                "properties":[
                    {
                        "name":"OS Architecture",
                        "content":"64 bit"
                    },
                    {
                        "name":"Operating System",
                        "content":"Windows 11 Home"
                    },
                    {
                        "name":"Supported Operating System",
                        "content":"Windows, Linux"
                    },
                    {
                        "name":"System Architecture",
                        "content":"64 bit"
                    }
                ]
            },
            {
                "category":"Port And Slot Features",
                "properties":[
                    {
                        "name":"S-video",
                        "content":"No"
                    },
                    {
                        "name":"Dock Port",
                        "content":"Yes"
                    },
                    {
                        "name":"Firewire Port",
                        "content":"No"
                    },
                    {
                        "name":"RJ11",
                        "content":"No"
                    },
                    {
                        "name":"Mic In",
                        "content":"Yes"
                    },
                    ...
                ]
            },
            {
                "category":"Display And Audio Features",
                "properties":[
                    {
                        "name":"Touchscreen",
                        "content":"No"
                    },
                    ...
                ]
            },
            {
                "category":"Connectivity Features",
                "properties":[
                    {
                        "name":"Wireless LAN",
                        "content":"Realtek RTL8822CE 802.11a/b/g/n/ac (2x2) Wi-Fi® with Bluetooth® 5 Combo"
                    },
                    {
                        "name":"Bluetooth",
                        "content":"Yes"
                    },
                    ...
                ]
            },
            {
                "category":"Dimensions",
                "properties":[
                    {
                        "name":"Dimensions",
                        "content":"37.6 x 24.6 x 2.25 cm"
                    },
                    {
                        "name":"Weight",
                        "content":"1.78 kg"
                    }
                ]
            },
            {
                "category":"Additional Features",
                "properties":[
                    {
                        "name":"Disk Drive",
                        "content":"Not Available"
                    },
                    {
                        "name":"Web Camera",
                        "content":"Yes"
                    },
                    ...
                ]
            },
            {
                "category":"Warranty",
                "properties":[
                    {
                        "name":"Warranty Summary",
                        "content":"1 Year"
                    },
                    {
                        "name":"Warranty Service Type",
                        "content":"On Site Warranty"
                    },
                    {
                        "name":"Covered in Warranty",
                        "content":"Hardware for 1 Year"
                    },
                    {
                        "name":"Not Covered in Warranty",
                        "content":"Physical Damage"
                    },
                    {
                        "name":"Domestic Warranty",
                        "content":"1 Year"
                    },
                    {
                        "name":"International Warranty",
                        "content":"0 Months"
                    }
                ]
            }
        ],
        "ratings":{
            "Overall":"4.2",
            "Performance":"4.0",
            "Battery":"3.8",
            "Design":"4.2",
            "Display":"3.8",
            "Value for Money":"4.0"
        },
        "reviews":[
            {
                "rating":"1",
                "title":"Useless product",
                "content":"Issues coming after 15 days only regarding software",
                "writtenBy":"...",
                "numberOfLikes":"26",
                "numberOfDislikes":"6"
            },
            {
                "rating":"4",
                "title":"Delightful",
                "content":"Very useful product.",
                "writtenBy":"...",
                "numberOfLikes":"56",
                "numberOfDislikes":"19"
            },
            ...
        ],
        "customer_questions":[
            {
                "question":"Is this with md office",
                "answers":[
                    {
                        "content":"NO",
                        "answeredBy":"...",
                        "answererRole":"Flipkart Seller",
                        "numberOfLikes":"15",
                        "numberOfDislikes":"7"
                    }
                ]
            },
            {
                "question":"Can I use AutoCAD software?",
                "answers":[
                    {
                        "content":"Yes",
                        "answeredBy":"...",
                        "answererRole":"Flipkart Seller",
                        "numberOfLikes":"4",
                        "numberOfDislikes":"2"
                    },
                    ...
                ]
            },
        ]
        ...
    }
]</pre>

