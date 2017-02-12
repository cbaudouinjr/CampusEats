"""
Takes the command line arguments of a filename to write the output of the code to.
Scrapes RIT Dining website for names locations and times
only the name is guaranteed


:author: Tucker Noniewicz

"""
from lxml import html
import requests
import sys


def scrape():
    """
    Scrapes the names, locations, and times for RIT dining
    Meaning: ?: one or zero instances of the previous thing
             *: zero or more instances of the previous thing
             ...: repeat the previous element in the list zero or more times
    :return: a 2DArray of the form [[Name, (Location)?, (time)*,], ...]
    """
    page = requests.get("https://www.rit.edu/fa/diningservices/hours-and-locations")
    tree = html.fromstring(page.content)
    locationData=[]
    rows = tree.xpath('//table[@class="views-table rwd-table cols-3"]/tbody/*')
    for row in rows:
        data = row.xpath('td[@class="views-field views-field-title persist essential"]/a/text() | ' +
                         'td[@class="views-field views-field-field-building-location persist essential"]/a/text() | ' +
                         'td[@class="views-field views-field-php persist essential"]/div[@class="menu-day-hours"]/text()')
        locationData.append(data)
        print(data)
    return locationData

def main():
    """
    Takes a filename on the command line to put the output of the script in 
    :return:
    """
    if len(sys.argv) != 2:
        sys.stdout = sys.stderr
        print("Usage: python filename")
        quit()

    i_ofile = open(str(sys.argv[1]), 'w')
    rows = scrape()
    for row in rows:
        i_ofile.write(str(row) + "\n")




    """
    print("Names, Location")
    print(len(my_list[0]))
    print(len(my_list[1]))
    print(len(my_list[2]))
    print(len(my_list[3]))
    print("[", end = " ")
    for _ in range(len(my_list[0])):
        print( "[", end="")
        print( my_list[0][_] , end = ", ")
        print( my_list[1][_] , end = ", ")
        print( my_list[2][_], end="]\n")
    print("]", end = " ")
    print(my_list[2])

    print("Location: ")
    print("[", end=" ")
    for _ in my_list[0]:
        print(_, end=",\n")
    print("]", end=" ")
    """

if __name__ == "__main__":
    main()