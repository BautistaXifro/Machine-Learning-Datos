def findDecision(obj): #obj[0]: Region, obj[1]: Total_Amount, obj[2]: Delivery_Year, obj[3]: Delivery_Quarter, obj[4]: TRF, obj[5]: Pricing, Delivery_Terms_Approved, obj[6]: Pricing, Delivery_Terms_Quote_Appr
   # {"feature": "TRF", "instances": 3017, "metric_value": 0.9858, "depth": 1}
   if obj[4]<=0:
      # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2177, "metric_value": 0.8964, "depth": 2}
      if obj[5]>0:
         # {"feature": "Region", "instances": 1282, "metric_value": 0.7102, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Delivery_Year", "instances": 613, "metric_value": 0.3025, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 439, "metric_value": 0.3766, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 143, "metric_value": 0.339, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 143, "metric_value": 0.339, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 109, "metric_value": 0.4423, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 109, "metric_value": 0.4423, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 102, "metric_value": 0.2822, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 102, "metric_value": 0.2822, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 85, "metric_value": 0.4501, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 85, "metric_value": 0.4501, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 174, "metric_value": 0.051, "depth": 5}
               if obj[3] == 'Q4':
                  return 'Closed Won'
               elif obj[3] == 'Q3':
                  return 'Closed Won'
               elif obj[3] == 'Q2':
                  return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 36, "metric_value": 0.1831, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 36, "metric_value": 0.1831, "depth": 7}
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
            # {"feature": "Delivery_Quarter", "instances": 266, "metric_value": 0.8201, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 116, "metric_value": 0.7355, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 96, "metric_value": 0.7383, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 96, "metric_value": 0.7383, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 20, "metric_value": 0.7219, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 20, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 67, "metric_value": 0.8971, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 41, "metric_value": 0.9789, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 41, "metric_value": 0.9789, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 26, "metric_value": 0.6194, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 26, "metric_value": 0.6194, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 53, "metric_value": 0.8037, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 49, "metric_value": 0.7683, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 49, "metric_value": 0.7683, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 30, "metric_value": 0.9183, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 22, "metric_value": 0.994, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 22, "metric_value": 0.994, "depth": 7}
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
            # {"feature": "Delivery_Year", "instances": 215, "metric_value": 0.8411, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 161, "metric_value": 0.9141, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 57, "metric_value": 0.8791, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 57, "metric_value": 0.8791, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 48, "metric_value": 0.9799, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 48, "metric_value": 0.9799, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 38, "metric_value": 0.8315, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 38, "metric_value": 0.8315, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 18, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 18, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 54, "metric_value": 0.4451, "depth": 5}
               if obj[3] == 'Q3':
                  return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 16, "metric_value": 0.3373, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 16, "metric_value": 0.3373, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 15, "metric_value": 0.7219, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 15, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=1052383.9593815366:
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
            # {"feature": "Delivery_Quarter", "instances": 175, "metric_value": 0.9971, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 59, "metric_value": 0.9647, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 54, "metric_value": 0.9641, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 54, "metric_value": 0.9641, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 47, "metric_value": 0.8787, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 36, "metric_value": 0.8524, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 36, "metric_value": 0.8524, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.9457, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.9457, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 43, "metric_value": 0.9996, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 39, "metric_value": 0.9995, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 39, "metric_value": 0.9995, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Total_Amount", "instances": 26, "metric_value": 0.9612, "depth": 5}
               if obj[1]<=1052383.9593815366:
                  # {"feature": "Delivery_Year", "instances": 26, "metric_value": 0.9612, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.9612, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.9612, "depth": 7}
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
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.9612, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 12, "metric_value": 0.9799, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[5]<=0:
         # {"feature": "Region", "instances": 895, "metric_value": 0.9991, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 275, "metric_value": 0.5499, "depth": 4}
            if obj[6]>0:
               # {"feature": "Delivery_Year", "instances": 245, "metric_value": 0.246, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Delivery_Quarter", "instances": 217, "metric_value": 0.0424, "depth": 6}
                  if obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 120, "metric_value": 0.0695, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 28, "metric_value": 0.9059, "depth": 6}
                  if obj[3] == 'Q2':
                     # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.8454, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     # {"feature": "Total_Amount", "instances": 8, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     # {"feature": "Total_Amount", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Lost'
            elif obj[6]<=0:
               # {"feature": "Delivery_Year", "instances": 30, "metric_value": 0.65, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 21, "metric_value": 0.7919, "depth": 6}
                  if obj[3] == 'Q2':
                     # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.684, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q3':
                     # {"feature": "Total_Amount", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 224, "metric_value": 0.9059, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 65, "metric_value": 0.8512, "depth": 5}
               if obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 52, "metric_value": 0.7444, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 49, "metric_value": 0.7683, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[6]>0:
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.9957, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 8, "metric_value": 0.9544, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 64, "metric_value": 0.8351, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 38, "metric_value": 0.868, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 26, "metric_value": 0.9306, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 12, "metric_value": 0.65, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 26, "metric_value": 0.7793, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 25, "metric_value": 0.7219, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 63, "metric_value": 0.9334, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 49, "metric_value": 0.8631, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 26, "metric_value": 0.7793, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 23, "metric_value": 0.9321, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.9852, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.994, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 32, "metric_value": 0.9972, "depth": 5}
               if obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 28, "metric_value": 0.9666, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 21, "metric_value": 0.9852, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 7, "metric_value": 0.8631, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[6]>0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Quarter", "instances": 199, "metric_value": 0.8434, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 63, "metric_value": 0.9468, "depth": 5}
               if obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 45, "metric_value": 0.971, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 44, "metric_value": 0.9624, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[6]>0:
                  # {"feature": "Delivery_Year", "instances": 18, "metric_value": 0.8524, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 14, "metric_value": 0.9403, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 52, "metric_value": 0.8113, "depth": 5}
               if obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 39, "metric_value": 0.6194, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 31, "metric_value": 0.6374, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[6]>0:
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.9957, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.994, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Total_Amount", "instances": 42, "metric_value": 0.7025, "depth": 5}
               if obj[1]<=1052383.9593815366:
                  # {"feature": "Delivery_Year", "instances": 41, "metric_value": 0.6594, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 37, "metric_value": 0.6395, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Won'
                     elif obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[1]>1052383.9593815366:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 42, "metric_value": 0.7919, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 40, "metric_value": 0.7219, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 30, "metric_value": 0.65, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 10, "metric_value": 0.8813, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Won'
         elif obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 193, "metric_value": 0.9166, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 53, "metric_value": 0.9997, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 43, "metric_value": 0.9965, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 34, "metric_value": 0.9975, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.9911, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.8813, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 50, "metric_value": 0.8267, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 48, "metric_value": 0.8113, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 38, "metric_value": 0.8315, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 10, "metric_value": 0.7219, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=1052383.9593815366:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 49, "metric_value": 0.8346, "depth": 5}
               if obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 38, "metric_value": 0.7897, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 36, "metric_value": 0.8113, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[6]>0:
                  # {"feature": "Delivery_Year", "instances": 11, "metric_value": 0.9457, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 8, "metric_value": 0.8113, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 41, "metric_value": 0.8722, "depth": 5}
               if obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 35, "metric_value": 0.8224, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 24, "metric_value": 0.7383, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.9457, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[6]>0:
                  # {"feature": "Delivery_Year", "instances": 6, "metric_value": 1.0, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=1052383.9593815366:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 4, "metric_value": 1.0, "depth": 4}
            if obj[3] == 'Q3':
               return 'Closed Won'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Won'
      else:
         return 'Closed Won'
   elif obj[4]>0:
      # {"feature": "Total_Amount", "instances": 840, "metric_value": 0.8366, "depth": 2}
      if obj[1]<=1052383.9593815366:
         # {"feature": "Region", "instances": 457, "metric_value": 0.9488, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Delivery_Year", "instances": 171, "metric_value": 0.9891, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 137, "metric_value": 0.9997, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 49, "metric_value": 0.9997, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 32, "metric_value": 0.9972, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 17, "metric_value": 0.9774, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 38, "metric_value": 0.992, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 22, "metric_value": 0.976, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 16, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 25, "metric_value": 0.971, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 18, "metric_value": 0.9183, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 25, "metric_value": 0.971, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 18, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Won'
                     elif obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 34, "metric_value": 0.7871, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 14, "metric_value": 0.7496, "depth": 6}
                  if obj[5]<=0:
                     return 'Closed Lost'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.5033, "depth": 6}
                  if obj[6]>0:
                     return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Year", "instances": 157, "metric_value": 0.8805, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 120, "metric_value": 0.9097, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 45, "metric_value": 0.8673, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 40, "metric_value": 0.8813, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 36, "metric_value": 0.9436, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 22, "metric_value": 0.976, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.8631, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 27, "metric_value": 0.951, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 24, "metric_value": 0.9183, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 12, "metric_value": 0.8113, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Lost'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 37, "metric_value": 0.7532, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 12, "metric_value": 0.65, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 10, "metric_value": 0.469, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 0.9544, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 7, "metric_value": 0.8631, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.8631, "depth": 7}
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
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Quarter", "instances": 87, "metric_value": 0.8498, "depth": 4}
            if obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 28, "metric_value": 0.8631, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 26, "metric_value": 0.8905, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 16, "metric_value": 0.9544, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     elif obj[5]>0:
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
               elif obj[2]<=2016:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 22, "metric_value": 0.8454, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.6194, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.5033, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]>0:
                     # {"feature": "Delivery_Year", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.9911, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 19, "metric_value": 0.4855, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 14, "metric_value": 0.3712, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.5033, "depth": 7}
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
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]>2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 18, "metric_value": 0.9911, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 10, "metric_value": 0.971, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9911, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 8, "metric_value": 1.0, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 35, "metric_value": 0.9852, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Year", "instances": 18, "metric_value": 0.8524, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 13, "metric_value": 0.9612, "depth": 6}
                  if obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 17, "metric_value": 0.9774, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.8631, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     elif obj[2]<=2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Delivery_Year", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Delivery_Year", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[2]<=2016:
                     return 'Closed Won'
                  elif obj[2]>2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 7, "metric_value": 0.8631, "depth": 4}
            if obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 4, "metric_value": 1.0, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[1]>1052383.9593815366:
         # {"feature": "Delivery_Year", "instances": 383, "metric_value": 0.6003, "depth": 3}
         if obj[2]>2016:
            # {"feature": "Delivery_Quarter", "instances": 260, "metric_value": 0.4049, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Region", "instances": 86, "metric_value": 0.4071, "depth": 5}
               if obj[0] == 'EMEA':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 34, "metric_value": 0.5226, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 32, "metric_value": 0.5436, "depth": 7}
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
               elif obj[0] == 'Americas':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 30, "metric_value": 0.3534, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 23, "metric_value": 0.258, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'APAC':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 18, "metric_value": 0.3095, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.5033, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'Middle East':
                  return 'Closed Lost'
               elif obj[0] == 'Japan':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Region", "instances": 72, "metric_value": 0.3095, "depth": 5}
               if obj[0] == 'Americas':
                  return 'Closed Lost'
               elif obj[0] == 'EMEA':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 27, "metric_value": 0.2285, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 19, "metric_value": 0.2975, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'APAC':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 15, "metric_value": 0.5665, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.7642, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'Japan':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Region", "instances": 68, "metric_value": 0.3228, "depth": 5}
               if obj[0] == 'Americas':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 30, "metric_value": 0.2108, "depth": 6}
                  if obj[5]<=0:
                     return 'Closed Lost'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.3912, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'EMEA':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 19, "metric_value": 0.2975, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 12, "metric_value": 0.4138, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'APAC':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 16, "metric_value": 0.5436, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 15, "metric_value": 0.3534, "depth": 7}
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
               elif obj[0] == 'Middle East':
                  return 'Closed Lost'
               elif obj[0] == 'Japan':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 34, "metric_value": 0.6723, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Region", "instances": 19, "metric_value": 0.8997, "depth": 6}
                  if obj[0] == 'Americas':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.9544, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[0] == 'APAC':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[0] == 'EMEA':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[0] == 'Middle East':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]>0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[2]<=2016:
            # {"feature": "Delivery_Quarter", "instances": 123, "metric_value": 0.8616, "depth": 4}
            if obj[3] == 'Q4':
               # {"feature": "Region", "instances": 39, "metric_value": 0.8213, "depth": 5}
               if obj[0] == 'EMEA':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 19, "metric_value": 0.7425, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 15, "metric_value": 0.5665, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[0] == 'Americas':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 12, "metric_value": 0.9183, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9911, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'APAC':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[5]<=0:
                     return 'Closed Lost'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[0] == 'Japan':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Region", "instances": 29, "metric_value": 0.7355, "depth": 5}
               if obj[0] == 'Americas':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 19, "metric_value": 0.8997, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.469, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9911, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[0] == 'EMEA':
                  return 'Closed Lost'
               elif obj[0] == 'Japan':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 28, "metric_value": 0.7496, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Region", "instances": 17, "metric_value": 0.874, "depth": 6}
                  if obj[0] == 'Americas':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.684, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[0] == 'EMEA':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[0] == 'APAC':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]<=0:
                  # {"feature": "Region", "instances": 11, "metric_value": 0.4395, "depth": 6}
                  if obj[0] == 'Americas':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[0] == 'APAC':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Region", "instances": 27, "metric_value": 0.999, "depth": 5}
               if obj[0] == 'Americas':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 11, "metric_value": 0.994, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'EMEA':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.971, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 9, "metric_value": 0.9183, "depth": 7}
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
               elif obj[0] == 'APAC':
                  return 'Closed Lost'
               elif obj[0] == 'Japan':
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   else:
      return 'Closed Lost'
