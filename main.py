# Joseph Schroedl
# https://github.com/corndog2000

# Libraries needed for scraping web pages
from bs4 import BeautifulSoup
import requests

# Library used to get the current date
import datetime


def main():

    # Placeholder list for the fetched menu items
    menu = []

    # Get the current date
    i = datetime.datetime.now()

    year = str(i.year)
    month = str(i.month)
    day = str(i.day)

    # If we are in a single digit month then add a leading zero
    if len(month) == 1:
        month = "0" + month

    # If we are on a single digit day then add a leading zero
    if len(day) == 1:
        day = "0" + day

    # Print the fetehed date
    print("Current year = %s" % year)
    print("Current month = %s" % month)
    print("Current date (day) = %s" % day)

    # Define webpage urls with the current date
    fountain_lunch = r"https://dining.ncsu.edu/wp-admin/admin-ajax.php?action=ncdining_ajax_menu_results&date=" + \
        year + r"-" + month + r"-" + day + \
        r"&meal=lunch&pid=45&dietAtts=%7B%22pref%22%3A%5B%5D%2C%22hide%22%3A%5B%5D%7D"

    print(f"URL to scrape: {fountain_lunch}")

    # Query the website and return the html to the variable ‘page’
    page = requests.get(fountain_lunch)
    # We only want the HTML from the query
    page = page.text

    # Parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, "html.parser")

    # Get only the elements that contain the names of food items
    anchors = soup.find_all(
        'a', {'class': 'dining-menu-item-modal', 'href': True})

    # Cycle through each found element and only grab the text
    # The text is what you would see as the hyperlink text
    # We add each menu item to the menu list
    for anchor in anchors:
        name = anchor.get_text()
        menu.append(name)
        # print(name)

    print(menu)


if __name__ == "__main__":
    main()
