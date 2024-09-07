import sys
import json

i = 0
output_data = []
for line in sys.stdin:
    
    line = line.strip().strip(",")
    if(len(line)>1):
        # print(f"[{line}]")
        # print(line["city"])
        data = json.loads(line)
        profit =0
        loss=0
        # Extract the city value
        city = data.get("city", "Unknown")
        sales_data = data.get("sales_data")
        id_data = data.get("store_id")

        
        n = len(sales_data)
       
        if(n):
            # first_key = list(sales_data.keys())[0]
            # first_value = sales_data.get(first_key, "Unknown")
        
            # print(f"[{first_value}]")
            for i in range(0,n):
                # print(sales_data)
                sales_data_key = list(sales_data.keys())[i]
                sales_data_value = sales_data.get(sales_data_key, "Unknown")
                # print(sales_data_value)
                revenue_val = sales_data_value.get('revenue', 0)
                cogs_val = sales_data_value.get('cogs', 0)
                # revenue_key = list(sales_data_value.keys())[0]
                # revenue_val = sales_data_value.get(revenue_key, 0)
                # cogs_key = list(sales_data_value.keys())[1]
                # cogs_val = sales_data_value.get(cogs_key, 0)

                # print(revenue_val, cogs_val)
                # print(type(revenue_val))
                if(revenue_val!="None"):
                    if(revenue_val- cogs_val>0):
                        profit +=1
                    else:
                        loss+=1
            # print("city", city, "profit: ", profit , " loss ", loss)
        
        entry = {
            "city": city,
            "profit_count": profit,
            "loss_count": loss
        }
        # print(json.dumps(entry, separators=(',', ':')))
        # Append the entry to the list
        output_data.append(entry)
    

    i += 1
# print(json.dumps(output_data, indent=0))
output_data.sort(key=lambda x: x['city'])
for entry in output_data:
    print(json.dumps(entry, separators=(',', ':')))