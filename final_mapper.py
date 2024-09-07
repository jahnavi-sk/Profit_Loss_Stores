#!/usr/bin/env python3

import sys
import json

i = 0
output_data = []

for line in sys.stdin:
    count =0
    line = line.strip().strip(",")
    if(len(line)>1):
       
        data = json.loads(line)

        
        profit =0
        loss=0
        rev = 0 
        cost =0
       
        city = data.get("city", "Unknown")
        sales_data = data.get("sales_data")
        id_data = data.get("store_id")
        cate = data.get("categories", "Unknown")
        # print(cate[0])

        m = len(cate)
        # print(m)
        n = len(sales_data)
        # print(n)

        for i in range(0,m):
            for j in range(0,n):
                
                    sales_data_key = list(sales_data.keys())[j]
                    if cate[i] == sales_data_key:
                        sales_data_value = sales_data.get(sales_data_key, "Unknown")
                        revenue_val = sales_data_value.get('revenue', None)
                        cogs_val = sales_data_value.get('cogs', None)
                        

                        if revenue_val is not None and cogs_val is not None:
                            # print("revenue_val", revenue_val)
                            # print("cogs_val", cogs_val)

                            rev += revenue_val
                            cost += cogs_val
                
        if(rev-cost>0):
            profit = 1
        else:
            loss = 1
        # 
        
        


        if(rev==0 and cost==0):
            continue
        else:
            entry = {
                        "city": city,
                        "profit_count": profit,
                        "loss_count": loss
                    }
            # print(json.dumps(entry, separators=(',', ':')))
            
            output_data.append(entry)
      

output_data.sort(key=lambda x: x['city'])
for entry in output_data:
    print(json.dumps(entry, separators=(',', ':')))