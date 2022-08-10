URL = "https://testing-www.codefellows.org/courses/code-400/"
page = requests.get(URL)

# print(page.content)


###############
# step 2
# Once we have the content it will be in raw html form, which is great for a browser, but not as easy for a human being to read.
# So let's see if we can make sense of the raw html by parsing it
###############

# NOTE: Move import to top of course to get rid of linter error
from bs4 import BeautifulSoup

# BeautifulSoup can parse many types of content.
# We're parsing html so let BeautifulSoup know
# conventionally you store the BeatifulSoup instance in a variable named soup
soup = BeautifulSoup(page.content, "html.parser")


###############
# step 3
# The soup instance has powerful capabilities for finding one or many elements based on different criteria
@@ -50,7 +46,6 @@
# calling prettify method makes output a lot easier to read
# print(results.prettify())


###############
# step 4
# We can then perform finds on previously found items
@@ -59,25 +54,22 @@

titles = results.find_all("h3")

# print(titles)

###############
# step 5
# result of find_all is iterable and can be used in for loops
###############
# for title in titles:
#     print(title.text)


###############
# step 6
###############

# find_all is so common there's a shortcut
anchors = results("a")

# print(type(anchors))

# for anchor in anchors:
#     print(anchor)

###############
# step 7
@@ -92,13 +84,15 @@
# step 8
###############
python_link = links[1]
link_content = requests.get("https://testing-www.codefellows.org" + python_link)
link_soup = BeautifulSoup(link_content.content, "html.parser")

article = link_soup("article")[1]

python_url = "https://testing-www.codefellows.org" + python_link
python_response = requests.get(python_url)
python_soup = BeautifulSoup(python_response.content, "html.parser")
article = python_soup("article")[1]
list_items = article.select("ul li ul li")

# get details about the object you're working with
# print(dir(titles[1]))

print(titles[1].text)
for li in list_items:
    print(li.text)