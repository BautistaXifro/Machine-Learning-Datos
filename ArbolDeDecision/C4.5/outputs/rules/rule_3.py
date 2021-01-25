def findDecision(obj): #obj[0]: Region, obj[1]: Total_Amount, obj[2]: Delivery_Year, obj[3]: Delivery_Quarter, obj[4]: Pricing, Delivery_Terms_Approved, obj[5]: Pricing, Delivery_Terms_Quote_Appr
   # {"feature": "Total_Amount", "instances": 3090, "metric_value": 0.9888, "depth": 1}
   if obj[1]<=998280.1686031374:
      # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2658, "metric_value": 0.9505, "depth": 2}
      if obj[4]>0:
         # {"feature": "Region", "instances": 1545, "metric_value": 0.8376, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Delivery_Year", "instances": 622, "metric_value": 0.3254, "depth": 4}
            if obj[2]<=2018:
               # {"feature": "Delivery_Quarter", "instances": 613, "metric_value": 0.2888, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 193, "metric_value": 0.2941, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 147, "metric_value": 0.3049, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 147, "metric_value": 0.2762, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 126, "metric_value": 0.2762, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]>2018:
               # {"feature": "Delivery_Quarter", "instances": 9, "metric_value": 0.9183, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.9544, "depth": 6}
                  if obj[5]>0:
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
            # {"feature": "Delivery_Year", "instances": 366, "metric_value": 0.9559, "depth": 4}
            if obj[2]<=2018:
               # {"feature": "Delivery_Quarter", "instances": 354, "metric_value": 0.9507, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 120, "metric_value": 0.9264, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 99, "metric_value": 0.9607, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 84, "metric_value": 0.9403, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 51, "metric_value": 0.9864, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]>2018:
               # {"feature": "Delivery_Quarter", "instances": 12, "metric_value": 0.9799, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 12, "metric_value": 0.9799, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 274, "metric_value": 1.0, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 89, "metric_value": 0.9846, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 89, "metric_value": 0.9846, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 81, "metric_value": 0.9946, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 81, "metric_value": 0.9946, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 66, "metric_value": 0.9894, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 59, "metric_value": 0.9831, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 38, "metric_value": 0.992, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 38, "metric_value": 0.992, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Quarter", "instances": 259, "metric_value": 0.9208, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 77, "metric_value": 0.7845, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 77, "metric_value": 0.7845, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 74, "metric_value": 0.9227, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 74, "metric_value": 0.9227, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 64, "metric_value": 0.9937, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 57, "metric_value": 0.9998, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2018:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 44, "metric_value": 0.7309, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 44, "metric_value": 0.7309, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 24, "metric_value": 0.9544, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.9183, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[4]<=0:
         # {"feature": "Region", "instances": 1113, "metric_value": 0.9996, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 299, "metric_value": 0.9409, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 184, "metric_value": 0.88, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 60, "metric_value": 0.8113, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 57, "metric_value": 0.8997, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 48, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 19, "metric_value": 0.8997, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 115, "metric_value": 0.9934, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 38, "metric_value": 0.7897, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 35, "metric_value": 0.9947, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 30, "metric_value": 0.9871, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 12, "metric_value": 0.9799, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Won'
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 297, "metric_value": 0.6382, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 260, "metric_value": 0.4182, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 135, "metric_value": 0.2285, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 75, "metric_value": 0.4898, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 41, "metric_value": 0.6006, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 37, "metric_value": 0.878, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 16, "metric_value": 0.6962, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 8, "metric_value": 0.9544, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 8, "metric_value": 0.9544, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 263, "metric_value": 0.9373, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 184, "metric_value": 0.8439, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 58, "metric_value": 0.9689, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 51, "metric_value": 0.8974, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 46, "metric_value": 0.5586, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 29, "metric_value": 0.6632, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 79, "metric_value": 0.9943, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 25, "metric_value": 0.971, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 23, "metric_value": 0.9321, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 18, "metric_value": 0.9641, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.9957, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 250, "metric_value": 0.9977, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 78, "metric_value": 0.9957, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 47, "metric_value": 0.9997, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 31, "metric_value": 0.9629, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 66, "metric_value": 0.9894, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 41, "metric_value": 0.9892, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 25, "metric_value": 0.9896, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 62, "metric_value": 0.988, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 32, "metric_value": 0.896, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  elif obj[2]>2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 30, "metric_value": 0.9871, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 44, "metric_value": 0.994, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 35, "metric_value": 0.9994, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
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
   elif obj[1]>998280.1686031374:
      # {"feature": "Region", "instances": 432, "metric_value": 0.5934, "depth": 2}
      if obj[0] == 'Americas':
         # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 189, "metric_value": 0.6052, "depth": 3}
         if obj[5]>0:
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 166, "metric_value": 0.5307, "depth": 4}
            if obj[4]>0:
               # {"feature": "Delivery_Quarter", "instances": 92, "metric_value": 0.4262, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 32, "metric_value": 0.4489, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 29, "metric_value": 0.3621, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 20, "metric_value": 0.2864, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 11, "metric_value": 0.684, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[4]<=0:
               # {"feature": "Delivery_Quarter", "instances": 74, "metric_value": 0.6395, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 26, "metric_value": 0.6194, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 19, "metric_value": 0.7425, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 16, "metric_value": 0.6962, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.3912, "depth": 6}
                  if obj[2]<=2018:
                     return 'Closed Lost'
                  elif obj[2]>2018:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[5]<=0:
            # {"feature": "Delivery_Quarter", "instances": 23, "metric_value": 0.9321, "depth": 4}
            if obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Lost'
      elif obj[0] == 'EMEA':
         # {"feature": "Delivery_Year", "instances": 150, "metric_value": 0.6944, "depth": 3}
         if obj[2]<=2018:
            # {"feature": "Delivery_Quarter", "instances": 140, "metric_value": 0.7219, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 45, "metric_value": 0.5033, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 44, "metric_value": 0.5108, "depth": 6}
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
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 42, "metric_value": 0.7496, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 39, "metric_value": 0.679, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 29, "metric_value": 0.8498, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 20, "metric_value": 0.8113, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 24, "metric_value": 0.8113, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 19, "metric_value": 0.7425, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[2]>2018:
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[0] == 'APAC':
         # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 79, "metric_value": 0.3404, "depth": 3}
         if obj[4]<=0:
            # {"feature": "Delivery_Quarter", "instances": 46, "metric_value": 0.1511, "depth": 4}
            if obj[3] == 'Q3':
               return 'Closed Lost'
            elif obj[3] == 'Q4':
               return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.3912, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.5033, "depth": 6}
                  if obj[5]>0:
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
            else:
               return 'Closed Lost'
         elif obj[4]>0:
            # {"feature": "Delivery_Quarter", "instances": 33, "metric_value": 0.5328, "depth": 4}
            if obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 12, "metric_value": 0.4138, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.4395, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2018:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[2]<=2018:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 6}
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
      elif obj[0] == 'Japan':
         # {"feature": "Delivery_Quarter", "instances": 11, "metric_value": 0.4395, "depth": 3}
         if obj[3] == 'Q2':
            return 'Closed Lost'
         elif obj[3] == 'Q1':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[4]<=0:
               return 'Closed Lost'
            elif obj[4]>0:
               return 'Closed Won'
            else:
               return 'Closed Won'
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
