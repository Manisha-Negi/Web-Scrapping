import json
import os
from scrapinghelp import htmlhelper
import requests
from datetime import datetime
from multiprocessing.pool import ThreadPool as Pool
import threading

session_obj = requests.session()
class data:

    def data(_Cookie:str,_JobNumber:str):
        print("Data Started")
        filename = os.path.dirname(__file__) + "/Log/" + str(_JobNumber) + "/mainlink_" + str(_JobNumber)+".txt"
        infile = open(filename,'r')
        mainlink_list = json.load(infile)
        infile.close()
        print("Mainlink Loaded to a list")

        pool_size = 200
        pool = Pool(pool_size)
        for link in mainlink_list:
            # pass
            #data.getdatafromweb(link, _Cookie,  _JobNumber,  mainlink_list)
            pool.apply_async(data.getdatafromweb, (link, _Cookie,  _JobNumber,  mainlink_list))
            #t1 = threading.Thread(target=data.getdatafromweb, args=(link, _Cookie, _JobNumber, mainlink_list))
            #t1.start()
            # list(map(data.getdatafromweb,(link, _Cookie,  _JobNumber,  mainlink_list)))
        pool.close()
        pool.join()

        print("Data End")

    def getdatafromweb(link, _Cookie,  _JobNumber,  mainlink_list):
        global session_obj
        id = link["id"]
        main_link = link["mainlink"]
        category1 = link["cat1"]
        category2 = link["cat2"]
        department = htmlhelper.returnvalue(main_link, "department[]=", "&category[]")
        category= htmlhelper.returnvalue(main_link+'last', "category[]=", "last")

        if main_link != "":
            totalcount =""
            noofpage=1
            startpage=1
            i=1
            flag=True

            while flag:

                headers = {
                          'Accept': '*/*',
                          'Accept-Encoding': 'gzip, deflate, br',
                          'Accept-Language': 'en-US,en;q=0.9',
                          'Connection': 'keep-alive',
                          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                          'Cookie': _Cookie ,
                          'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                          'sec-ch-ua-mobile': '?0',
                          'sec-ch-ua-platform': '"Windows"',
                          'Sec-Fetch-Dest': 'empty',
                          'Sec-Fetch-Mode': 'cors',
                          'Sec-Fetch-Site': 'same-origin',
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                          'X-Requested-With': 'XMLHttpRequest'
                           }

                url="https://www.foodcity.com/index.php"
                PostData = 'vica=ctl_elastic_search&vicb=getItemsByPage&vicc=h&searchType=All&Search=&department[]=' + department + '&category[]=' + category + '&page=' + str(i)


                if category1 == 'oil' or category1 == 'mayo':
                    PostData = 'vica=ctl_elastic_search&vicb=getItemsByPage&vicc=h&searchType=All&Search='+category1+'&page='+str(i)
                # proxies = {'http': 'http://intrics-res-us-sid:MpyRwi4gJpZP@gw.ntnt.io:5959',
                #            'https': 'http://intrics-res-us-sid:MpyRwi4gJpZP@gw.ntnt.io:5959'}
                proxies = {'http': 'http://us.proxymesh.com:31280',
                           'https': 'http://us.proxymesh.com:31280'}

                outfilename = os.path.dirname(__file__) + "/Log/" + str(_JobNumber) + "/Data_" + str(id) + "_" + str(i) + ".txt"
                print(outfilename)
                if not os.path.exists(outfilename):
                    ProducturlJsonsource = ""
                    while ProducturlJsonsource == "" or ProducturlJsonsource.status_code != 200 or 'Request Rejected' in ProducturlJsonsource.text:
                        try:

                            ProducturlJsonsource = session_obj.post(url,data=PostData,headers=headers,verify=False,timeout=100)

                            source = ProducturlJsonsource.text
                            #print(source)

                        except Exception as e:
                            session_obj = requests.session()
                            ProducturlJsonsource = ""
                            print(e)


                    if source=="" or i==100:
                        flag=False
                    else:
                        print("Scrapping: id-" + str(id) + "/" + str(len(mainlink_list)) + " - Time-" + str(datetime.now())+" - Page N.- "+str(i))

                        fileout = open(outfilename, 'w')
                        #DATE = "TIMESTAMP:[" + datetime.now(timezone('US/Eastern')).strftime("%m/%d/%Y %I:%M:%S %p") + "]"
                        json.dump(source, fileout)
                        fileout.close()


                    i=i+1
                else:
                    print('exist')
                    infile1 = open(outfilename, 'r')
                    datafromfile = str(infile1.read()).replace('\\', '')
                    ProductArr = htmlhelper.collecturl(datafromfile, "", "class=\"product-module-wrap item","</section>")
                    if len(ProductArr)<25:
                        flag=False
                    i=i+1







