def findDecision(obj): #obj[0]: Region, obj[1]: Total_Amount, obj[2]: Delivery_Year, obj[3]: Delivery_Quarter, obj[4]: TRF, obj[5]: Pricing, Delivery_Terms_Approved, obj[6]: Pricing, Delivery_Terms_Quote_Appr
   # {"feature": "TRF", "instances": 3017, "metric_value": 0.9896, "depth": 1}
   if obj[4]<=0:
      # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2130, "metric_value": 0.9036, "depth": 2}
      if obj[5]>0:
         # {"feature": "Region", "instances": 1244, "metric_value": 0.7109, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Delivery_Year", "instances": 594, "metric_value": 0.2441, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 406, "metric_value": 0.3239, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 118, "metric_value": 0.2136, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 118, "metric_value": 0.2136, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 108, "metric_value": 0.3463, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 108, "metric_value": 0.3463, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 100, "metric_value": 0.3274, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 100, "metric_value": 0.3274, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 80, "metric_value": 0.4281, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 80, "metric_value": 0.4281, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 242, "metric_value": 0.8568, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 96, "metric_value": 0.7766, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 77, "metric_value": 0.7845, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 77, "metric_value": 0.7845, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 19, "metric_value": 0.7425, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 19, "metric_value": 0.7425, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 62, "metric_value": 0.9072, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 43, "metric_value": 0.933, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 43, "metric_value": 0.933, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 19, "metric_value": 0.8315, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 19, "metric_value": 0.8315, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 46, "metric_value": 0.9321, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 41, "metric_value": 0.9012, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 41, "metric_value": 0.9012, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 38, "metric_value": 0.8315, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 26, "metric_value": 0.9612, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 26, "metric_value": 0.9612, "depth": 7}
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
            # {"feature": "Delivery_Quarter", "instances": 214, "metric_value": 0.7922, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 76, "metric_value": 0.8504, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 69, "metric_value": 0.8491, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 69, "metric_value": 0.8491, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 7, "metric_value": 0.8631, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.8631, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 74, "metric_value": 0.6395, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 53, "metric_value": 0.7717, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 53, "metric_value": 0.7717, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 43, "metric_value": 0.8542, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 35, "metric_value": 0.7755, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 35, "metric_value": 0.7755, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 8, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 21, "metric_value": 0.8631, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.4395, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.4395, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 10, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 1.0, "depth": 7}
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
            # {"feature": "Delivery_Quarter", "instances": 178, "metric_value": 1.0, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 61, "metric_value": 0.967, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 55, "metric_value": 0.9806, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 55, "metric_value": 0.9806, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 6, "metric_value": 0.65, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 53, "metric_value": 0.9414, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 48, "metric_value": 0.896, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 48, "metric_value": 0.896, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 33, "metric_value": 0.9673, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 18, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 18, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 15, "metric_value": 0.8366, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 15, "metric_value": 0.8366, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 31, "metric_value": 0.9812, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 29, "metric_value": 0.9923, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 29, "metric_value": 0.9923, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 16, "metric_value": 0.9544, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Total_Amount", "instances": 8, "metric_value": 0.8113, "depth": 5}
               if obj[1]<=1150892.3943513408:
                  # {"feature": "Delivery_Year", "instances": 8, "metric_value": 0.8113, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Total_Amount", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[1]<=1150892.3943513408:
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
               # {"feature": "Total_Amount", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[1]<=1150892.3943513408:
                  # {"feature": "Delivery_Year", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Lost'
      elif obj[5]<=0:
         # {"feature": "Region", "instances": 886, "metric_value": 0.9999, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 287, "metric_value": 0.4723, "depth": 4}
            if obj[6]>0:
               # {"feature": "Delivery_Year", "instances": 261, "metric_value": 0.2345, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Delivery_Quarter", "instances": 240, "metric_value": 0.0695, "depth": 6}
                  if obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 132, "metric_value": 0.0643, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     # {"feature": "Total_Amount", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 21, "metric_value": 0.9587, "depth": 6}
                  if obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     # {"feature": "Total_Amount", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q3':
                     # {"feature": "Total_Amount", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Lost'
            elif obj[6]<=0:
               # {"feature": "Delivery_Quarter", "instances": 26, "metric_value": 0.8404, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.8905, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.9457, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 6, "metric_value": 0.65, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]>2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Year", "instances": 226, "metric_value": 0.8538, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 175, "metric_value": 0.8848, "depth": 5}
               if obj[6]<=0:
                  # {"feature": "Delivery_Quarter", "instances": 119, "metric_value": 0.9438, "depth": 6}
                  if obj[3] == 'Q3':
                     # {"feature": "Total_Amount", "instances": 47, "metric_value": 0.7467, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 27, "metric_value": 0.9911, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q2':
                     # {"feature": "Total_Amount", "instances": 24, "metric_value": 0.995, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q4':
                     # {"feature": "Total_Amount", "instances": 21, "metric_value": 0.9984, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[6]>0:
                  # {"feature": "Delivery_Quarter", "instances": 56, "metric_value": 0.6769, "depth": 6}
                  if obj[3] == 'Q2':
                     # {"feature": "Total_Amount", "instances": 23, "metric_value": 0.4262, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 19, "metric_value": 0.2975, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q3':
                     # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.994, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     # {"feature": "Total_Amount", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 51, "metric_value": 0.714, "depth": 5}
               if obj[6]<=0:
                  # {"feature": "Delivery_Quarter", "instances": 46, "metric_value": 0.6153, "depth": 6}
                  if obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 21, "metric_value": 0.7025, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q2':
                     # {"feature": "Total_Amount", "instances": 10, "metric_value": 0.7219, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q4':
                     # {"feature": "Total_Amount", "instances": 10, "metric_value": 0.469, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q3':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[6]>0:
                  # {"feature": "Delivery_Quarter", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[3] == 'Q3':
                     # {"feature": "Total_Amount", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 217, "metric_value": 0.8807, "depth": 4}
            if obj[6]<=0:
               # {"feature": "Delivery_Year", "instances": 154, "metric_value": 0.7955, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 146, "metric_value": 0.771, "depth": 6}
                  if obj[3] == 'Q4':
                     # {"feature": "Total_Amount", "instances": 43, "metric_value": 0.7824, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q2':
                     # {"feature": "Total_Amount", "instances": 37, "metric_value": 0.7532, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q3':
                     # {"feature": "Total_Amount", "instances": 34, "metric_value": 0.6024, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 32, "metric_value": 0.896, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 8, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Delivery_Quarter", "instances": 8, "metric_value": 1.0, "depth": 7}
                     if obj[3] == 'Q3':
                        return 'Closed Won'
                     elif obj[3] == 'Q4':
                        return 'Closed Won'
                     elif obj[3] == 'Q1':
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[6]>0:
               # {"feature": "Delivery_Quarter", "instances": 63, "metric_value": 0.9911, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 20, "metric_value": 0.971, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 17, "metric_value": 0.9975, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 19, "metric_value": 0.9819, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 17, "metric_value": 0.9367, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.8905, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.7642, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.8454, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Delivery_Year", "instances": 11, "metric_value": 0.8454, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Won'
         elif obj[0] == 'Americas':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 155, "metric_value": 0.9204, "depth": 4}
            if obj[6]<=0:
               # {"feature": "Delivery_Year", "instances": 116, "metric_value": 0.8498, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 98, "metric_value": 0.8762, "depth": 6}
                  if obj[3] == 'Q2':
                     # {"feature": "Total_Amount", "instances": 40, "metric_value": 0.8485, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 23, "metric_value": 0.7554, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q3':
                     # {"feature": "Total_Amount", "instances": 18, "metric_value": 0.9641, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q4':
                     # {"feature": "Total_Amount", "instances": 17, "metric_value": 0.9367, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Delivery_Quarter", "instances": 18, "metric_value": 0.65, "depth": 6}
                  if obj[3] == 'Q4':
                     # {"feature": "Total_Amount", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q3':
                     # {"feature": "Total_Amount", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q2':
                     return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[6]>0:
               # {"feature": "Delivery_Quarter", "instances": 39, "metric_value": 0.9995, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 12, "metric_value": 0.9799, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.9457, "depth": 7}
                     if obj[1]<=1150892.3943513408:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.9457, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Delivery_Year", "instances": 11, "metric_value": 0.9457, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.9183, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     elif obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 7, "metric_value": 0.8631, "depth": 6}
                  if obj[1]<=1150892.3943513408:
                     # {"feature": "Delivery_Year", "instances": 7, "metric_value": 0.8631, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Middle East':
            return 'Closed Won'
         else:
            return 'Closed Won'
      else:
         return 'Closed Won'
   elif obj[4]>0:
      # {"feature": "Total_Amount", "instances": 887, "metric_value": 0.8407, "depth": 2}
      if obj[1]<=1150892.3943513408:
         # {"feature": "Region", "instances": 527, "metric_value": 0.9477, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 203, "metric_value": 0.9784, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 69, "metric_value": 0.9926, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 56, "metric_value": 1.0, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 33, "metric_value": 0.9834, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 23, "metric_value": 0.9656, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 13, "metric_value": 0.7793, "depth": 6}
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
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 50, "metric_value": 0.8813, "depth": 5}
               if obj[6]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 40, "metric_value": 0.8113, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Delivery_Year", "instances": 28, "metric_value": 0.9059, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     elif obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]<=0:
                     # {"feature": "Delivery_Year", "instances": 12, "metric_value": 0.4138, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[6]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 10, "metric_value": 1.0, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Delivery_Year", "instances": 10, "metric_value": 1.0, "depth": 7}
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
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 48, "metric_value": 0.9685, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 39, "metric_value": 0.9881, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 21, "metric_value": 0.9587, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 18, "metric_value": 1.0, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Won'
                     elif obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 9, "metric_value": 0.7642, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
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
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 36, "metric_value": 0.9978, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 22, "metric_value": 0.9457, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 15, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.8631, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.9403, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Delivery_Year", "instances": 8, "metric_value": 1.0, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     elif obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Delivery_Year", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Won'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Year", "instances": 178, "metric_value": 0.892, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 131, "metric_value": 0.9351, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 53, "metric_value": 0.9414, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 46, "metric_value": 0.8865, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 7, "metric_value": 0.8631, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 37, "metric_value": 0.9953, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 36, "metric_value": 0.9978, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 33, "metric_value": 0.8454, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 21, "metric_value": 0.7919, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 12, "metric_value": 0.9183, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Lost'
                     elif obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 0.5436, "depth": 6}
                  if obj[5]<=0:
                     return 'Closed Lost'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 47, "metric_value": 0.7046, "depth": 5}
               if obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 16, "metric_value": 0.8113, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.8631, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 13, "metric_value": 0.3912, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.469, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 9, "metric_value": 0.9911, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Won'
                     elif obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 101, "metric_value": 0.9309, "depth": 4}
            if obj[6]>0:
               # {"feature": "Delivery_Year", "instances": 74, "metric_value": 0.966, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 57, "metric_value": 0.9183, "depth": 6}
                  if obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 20, "metric_value": 0.971, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     elif obj[5]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 18, "metric_value": 0.9183, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 14, "metric_value": 0.8631, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     elif obj[5]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Delivery_Quarter", "instances": 17, "metric_value": 0.9774, "depth": 6}
                  if obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 0.9544, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     elif obj[5]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[6]<=0:
               # {"feature": "Delivery_Quarter", "instances": 27, "metric_value": 0.7642, "depth": 5}
               if obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 10, "metric_value": 0.7219, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 0.8113, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[5]<=0:
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
            # {"feature": "Delivery_Year", "instances": 27, "metric_value": 0.9911, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 22, "metric_value": 1.0, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 1.0, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
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
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[5]<=0:
                     return 'Closed Lost'
                  elif obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Lost'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Won'
                     elif obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  return 'Closed Won'
               elif obj[3] == 'Q3':
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 18, "metric_value": 0.7642, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 7, "metric_value": 0.8631, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
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
      elif obj[1]>1150892.3943513408:
         # {"feature": "Delivery_Year", "instances": 360, "metric_value": 0.5513, "depth": 3}
         if obj[2]>2016:
            # {"feature": "Region", "instances": 257, "metric_value": 0.3804, "depth": 4}
            if obj[0] == 'Americas':
               # {"feature": "Delivery_Quarter", "instances": 108, "metric_value": 0.1831, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 35, "metric_value": 0.1872, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 22, "metric_value": 0.2668, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 22, "metric_value": 0.4395, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'EMEA':
               # {"feature": "Delivery_Quarter", "instances": 88, "metric_value": 0.5436, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 29, "metric_value": 0.5788, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 12, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 28, "metric_value": 0.4912, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 15, "metric_value": 0.5665, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
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
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 21, "metric_value": 0.2762, "depth": 6}
                  if obj[5]>0:
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
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.8813, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 9, "metric_value": 0.9183, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[0] == 'APAC':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 55, "metric_value": 0.4395, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Delivery_Quarter", "instances": 30, "metric_value": 0.2108, "depth": 6}
                  if obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 12, "metric_value": 0.4138, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  # {"feature": "Delivery_Quarter", "instances": 25, "metric_value": 0.6343, "depth": 6}
                  if obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Lost'
                     elif obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 7}
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
            elif obj[0] == 'Japan':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[2]<=2016:
            # {"feature": "Delivery_Quarter", "instances": 103, "metric_value": 0.83, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Region", "instances": 32, "metric_value": 0.8571, "depth": 5}
               if obj[0] == 'Americas':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 19, "metric_value": 0.8997, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.9457, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'EMEA':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 9, "metric_value": 0.9183, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.9544, "depth": 7}
                     if obj[6]>0:
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
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 29, "metric_value": 0.6632, "depth": 5}
               if obj[6]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 27, "metric_value": 0.6052, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Region", "instances": 20, "metric_value": 0.7219, "depth": 7}
                     if obj[0] == 'EMEA':
                        return 'Closed Lost'
                     elif obj[0] == 'Americas':
                        return 'Closed Lost'
                     elif obj[0] == 'APAC':
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[6]<=0:
                  # {"feature": "Region", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[0] == 'Americas':
                     return 'Closed Lost'
                  elif obj[0] == 'EMEA':
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 27, "metric_value": 0.6913, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Region", "instances": 18, "metric_value": 0.5033, "depth": 6}
                  if obj[0] == 'Americas':
                     return 'Closed Lost'
                  elif obj[0] == 'EMEA':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.8631, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  # {"feature": "Region", "instances": 9, "metric_value": 0.9183, "depth": 6}
                  if obj[0] == 'Americas':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[0] == 'APAC':
                     return 'Closed Lost'
                  elif obj[0] == 'EMEA':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Region", "instances": 15, "metric_value": 0.9968, "depth": 5}
               if obj[0] == 'EMEA':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'Americas':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
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
               return 'Closed Won'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   else:
      return 'Closed Lost'
