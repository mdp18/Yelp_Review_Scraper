import bs4  # importing soup
from urllib.request import urlopen as url  # importing urllib for url request
from bs4 import BeautifulSoup as soup
import pandas as pd

x = 0
filename = "datasets.csv"  # saving data as csv
f = open(filename, "w")
headers = "Review_Body\n"  # these are the features that are scraped
f.write(headers)
dict = {}
counter = 0

for _ in range(4):  # regex could have been used here but this is to increment the url page(keeping it simple.)
    my_url = "http://www.yelp.com/biz/musashis-seattle?&start=" + str(x)
    request = url(my_url)  # taking url as a parameter
    htmlscrap = request.read()
    request.close()
    page_soup = soup(htmlscrap, "html.parser")  # parsing as html
    container = page_soup.findAll("div", {
        "class": "review review--with-sidebar"})  # the class name where all the features are contained
    #print("Amount of reviews on this page: " + str(len(container)))



    for i in container:

        # print(container)
        friend_counter = i.findAll("li", {"class": "friend-count responsive-small-display-inline-block"})
        friend_count = friend_counter[0].b.text
        review_counter = i.findAll("li", {"class": "review-count responsive-small-display-inline-block"})
        review_count = review_counter[0].b.text
        photo_counter = i.findAll("li", {"class": "photo-count responsive-small-display-inline-block"})
        review = i.findAll('p', {"lang": "en"})

        strReview = str(review) #converts the review to a string
        #print(type(review))
        #print(strReview)
        formatStrReview = strReview[14:] #cuts beginning javascript syntax from review, needs work
        dict[counter] = formatStrReview #fills python dictionary
        counter = counter + 1
        #print(strReview.rindex("a"))



        #print(review[0])      don't want to print to console rn

        if photo_counter:
            photo_count = photo_counter[0].b.text
        else:
            photo_count = 0
        elite_counter = i.findAll("li", {"class": "is-elite responsive-small-display-inline-block"})
        if elite_counter:
            elite_count = 1
        else:
            elite_count = 0
        funny_counter = i.findAll("a", {"class": "ybtn ybtn--small ybtn--secondary funny js-analytics-click"})
        funny_count1 = funny_counter[0].findAll("span", {"class": "count"})
        funny_count = funny_count1[0].text
        if funny_count:
            funny_count = funny_count
        else:
            funny_count = 0
        cool_counter = i.findAll("a", {"class": "ybtn ybtn--small ybtn--secondary cool js-analytics-click"})
        cool_count1 = cool_counter[0].findAll("span", {"class": "count"})
        cool_count = cool_count1[0].text
        if cool_count:
            cool_count = cool_count
        else:
            cool_count = 0
        useful_counter = i.findAll("a", {"class": "ybtn ybtn--small ybtn--secondary useful js-analytics-click"})
        useful_count1 = useful_counter[0].findAll("span", {"class": "count"})
        useful_count = useful_count1[0].text
        if useful_count:
            useful_count = useful_count
        else:
            useful_count = 0
        user_counter = i.findAll("a", {"class": "user-display-name js-analytics-click"})
        user_count = user_counter[0].text
        rating_counter = i.findAll("div", {"class": "biz-rating biz-rating-large clearfix"})
        rating_count = rating_counter[0].div.div["title"]
        rating_count = (int(rating_count[0]))

        length_counter = i.findAll("p", {"lang": "en"})
        xx = str(length_counter[0])
        length_count = len(xx)
        # print(length_count)

        checkin_counter = i.findAll("li", {"class": "review-tags_item"})
        if checkin_counter:
            var1 = checkin_counter[0].text.strip()
            checkin_count = (int(var1[0]))
        else:
            checkin_count = 0

        #f.write(
        #    (str(review) + "\n")
        #)

    x = x + 20
print(len(dict)) #testing whether all reviews are placed in dictionary
#print(dict)

panda = pd.DataFrame.from_dict(dict, orient="index", columns=["Reviews"]) #creates dataframe from the dictionary
print(panda)

panda.to_csv(filename) #creates csv file from panda dataframe

f.close()