import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    start_urls = ['https://www.ebay.com/sch/garlandcomputer/m.html']

    def parse(self, response):
        for product in response.css('.srp-list .s-item'):
            condition = product.css(".s-item__subtitle > .SECONDARY_INFO::text").get()
            if self.condition and self.condition != condition:
                continue

            yield {
                'title': product.css('.s-item__title > span::text').get(),
                'condition': condition,
                'price': product.css(".s-item__price::text").get(),
                'product_url': product.css(".s-item__link::attr(href)").get()
            }

        for next_page in response.css('a.pagination__next'):
            yield response.follow(next_page, self.parse)
