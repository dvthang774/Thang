import scrapy


class crawling(scrapy.Spider):
    name= 'test'
    start_urls = ['https://baomoi.com/tin-moi.epi']

    def parse(self,response):
        for title in response.xpath("//div[@class='story']"):
            yield {
                'title': title.xpath(".//h4[@class='story__heading']").extract_first()
            }
print(matran)
# cào dữ liệu