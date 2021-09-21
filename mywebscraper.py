from bs4 import BeautifulSoup
import requests
import csv



def writeimage(url,impath):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    img = soup.find_all('img')
    imUrl = img.attrs.get('src')
    #img = soup.find('img')['src'] also possible
    response = requests.get(imUrl)
    with open('{}'.format(impath) + imUrl[imUrl.rfind('/'):], "wb") as file: # wb here stands for binary mode.
    # Binary mode indicates no changes on data as it is written to the file (w - writing , b- binary mode)
        file.write(response.content)

def writetext(textData, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(textData)

def getTextData(url):
    #tags may differ by website.
    #use print(soup.prettify()) to display whole html to see the tags of interest.
    response = requests.get(url) #returns a response object, so that we can get the source code of whole webpage
#from this object
    soup = BeautifulSoup(response.text, "html.parser")
    #print(soup.prettify()) -- You need to pinpoint where exactly is the scope information
    myData = []

    for i in soup.find_all('tag'):
        data1 = i.find("tag", class_="tag").get_text()
        #data1 = i.find("tag", class_="tag").h2.a.get_text() depending on your tags
        data2 = i.find("othertag", class_="othertag").get_text()
        myData.append([data1,data2])
    return myData


if __name__ == "__main__":

    imagepath = 'images/'
    baseurl = "sequentWebpageUrl/"
    page = 1
    lastpage = 20
    filename = 'myData.csv'


    while page <= lastpage:
        pageUrl = baseurl + str(page)
        dataToWrite = getTextData(pageUrl)
        writetext(dataToWrite, filename)
        writeimage(pageUrl, imagepath)
        page += 1




