#!/usr/bin/env python
# coding: utf-8

# In[6]:


#LOT_E - LAX_ParkingJSON
import urllib.request, json 
with urllib.request.urlopen("https://data.lacity.org/resource/xzkr-5anj.json") as url:
    lot_e = json.loads(url.read().decode())[8] ## - lot_e
lst_lot_e= [{"OwnerInfo":"LAX_LotE"},{"AreaID":"laxlote123"},
          {"AreaName":"LAXLotE"}, {"AreaLatLong":[33.935165, -118.374192]},
          {"AreaGeometry":{
                "type": "rectangle",
                "coordinates": [
                    [
                        [33.935743, -118.374893],
                        [33.935737, -118.373474],
                        [33.934564, -118.373475],
                        [33.934549, -118.374892],

                    ]
                ]}}, 
          {"Timestamp":lot_e['dataexportdatetime']},
          {"TotalSpots":lot_e['totalparkingspaces']},{"OccupiedSpots":lot_e['occupied']}]
lot_e_area={"Type":"Area","Attributes":lst_lot_e}

##Lot Description

lot_attr=[]
lot_attr.append({"OwnerInfo":"LAX",
          "LotID":lot_e['key_value'], 
          "LotName":lot_e['parkingname'],
           "LotLatLong":[33.935165, -118.374192], #LotE Coordinates updated - due to source data discrepancies
           "LotGeometry":{
                "type": "rectangle",
                "coordinates": [[33.935743, -118.374893],
                        [33.935737, -118.373474],
                        [33.934564, -118.373475],
                        [33.934549, -118.374892],
] 
           },
             "Timestamp":lot_e['dataexportdatetime'],   
              "TotalSpots":lot_e['totalparkingspaces'],
            "OccupiedSpots":lot_e['occupied']
             })
lot_e_lot={"Type":"Lot","Attributes":lot_attr}

lax_lote_area={"Type":"Area","Attributes":lst_lot_e,"Lots":lot_attr}
lax_lot_e_ParkingJson=json.dumps(lax_lote_area)
print(lax_lot_e_ParkingJson)
 

# In[3]:


# In[ ]:




