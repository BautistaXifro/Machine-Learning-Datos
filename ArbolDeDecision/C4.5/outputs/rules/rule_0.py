def findDecision(obj): #obj[0]: Region, obj[1]: Total_Amount, obj[2]: Delivery_Year, obj[3]: Delivery_Quarter, obj[4]: Pricing, Delivery_Terms_Approved, obj[5]: Pricing, Delivery_Terms_Quote_Appr
   # {"feature": "Total_Amount", "instances": 3090, "metric_value": 0.9853, "depth": 1}
   if obj[1]<=983875.5657078632:
      # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2689, "metric_value": 0.9463, "depth": 2}
      if obj[4]>0:
         # {"feature": "Region", "instances": 1558, "metric_value": 0.8427, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Delivery_Year", "instances": 623, "metric_value": 0.3186, "depth": 4}
            if obj[2]<=2018:
               # {"feature": "Delivery_Quarter", "instances": 613, "metric_value": 0.2749, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 175, "metric_value": 0.2924, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 161, "metric_value": 0.3358, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 155, "metric_value": 0.2655, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 122, "metric_value": 0.1665, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]>2018:
               # {"feature": "Delivery_Quarter", "instances": 10, "metric_value": 0.8813, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  return 'Closed Lost'
               elif obj[3] == 'Q2':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 359, "metric_value": 0.9666, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 142, "metric_value": 0.942, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 141, "metric_value": 0.9381, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2018:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 100, "metric_value": 0.9507, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 100, "metric_value": 0.9507, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 80, "metric_value": 0.9959, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 71, "metric_value": 0.9964, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9911, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 37, "metric_value": 0.9868, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 37, "metric_value": 0.9868, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 276, "metric_value": 0.9969, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 91, "metric_value": 0.9957, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 91, "metric_value": 0.9957, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 78, "metric_value": 0.9829, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 78, "metric_value": 0.9829, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 60, "metric_value": 0.9928, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 56, "metric_value": 0.9963, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 47, "metric_value": 0.9918, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 47, "metric_value": 0.9918, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Quarter", "instances": 274, "metric_value": 0.9311, "depth": 4}
            if obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 79, "metric_value": 0.9971, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 68, "metric_value": 0.9774, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.684, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 75, "metric_value": 0.9844, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 75, "metric_value": 0.9844, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 68, "metric_value": 0.8338, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 68, "metric_value": 0.8338, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 52, "metric_value": 0.6194, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 52, "metric_value": 0.6194, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 26, "metric_value": 0.7063, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 16, "metric_value": 0.8113, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 16, "metric_value": 0.8113, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            elif obj[3] == 'Q1':
               return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[4]<=0:
         # {"feature": "Region", "instances": 1131, "metric_value": 0.9999, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 313, "metric_value": 0.9073, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 92, "metric_value": 0.8991, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 65, "metric_value": 0.8051, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 27, "metric_value": 0.999, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 90, "metric_value": 0.8024, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 88, "metric_value": 0.8113, "depth": 6}
                  if obj[5]<=0:
                     return 'Closed Won'
                  elif obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2018:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 89, "metric_value": 0.9669, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 49, "metric_value": 0.9486, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 40, "metric_value": 0.9837, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 42, "metric_value": 0.9403, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 34, "metric_value": 0.9082, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 8, "metric_value": 1.0, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Won'
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 292, "metric_value": 0.6284, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Year", "instances": 255, "metric_value": 0.3534, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Delivery_Quarter", "instances": 248, "metric_value": 0.3132, "depth": 6}
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
               elif obj[2]>2018:
                  # {"feature": "Delivery_Quarter", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[3] == 'Q1':
                     return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 37, "metric_value": 0.7532, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 12, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 11, "metric_value": 0.4395, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 10, "metric_value": 0.8813, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Americas':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 262, "metric_value": 0.9796, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Year", "instances": 184, "metric_value": 0.9416, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Delivery_Quarter", "instances": 183, "metric_value": 0.9432, "depth": 6}
                  if obj[3] == 'Q2':
                     return 'Closed Won'
                  elif obj[3] == 'Q1':
                     return 'Closed Won'
                  elif obj[3] == 'Q4':
                     return 'Closed Won'
                  elif obj[3] == 'Q3':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2018:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[5]>0:
               # {"feature": "Delivery_Year", "instances": 78, "metric_value": 0.9924, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Delivery_Quarter", "instances": 74, "metric_value": 0.9953, "depth": 6}
                  if obj[3] == 'Q3':
                     return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2018:
                  # {"feature": "Delivery_Quarter", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[3] == 'Q1':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Quarter", "instances": 262, "metric_value": 0.9618, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 76, "metric_value": 0.9955, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 57, "metric_value": 0.9998, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 19, "metric_value": 0.8997, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 68, "metric_value": 0.9231, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 45, "metric_value": 0.8366, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  elif obj[2]>2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 23, "metric_value": 0.9986, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 63, "metric_value": 0.8631, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 49, "metric_value": 0.8886, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 14, "metric_value": 0.7496, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 55, "metric_value": 0.9299, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 38, "metric_value": 0.6292, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 17, "metric_value": 0.7871, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Won'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 2, "metric_value": 1.0, "depth": 4}
            if obj[3] == 'Q2':
               return 'Closed Lost'
            elif obj[3] == 'Q3':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Won'
   elif obj[1]>983875.5657078632:
      # {"feature": "Delivery_Quarter", "instances": 401, "metric_value": 0.5833, "depth": 2}
      if obj[3] == 'Q3':
         # {"feature": "Delivery_Year", "instances": 118, "metric_value": 0.7116, "depth": 3}
         if obj[2]<=2018:
            # {"feature": "Region", "instances": 113, "metric_value": 0.6326, "depth": 4}
            if obj[0] == 'EMEA':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 52, "metric_value": 0.6647, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 31, "metric_value": 0.6374, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 21, "metric_value": 0.7025, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'Americas':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 50, "metric_value": 0.5294, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 33, "metric_value": 0.4395, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 17, "metric_value": 0.6723, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'APAC':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.8813, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 0.8113, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'Middle East':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[2]>2018:
            return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[3] == 'Q2':
         # {"feature": "Delivery_Year", "instances": 116, "metric_value": 0.5061, "depth": 3}
         if obj[2]<=2018:
            # {"feature": "Region", "instances": 103, "metric_value": 0.547, "depth": 4}
            if obj[0] == 'EMEA':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 41, "metric_value": 0.5349, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 23, "metric_value": 0.6666, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 18, "metric_value": 0.3095, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'Americas':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 38, "metric_value": 0.6292, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 35, "metric_value": 0.661, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'APAC':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 20, "metric_value": 0.2864, "depth": 5}
               if obj[4]>0:
                  return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.5033, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'Japan':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'Middle East':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[2]>2018:
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[3] == 'Q1':
         # {"feature": "Region", "instances": 108, "metric_value": 0.4748, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Delivery_Year", "instances": 55, "metric_value": 0.4972, "depth": 4}
            if obj[2]<=2018:
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 47, "metric_value": 0.551, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 24, "metric_value": 0.4138, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 23, "metric_value": 0.6666, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[2]>2018:
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'EMEA':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 29, "metric_value": 0.2164, "depth": 4}
            if obj[4]>0:
               # {"feature": "Delivery_Year", "instances": 19, "metric_value": 0.2975, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 18, "metric_value": 0.3095, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2018:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[4]<=0:
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 21, "metric_value": 0.4537, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Year", "instances": 20, "metric_value": 0.2864, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 14, "metric_value": 0.3712, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2018:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[5]<=0:
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Japan':
            return 'Closed Won'
         elif obj[0] == 'Middle East':
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[3] == 'Q4':
         # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 59, "metric_value": 0.6162, "depth": 3}
         if obj[5]>0:
            # {"feature": "Region", "instances": 54, "metric_value": 0.5564, "depth": 4}
            if obj[0] == 'Americas':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 26, "metric_value": 0.5159, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.3912, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.6194, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'EMEA':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 16, "metric_value": 0.6962, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Delivery_Year", "instances": 14, "metric_value": 0.5917, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Delivery_Year", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'APAC':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 0.5436, "depth": 5}
               if obj[4]<=0:
                  return 'Closed Lost'
               elif obj[4]>0:
                  # {"feature": "Delivery_Year", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'Japan':
               return 'Closed Lost'
            elif obj[0] == 'Middle East':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[5]<=0:
            # {"feature": "Region", "instances": 5, "metric_value": 0.971, "depth": 4}
            if obj[0] == 'Americas':
               # {"feature": "Delivery_Year", "instances": 4, "metric_value": 1.0, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'EMEA':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   else:
      return 'Closed Lost'
