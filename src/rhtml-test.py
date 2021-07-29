from requests_html import HTML, HTMLSession
import csv

with open('scraped.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['title', 'description', 'image'])

    session = HTMLSession()
    response = session.get('https://fouadben.herokuapp.com/')

    services = response.html.find('div.service-item')

    for service in services:

        title = service.find('h4', first=True).text

        description = service.find('p', first=True).text

        image_src = service.find('img', first=True).attrs['src']

        print(title)
        print(description)
        print(image_src)
        print()

        csv_writer.writerow([title, description, image_src])
