from requests_html import HTML


# session = HTMLSession()
# response = session.get('https://fouadben.herokuapp.com/')

# for link in response.html.links: # or absolute_links
#     print(link)


with open('test.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    html.render()

match = html.find('footer', first=True)
print(match.html)
