from src.Spider import Spider

spider = Spider()

spider.scrap("a", "Navigation")
qualification_types = spider.get_entries()
spider.refine_urls()
print(qualification_types)

spider.scrap("a", "Navigation")
qualifications = spider.get_entries()
spider.refine_urls()
print(qualifications)