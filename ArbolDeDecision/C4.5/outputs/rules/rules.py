def findDecision(obj): #obj[0]: Region, obj[1]: Total_Amount, obj[2]: Delivery_Year, obj[3]: Delivery_Quarter, obj[4]: TRF, obj[5]: Pricing, Delivery_Terms_Approved, obj[6]: Pricing, Delivery_Terms_Quote_Appr
   # {"feature": "TRF", "instances": 15083, "metric_value": 0.9848, "depth": 1}
   if obj[4]<=2.1466551746999936:
      # {"feature": "Total_Amount", "instances": 13223, "metric_value": 0.9471, "depth": 2}
      if obj[1]<=959840.9042772575:
         # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 13067, "metric_value": 0.9431, "depth": 3}
         if obj[5]>0:
            # {"feature": "Region", "instances": 7565, "metric_value": 0.8191, "depth": 4}
            if obj[0] == 'Japan':
               # {"feature": "Delivery_Year", "instances": 3134, "metric_value": 0.3042, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 2198, "metric_value": 0.3813, "depth": 6}
                  if obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 651, "metric_value": 0.3271, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 556, "metric_value": 0.3927, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 555, "metric_value": 0.406, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 436, "metric_value": 0.4112, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Delivery_Quarter", "instances": 936, "metric_value": 0.0636, "depth": 6}
                  if obj[3] == 'Q4':
                     return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 221, "metric_value": 0.1037, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 217, "metric_value": 0.1052, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 209, "metric_value": 0.0438, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[0] == 'EMEA':
               # {"feature": "Delivery_Quarter", "instances": 1770, "metric_value": 0.9696, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 689, "metric_value": 0.9313, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 574, "metric_value": 0.905, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 115, "metric_value": 0.9986, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 481, "metric_value": 0.9898, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 364, "metric_value": 0.9982, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 117, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 388, "metric_value": 0.9849, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 343, "metric_value": 0.9852, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 45, "metric_value": 0.9825, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 212, "metric_value": 0.9767, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 154, "metric_value": 0.9995, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 58, "metric_value": 0.7355, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[0] == 'APAC':
               # {"feature": "Delivery_Year", "instances": 1288, "metric_value": 0.859, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 936, "metric_value": 0.9183, "depth": 6}
                  if obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 321, "metric_value": 0.8949, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 277, "metric_value": 0.9714, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 258, "metric_value": 0.8933, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 80, "metric_value": 0.8305, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Delivery_Quarter", "instances": 352, "metric_value": 0.6041, "depth": 6}
                  if obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 127, "metric_value": 0.5463, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 123, "metric_value": 0.4067, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 64, "metric_value": 0.7579, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 38, "metric_value": 0.8997, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[0] == 'Americas':
               # {"feature": "Delivery_Quarter", "instances": 1261, "metric_value": 0.9997, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 407, "metric_value": 0.9947, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 366, "metric_value": 0.9964, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 41, "metric_value": 0.965, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 364, "metric_value": 0.9863, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 289, "metric_value": 0.9808, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 75, "metric_value": 0.9988, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 274, "metric_value": 1.0, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 249, "metric_value": 0.9994, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 25, "metric_value": 0.9044, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 216, "metric_value": 0.9978, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 150, "metric_value": 0.9918, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 66, "metric_value": 0.9973, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            elif obj[0] == 'Middle East':
               # {"feature": "Delivery_Quarter", "instances": 112, "metric_value": 0.9325, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 49, "metric_value": 0.9633, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 49, "metric_value": 0.9633, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 27, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 27, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 20, "metric_value": 0.6098, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 20, "metric_value": 0.6098, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 16, "metric_value": 1.0, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[5]<=0:
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5502, "metric_value": 0.9999, "depth": 4}
            if obj[6]<=0:
               # {"feature": "Delivery_Year", "instances": 2857, "metric_value": 0.8917, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 2412, "metric_value": 0.9058, "depth": 6}
                  if obj[3] == 'Q3':
                     # {"feature": "Region", "instances": 699, "metric_value": 0.8521, "depth": 7}
                     if obj[0] == 'EMEA':
                        return 'Closed Won'
                     elif obj[0] == 'APAC':
                        return 'Closed Won'
                     elif obj[0] == 'Americas':
                        return 'Closed Won'
                     elif obj[0] == 'Japan':
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q2':
                     # {"feature": "Region", "instances": 682, "metric_value": 0.9658, "depth": 7}
                     if obj[0] == 'Americas':
                        return 'Closed Won'
                     elif obj[0] == 'APAC':
                        return 'Closed Won'
                     elif obj[0] == 'EMEA':
                        return 'Closed Won'
                     elif obj[0] == 'Japan':
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Region", "instances": 569, "metric_value": 0.8547, "depth": 7}
                     if obj[0] == 'APAC':
                        return 'Closed Won'
                     elif obj[0] == 'Americas':
                        return 'Closed Won'
                     elif obj[0] == 'EMEA':
                        return 'Closed Won'
                     elif obj[0] == 'Japan':
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q4':
                     # {"feature": "Region", "instances": 462, "metric_value": 0.9204, "depth": 7}
                     if obj[0] == 'APAC':
                        return 'Closed Won'
                     elif obj[0] == 'Americas':
                        return 'Closed Won'
                     elif obj[0] == 'EMEA':
                        return 'Closed Won'
                     elif obj[0] == 'Japan':
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Region", "instances": 445, "metric_value": 0.7958, "depth": 6}
                  if obj[0] == 'EMEA':
                     # {"feature": "Delivery_Quarter", "instances": 225, "metric_value": 0.8431, "depth": 7}
                     if obj[3] == 'Q1':
                        return 'Closed Won'
                     elif obj[3] == 'Q2':
                        return 'Closed Won'
                     elif obj[3] == 'Q4':
                        return 'Closed Won'
                     elif obj[3] == 'Q3':
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[0] == 'Americas':
                     # {"feature": "Delivery_Quarter", "instances": 134, "metric_value": 0.6781, "depth": 7}
                     if obj[3] == 'Q4':
                        return 'Closed Won'
                     elif obj[3] == 'Q3':
                        return 'Closed Won'
                     elif obj[3] == 'Q1':
                        return 'Closed Won'
                     elif obj[3] == 'Q2':
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[0] == 'APAC':
                     # {"feature": "Delivery_Quarter", "instances": 44, "metric_value": 0.994, "depth": 7}
                     if obj[3] == 'Q3':
                        return 'Closed Won'
                     elif obj[3] == 'Q4':
                        return 'Closed Lost'
                     elif obj[3] == 'Q1':
                        return 'Closed Lost'
                     elif obj[3] == 'Q2':
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[0] == 'Japan':
                     # {"feature": "Delivery_Quarter", "instances": 42, "metric_value": 0.2762, "depth": 7}
                     if obj[3] == 'Q1':
                        return 'Closed Won'
                     elif obj[3] == 'Q3':
                        return 'Closed Won'
                     elif obj[3] == 'Q2':
                        return 'Closed Won'
                     elif obj[3] == 'Q4':
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[6]>0:
               # {"feature": "Delivery_Year", "instances": 2645, "metric_value": 0.8582, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Region", "instances": 1363, "metric_value": 0.3134, "depth": 6}
                  if obj[0] == 'Japan':
                     # {"feature": "Delivery_Quarter", "instances": 1136, "metric_value": 0.0541, "depth": 7}
                     if obj[3] == 'Q1':
                        return 'Closed Lost'
                     elif obj[3] == 'Q2':
                        return 'Closed Lost'
                     elif obj[3] == 'Q3':
                        return 'Closed Lost'
                     elif obj[3] == 'Q4':
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[0] == 'EMEA':
                     # {"feature": "Delivery_Quarter", "instances": 78, "metric_value": 0.7321, "depth": 7}
                     if obj[3] == 'Q3':
                        return 'Closed Lost'
                     elif obj[3] == 'Q2':
                        return 'Closed Lost'
                     elif obj[3] == 'Q4':
                        return 'Closed Lost'
                     elif obj[3] == 'Q1':
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[0] == 'Americas':
                     # {"feature": "Delivery_Quarter", "instances": 78, "metric_value": 0.8905, "depth": 7}
                     if obj[3] == 'Q2':
                        return 'Closed Lost'
                     elif obj[3] == 'Q3':
                        return 'Closed Lost'
                     elif obj[3] == 'Q4':
                        return 'Closed Lost'
                     elif obj[3] == 'Q1':
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[0] == 'APAC':
                     # {"feature": "Delivery_Quarter", "instances": 71, "metric_value": 0.9826, "depth": 7}
                     if obj[3] == 'Q2':
                        return 'Closed Won'
                     elif obj[3] == 'Q3':
                        return 'Closed Lost'
                     elif obj[3] == 'Q4':
                        return 'Closed Lost'
                     elif obj[3] == 'Q1':
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2016:
                  # {"feature": "Region", "instances": 1282, "metric_value": 0.9986, "depth": 6}
                  if obj[0] == 'EMEA':
                     # {"feature": "Delivery_Quarter", "instances": 461, "metric_value": 0.9463, "depth": 7}
                     if obj[3] == 'Q2':
                        return 'Closed Won'
                     elif obj[3] == 'Q1':
                        return 'Closed Won'
                     elif obj[3] == 'Q3':
                        return 'Closed Lost'
                     elif obj[3] == 'Q4':
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[0] == 'Americas':
                     # {"feature": "Delivery_Quarter", "instances": 344, "metric_value": 0.9998, "depth": 7}
                     if obj[3] == 'Q3':
                        return 'Closed Won'
                     elif obj[3] == 'Q1':
                        return 'Closed Lost'
                     elif obj[3] == 'Q2':
                        return 'Closed Lost'
                     elif obj[3] == 'Q4':
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[0] == 'APAC':
                     # {"feature": "Delivery_Quarter", "instances": 308, "metric_value": 0.9999, "depth": 7}
                     if obj[3] == 'Q1':
                        return 'Closed Won'
                     elif obj[3] == 'Q3':
                        return 'Closed Lost'
                     elif obj[3] == 'Q2':
                        return 'Closed Lost'
                     elif obj[3] == 'Q4':
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[0] == 'Japan':
                     # {"feature": "Delivery_Quarter", "instances": 147, "metric_value": 0.9113, "depth": 7}
                     if obj[3] == 'Q3':
                        return 'Closed Lost'
                     elif obj[3] == 'Q2':
                        return 'Closed Lost'
                     elif obj[3] == 'Q1':
                        return 'Closed Lost'
                     elif obj[3] == 'Q4':
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[0] == 'Middle East':
                     # {"feature": "Delivery_Quarter", "instances": 22, "metric_value": 0.9024, "depth": 7}
                     if obj[3] == 'Q3':
                        return 'Closed Lost'
                     elif obj[3] == 'Q2':
                        return 'Closed Lost'
                     elif obj[3] == 'Q4':
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[1]>959840.9042772575:
         # {"feature": "Region", "instances": 156, "metric_value": 0.7564, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Delivery_Year", "instances": 70, "metric_value": 0.9403, "depth": 4}
            if obj[2]<=2016:
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 41, "metric_value": 0.9961, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Delivery_Quarter", "instances": 26, "metric_value": 0.9612, "depth": 6}
                  if obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.9957, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  # {"feature": "Delivery_Quarter", "instances": 15, "metric_value": 0.971, "depth": 6}
                  if obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     return 'Closed Won'
                  elif obj[3] == 'Q3':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]>2016:
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 29, "metric_value": 0.7355, "depth": 5}
               if obj[6]>0:
                  # {"feature": "Delivery_Quarter", "instances": 21, "metric_value": 0.4537, "depth": 6}
                  if obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 10, "metric_value": 0.469, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[6]<=0:
                  # {"feature": "Delivery_Quarter", "instances": 8, "metric_value": 1.0, "depth": 6}
                  if obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'EMEA':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 54, "metric_value": 0.4451, "depth": 4}
            if obj[6]>0:
               # {"feature": "Delivery_Quarter", "instances": 46, "metric_value": 0.3478, "depth": 5}
               if obj[3] == 'Q2':
                  return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 14, "metric_value": 0.3712, "depth": 6}
                  if obj[2]<=2016:
                     return 'Closed Lost'
                  elif obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 11, "metric_value": 0.4395, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]>2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]>2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[6]<=0:
               # {"feature": "Delivery_Quarter", "instances": 8, "metric_value": 0.8113, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  return 'Closed Lost'
               elif obj[3] == 'Q3':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'APAC':
            return 'Closed Lost'
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 13, "metric_value": 0.8905, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 10, "metric_value": 0.971, "depth": 5}
               if obj[3] == 'Q3':
                  return 'Closed Lost'
               elif obj[3] == 'Q1':
                  return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[5]<=0:
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Middle East':
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[4]>2.1466551746999936:
      # {"feature": "Delivery_Year", "instances": 1860, "metric_value": 0.5577, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Total_Amount", "instances": 1339, "metric_value": 0.4277, "depth": 3}
         if obj[1]>959840.9042772575:
            # {"feature": "Region", "instances": 1313, "metric_value": 0.4101, "depth": 4}
            if obj[0] == 'Americas':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 538, "metric_value": 0.3179, "depth": 5}
               if obj[6]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 491, "metric_value": 0.2728, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Delivery_Quarter", "instances": 294, "metric_value": 0.2303, "depth": 7}
                     if obj[3] == 'Q3':
                        return 'Closed Lost'
                     elif obj[3] == 'Q2':
                        return 'Closed Lost'
                     elif obj[3] == 'Q1':
                        return 'Closed Lost'
                     elif obj[3] == 'Q4':
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Delivery_Quarter", "instances": 197, "metric_value": 0.3311, "depth": 7}
                     if obj[3] == 'Q1':
                        return 'Closed Lost'
                     elif obj[3] == 'Q3':
                        return 'Closed Lost'
                     elif obj[3] == 'Q4':
                        return 'Closed Lost'
                     elif obj[3] == 'Q2':
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[6]<=0:
                  # {"feature": "Delivery_Quarter", "instances": 47, "metric_value": 0.6582, "depth": 6}
                  if obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 17, "metric_value": 0.9367, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 14, "metric_value": 0.3712, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'EMEA':
               # {"feature": "Delivery_Quarter", "instances": 459, "metric_value": 0.5413, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 152, "metric_value": 0.5054, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 142, "metric_value": 0.4866, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 10, "metric_value": 0.7219, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 137, "metric_value": 0.4284, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 133, "metric_value": 0.4372, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 117, "metric_value": 0.5757, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 109, "metric_value": 0.578, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 53, "metric_value": 0.7717, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 49, "metric_value": 0.8031, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'APAC':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 271, "metric_value": 0.3236, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Quarter", "instances": 142, "metric_value": 0.4179, "depth": 6}
                  if obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 46, "metric_value": 0.4262, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 40, "metric_value": 0.5436, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 29, "metric_value": 0.2164, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 27, "metric_value": 0.3809, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]>0:
                  # {"feature": "Delivery_Quarter", "instances": 129, "metric_value": 0.1994, "depth": 6}
                  if obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 40, "metric_value": 0.1687, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 36, "metric_value": 0.3095, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 16, "metric_value": 0.3373, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'Japan':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 28, "metric_value": 0.5917, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Delivery_Quarter", "instances": 15, "metric_value": 0.8366, "depth": 6}
                  if obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'Middle East':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[1]<=959840.9042772575:
            # {"feature": "Delivery_Quarter", "instances": 26, "metric_value": 0.9306, "depth": 4}
            if obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 10, "metric_value": 0.8813, "depth": 5}
               if obj[5]>0:
                  return 'Closed Won'
               elif obj[5]<=0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 0.8113, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Region", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[0] == 'Americas':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[0] == 'APAC':
                     return 'Closed Lost'
                  elif obj[0] == 'EMEA':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]<=2016:
         # {"feature": "Total_Amount", "instances": 521, "metric_value": 0.7949, "depth": 3}
         if obj[1]>959840.9042772575:
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 482, "metric_value": 0.8226, "depth": 4}
            if obj[6]>0:
               # {"feature": "Region", "instances": 465, "metric_value": 0.8104, "depth": 5}
               if obj[0] == 'Americas':
                  # {"feature": "Delivery_Quarter", "instances": 216, "metric_value": 0.8459, "depth": 6}
                  if obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 69, "metric_value": 0.9321, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 69, "metric_value": 0.6329, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 52, "metric_value": 0.7444, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 26, "metric_value": 1.0, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     elif obj[5]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'EMEA':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 179, "metric_value": 0.786, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Delivery_Quarter", "instances": 148, "metric_value": 0.8113, "depth": 7}
                     if obj[3] == 'Q4':
                        return 'Closed Lost'
                     elif obj[3] == 'Q2':
                        return 'Closed Lost'
                     elif obj[3] == 'Q3':
                        return 'Closed Lost'
                     elif obj[3] == 'Q1':
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Delivery_Quarter", "instances": 31, "metric_value": 0.6374, "depth": 7}
                     if obj[3] == 'Q4':
                        return 'Closed Lost'
                     elif obj[3] == 'Q1':
                        return 'Closed Lost'
                     elif obj[3] == 'Q2':
                        return 'Closed Lost'
                     elif obj[3] == 'Q3':
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'APAC':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 64, "metric_value": 0.662, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Delivery_Quarter", "instances": 33, "metric_value": 0.9183, "depth": 7}
                     if obj[3] == 'Q4':
                        return 'Closed Lost'
                     elif obj[3] == 'Q2':
                        return 'Closed Lost'
                     elif obj[3] == 'Q1':
                        return 'Closed Lost'
                     elif obj[3] == 'Q3':
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'Japan':
                  return 'Closed Won'
               elif obj[0] == 'Middle East':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[6]<=0:
               # {"feature": "Region", "instances": 17, "metric_value": 0.9975, "depth": 5}
               if obj[0] == 'Americas':
                  # {"feature": "Delivery_Quarter", "instances": 10, "metric_value": 0.8813, "depth": 6}
                  if obj[3] == 'Q3':
                     return 'Closed Won'
                  elif obj[3] == 'Q1':
                     return 'Closed Won'
                  elif obj[3] == 'Q4':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'EMEA':
                  # {"feature": "Delivery_Quarter", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[3] == 'Q3':
                     return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[1]<=959840.9042772575:
            # {"feature": "Region", "instances": 39, "metric_value": 0.172, "depth": 4}
            if obj[0] == 'Americas':
               return 'Closed Lost'
            elif obj[0] == 'EMEA':
               return 'Closed Lost'
            elif obj[0] == 'Japan':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[5]<=0:
                  return 'Closed Lost'
               elif obj[5]>0:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[0] == 'APAC':
               return 'Closed Lost'
            elif obj[0] == 'Middle East':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   else:
      return 'Closed Lost'
