def findDecision(obj): #obj[0]: Region, obj[1]: Total_Amount, obj[2]: Delivery_Year, obj[3]: Delivery_Quarter, obj[4]: Pricing, Delivery_Terms_Approved, obj[5]: Pricing, Delivery_Terms_Quote_Appr
   # {"feature": "Total_Amount", "instances": 3090, "metric_value": 0.986, "depth": 1}
   if obj[1]<=931477.7482995779:
      # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2669, "metric_value": 0.9464, "depth": 2}
      if obj[4]>0:
         # {"feature": "Region", "instances": 1533, "metric_value": 0.8242, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Delivery_Year", "instances": 670, "metric_value": 0.3263, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 472, "metric_value": 0.404, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 135, "metric_value": 0.3245, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 124, "metric_value": 0.4321, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 122, "metric_value": 0.437, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 91, "metric_value": 0.4295, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 198, "metric_value": 0.0815, "depth": 5}
               if obj[3] == 'Q4':
                  return 'Closed Won'
               elif obj[3] == 'Q2':
                  return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 45, "metric_value": 0.1537, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 40, "metric_value": 0.1687, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 371, "metric_value": 0.9852, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 153, "metric_value": 0.9807, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 127, "metric_value": 0.9621, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 26, "metric_value": 0.9829, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 92, "metric_value": 0.9877, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 67, "metric_value": 0.9986, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 25, "metric_value": 0.9044, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 90, "metric_value": 0.9968, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 73, "metric_value": 0.9966, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 17, "metric_value": 0.9975, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 36, "metric_value": 0.9436, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 26, "metric_value": 0.9957, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.469, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Quarter", "instances": 241, "metric_value": 0.8584, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 73, "metric_value": 0.783, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 66, "metric_value": 0.799, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 72, "metric_value": 0.7885, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 48, "metric_value": 0.8709, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 24, "metric_value": 0.5436, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 58, "metric_value": 0.9991, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 54, "metric_value": 1.0, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 38, "metric_value": 0.6292, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 23, "metric_value": 0.5586, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 15, "metric_value": 0.7219, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 230, "metric_value": 0.9999, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 80, "metric_value": 0.9959, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 67, "metric_value": 0.9998, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.8905, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 58, "metric_value": 0.9294, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 44, "metric_value": 0.9457, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.8631, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 54, "metric_value": 0.9751, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 51, "metric_value": 0.9662, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 38, "metric_value": 1.0, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 27, "metric_value": 0.999, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.994, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 21, "metric_value": 0.8631, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 8, "metric_value": 0.9544, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.9544, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 6}
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
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[4]<=0:
         # {"feature": "Region", "instances": 1136, "metric_value": 0.9998, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 324, "metric_value": 0.9273, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 209, "metric_value": 0.8586, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 68, "metric_value": 0.6723, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 68, "metric_value": 0.8918, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 44, "metric_value": 0.9624, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 29, "metric_value": 0.8936, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 115, "metric_value": 0.9934, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 44, "metric_value": 0.9457, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 31, "metric_value": 0.9072, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 30, "metric_value": 0.8366, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 10, "metric_value": 0.8813, "depth": 6}
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
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 299, "metric_value": 0.4594, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Year", "instances": 269, "metric_value": 0.174, "depth": 5}
               if obj[2]<=2016:
                  return 'Closed Lost'
               elif obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 32, "metric_value": 0.7579, "depth": 6}
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
               else:
                  return 'Closed Lost'
            elif obj[5]<=0:
               # {"feature": "Delivery_Year", "instances": 30, "metric_value": 0.8366, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 22, "metric_value": 0.9024, "depth": 6}
                  if obj[3] == 'Q3':
                     return 'Closed Won'
                  elif obj[3] == 'Q1':
                     return 'Closed Won'
                  elif obj[3] == 'Q2':
                     return 'Closed Won'
                  elif obj[3] == 'Q4':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Delivery_Quarter", "instances": 8, "metric_value": 0.5436, "depth": 6}
                  if obj[3] == 'Q1':
                     return 'Closed Won'
                  elif obj[3] == 'Q3':
                     return 'Closed Won'
                  elif obj[3] == 'Q2':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Americas':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 270, "metric_value": 0.979, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 176, "metric_value": 0.9544, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 54, "metric_value": 0.951, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 49, "metric_value": 0.9313, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 38, "metric_value": 0.9495, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 35, "metric_value": 0.9852, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 94, "metric_value": 0.9997, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 34, "metric_value": 0.99, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 24, "metric_value": 0.995, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 22, "metric_value": 0.9457, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 14, "metric_value": 0.8631, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Quarter", "instances": 237, "metric_value": 0.9225, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 67, "metric_value": 0.8603, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 49, "metric_value": 0.5917, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 18, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 61, "metric_value": 0.8537, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 39, "metric_value": 0.7321, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 22, "metric_value": 0.976, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 59, "metric_value": 0.9998, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 50, "metric_value": 1.0, "depth": 6}
                  if obj[5]<=0:
                     return 'Closed Won'
                  elif obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9911, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 50, "metric_value": 0.8555, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 34, "metric_value": 0.8338, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 16, "metric_value": 0.896, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 6, "metric_value": 0.9183, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            elif obj[3] == 'Q4':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1]>931477.7482995779:
      # {"feature": "Delivery_Year", "instances": 421, "metric_value": 0.6149, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Delivery_Quarter", "instances": 318, "metric_value": 0.5369, "depth": 3}
         if obj[3] == 'Q2':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 96, "metric_value": 0.4821, "depth": 4}
            if obj[5]>0:
               # {"feature": "Region", "instances": 83, "metric_value": 0.5307, "depth": 5}
               if obj[0] == 'EMEA':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 35, "metric_value": 0.316, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'Americas':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 31, "metric_value": 0.6374, "depth": 6}
                  if obj[4]>0:
                     return 'Closed Lost'
                  elif obj[4]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'APAC':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 15, "metric_value": 0.7219, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  elif obj[4]>0:
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
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[3] == 'Q3':
            # {"feature": "Region", "instances": 93, "metric_value": 0.5244, "depth": 4}
            if obj[0] == 'Americas':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 37, "metric_value": 0.5714, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 28, "metric_value": 0.5917, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.5033, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'EMEA':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 29, "metric_value": 0.4798, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 16, "metric_value": 0.5436, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.3912, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'APAC':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 23, "metric_value": 0.5586, "depth": 5}
               if obj[4]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 18, "metric_value": 0.65, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]>0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'Japan':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[3] == 'Q1':
            # {"feature": "Region", "instances": 79, "metric_value": 0.4318, "depth": 4}
            if obj[0] == 'Americas':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 31, "metric_value": 0.2056, "depth": 5}
               if obj[4]<=0:
                  return 'Closed Lost'
               elif obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.4395, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'EMEA':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 25, "metric_value": 0.7219, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 22, "metric_value": 0.7732, "depth": 6}
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
               return 'Closed Lost'
            elif obj[0] == 'Japan':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[4]<=0:
                  return 'Closed Lost'
               elif obj[4]>0:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[0] == 'Middle East':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[3] == 'Q4':
            # {"feature": "Region", "instances": 50, "metric_value": 0.7602, "depth": 4}
            if obj[0] == 'EMEA':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 19, "metric_value": 0.9495, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 18, "metric_value": 0.9641, "depth": 6}
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
            elif obj[0] == 'Americas':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 17, "metric_value": 0.7871, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9911, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'APAC':
               return 'Closed Lost'
            elif obj[0] == 'Japan':
               return 'Closed Lost'
            elif obj[0] == 'Middle East':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 103, "metric_value": 0.7995, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 44, "metric_value": 0.8757, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 21, "metric_value": 0.9183, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.9612, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.8113, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 12, "metric_value": 0.9183, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 10, "metric_value": 0.7219, "depth": 6}
                  if obj[4]<=0:
                     return 'Closed Lost'
                  elif obj[4]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[4]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 39, "metric_value": 0.679, "depth": 4}
            if obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 16, "metric_value": 0.896, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.971, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.65, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 10, "metric_value": 0.469, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.5436, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 0.65, "depth": 5}
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
            # {"feature": "Delivery_Quarter", "instances": 14, "metric_value": 0.3712, "depth": 4}
            if obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 0.65, "depth": 5}
               if obj[4]>0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[4]<=0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            elif obj[3] == 'Q1':
               return 'Closed Lost'
            elif obj[3] == 'Q3':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Japan':
            # {"feature": "Delivery_Quarter", "instances": 5, "metric_value": 0.7219, "depth": 4}
            if obj[3] == 'Q1':
               return 'Closed Won'
            elif obj[3] == 'Q2':
               return 'Closed Won'
            elif obj[3] == 'Q3':
               return 'Closed Won'
            elif obj[3] == 'Q4':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Middle East':
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   else:
      return 'Closed Lost'
