def findDecision(obj): #obj[0]: Region, obj[1]: Total_Amount, obj[2]: Delivery_Year, obj[3]: Delivery_Quarter, obj[4]: Pricing, Delivery_Terms_Approved, obj[5]: Pricing, Delivery_Terms_Quote_Appr
   # {"feature": "Total_Amount", "instances": 3090, "metric_value": 0.9881, "depth": 1}
   if obj[1]<=1010547.7888215517:
      # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2660, "metric_value": 0.9462, "depth": 2}
      if obj[4]>0:
         # {"feature": "Region", "instances": 1551, "metric_value": 0.8294, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Delivery_Year", "instances": 647, "metric_value": 0.3407, "depth": 4}
            if obj[2]<=2018:
               # {"feature": "Delivery_Quarter", "instances": 638, "metric_value": 0.2871, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 189, "metric_value": 0.2031, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 164, "metric_value": 0.2812, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 147, "metric_value": 0.3837, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 138, "metric_value": 0.2895, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]>2018:
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 381, "metric_value": 0.9566, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 162, "metric_value": 0.9301, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 162, "metric_value": 0.9301, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 96, "metric_value": 0.9544, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 85, "metric_value": 0.9465, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.994, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 88, "metric_value": 0.9257, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 88, "metric_value": 0.9257, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 35, "metric_value": 0.9518, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 35, "metric_value": 0.9518, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 251, "metric_value": 0.9997, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 81, "metric_value": 0.9301, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 81, "metric_value": 0.9301, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 71, "metric_value": 0.9757, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 71, "metric_value": 0.9757, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 55, "metric_value": 0.9979, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 51, "metric_value": 0.9931, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 44, "metric_value": 0.994, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 44, "metric_value": 0.994, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Quarter", "instances": 248, "metric_value": 0.9028, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 79, "metric_value": 0.9005, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 79, "metric_value": 0.9005, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 67, "metric_value": 0.9412, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 61, "metric_value": 0.9127, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 61, "metric_value": 0.967, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 61, "metric_value": 0.967, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 41, "metric_value": 0.6006, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 41, "metric_value": 0.6006, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 24, "metric_value": 0.9799, "depth": 4}
            if obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.9911, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9911, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 8, "metric_value": 1.0, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 1.0, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 4, "metric_value": 1.0, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[4]<=0:
         # {"feature": "Region", "instances": 1109, "metric_value": 0.9998, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 342, "metric_value": 0.9348, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 218, "metric_value": 0.8674, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 71, "metric_value": 0.7698, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 63, "metric_value": 0.8412, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 49, "metric_value": 0.9852, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 35, "metric_value": 0.8224, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 124, "metric_value": 0.9953, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 44, "metric_value": 0.994, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 39, "metric_value": 0.8905, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 31, "metric_value": 0.9383, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 10, "metric_value": 1.0, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Won'
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 295, "metric_value": 0.5904, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 253, "metric_value": 0.2216, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 138, "metric_value": 0.0619, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 63, "metric_value": 0.2762, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 39, "metric_value": 0.2918, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.7793, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 42, "metric_value": 0.7496, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 17, "metric_value": 0.7871, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 17, "metric_value": 0.7871, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Americas':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 254, "metric_value": 0.9762, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 166, "metric_value": 0.9101, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 48, "metric_value": 0.9799, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 45, "metric_value": 0.7642, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  elif obj[2]>2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 41, "metric_value": 0.9012, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 32, "metric_value": 0.9284, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 88, "metric_value": 0.9865, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 27, "metric_value": 0.999, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 24, "metric_value": 0.8113, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 22, "metric_value": 0.994, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 15, "metric_value": 0.971, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 214, "metric_value": 0.9634, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 151, "metric_value": 0.9226, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 44, "metric_value": 0.994, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 42, "metric_value": 0.8926, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 33, "metric_value": 0.8454, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 32, "metric_value": 0.8571, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            elif obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 63, "metric_value": 0.9998, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 21, "metric_value": 0.8631, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 18, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 18, "metric_value": 0.9911, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 6, "metric_value": 0.65, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 4, "metric_value": 0.8113, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1]>1010547.7888215517:
      # {"feature": "Region", "instances": 430, "metric_value": 0.532, "depth": 2}
      if obj[0] == 'Americas':
         # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 192, "metric_value": 0.5859, "depth": 3}
         if obj[5]>0:
            # {"feature": "Delivery_Quarter", "instances": 180, "metric_value": 0.5513, "depth": 4}
            if obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 59, "metric_value": 0.4187, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 50, "metric_value": 0.469, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  elif obj[4]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2018:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 57, "metric_value": 0.6292, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 52, "metric_value": 0.5159, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2018:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 44, "metric_value": 0.6321, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Delivery_Year", "instances": 32, "metric_value": 0.6962, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Delivery_Year", "instances": 12, "metric_value": 0.4138, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 20, "metric_value": 0.469, "depth": 5}
               if obj[4]<=0:
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.6194, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]>0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[5]<=0:
            # {"feature": "Delivery_Quarter", "instances": 12, "metric_value": 0.9183, "depth": 4}
            if obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 6, "metric_value": 1.0, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 1.0, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[0] == 'EMEA':
         # {"feature": "Delivery_Quarter", "instances": 143, "metric_value": 0.546, "depth": 3}
         if obj[3] == 'Q1':
            # {"feature": "Delivery_Year", "instances": 42, "metric_value": 0.4537, "depth": 4}
            if obj[2]<=2018:
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 35, "metric_value": 0.5127, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 32, "metric_value": 0.4489, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[2]>2018:
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[3] == 'Q2':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 39, "metric_value": 0.3912, "depth": 4}
            if obj[4]>0:
               # {"feature": "Delivery_Year", "instances": 31, "metric_value": 0.3451, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 31, "metric_value": 0.3451, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[4]<=0:
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.5436, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[3] == 'Q3':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 36, "metric_value": 0.65, "depth": 4}
            if obj[5]>0:
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 31, "metric_value": 0.7088, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Delivery_Year", "instances": 17, "metric_value": 0.6723, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Delivery_Year", "instances": 14, "metric_value": 0.7496, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[5]<=0:
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[3] == 'Q4':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 26, "metric_value": 0.7063, "depth": 4}
            if obj[4]>0:
               # {"feature": "Delivery_Year", "instances": 18, "metric_value": 0.65, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 18, "metric_value": 0.65, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[4]<=0:
               # {"feature": "Delivery_Year", "instances": 8, "metric_value": 0.8113, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.8113, "depth": 6}
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
      elif obj[0] == 'APAC':
         # {"feature": "Delivery_Quarter", "instances": 79, "metric_value": 0.2329, "depth": 3}
         if obj[3] == 'Q3':
            # {"feature": "Delivery_Year", "instances": 26, "metric_value": 0.3912, "depth": 4}
            if obj[2]<=2018:
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 23, "metric_value": 0.4262, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 22, "metric_value": 0.4395, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  elif obj[4]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[2]>2018:
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[3] == 'Q1':
            return 'Closed Lost'
         elif obj[3] == 'Q4':
            return 'Closed Lost'
         elif obj[3] == 'Q2':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 13, "metric_value": 0.3912, "depth": 4}
            if obj[4]<=0:
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[4]>0:
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[0] == 'Japan':
         # {"feature": "Delivery_Quarter", "instances": 11, "metric_value": 0.9457, "depth": 3}
         if obj[3] == 'Q2':
            # {"feature": "Delivery_Year", "instances": 4, "metric_value": 0.8113, "depth": 4}
            if obj[2]<=2018:
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 6}
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
         elif obj[3] == 'Q1':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 0.8113, "depth": 4}
            if obj[4]>0:
               return 'Closed Won'
            elif obj[4]<=0:
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[3] == 'Q4':
            return 'Closed Lost'
         elif obj[3] == 'Q3':
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[0] == 'Middle East':
         return 'Closed Lost'
      else:
         return 'Closed Lost'
   else:
      return 'Closed Lost'
