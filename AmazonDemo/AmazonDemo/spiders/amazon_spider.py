import scrapy

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=laptop+accessories&crid=3QLHB1VVTCJAM&sprefix=laptop+ass%2Caps%2C355&ref=nb_sb_ss_ts-doa-p_1_10']

    def parse(self, response):
        products = response.css('div[data-component-type="s-search-result"]')

        for product in products:
            product_name = product.css('span.a-size-medium.a-color-base.a-text-normal::text').get()
            product_price = product.css('span.a-offscreen::text').get()
            rating = product.css('span.a-icon-alt::text').get().split()[0]
            review_count = product.css('span.a-size-base::text').get()

            print("Product Name:", product_name)
            print("Product Price:", product_price)
            print("Rating:", rating)
            print("Review Count:", review_count)
            print()

        # Follow pagination links
        next_page = response.css('li.a-last a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
