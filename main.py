import re
from collections import Counter 
from bs4 import BeautifulSoup
from urllib.request import urlopen


def getSyns(word):
    url="https://www.thesaurus.com/browse/"+word+"?s=t"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")


    finalList=[]

    for a in soup.find_all('a', class_="css-1m14xsh eh475bn1", href=True):
        finalList.append(a['href'])

    outList=[]
    for x in finalList:
        x=x[8:]
        outList.append(x)
    return outList

with open('commonWords.txt', 'r') as file:
    commonWords=file.read().replace('\n', ' ')




commonWords=commonWords.lower()
commonList=commonWords.split(" ")

check=True
extra=input("Any words you want added to the common words list? y/n ")
if (extra=="n"):
    check=False
while check==True:
    extraCommon=input("Enter Word (lowercase pls): ")
    commonList.append(extraCommon)
    checker=input("Any more? y/n " )
    if(checker=="n"):
        check=False




#print(commonList[1])
fileName=input("enter name of txt file, with .txt included: ")
with open(fileName, 'r') as file:
    data = file.read().replace('\n', ' ')
data=data.lower()
    # split() returns list of all the words in the string 
split_it = data.split()

l3 = [x for x in split_it if x not in commonList]
  
    # Pass the split_it list to instance of Counter class. 
Counter = Counter(l3) 
  
    # most_common() produces k frequently encountered 
    # input values and their respective counts. 
val=int(input("How many words do you want Synonyms of? "))
most_occur = Counter.most_common(val)
x=0
#print(getSyns("test"))
while x< val:
    w1=most_occur[x][0]
    print(most_occur[x])
    print("Synonyms: ")
    print(getSyns(w1))
    print("")
    #+str(most_occur[x][1])+"occurences")
    
    x=x+1

