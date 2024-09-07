#!/usr/bin/env python3


import sys
import json

old_city = None
profit_stores = 0
loss_stores = 0

for line in sys.stdin:
   
        line = line.strip()
        data = json.loads(line)
        city = data.get("city", "Unknown")
        
        # city = data.get("city", "Unknown")
        p_c = data.get("profit_count", 0)
        l_c = data.get("loss_count",0)

        if city == old_city:

            if(p_c > l_c):
                profit_stores+=1
            elif(l_c >= p_c):
                # if(l_c==0 and p_c==0):
                #     loss_stores = loss_stores*1
                # else:
                    loss_stores+=1
              
        else:
            if old_city:
                entry = {
                        "city": old_city,
                        "profit_stores": profit_stores,
                        "loss_stores": loss_stores
                    }
                # print(f"City: {old_city}, Profit Stores: {profit_stores}, Loss Stores: {loss_stores}")
                print(json.dumps(entry, separators=(', ', ': ')))
            
            old_city = city
            profit_stores = 1 if p_c > l_c else 0
            loss_stores = 1 if l_c >= p_c else 0
            

if old_city is not None:
    entry = {
                "city": old_city,
                "profit_stores": profit_stores,
                "loss_stores": loss_stores
            }
    print(json.dumps(entry, indent=None,separators=(', ', ': ')))
    # print(f"City: {old_city}, Profit Stores: {profit_stores}, Loss Stores: {loss_stores}")