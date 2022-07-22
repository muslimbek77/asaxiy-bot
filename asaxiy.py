import requests
from bs4 import BeautifulSoup


def rasm_content(q):
    URL=f'https://asaxiy.uz/product?key={q}'
    page=requests.get(URL)
    soup=BeautifulSoup(page.content,'html.parser')

# results = soup.find(class_='col-6 col-xl-3 col-md-4')
    results=soup.find_all('div',class_='col-6 col-xl-3 col-md-4')
    images_content=[]
    for i in results:
        content=[]
        image=i.find('img', class_='img-fluid lazyload')
        
        content.append((image.get('data-src').split('.webp')[0]))
              
        content.append(i.find('h5', class_='product__item__info-title').text)
        
        
        content.append( i.find('div', class_='produrct__item-prices--wrapper').text)
        content.append( i.find('div', class_='installment__price').text)

               
        images_content.append(content)
        
        
    # print(image_content[0]['month-price'])
    # print(len(image_content))
    return images_content
    
# rasm_content('telefon')