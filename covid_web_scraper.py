def kj():
        import requests
        import lxml.html as lh
        import pandas as pd
        
        import schedule
        import time


        
        url='https://www.worldometers.info/coronavirus/#countries'
        #Create a handle, page, to handle the contents of the website
        page = requests.get(url)
        #Store the contents of the website under doc
        doc = lh.fromstring(page.content)
        
        #Parse data that are stored between <tr>..</tr> of HTML
        
        tr = doc.xpath('//*[@id="main_table_countries_today"]/thead/tr')
        tr=tr[0][0:-1]
        print(len(tr))
        #for i in tr_elements:
        #    print(i)
        #    print("aSdsC")
        h=[]
        for i in tr:
            
            h.append(i.text_content())
        print(h)    
        h.append('Continent')
        
        
        tb = doc.xpath('//*[@id="main_table_countries_today"]/tbody[1]')
        tb=tb[0]
        print(len(tb))
        bc=[]
        bc.append(h)
        kl=0
        for i in tb:
            kl=kl+1
            if(kl>7):
            
                x=i.text_content()
                
                v=["".join(jg for jg in t.strip() if (jg.isalnum() or jg=='.')  ) for t in x.split("\n")]
                del v[0]; del v[len(v)-1]
        #        print(v)
                
                for hc in range(len(v)): 
                    if(hc>=1 and hc<=len(v)-2):
                      try:  
                        v[hc]=float(v[hc])
                      except ValueError:
                         print(hc)
                         print("######")
                         print(v[hc])      
                print(v)  
                bc.append(v)
            print("**********************")
        print(h) 
        from datetime import datetime as dt
        gb=str(dt.date(dt.now()))
        import csv
        
        
        import random

#        lmb=random.randint(0, 100000000)
        with open("/home/ubuntu/data/COVID-19_"+gb+".csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(bc) 

kj()
