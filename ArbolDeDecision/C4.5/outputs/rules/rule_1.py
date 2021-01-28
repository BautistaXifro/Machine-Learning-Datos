def findDecision(obj): #obj[0]: Region, obj[1]: Total_Amount, obj[2]: Delivery_Year, obj[3]: Delivery_Quarter, obj[4]: TRF, obj[5]: Pricing, Delivery_Terms_Approved, obj[6]: Pricing, Delivery_Terms_Quote_Appr
   # {"feature": "TRF", "instances": 3017, "metric_value": 0.984, "depth": 1}
   if obj[4]<=0:
      # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 2186, "metric_value": 0.8955, "depth": 2}
      if obj[5]>0:
         # {"feature": "Region", "instances": 1291, "metric_value": 0.6994, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Delivery_Year", "instances": 621, "metric_value": 0.3447, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 433, "metric_value": 0.4444, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 140, "metric_value": 0.3712, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 140, "metric_value": 0.3712, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 115, "metric_value": 0.4826, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 115, "metric_value": 0.4826, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 95, "metric_value": 0.4521, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 95, "metric_value": 0.4521, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 83, "metric_value": 0.4952, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 83, "metric_value": 0.4952, "depth": 7}
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
            # {"feature": "Delivery_Quarter", "instances": 262, "metric_value": 0.8374, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 113, "metric_value": 0.7112, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 101, "metric_value": 0.6762, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 101, "metric_value": 0.6762, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 12, "metric_value": 0.9183, "depth": 6}
                  if obj[1]<=972265.2204599264:
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
               # {"feature": "Delivery_Year", "instances": 62, "metric_value": 0.889, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 44, "metric_value": 0.9457, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 44, "metric_value": 0.9457, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 18, "metric_value": 0.65, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 18, "metric_value": 0.65, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 49, "metric_value": 0.8886, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 44, "metric_value": 0.9024, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 44, "metric_value": 0.9024, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 38, "metric_value": 0.9495, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 24, "metric_value": 0.995, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 24, "metric_value": 0.995, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 14, "metric_value": 0.3712, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.3712, "depth": 7}
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
            # {"feature": "Delivery_Year", "instances": 234, "metric_value": 0.7939, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 161, "metric_value": 0.879, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 60, "metric_value": 0.9007, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 60, "metric_value": 0.9007, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 45, "metric_value": 0.7642, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 45, "metric_value": 0.7642, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 45, "metric_value": 0.9389, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 45, "metric_value": 0.9389, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.8454, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.8454, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 73, "metric_value": 0.4987, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 31, "metric_value": 0.2056, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 31, "metric_value": 0.2056, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 18, "metric_value": 0.7642, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 18, "metric_value": 0.7642, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 18, "metric_value": 0.5033, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 18, "metric_value": 0.5033, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 6, "metric_value": 0.65, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.65, "depth": 7}
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
            # {"feature": "Delivery_Quarter", "instances": 161, "metric_value": 0.9877, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 54, "metric_value": 0.999, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 52, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 52, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 51, "metric_value": 0.8974, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 43, "metric_value": 0.8841, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 43, "metric_value": 0.8841, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 8, "metric_value": 0.9544, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.9544, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 33, "metric_value": 0.9834, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 31, "metric_value": 0.9629, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 31, "metric_value": 0.9629, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 23, "metric_value": 0.9656, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Total_Amount", "instances": 14, "metric_value": 0.9403, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.9403, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[2]<=2016:
                  # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.9911, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9911, "depth": 7}
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
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.9612, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 12, "metric_value": 0.9183, "depth": 5}
               if obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Total_Amount", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=972265.2204599264:
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
      elif obj[5]<=0:
         # {"feature": "Region", "instances": 895, "metric_value": 0.9997, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 300, "metric_value": 0.6343, "depth": 4}
            if obj[6]>0:
               # {"feature": "Delivery_Year", "instances": 258, "metric_value": 0.2366, "depth": 5}
               if obj[2]<=2016:
                  # {"feature": "Delivery_Quarter", "instances": 238, "metric_value": 0.07, "depth": 6}
                  if obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 132, "metric_value": 0.1133, "depth": 7}
                     if obj[1]<=972265.2204599264:
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
                  # {"feature": "Delivery_Quarter", "instances": 20, "metric_value": 0.971, "depth": 6}
                  if obj[3] == 'Q1':
                     # {"feature": "Total_Amount", "instances": 7, "metric_value": 0.8631, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q3':
                     # {"feature": "Total_Amount", "instances": 6, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[3] == 'Q2':
                     # {"feature": "Total_Amount", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=972265.2204599264:
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
               # {"feature": "Delivery_Quarter", "instances": 42, "metric_value": 0.4537, "depth": 5}
               if obj[3] == 'Q1':
                  return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 15, "metric_value": 0.7219, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 13, "metric_value": 0.7793, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Total_Amount", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Delivery_Year", "instances": 4, "metric_value": 0.8113, "depth": 7}
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
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 220, "metric_value": 0.8388, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 67, "metric_value": 0.7395, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 60, "metric_value": 0.65, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 48, "metric_value": 0.5436, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 12, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 6, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 65, "metric_value": 0.6901, "depth": 5}
               if obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 45, "metric_value": 0.7642, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 29, "metric_value": 0.7973, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 16, "metric_value": 0.6962, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[6]>0:
                  # {"feature": "Delivery_Year", "instances": 20, "metric_value": 0.469, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 19, "metric_value": 0.4855, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 59, "metric_value": 0.9529, "depth": 5}
               if obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 38, "metric_value": 0.9268, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 25, "metric_value": 0.9427, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 13, "metric_value": 0.8905, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[6]>0:
                  # {"feature": "Delivery_Year", "instances": 21, "metric_value": 0.9852, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 19, "metric_value": 0.9819, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 29, "metric_value": 0.9576, "depth": 5}
               if obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 19, "metric_value": 0.8315, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 13, "metric_value": 0.8905, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[6]>0:
                  # {"feature": "Delivery_Year", "instances": 10, "metric_value": 0.971, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.9911, "depth": 7}
                     if obj[1]<=972265.2204599264:
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
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 191, "metric_value": 0.8857, "depth": 4}
            if obj[6]<=0:
               # {"feature": "Delivery_Quarter", "instances": 143, "metric_value": 0.7793, "depth": 5}
               if obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 44, "metric_value": 0.6321, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 43, "metric_value": 0.6409, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 38, "metric_value": 0.8997, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Delivery_Year", "instances": 38, "metric_value": 0.8997, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 33, "metric_value": 0.885, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 31, "metric_value": 0.8691, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 28, "metric_value": 0.5917, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 25, "metric_value": 0.6343, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[6]>0:
               # {"feature": "Delivery_Quarter", "instances": 48, "metric_value": 0.9987, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.8905, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.7642, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     # {"feature": "Total_Amount", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Total_Amount", "instances": 13, "metric_value": 0.9957, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.9957, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 12, "metric_value": 0.9799, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.7642, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Total_Amount", "instances": 10, "metric_value": 1.0, "depth": 6}
                  if obj[1]<=972265.2204599264:
                     # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.9911, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     elif obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[1]>972265.2204599264:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Americas':
            # {"feature": "Delivery_Year", "instances": 181, "metric_value": 0.9465, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 153, "metric_value": 0.9702, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 46, "metric_value": 0.9877, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 35, "metric_value": 0.9518, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 11, "metric_value": 0.9457, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 45, "metric_value": 0.8673, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 36, "metric_value": 0.8524, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 9, "metric_value": 0.9183, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 42, "metric_value": 0.9852, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 37, "metric_value": 0.9569, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]>0:
                     # {"feature": "Total_Amount", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 20, "metric_value": 1.0, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 17, "metric_value": 0.9774, "depth": 7}
                     if obj[1]<=972265.2204599264:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 28, "metric_value": 0.6769, "depth": 5}
               if obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 16, "metric_value": 0.6962, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Total_Amount", "instances": 13, "metric_value": 0.7793, "depth": 7}
                     if obj[1]<=972265.2204599264:
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
                     return 'Closed Won'
                  elif obj[6]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  return 'Closed Won'
               elif obj[3] == 'Q1':
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Middle East':
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Won'
   elif obj[4]>0:
      # {"feature": "Total_Amount", "instances": 831, "metric_value": 0.8493, "depth": 2}
      if obj[1]<=972265.2204599264:
         # {"feature": "Region", "instances": 444, "metric_value": 0.9715, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Delivery_Year", "instances": 168, "metric_value": 0.9974, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 129, "metric_value": 0.9979, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 40, "metric_value": 0.9928, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 39, "metric_value": 0.9881, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Won'
                     elif obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 40, "metric_value": 0.9928, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 23, "metric_value": 0.9321, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Won'
                     elif obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 17, "metric_value": 0.9774, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 33, "metric_value": 0.9673, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 27, "metric_value": 0.9183, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 16, "metric_value": 0.896, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 13, "metric_value": 0.9612, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Won'
                     elif obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]<=0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 39, "metric_value": 0.8582, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 14, "metric_value": 0.8631, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.9911, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.4395, "depth": 6}
                  if obj[6]>0:
                     return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 10, "metric_value": 1.0, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.9852, "depth": 7}
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
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 0.8113, "depth": 6}
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
         elif obj[0] == 'EMEA':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 152, "metric_value": 0.9069, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 96, "metric_value": 0.8427, "depth": 5}
               if obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 33, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 25, "metric_value": 0.9896, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 29, "metric_value": 0.7973, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 26, "metric_value": 0.7793, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 23, "metric_value": 0.6666, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 19, "metric_value": 0.4855, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 11, "metric_value": 0.9457, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 56, "metric_value": 0.9769, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 20, "metric_value": 1.0, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Delivery_Year", "instances": 15, "metric_value": 0.971, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     elif obj[2]<=2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.9957, "depth": 6}
                  if obj[6]<=0:
                     # {"feature": "Delivery_Year", "instances": 8, "metric_value": 0.9544, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     elif obj[2]<=2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]>0:
                     # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     elif obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 12, "metric_value": 0.8113, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.8454, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.9457, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Delivery_Year", "instances": 6, "metric_value": 1.0, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     elif obj[2]<=2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     elif obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Quarter", "instances": 75, "metric_value": 0.9183, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 25, "metric_value": 0.8555, "depth": 5}
               if obj[6]>0:
                  # {"feature": "Delivery_Year", "instances": 18, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 14, "metric_value": 0.9403, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 22, "metric_value": 0.9457, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.7793, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 12, "metric_value": 0.65, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.9911, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.9544, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 15, "metric_value": 0.9183, "depth": 5}
               if obj[6]>0:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 12, "metric_value": 0.8113, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Delivery_Year", "instances": 7, "metric_value": 0.5917, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     elif obj[2]<=2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[6]<=0:
                  # {"feature": "Delivery_Year", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 13, "metric_value": 0.9612, "depth": 5}
               if obj[5]<=0:
                  # {"feature": "Delivery_Year", "instances": 8, "metric_value": 0.8113, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 7}
                     if obj[6]<=0:
                        return 'Closed Lost'
                     elif obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]>2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 37, "metric_value": 0.974, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 20, "metric_value": 0.8113, "depth": 5}
               if obj[3] == 'Q3':
                  return 'Closed Won'
               elif obj[3] == 'Q4':
                  # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Delivery_Year", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Won'
            elif obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 17, "metric_value": 0.9774, "depth": 5}
               if obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.7642, "depth": 6}
                  if obj[6]>0:
                     return 'Closed Lost'
                  elif obj[6]<=0:
                     # {"feature": "Delivery_Year", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Lost'
                     elif obj[2]<=2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Delivery_Year", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]<=0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[2]<=2016:
                     return 'Closed Won'
                  elif obj[2]>2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q3':
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 12, "metric_value": 0.8113, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 6, "metric_value": 0.9183, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
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
            elif obj[3] == 'Q1':
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
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[1]>972265.2204599264:
         # {"feature": "Region", "instances": 387, "metric_value": 0.5623, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Delivery_Year", "instances": 164, "metric_value": 0.5521, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 108, "metric_value": 0.3463, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 43, "metric_value": 0.4465, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 30, "metric_value": 0.3534, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 13, "metric_value": 0.6194, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 24, "metric_value": 0.2499, "depth": 6}
                  if obj[5]>0:
                     return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.469, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     elif obj[6]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 15, "metric_value": 0.5665, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.8113, "depth": 7}
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
               else:
                  return 'Closed Lost'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 56, "metric_value": 0.8113, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 19, "metric_value": 0.7425, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.8813, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 9, "metric_value": 0.5033, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 17, "metric_value": 0.9367, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 11, "metric_value": 0.994, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q2':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 12, "metric_value": 0.65, "depth": 6}
                  if obj[5]<=0:
                     return 'Closed Lost'
                  elif obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.9183, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[3] == 'Q1':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 8, "metric_value": 0.8113, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 7, "metric_value": 0.8631, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[5]>0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Year", "instances": 139, "metric_value": 0.5561, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 92, "metric_value": 0.6153, "depth": 5}
               if obj[6]>0:
                  # {"feature": "Delivery_Quarter", "instances": 87, "metric_value": 0.6365, "depth": 6}
                  if obj[3] == 'Q3':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 34, "metric_value": 0.6024, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q2':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 26, "metric_value": 0.6194, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q1':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 18, "metric_value": 0.7642, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Lost'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[3] == 'Q4':
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 9, "metric_value": 0.5033, "depth": 7}
                     if obj[5]<=0:
                        return 'Closed Lost'
                     elif obj[5]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[6]<=0:
                  return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 47, "metric_value": 0.4199, "depth": 5}
               if obj[3] == 'Q4':
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 21, "metric_value": 0.5917, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 20, "metric_value": 0.469, "depth": 7}
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
               elif obj[3] == 'Q2':
                  return 'Closed Lost'
               elif obj[3] == 'Q3':
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 9, "metric_value": 0.5033, "depth": 6}
                  if obj[5]>0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 6, "metric_value": 0.65, "depth": 7}
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
               else:
                  return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Quarter", "instances": 70, "metric_value": 0.469, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 22, "metric_value": 0.4395, "depth": 5}
               if obj[2]>2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 19, "metric_value": 0.2975, "depth": 6}
                  if obj[5]<=0:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 10, "metric_value": 0.469, "depth": 7}
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
               elif obj[2]<=2016:
                  # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[5]<=0:
                     return 'Closed Lost'
                  elif obj[5]>0:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q4':
               return 'Closed Lost'
            elif obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 14, "metric_value": 0.7496, "depth": 5}
               if obj[5]>0:
                  # {"feature": "Delivery_Year", "instances": 9, "metric_value": 0.5033, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 8, "metric_value": 0.5436, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  elif obj[2]<=2016:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[5]<=0:
                  # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 5, "metric_value": 0.971, "depth": 6}
                  if obj[6]>0:
                     # {"feature": "Delivery_Year", "instances": 4, "metric_value": 1.0, "depth": 7}
                     if obj[2]>2016:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[6]<=0:
                     return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               else:
                  return 'Closed Lost'
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 14, "metric_value": 0.5917, "depth": 5}
               if obj[6]>0:
                  # {"feature": "Delivery_Year", "instances": 13, "metric_value": 0.3912, "depth": 6}
                  if obj[2]>2016:
                     return 'Closed Lost'
                  elif obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[5]>0:
                        return 'Closed Won'
                     elif obj[5]<=0:
                        return 'Closed Lost'
                     else:
                        return 'Closed Lost'
                  else:
                     return 'Closed Lost'
               elif obj[6]<=0:
                  return 'Closed Won'
               else:
                  return 'Closed Won'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 11, "metric_value": 0.994, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 8, "metric_value": 0.9544, "depth": 5}
               if obj[3] == 'Q3':
                  # {"feature": "Delivery_Year", "instances": 4, "metric_value": 1.0, "depth": 6}
                  if obj[2]<=2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q1':
                  # {"feature": "Delivery_Year", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[2]>2016:
                     # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[6]>0:
                        return 'Closed Won'
                     else:
                        return 'Closed Won'
                  elif obj[2]<=2016:
                     return 'Closed Won'
                  else:
                     return 'Closed Won'
               elif obj[3] == 'Q2':
                  return 'Closed Won'
               else:
                  return 'Closed Won'
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
   else:
      return 'Closed Lost'
