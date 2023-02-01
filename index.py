from bs4 import BeautifulSoup
import requests



url = "https://www.imdb.com/chart/moviemeter/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
names=[]
years=[]
ratings=[]

img=[]
movie_data = soup.findAll('tbody',  {'class': 'lister-list'})

scrap_name=soup.findAll('td',{'class': 'titleColumn'})
for n in scrap_name :
    movie_name=n.a.text
    names.append(movie_name)
    movie_year=n.span.text
    years.append(movie_year)

    


scrap_rate=soup.findAll('td',{'class': 'ratingColumn imdbRating'})
for n in scrap_rate :
    movie_rate= n.text
    ratings.append(movie_rate)
    
scrap_img_url=soup.findAll('td',{'class': 'posterColumn'})
for n in scrap_img_url:
    image=n.a.img['src']
img.append(img)
    


data={'names':names,'years':years,'ratings':ratings,'img':img}   

context={'data':data}
print (context)