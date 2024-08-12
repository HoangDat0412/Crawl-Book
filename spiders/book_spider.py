import scrapy
from urllib.parse import urlparse

class BookSpiderSpider(scrapy.Spider):
    name = "book_spider"
    allowed_domains = ["thuviensach.vn"]
    start_urls = ["https://thuviensach.vn/thu-vien/"]

    def parse(self, response):
        books = response.css('.block_product_thumbnail')
        for book in books:
            relative_url = response.urljoin(book.css('a::attr(href)').get())
            yield response.follow(relative_url, self.parse_book_page)

        # # Pagination
        # next_page = response.css('a.middle_link::attr(href)').get()
        # if next_page:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

    def parse_book_page(self, response):
        title = response.css('h1.fs20::text').get().strip()
        author = response.css('p.mt10.mb10').xpath('b[text()="Tác giả :"]/following-sibling::a/text()').get().strip()
        genres = response.css('fieldset#pdf button::text').getall()
        image_url = response.css('div.size-shop_catalog img::attr(src)').get()
        image_url = image_url.split('?')[0]
        if image_url:
            image_url = response.urljoin(image_url)

        def convert_url (url):
            path = urlparse(url).path
            path = path.strip('/').replace('.html','')
            parts = path.split('-')
            if len(parts) > 1:
                converted = f"{parts[-1]}-{'-'.join(parts[:-1])}"
            else:
                converted = path 
            return converted

        converted_identifier = convert_url(response.url)
        pdf_url = f"https://thuviensach.vn/img/pdf/{converted_identifier}-thuviensach.vn.pdf"

        # Yielding item with image and PDF URLs
        yield {
            'title': title,
            'author': author,
            'genres': genres,
            'image_urls': [image_url] if image_url else [],
            'files_urls': [pdf_url],
        }
