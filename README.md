# Crawler Demo using Scrapy 

This is a small demo of how to crawl an ebay product page using scrappy.

This project is only meant for educational purposes.


## Data

This project gets the product data and writes it into a directory called products.
Each product gets written into it's own file with the file name being the id of the product.

The extracted data looks like this sample:

    {
        'title': 'A nice product',
        'condition': 'Used',
        'price': '19.99',
        'product_url': 'https://www.url.com/itm/234908325972?hash=item36b1a09854:g:czcAAOSwHoRlFfxf'
    }


## Spiders

This project contains one spiders and you can list them using the `list`
command:

    $ scrapy list
    products

## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl products

If you want to filter by condition you can pass `a` flag to search for a exact condition math:

    $ scrapy crawl products -a condition="Used"

