from requests_html import HTML

with open('test.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

articles = html.find('div.article')

for article in articles:
    title = article.find('h2', first=True).text
    description = article.find('p', first=True).text

    print(title)
    print(description)
    print()