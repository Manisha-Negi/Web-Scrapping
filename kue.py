import requests
from bs4 import BeautifulSoup
import csv

url = "https://mykn.kuehne-nagel.com/public-tracking/shipments?query=PNQ0165780"

r = requests.get(url)

r_html = r.content

soup = BeautifulSoup(r_html , "html5lib")

#Finding start date and Time

#print(soup.prettify)
Date_Time = []
start_date = soup.find_all('td' , attrs = {'class':'table-readonly__cell t-statusdatetime statusdatetime'})
for item in start_date :
    print(item)
    for  i in item.strings:
        print(i)
        Date_Time.append(i)

length_Date_Time = len(Date_Time)
#print(length_Date_Time)
#print(Date_Time)
print("Start Date : " + Date_Time[0].strip())
print("Start Time : " + Date_Time[1])

print("End Date : " + Date_Time[int(length_Date_Time) - 3].strip())
print("End Time : " + Date_Time[int(length_Date_Time) - 2])

#Finding start location
#td 'class'='table-readonly__cell t-statuslocation statuslocation' data-tooltip-ellipsis data-title="Pune">Pune</td>

Location = []
start_place = soup.find_all('td' , attrs = {'class':'table-readonly__cell t-statuslocation statuslocation'})
for item in start_place :
    for i in item.strings:
        #print(i)
        Location.append(i)

length_Location = len(Location)
start_point = Location[0]
end_point = Location[int(length_Location) - 1]

print("Start Place: " + start_point)
print("Destination: " + end_point)

file = open("scarp_data.csv" , "a")

writer = csv.writer(file)
#writer.writerow(["Start Date" , "End Date" , "Start Place" , "Destination"])
writer.writerow([Date_Time[0].strip() , Date_Time[int(length_Date_Time) - 3].strip() , start_point , end_point])

file.close()