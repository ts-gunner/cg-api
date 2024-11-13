import requests
from lxml import etree
response = requests.get("https://nav.liwenkai.fun/")
data = []
tree = etree.HTML(response.text)

element = tree.xpath("//div[@class='space-y-1']")[0]
for index, node in enumerate(element.getchildren()):
    ele = node.xpath("./div//span[@class='truncate text-sm']")[0]
    data.append({
        "index": index,
        "category": ele.text
    })
print(ele)