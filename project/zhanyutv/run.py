from scrapy.cmdline import execute
import os
import sys

anchor_name = "douyu_anchor"


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", anchor_name])
