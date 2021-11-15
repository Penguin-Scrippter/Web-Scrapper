#!/usr/bin/python3 


import requests
from bs4 import BeautifulSoup
from rich import print


print("""[red bold]
  o__ __o__/_   o                 o                            o__ __o                                                      o              
 <|    v       <|>              _<|>_                         <|     v\                                                   _<|>_            
 < >           / \                                            / \     <\                                                                   
  |            \o/   o      o     o    \o__ __o     o__ __o/  \o/     o/   o__  __o   \o__ __o     o__ __o/   o       o     o    \o__ __o  
  o__/_         |   <|>    <|>   <|>    |     |>   /v     |    |__  _<|/  /v      |>   |     |>   /v     |   <|>     <|>   <|>    |     |> 
  |            / \  < >    < >   / \   / \   / \  />     / \   |         />      //   / \   / \  />     / \  < >     < >   / \   / \   / \ 
 <o>           \o/   \o    o/    \o/   \o/   \o/  \      \o/  <o>        \o    o/     \o/   \o/  \      \o/   |       |    \o/   \o/   \o/ 
  |             |     v\  /v      |     |     |    o      |    |          v\  /v __o   |     |    o      |    o       o     |     |     |  
 / \           / \     <\/>      / \   / \   / \   <\__  < >  / \          <\/> __/>  / \   / \   <\__  < >   <\__ __/>    / \   / \   / \ 
                        /                                 |                                              |                                 
                       o                          o__     o                                      o__     o                                 
                    __/>                          <\__ __/>                                      <\__ __/>                                 
                                                                                            Code by >>> Muhammad Zeeshan!
[/red bold]""")


url = input("Enter a Url  :  -  ")
dr = input("Enter Directory name you want to check in the scrapper urls: -")
_url = []
req = requests.get(url)
req1 = req.text


bsoup = BeautifulSoup(req1,"html.parser")

for i in bsoup.find_all("a"):
       org = str(i.get("href"))
       if org.startswith("https") or org.startswith("http") :
           _url.append(org)
       else:
           pass
print(f"[bold blue]your final list or url is : {_url}")

for i in _url:
    req2 = i + dr
    reqObj =  requests.get(req2)

    print(f"[bold yellow]{req2}:-[/bold yellow]{reqObj.status_code} ")    


