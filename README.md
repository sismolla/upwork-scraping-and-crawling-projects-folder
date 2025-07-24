📚 Bookscraper – OpenLibrary Trending Books Scraper
This project is a Python Scrapy spider that scrapes detailed information about trending books from OpenLibrary.org.
It extracts the title, author, rating, introduction, publish date, publisher, language, and number of pages for each book across multiple trending pages.

🚀 Features
Scrapes multiple paginated trending book pages

Follows individual book links to extract detailed data

Outputs clean structured data in JSON, CSV, or other Scrapy-supported formats

🛠 Built With
Python

Scrapy framework

CSS and XPath selectors for data extraction

📦 Installation
Clone the repository and navigate into the project folder:

bash
Copy
Edit
git clone https://github.com/sismolla/upwork-scraping-and-crawling-projects-folder.git
cd upwork-scraping-and-crawling-projects-folder
Install required dependencies:

bash
Copy
Edit
pip install scrapy
▶️ Usage
To run the spider and output data to a JSON file:

bash
Copy
Edit
scrapy crawl bookscraper -o books.json
You can also export to other formats like CSV:

bash
Copy
Edit
scrapy crawl bookscraper -o books.csv
📄 Project Structure
text
Copy
Edit
bookscraper/
├── bookscraper/            # Scrapy project folder
│   ├── spiders/
│   │   └── bookscraper.py  # The spider code
│   └── ...
├── scrapy.cfg
└── README.md
✏ How It Works
Starts from the OpenLibrary trending page

Follows pagination up to page 10

Visits each book’s detail page

Extracts and yields fields like:

Title

Author

Rating

Intro / description

Publish date

Publisher

Language

Number of pages

📌 License
This project is for educational and demo purposes.
