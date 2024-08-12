
BOT_NAME = "library"

SPIDER_MODULES = ["library.spiders"]
NEWSPIDER_MODULE = "library.spiders"

ROBOTSTXT_OBEY = True

# settings.py

# Enable Images Pipeline
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
    'scrapy.pipelines.files.FilesPipeline': 2,
}

# Define where images should be saved
IMAGES_STORE = 'images'  # Folder where images will be saved

# Define where files (PDFs) should be saved
FILES_STORE = 'files'  # Folder where files will be saved
FILES_URLS_FIELD = 'files_urls'  # Tên trường chứa URL của PDF

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
