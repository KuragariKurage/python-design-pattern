from abstract_factory import Factory, LinkItem, ListItem, PageItem


class HtmlPageItem(PageItem):
    def __init__(self, title, author):
        super().__init__(title, author)

    def make_html(self):
        output = f"<html>\n<head>\n<title>{self.title}</title>\n</head>\n"
        output += f"<body>\n"
        output += f"<h1>{self.title}</h1>\n"
        output += f"<ul>"

        for list_item in self.content:
            output += list_item.make_html()

        output += f"</ul>\n"
        output += f"<hr>\n<address>{self.author}</address>\n"
        output += f"</body>\n</html>\n"

        return output


class HtmlLinkItem(LinkItem):
    def __init__(self, caption, url):
        super().__init__(caption, url)

    def make_html(self):
        return f'<li><a href="{self.url}">{self.caption}</a></li>\n'


class HtmlListItem(ListItem):
    def __init__(self, caption):
        super().__init__(caption)

    def make_html(self):
        output = f"<li>\n{self.caption}\n"
        output += f"<ul>\n"

        for link_item in self.items:
            output += link_item.make_html()

        output += f"</ul>\n"
        output += f"</li>\n"

        return output


class HtmlFactory(Factory):
    def __init__(self) -> None:
        super().__init__()

    def create_link_item(self, caption, url):
        return HtmlLinkItem(caption, url)

    def create_list_item(self, caption):
        return HtmlListItem(caption)

    def create_page_item(self, title, author):
        return HtmlPageItem(title, author)


html_factory = HtmlFactory()

asahi = html_factory.create_link_item("朝日新聞", "https://www.asahi.com/")
yomiuri = html_factory.create_link_item("読売新聞", "https://www.yomiuri.co.jp/")
mainichi = html_factory.create_link_item("毎日新聞", "https://mainichi.jp/")

news_pages = html_factory.create_list_item("新聞")

news_pages.add(asahi)
news_pages.add(yomiuri)
news_pages.add(mainichi)

google = html_factory.create_link_item("Google", "https://www.google.com/")
yahoo = html_factory.create_link_item("Yahoo!", "https://www.yahoo.co.jp/")

search_pages = html_factory.create_list_item("検索エンジン")

search_pages.add(google)
search_pages.add(yahoo)

page = html_factory.create_page_item("my page", "john doe")

page.add(news_pages)
page.add(search_pages)

page.write_html("tmp.html")
