import scrapy

class BookscraperSpider(scrapy.Spider):
    name = "bookscraper"
    allowed_domains = ["openlibrary.org"]
    start_urls = ["https://openlibrary.org/trending/now"]

    def parse(self, response):
        yield from self.parse_list_page(response)

        for i in range(2, 11):
            next_page = f'https://openlibrary.org/trending/now?page={i}'
            yield scrapy.Request(url=next_page, callback=self.parse_list_page)

    def parse_list_page(self, response):
        for book in response.css('ul.list-books li.searchResultItem'):
            next_url = book.css('span a::attr(href)').get()
            if next_url:
                url = 'https://openlibrary.org' + next_url
                yield scrapy.Request(url, callback=self.parse_book)

    def parse_book(self, response):
        pub = response.css('div.edition-omniline div.edition-omniline-item span::text').getall()
        links = response.css('div.edition-omniline div.edition-omniline-item span a::text').getall()

        yield {
            'title': response.css('h1.work-title::text').get(default=''),
            'author': response.css('h2.edition-byline a::text').get(default=''),
            'rating': response.xpath('//*[@id="contentBody"]/div[1]/div[3]/div[2]/span/ul/li[1]/span[5]/text()').get(default=''),
            'intro': response.css('div.read-more__content p::text').get(default=''),
            'publish_date': pub[0] if len(pub) > 0 else '',
            'publisher': links[0] if len(links) > 0 else '',
            'language': links[1] if len(links) > 1 else '',
            'pages': pub[3] if len(pub) > 3 else ''
        }
