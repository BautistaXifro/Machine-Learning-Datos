def findDecision(obj): #obj[0]: Region, obj[1]: Total_Amount, obj[2]: Delivery_Year, obj[3]: Delivery_Quarter, obj[4]: TRF, obj[5]: Pricing, Delivery_Terms_Approved, obj[6]: Pricing, Delivery_Terms_Quote_Appr
   # {"feature": "TRF", "instances": 3017, "metric_value": 0.9872, "depth": 1}
   if obj[4]<=0:
      # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2154, "metric_value": 0.896, "depth": 2}
      if obj[5]>0:
         # {"feature": "Region", "instances": 1252, "metric_value": 0.6812, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Delivery_Year", "instances": 606, "metric_value": 0.2913, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 419, "metric_value": 0.354, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 134, "metric_value": 0.3553, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 134, "metric_value": 0.3553, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 103, "metric_value": 0.3583, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 103, "metric_value": 0.3583, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 100, "metric_value": 0.3659, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 100, "metric_value": 0.3659, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 82, "metric_value": 0.3313, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 82, "metric_value": 0.3313, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 187, "metric_value": 0.1186, "depth": 5}
               if obj[3] == 'Q4':
                  return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 45, "metric_value": 0.2623, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 45, "metric_value": 0.2623, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 40, "metric_value": 0.1687, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 40, "metric_value": 0.1687, "depth": 7}
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
            # {"feature": "Delivery_Quarter", "instances": 261, "metric_value": 0.8098, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 97, "metric_value": 0.7136, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 85, "metric_value": 0.6723, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 85, "metric_value": 0.6723, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 12, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 12, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 70, "metric_value": 0.7998, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 56, "metric_value": 0.8384, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 56, "metric_value": 0.8384, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 14, "metric_value": 0.5917, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.5917, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 62, "metric_value": 0.9236, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 53, "metric_value": 0.9245, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 53, "metric_value": 0.9245, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 32, "metric_value": 0.8113, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 24, "metric_value": 0.8113, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 24, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 8, "metric_value": 0.8113, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.8113, "depth": 7}
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
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Year", "instances": 217, "metric_value": 0.7453, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 149, "metric_value": 0.8392, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 46, "metric_value": 0.7554, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 46, "metric_value": 0.7554, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 45, "metric_value": 0.8945, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 45, "metric_value": 0.8945, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 45, "metric_value": 0.8673, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 45, "metric_value": 0.8673, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 13, "metric_value": 0.7793, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.7793, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 68, "metric_value": 0.4306, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 25, "metric_value": 0.4022, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 25, "metric_value": 0.4022, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 25, "metric_value": 0.2423, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 25, "metric_value": 0.2423, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 10, "metric_value": 0.8813, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.8813, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 149, "metric_value": 0.9997, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 59, "metric_value": 0.9998, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 54, "metric_value": 0.996, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 54, "metric_value": 0.996, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 44, "metric_value": 0.9457, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 33, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 33, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.994, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.994, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 25, "metric_value": 0.9044, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 13, "metric_value": 0.8905, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.8905, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 12, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 12, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 21, "metric_value": 0.9984, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 19, "metric_value": 0.998, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 19, "metric_value": 0.998, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=974328.6423495198:
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
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 19, "metric_value": 0.9819, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Total_Amount", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[1]<=974328.6423495198:
                  # {"feature": "Delivery_Year", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Total_Amount", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[1]<=974328.6423495198:
                  # {"feature": "Delivery_Year", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
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
            elif obj[3] == 'Q2':
               # {"feature": "Total_Amount", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[1]<=974328.6423495198:
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
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[5]<=0:
         # {"feature": "Region", "instances": 902, "metric_value": 0.9999, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 289, "metric_value": 0.5891, "depth": 4}
            if obj[6]>0:
               # {"feature": "Delivery_Year", "instances": 255, "metric_value": 0.2565, "depth": 5}
               if obj[2]<=2016:
                  return 'Closed Lost'
               elif obj[2]>2016:
                  # {"feature": "Delivery_Quarter", "instances": 28, "metric_value": 0.9666, "depth": 6}
                  if obj[3] == 'Q3':
                     # {"feature": "Total_Amount", "instances": 12, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q4':
                     # {"feature": "Total_Amount", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[6]<=0:
               # {"feature": "Delivery_Quarter", "instances": 34, "metric_value": 0.5226, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 14, "metric_value": 0.5917, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Delivery_Year", "instances": 14, "metric_value": 0.5917, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Delivery_Year", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Year", "instances": 258, "metric_value": 0.9103, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 202, "metric_value": 0.8776, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 73, "metric_value": 0.7587, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 58, "metric_value": 0.7007, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 15, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 52, "metric_value": 0.9471, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 34, "metric_value": 0.9082, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 18, "metric_value": 0.9911, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 52, "metric_value": 0.8667, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 30, "metric_value": 0.9481, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 22, "metric_value": 0.684, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 25, "metric_value": 0.971, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 21, "metric_value": 0.9587, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 56, "metric_value": 0.9852, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 20, "metric_value": 0.8813, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 20, "metric_value": 0.8813, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.9957, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 10, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.7793, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.684, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.7219, "depth": 6}
                  if obj[6]>0:
                     return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 185, "metric_value": 0.834, "depth": 4}
            if obj[6]<=0:
               # {"feature": "Delivery_Quarter", "instances": 139, "metric_value": 0.7784, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 41, "metric_value": 0.4612, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 38, "metric_value": 0.4855, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 39, "metric_value": 0.9612, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Delivery_Year", "instances": 39, "metric_value": 0.9612, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 30, "metric_value": 0.7219, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 29, "metric_value": 0.7355, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 29, "metric_value": 0.7973, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 27, "metric_value": 0.6913, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            elif obj[6]>0:
               # {"feature": "Delivery_Quarter", "instances": 46, "metric_value": 0.9503, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 15, "metric_value": 0.971, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Delivery_Year", "instances": 14, "metric_value": 0.9852, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     elif obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[1]>974328.6423495198:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.8905, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 12, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.7642, "depth": 6}
                  if obj[2]<=2016:
                     return 'Closed Won'
                  elif obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.7642, "depth": 6}
                  if obj[1]<=974328.6423495198:
                     # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.7642, "depth": 7}
                     if obj[2]>2016:
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
            # {"feature": "Delivery_Year", "instances": 170, "metric_value": 0.9637, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 141, "metric_value": 0.9869, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 41, "metric_value": 0.9961, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 30, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.9457, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 41, "metric_value": 0.9789, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 32, "metric_value": 0.896, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.7642, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 38, "metric_value": 0.9495, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 33, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 21, "metric_value": 0.9984, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 16, "metric_value": 0.9887, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Lost'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 29, "metric_value": 0.6632, "depth": 5}
               if obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 18, "metric_value": 0.3095, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 16, "metric_value": 0.3373, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=974328.6423495198:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      else:
         return 'Closed Won'
   elif obj[4]>0:
      # {"feature": "Total_Amount", "instances": 863, "metric_value": 0.833, "depth": 2}
      if obj[1]<=974328.6423495198:
         # {"feature": "Region", "instances": 460, "metric_value": 0.9642, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Delivery_Year", "instances": 172, "metric_value": 1.0, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 141, "metric_value": 0.9939, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 42, "metric_value": 0.9587, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 27, "metric_value": 0.9911, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 15, "metric_value": 0.8366, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 38, "metric_value": 0.998, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 29, "metric_value": 0.9576, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.7642, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 35, "metric_value": 0.9852, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 18, "metric_value": 0.9911, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Lost'
                     elif obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 17, "metric_value": 0.9774, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 26, "metric_value": 0.9612, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 21, "metric_value": 0.8631, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Won'
                     elif obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 31, "metric_value": 0.8691, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 13, "metric_value": 0.9612, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 0.5436, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 0.65, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[6]<=0:
                     return 'Closed Won'
                  elif obj[6]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 164, "metric_value": 0.8872, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 54, "metric_value": 0.8524, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 47, "metric_value": 0.9035, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 39, "metric_value": 0.9418, "depth": 7}
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
               elif obj[2]<=2016:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 47, "metric_value": 0.8196, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 42, "metric_value": 0.8631, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 35, "metric_value": 0.8224, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 7, "metric_value": 0.9852, "depth": 7}
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
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 36, "metric_value": 0.8524, "depth": 5}
               if obj[6]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 31, "metric_value": 0.7706, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Delivery_Year", "instances": 21, "metric_value": 0.8631, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     elif obj[2]<=2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
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
                  # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 7}
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
               # {"feature": "Delivery_Year", "instances": 27, "metric_value": 0.999, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 14, "metric_value": 0.9403, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9911, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 13, "metric_value": 0.9612, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9911, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Won'
                     elif obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]>0:
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
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 82, "metric_value": 0.8722, "depth": 4}
            if obj[6]>0:
               # {"feature": "Delivery_Quarter", "instances": 58, "metric_value": 0.9124, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 22, "metric_value": 0.9457, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Delivery_Year", "instances": 15, "metric_value": 0.8366, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Delivery_Year", "instances": 7, "metric_value": 0.9852, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 17, "metric_value": 0.9774, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Delivery_Year", "instances": 12, "metric_value": 1.0, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     elif obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]<=0:
                     # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     elif obj[2]<=2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 11, "metric_value": 0.684, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Delivery_Year", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     elif obj[2]<=2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 8, "metric_value": 0.8113, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]>2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[6]<=0:
               # {"feature": "Delivery_Quarter", "instances": 24, "metric_value": 0.7383, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 11, "metric_value": 0.4395, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 10, "metric_value": 0.469, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 7, "metric_value": 0.8631, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 32, "metric_value": 0.9972, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 19, "metric_value": 0.8997, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[6]<=0:
                     return 'Closed Won'
                  elif obj[6]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  return 'Closed Lost'
               elif obj[3] == 'Q1':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 13, "metric_value": 0.6194, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]>2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  return 'Closed Won'
               elif obj[3] == 'Q1':
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 10, "metric_value": 0.7219, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[5]>0:
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
               return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[5]>0:
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
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[1]>974328.6423495198:
         # {"feature": "Delivery_Year", "instances": 403, "metric_value": 0.5339, "depth": 3}
         if obj[2]>2016:
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 279, "metric_value": 0.3451, "depth": 4}
            if obj[5]>0:
               # {"feature": "Region", "instances": 172, "metric_value": 0.2183, "depth": 5}
               if obj[0] == 'Americas':
                  # {"feature": "Delivery_Quarter", "instances": 72, "metric_value": 0.1831, "depth": 6}
                  if obj[3] == 'Q3':
                     return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 24, "metric_value": 0.2499, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.3712, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'EMEA':
                  # {"feature": "Delivery_Quarter", "instances": 68, "metric_value": 0.3228, "depth": 6}
                  if obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 21, "metric_value": 0.4537, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 19, "metric_value": 0.2975, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 19, "metric_value": 0.2975, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
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
            elif obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 107, "metric_value": 0.5064, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Region", "instances": 39, "metric_value": 0.3912, "depth": 6}
                  if obj[0] == 'Americas':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 21, "metric_value": 0.4537, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[0] == 'EMEA':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.5033, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[0] == 'APAC':
                     return 'Closed Lost'
                  elif obj[0] == 'Japan':
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 27, "metric_value": 0.3809, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Region", "instances": 26, "metric_value": 0.2352, "depth": 7}
                     if obj[0] == 'EMEA':
                        return 'Closed Lost'
                     elif obj[0] == 'Americas':
                        return 'Closed Lost'
                     elif obj[0] == 'APAC':
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 22, "metric_value": 0.684, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Region", "instances": 14, "metric_value": 0.8631, "depth": 7}
                     if obj[0] == 'APAC':
                        return 'Closed Lost'
                     elif obj[0] == 'Americas':
                        return 'Closed Won'
                     elif obj[0] == 'EMEA':
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Region", "instances": 19, "metric_value": 0.6292, "depth": 6}
                  if obj[0] == 'Americas':
                     return 'Closed Lost'
                  elif obj[0] == 'APAC':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[0] == 'EMEA':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
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
         elif obj[2]<=2016:
            # {"feature": "Delivery_Quarter", "instances": 124, "metric_value": 0.8113, "depth": 4}
            if obj[3] == 'Q4':
               # {"feature": "Region", "instances": 41, "metric_value": 0.9262, "depth": 5}
               if obj[0] == 'Americas':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 23, "metric_value": 0.9656, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 22, "metric_value": 0.976, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     elif obj[5]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'EMEA':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 11, "metric_value": 0.9457, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.7642, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[0] == 'APAC':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 7}
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
            elif obj[3] == 'Q2':
               # {"feature": "Region", "instances": 34, "metric_value": 0.7871, "depth": 5}
               if obj[0] == 'Americas':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 16, "metric_value": 0.8113, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.9544, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'EMEA':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 13, "metric_value": 0.7793, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.7219, "depth": 7}
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
               elif obj[0] == 'APAC':
                  return 'Closed Lost'
               elif obj[0] == 'Japan':
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 33, "metric_value": 0.3298, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Region", "instances": 22, "metric_value": 0.4395, "depth": 6}
                  if obj[0] == 'Americas':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 12, "metric_value": 0.4138, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[0] == 'EMEA':
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[6]>0:
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
            elif obj[3] == 'Q1':
               # {"feature": "Region", "instances": 16, "metric_value": 0.9887, "depth": 5}
               if obj[0] == 'Americas':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 1.0, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[0] == 'EMEA':
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
               elif obj[0] == 'APAC':
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
   else:
      return 'Closed Lost'
