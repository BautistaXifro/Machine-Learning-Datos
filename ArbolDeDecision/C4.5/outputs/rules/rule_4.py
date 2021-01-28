def findDecision(obj): #obj[0]: Region, obj[1]: Total_Amount, obj[2]: Delivery_Year, obj[3]: Delivery_Quarter, obj[4]: TRF, obj[5]: Pricing, Delivery_Terms_Approved, obj[6]: Pricing, Delivery_Terms_Quote_Appr
   # {"feature": "TRF", "instances": 3017, "metric_value": 0.9891, "depth": 1}
   if obj[4]<=0:
      # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2141, "metric_value": 0.8928, "depth": 2}
      if obj[5]>0:
         # {"feature": "Region", "instances": 1208, "metric_value": 0.6988, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Delivery_Year", "instances": 566, "metric_value": 0.2288, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 386, "metric_value": 0.2941, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 118, "metric_value": 0.2531, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 118, "metric_value": 0.2531, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 92, "metric_value": 0.3478, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 92, "metric_value": 0.3478, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 89, "metric_value": 0.1551, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 89, "metric_value": 0.1551, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 87, "metric_value": 0.4038, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 87, "metric_value": 0.4038, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 180, "metric_value": 0.0496, "depth": 5}
               if obj[3] == 'Q4':
                  return 'Closed Won'
               elif obj[3] == 'Q1':
                  return 'Closed Won'
               elif obj[3] == 'Q2':
                  return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 32, "metric_value": 0.2006, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 32, "metric_value": 0.2006, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 255, "metric_value": 0.8479, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 90, "metric_value": 0.8024, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 75, "metric_value": 0.7478, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 75, "metric_value": 0.7478, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 15, "metric_value": 0.971, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 15, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 69, "metric_value": 0.9656, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 64, "metric_value": 0.9422, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 64, "metric_value": 0.9422, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 66, "metric_value": 0.684, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 50, "metric_value": 0.7602, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 50, "metric_value": 0.7602, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 16, "metric_value": 0.3373, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 16, "metric_value": 0.3373, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 30, "metric_value": 0.8813, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 26, "metric_value": 0.9306, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 26, "metric_value": 0.9306, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2016:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Year", "instances": 219, "metric_value": 0.7416, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 162, "metric_value": 0.8256, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 54, "metric_value": 0.8524, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 54, "metric_value": 0.8524, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 52, "metric_value": 0.7444, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 52, "metric_value": 0.7444, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 42, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 42, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 14, "metric_value": 0.5917, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.5917, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 57, "metric_value": 0.3666, "depth": 5}
               if obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 24, "metric_value": 0.4138, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 24, "metric_value": 0.4138, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 10, "metric_value": 0.469, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.469, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 157, "metric_value": 0.9986, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 65, "metric_value": 0.971, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 57, "metric_value": 0.973, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 57, "metric_value": 0.973, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 8, "metric_value": 0.9544, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.9544, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 47, "metric_value": 0.9441, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 38, "metric_value": 0.9268, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 38, "metric_value": 0.9268, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.9911, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9911, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 23, "metric_value": 0.9986, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 20, "metric_value": 0.9928, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 20, "metric_value": 0.9928, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 22, "metric_value": 0.9457, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 13, "metric_value": 0.7793, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.7793, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.9911, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9911, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 11, "metric_value": 0.684, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Total_Amount", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[1]<=983943.4112074913:
                  # {"feature": "Delivery_Year", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Total_Amount", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[1]<=983943.4112074913:
                  # {"feature": "Delivery_Year", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               return 'Closed Lost'
            elif obj[3] == 'Q4':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[5]<=0:
         # {"feature": "Region", "instances": 933, "metric_value": 0.9967, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 280, "metric_value": 0.5436, "depth": 4}
            if obj[6]>0:
               # {"feature": "Delivery_Year", "instances": 253, "metric_value": 0.2401, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Delivery_Quarter", "instances": 226, "metric_value": 0.041, "depth": 6}
                  if obj[3] == 'Q1':
                     return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 27, "metric_value": 0.9183, "depth": 6}
                  if obj[3] == 'Q3':
                     # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     # {"feature": "Total_Amount", "instances": 8, "metric_value": 0.9544, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 7, "metric_value": 0.8631, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     # {"feature": "Total_Amount", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[6]<=0:
               # {"feature": "Delivery_Year", "instances": 27, "metric_value": 0.3809, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 21, "metric_value": 0.2762, "depth": 6}
                  if obj[3] == 'Q2':
                     # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.5033, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     return 'Closed Won'
                  elif obj[3] == 'Q4':
                     return 'Closed Won'
                  elif obj[3] == 'Q3':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Delivery_Quarter", "instances": 6, "metric_value": 0.65, "depth": 6}
                  if obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q2':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 252, "metric_value": 0.8113, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 84, "metric_value": 0.7713, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 73, "metric_value": 0.6759, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 59, "metric_value": 0.6565, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 14, "metric_value": 0.7496, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.994, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 73, "metric_value": 0.5763, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 59, "metric_value": 0.5255, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 40, "metric_value": 0.6098, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 19, "metric_value": 0.2975, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.7496, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 10, "metric_value": 0.7219, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 63, "metric_value": 0.9016, "depth": 5}
               if obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 41, "metric_value": 0.9262, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 28, "metric_value": 0.9403, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 13, "metric_value": 0.8905, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[6]>0:
                  # {"feature": "Delivery_Year", "instances": 22, "metric_value": 0.8454, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 21, "metric_value": 0.7919, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 32, "metric_value": 0.9887, "depth": 5}
               if obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 24, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 13, "metric_value": 0.9612, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.8454, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[6]>0:
                  # {"feature": "Delivery_Year", "instances": 8, "metric_value": 0.8113, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Total_Amount", "instances": 212, "metric_value": 0.8836, "depth": 4}
            if obj[1]<=983943.4112074913:
               # {"feature": "Delivery_Quarter", "instances": 211, "metric_value": 0.8795, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 63, "metric_value": 0.9468, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 56, "metric_value": 0.9666, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Won'
                     elif obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 53, "metric_value": 0.8595, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 50, "metric_value": 0.8267, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Won'
                     elif obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 50, "metric_value": 0.8267, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Delivery_Year", "instances": 40, "metric_value": 0.7692, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     elif obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Delivery_Year", "instances": 10, "metric_value": 0.971, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     elif obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 45, "metric_value": 0.8366, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 38, "metric_value": 0.7425, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Won'
                     elif obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            elif obj[1]>983943.4112074913:
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Americas':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 188, "metric_value": 0.9147, "depth": 4}
            if obj[6]<=0:
               # {"feature": "Delivery_Year", "instances": 145, "metric_value": 0.8498, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 121, "metric_value": 0.8882, "depth": 6}
                  if obj[3] == 'Q3':
                     # {"feature": "Total_Amount", "instances": 37, "metric_value": 0.878, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 37, "metric_value": 0.878, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q2':
                     # {"feature": "Total_Amount", "instances": 31, "metric_value": 0.9629, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q4':
                     # {"feature": "Total_Amount", "instances": 16, "metric_value": 0.6962, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Delivery_Quarter", "instances": 24, "metric_value": 0.5436, "depth": 6}
                  if obj[3] == 'Q4':
                     # {"feature": "Total_Amount", "instances": 18, "metric_value": 0.65, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q3':
                     return 'Closed Won'
                  elif obj[3] == 'Q2':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[6]>0:
               # {"feature": "Delivery_Quarter", "instances": 43, "metric_value": 0.9996, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 13, "metric_value": 0.8905, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.8905, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.994, "depth": 6}
                  if obj[1]<=983943.4112074913:
                     # {"feature": "Delivery_Year", "instances": 11, "metric_value": 0.994, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 10, "metric_value": 1.0, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.9911, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=983943.4112074913:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Middle East':
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Won'
   elif obj[4]>0:
      # {"feature": "Total_Amount", "instances": 876, "metric_value": 0.8058, "depth": 2}
      if obj[1]<=983943.4112074913:
         # {"feature": "Region", "instances": 486, "metric_value": 0.9444, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 194, "metric_value": 0.8602, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 64, "metric_value": 0.6962, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 57, "metric_value": 0.7425, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 46, "metric_value": 0.7936, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 11, "metric_value": 0.4395, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 57, "metric_value": 0.8997, "depth": 5}
               if obj[6]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 47, "metric_value": 0.785, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Delivery_Year", "instances": 37, "metric_value": 0.8419, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     elif obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]<=0:
                     # {"feature": "Delivery_Year", "instances": 10, "metric_value": 0.469, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     elif obj[2]<=2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 10, "metric_value": 0.8813, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 10, "metric_value": 0.8813, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 50, "metric_value": 0.8555, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 30, "metric_value": 0.65, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 29, "metric_value": 0.5788, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 20, "metric_value": 0.9928, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.9457, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.7642, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 23, "metric_value": 0.9986, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 12, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.8631, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Lost'
                     elif obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Lost'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 11, "metric_value": 0.9457, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 171, "metric_value": 0.9944, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 51, "metric_value": 0.9975, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 38, "metric_value": 0.9819, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 23, "metric_value": 0.9877, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 15, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 13, "metric_value": 0.9612, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 49, "metric_value": 0.9925, "depth": 5}
               if obj[6]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 38, "metric_value": 0.9819, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Delivery_Year", "instances": 22, "metric_value": 0.994, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     elif obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]<=0:
                     # {"feature": "Delivery_Year", "instances": 16, "metric_value": 0.9544, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     elif obj[2]<=2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 11, "metric_value": 0.994, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 11, "metric_value": 0.994, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 44, "metric_value": 0.976, "depth": 5}
               if obj[6]>0:
                  # {"feature": "Delivery_Year", "instances": 38, "metric_value": 0.9495, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 35, "metric_value": 0.9275, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 27, "metric_value": 0.9751, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 19, "metric_value": 0.998, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 15, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 8, "metric_value": 0.5436, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Lost'
                     elif obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 75, "metric_value": 0.8893, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 46, "metric_value": 0.7554, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 16, "metric_value": 0.5436, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.5917, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Lost'
                     elif obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.8454, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Delivery_Year", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     elif obj[2]<=2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Delivery_Year", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 10, "metric_value": 0.7219, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Lost'
                     elif obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9183, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Delivery_Year", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     elif obj[2]<=2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 29, "metric_value": 0.9923, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.7642, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 29, "metric_value": 0.9923, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 15, "metric_value": 0.8366, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  return 'Closed Won'
               elif obj[3] == 'Q2':
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 14, "metric_value": 0.9403, "depth": 5}
               if obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     elif obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[6]<=0:
                     return 'Closed Lost'
                  elif obj[6]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Year", "instances": 17, "metric_value": 0.7871, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 15, "metric_value": 0.5665, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 0.5436, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[2]<=2016:
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Lost'
      elif obj[1]>983943.4112074913:
         # {"feature": "Delivery_Year", "instances": 390, "metric_value": 0.4771, "depth": 3}
         if obj[2]>2016:
            # {"feature": "Region", "instances": 275, "metric_value": 0.3625, "depth": 4}
            if obj[0] == 'Americas':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 117, "metric_value": 0.215, "depth": 5}
               if obj[6]>0:
                  # {"feature": "Delivery_Quarter", "instances": 107, "metric_value": 0.134, "depth": 6}
                  if obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 37, "metric_value": 0.1793, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     elif obj[5]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 32, "metric_value": 0.2006, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[6]<=0:
                  # {"feature": "Delivery_Quarter", "instances": 10, "metric_value": 0.7219, "depth": 6}
                  if obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'EMEA':
               # {"feature": "Delivery_Quarter", "instances": 96, "metric_value": 0.5136, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 38, "metric_value": 0.3985, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 37, "metric_value": 0.406, "depth": 7}
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
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 29, "metric_value": 0.2164, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.3912, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 17, "metric_value": 0.874, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.8631, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 12, "metric_value": 0.65, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'APAC':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 56, "metric_value": 0.3014, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Quarter", "instances": 28, "metric_value": 0.4912, "depth": 6}
                  if obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]>0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'Japan':
               # {"feature": "Delivery_Quarter", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'Middle East':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[2]<=2016:
            # {"feature": "Region", "instances": 115, "metric_value": 0.6858, "depth": 4}
            if obj[0] == 'Americas':
               # {"feature": "Delivery_Quarter", "instances": 48, "metric_value": 0.8427, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 17, "metric_value": 0.874, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 15, "metric_value": 0.9183, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 14, "metric_value": 0.8631, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 12, "metric_value": 0.65, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 10, "metric_value": 0.7219, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     elif obj[5]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'EMEA':
               # {"feature": "Delivery_Quarter", "instances": 44, "metric_value": 0.5108, "depth": 5}
               if obj[3] == 'Q2':
                  return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 10, "metric_value": 0.469, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 9, "metric_value": 0.7642, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 9, "metric_value": 0.7642, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'APAC':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 22, "metric_value": 0.5746, "depth": 5}
               if obj[5]<=0:
                  return 'Closed Lost'
               elif obj[5]>0:
                  # {"feature": "Delivery_Quarter", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[3] == 'Q3':
                     return 'Closed Won'
                  elif obj[3] == 'Q2':
                     return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'Japan':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   else:
      return 'Closed Lost'
