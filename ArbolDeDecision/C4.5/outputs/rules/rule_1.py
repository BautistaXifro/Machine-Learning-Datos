def findDecision(obj): #obj[0]: Region, obj[1]: Total_Amount, obj[2]: Delivery_Year, obj[3]: Delivery_Quarter, obj[4]: Pricing, Delivery_Terms_Approved, obj[5]: Pricing, Delivery_Terms_Quote_Appr
   # {"feature": "Total_Amount", "instances": 3090, "metric_value": 0.9876, "depth": 1}
   if obj[1]<=944524.6739269885:
      # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2649, "metric_value": 0.9431, "depth": 2}
      if obj[4]>0:
         # {"feature": "Region", "instances": 1519, "metric_value": 0.8198, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Delivery_Year", "instances": 620, "metric_value": 0.2999, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 419, "metric_value": 0.3893, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 130, "metric_value": 0.3335, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 107, "metric_value": 0.3835, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 97, "metric_value": 0.4457, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 85, "metric_value": 0.4104, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 201, "metric_value": 0.0452, "depth": 5}
               if obj[3] == 'Q4':
                  return 'Closed Won'
               elif obj[3] == 'Q1':
                  return 'Closed Won'
               elif obj[3] == 'Q2':
                  return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 42, "metric_value": 0.1623, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 368, "metric_value": 0.9673, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 128, "metric_value": 0.896, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 107, "metric_value": 0.8429, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 21, "metric_value": 0.9984, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 102, "metric_value": 0.9956, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 77, "metric_value": 0.9999, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 25, "metric_value": 0.9427, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 97, "metric_value": 0.9938, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 87, "metric_value": 0.9923, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 1.0, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 41, "metric_value": 0.9262, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 25, "metric_value": 0.9896, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 16, "metric_value": 0.6962, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 258, "metric_value": 0.9989, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 83, "metric_value": 0.9991, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 72, "metric_value": 0.9994, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.994, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 73, "metric_value": 0.9605, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 59, "metric_value": 0.9238, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.9852, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 56, "metric_value": 0.9769, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 51, "metric_value": 0.9774, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 46, "metric_value": 0.9877, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 30, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 16, "metric_value": 0.9544, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Quarter", "instances": 252, "metric_value": 0.8734, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 77, "metric_value": 0.7616, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 68, "metric_value": 0.8113, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 67, "metric_value": 0.8795, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 46, "metric_value": 0.9321, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 21, "metric_value": 0.7025, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 67, "metric_value": 0.9986, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 60, "metric_value": 0.9992, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 41, "metric_value": 0.5349, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 28, "metric_value": 0.5917, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.3912, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 21, "metric_value": 0.9852, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.9911, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9911, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 8, "metric_value": 0.9544, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.9544, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            elif obj[3] == 'Q4':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Lost'
      elif obj[4]<=0:
         # {"feature": "Region", "instances": 1130, "metric_value": 1.0, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 307, "metric_value": 0.9205, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 98, "metric_value": 0.9003, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 68, "metric_value": 0.6723, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 30, "metric_value": 0.9481, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 88, "metric_value": 0.9865, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 66, "metric_value": 0.9673, "depth": 6}
                  if obj[5]<=0:
                     return 'Closed Won'
                  elif obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 22, "metric_value": 0.994, "depth": 6}
                  if obj[5]<=0:
                     return 'Closed Won'
                  elif obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 86, "metric_value": 0.7401, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 64, "metric_value": 0.662, "depth": 6}
                  if obj[5]<=0:
                     return 'Closed Won'
                  elif obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 22, "metric_value": 0.9024, "depth": 6}
                  if obj[5]<=0:
                     return 'Closed Won'
                  elif obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 35, "metric_value": 0.9947, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 22, "metric_value": 0.9024, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.8905, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Won'
         elif obj[0] == 'Americas':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 286, "metric_value": 0.9722, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 181, "metric_value": 0.8988, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 51, "metric_value": 0.874, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 49, "metric_value": 0.8031, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 48, "metric_value": 0.9799, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 33, "metric_value": 0.885, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[5]>0:
               # {"feature": "Delivery_Year", "instances": 105, "metric_value": 0.9921, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 81, "metric_value": 0.9999, "depth": 6}
                  if obj[3] == 'Q1':
                     return 'Closed Won'
                  elif obj[3] == 'Q3':
                     return 'Closed Won'
                  elif obj[3] == 'Q2':
                     return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Delivery_Quarter", "instances": 24, "metric_value": 0.8113, "depth": 6}
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
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Japan':
            # {"feature": "Delivery_Year", "instances": 274, "metric_value": 0.5093, "depth": 4}
            if obj[2]<=2016:
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 224, "metric_value": 0.0736, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Delivery_Quarter", "instances": 222, "metric_value": 0.0416, "depth": 6}
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
               elif obj[5]<=0:
                  # {"feature": "Delivery_Quarter", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[3] == 'Q3':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[2]>2016:
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 50, "metric_value": 0.9815, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Delivery_Quarter", "instances": 25, "metric_value": 0.9988, "depth": 6}
                  if obj[3] == 'Q2':
                     return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     return 'Closed Won'
                  elif obj[3] == 'Q4':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  # {"feature": "Delivery_Quarter", "instances": 25, "metric_value": 0.9044, "depth": 6}
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
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 257, "metric_value": 0.9714, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Year", "instances": 171, "metric_value": 0.9123, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 163, "metric_value": 0.8894, "depth": 6}
                  if obj[3] == 'Q4':
                     return 'Closed Won'
                  elif obj[3] == 'Q2':
                     return 'Closed Won'
                  elif obj[3] == 'Q3':
                     return 'Closed Won'
                  elif obj[3] == 'Q1':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Delivery_Quarter", "instances": 8, "metric_value": 0.8113, "depth": 6}
                  if obj[3] == 'Q3':
                     return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 86, "metric_value": 0.9937, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 26, "metric_value": 0.9829, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 24, "metric_value": 0.9544, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 22, "metric_value": 0.7732, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 14, "metric_value": 0.9852, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 6, "metric_value": 1.0, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 4, "metric_value": 1.0, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            elif obj[3] == 'Q1':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1]>944524.6739269885:
      # {"feature": "Delivery_Year", "instances": 441, "metric_value": 0.5299, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 319, "metric_value": 0.3621, "depth": 3}
         if obj[5]>0:
            # {"feature": "Region", "instances": 296, "metric_value": 0.3307, "depth": 4}
            if obj[0] == 'Americas':
               # {"feature": "Delivery_Quarter", "instances": 123, "metric_value": 0.3151, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 41, "metric_value": 0.1654, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  elif obj[4]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 38, "metric_value": 0.3985, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 34, "metric_value": 0.3228, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 10, "metric_value": 0.469, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  elif obj[4]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'EMEA':
               # {"feature": "Delivery_Quarter", "instances": 109, "metric_value": 0.3785, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 38, "metric_value": 0.3985, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 30, "metric_value": 0.2108, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 30, "metric_value": 0.469, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 11, "metric_value": 0.4395, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'APAC':
               # {"feature": "Delivery_Quarter", "instances": 52, "metric_value": 0.2352, "depth": 5}
               if obj[3] == 'Q1':
                  return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 15, "metric_value": 0.5665, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  return 'Closed Lost'
               elif obj[3] == 'Q4':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'Japan':
               # {"feature": "Delivery_Quarter", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  elif obj[4]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  return 'Closed Lost'
               elif obj[3] == 'Q4':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'Middle East':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[5]<=0:
            # {"feature": "Delivery_Quarter", "instances": 23, "metric_value": 0.6666, "depth": 4}
            if obj[3] == 'Q4':
               # {"feature": "Region", "instances": 7, "metric_value": 0.8631, "depth": 5}
               if obj[0] == 'Americas':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'APAC':
                  return 'Closed Lost'
               elif obj[0] == 'EMEA':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Region", "instances": 6, "metric_value": 0.65, "depth": 5}
               if obj[0] == 'Americas':
                  return 'Closed Lost'
               elif obj[0] == 'APAC':
                  return 'Closed Won'
               elif obj[0] == 'EMEA':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Region", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[0] == 'EMEA':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'APAC':
                  return 'Closed Lost'
               elif obj[0] == 'Americas':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 122, "metric_value": 0.8177, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 57, "metric_value": 0.9348, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 53, "metric_value": 0.9052, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 16, "metric_value": 0.896, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 16, "metric_value": 0.9544, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 14, "metric_value": 0.7496, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[3] == 'Q3':
                  return 'Closed Won'
               elif obj[3] == 'Q4':
                  return 'Closed Lost'
               elif obj[3] == 'Q1':
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 44, "metric_value": 0.7309, "depth": 4}
            if obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 18, "metric_value": 0.9183, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 17, "metric_value": 0.874, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 10, "metric_value": 0.7219, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.7642, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 0.5436, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Quarter", "instances": 17, "metric_value": 0.3228, "depth": 4}
            if obj[3] == 'Q4':
               return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[4]<=0:
                  return 'Closed Lost'
               elif obj[4]>0:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Japan':
            # {"feature": "Delivery_Quarter", "instances": 4, "metric_value": 0.8113, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               return 'Closed Lost'
            elif obj[3] == 'Q3':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   else:
      return 'Closed Lost'
