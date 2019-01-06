import requests
from lxml import etree

def table_to_markdown(url="https://docs.python.org/3/library/itertools.html"):
    response = requests.get(url)
    html = etree.HTML(response.text)
    tables = html.xpath("//table")
    for table in tables:
        trs = table.xpath("./*/tr")
        for tr in trs:
            trstr = " | ".join([ "".join([text.strip() for text in td.xpath(".//text()")]).replace("|","&#124;")
                for td in tr.xpath("./td | ./th")]).replace("â¦","...")
            print("| "+trstr+" |")
        print("#"*20)

if __name__ == "__main__":
    table_to_markdown("https://blog.csdn.net/gongbing798930123/article/details/78955597")