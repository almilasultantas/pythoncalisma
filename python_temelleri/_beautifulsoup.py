# html_doc="""
# <!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="UTF-8">
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
# <title>İlk web sayfam</title>
# </head>
# <body>
#     <h1>
#         RUSÇA ÖĞRENİYORUM
# </h1>
#     <div class ="Başalayalım">
#         <h2>
#             Siz isteyin her şey kolaylaşır...
#         </h2>
    
#         <ul>
#             <li>Türkçeden Rusçaya çeviri</li>
#             <li>Rusçaya Türkçeden çeviri</li>
#             <li>Grammer Kontrolü</li>
#         </ul>
#     </div>
#     <h2>Hocamız Yağmur TOPAL</h2>
#     <img src="yağmur.jfif" alt="">
    
# </body>
# </html>
# """


# from bs4 import BeautifulSoup


# soup=BeautifulSoup(html_doc,"html.parser")
# result=soup.prettify()
# result=soup.title
# result=soup.title.string


# print(result)

# # web scraping- beautiful soup- imdb
# import requests
# from bs4 import BeautifulSoup
# url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"

# # response=requests.get(url).content
# # content=response.content
# html=requests.get(url).content
# soup=BeautifulSoup(html,"html.parser")
# list=soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=1)
# for tr in list:
#     title=tr.find("td",{"class":"titleColumn"}).find("a").text
#     year=tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
#     rate=tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
#     print(title,year,rate)
# # print(list)

# web scraping- beautiful soup- imdb
import requests
from bs4 import BeautifulSoup
url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html=requests.get(url).content
soup=BeautifulSoup(html,"html.parser")
list=soup.find_all("li",{"class":"column"},limit=1)

print(list)



