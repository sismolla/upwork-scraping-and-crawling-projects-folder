# 📚 Bookscraper – OpenLibrary Trending Books Scraper

A Python Scrapy spider that collects detailed information about trending books from [OpenLibrary.org](https://openlibrary.org).  
This scraper extracts data like title, author, rating, description, publish date, and more — perfect for data analysis, research, or building datasets.

---

## ✨ Features
- ✅ Scrapes trending books across multiple paginated pages
- ✅ Visits individual book pages for detailed data
- ✅ Outputs structured data to JSON, CSV, or other formats supported by Scrapy
- ✅ Clean and easy-to-read spider structure

---

## 🛠 Built With
- **Python 3**
- **Scrapy framework**
- CSS & XPath selectors for robust data extraction

---

## 📦 Installation

Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/sismolla/upwork-scraping-and-crawling-projects-folder.git
cd upwork-scraping-and-crawling-projects-folder
Install dependencies:

bash
Copy
Edit
pip install scrapy
▶️ Usage
Run the spider and save output to JSON:

bash
Copy
Edit
scrapy crawl bookscraper -o books.json
Or save to CSV:

bash
Copy
Edit
scrapy crawl bookscraper -o books.csv
Tip: Scrapy supports other formats too (e.g., XML, JL).

📄 Project Structure
plaintext
Copy
Edit
upwork-scraping-and-crawling-projects-folder/
├── bookscraper/                # Scrapy project folder
│   ├── spiders/
│   │   └── bookscraper.py      # The spider code
│   └── ...
├── scrapy.cfg
└── README.md
📊 What the Spider Scrapes
For each trending book, the spider collects:

Title

Author

Rating

Introduction / description

Publish date

Publisher

Language

Number of pages

📌 License
This project is intended for educational and demo purposes.

📷 Example Output (JSON)
json
Copy
Edit
{
  "title": "Example Book Title",
  "author": "Author Name",
  "rating": "4.2",
  "intro": "Short book description...",
  "publish_date": "2015",
  "publisher": "Publisher Name",
  "language": "English",
  "pages": "320"
}
🤝 Contributing
Pull requests and suggestions are welcome!
Feel free to fork the repo and submit improvements.

Developed by sismolla | 🌐 OpenLibrary.org

yaml
Copy
Edit

---









Ask ChatGPT
