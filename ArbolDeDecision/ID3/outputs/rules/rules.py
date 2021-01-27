def findDecision(obj): #obj[0]: Region, obj[1]: Account_Owner, obj[2]: Year Created, obj[3]: Quote_Type
   # {"feature": "Account_Owner", "instances": 5065, "metric_value": 0.9859, "depth": 1}
   if obj[1] == 'Person_Name_50':
      # {"feature": "Year Created", "instances": 1109, "metric_value": 0.9265, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 557, "metric_value": 0.3727, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Quote_Type", "instances": 557, "metric_value": 0.3727, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 552, "metric_value": 0.9621, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Quote_Type", "instances": 552, "metric_value": 0.9621, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_13':
      # {"feature": "Year Created", "instances": 429, "metric_value": 0.9379, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 313, "metric_value": 0.8655, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Quote_Type", "instances": 309, "metric_value": 0.8576, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Quote_Type", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Middle East':
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 116, "metric_value": 0.9966, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Quote_Type", "instances": 113, "metric_value": 0.9986, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Americas':
            return 'Closed Lost'
         elif obj[0] == 'APAC':
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_43':
      # {"feature": "Quote_Type", "instances": 374, "metric_value": 0.9746, "depth": 2}
      if obj[3] == 'Non Binding':
         # {"feature": "Year Created", "instances": 365, "metric_value": 0.9677, "depth": 3}
         if obj[2]>2016:
            # {"feature": "Region", "instances": 324, "metric_value": 0.9828, "depth": 4}
            if obj[0] == 'APAC':
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[2]<=2016:
            # {"feature": "Region", "instances": 41, "metric_value": 0.6594, "depth": 4}
            if obj[0] == 'APAC':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[3] == 'Binding':
         # {"feature": "Year Created", "instances": 9, "metric_value": 0.5033, "depth": 3}
         if obj[2]<=2016:
            # {"feature": "Region", "instances": 7, "metric_value": 0.5917, "depth": 4}
            if obj[0] == 'APAC':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[2]>2016:
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_8':
      # {"feature": "Region", "instances": 373, "metric_value": 0.9752, "depth": 2}
      if obj[0] == 'Americas':
         # {"feature": "Quote_Type", "instances": 369, "metric_value": 0.9716, "depth": 3}
         if obj[3] == 'Non Binding':
            # {"feature": "Year Created", "instances": 365, "metric_value": 0.9741, "depth": 4}
            if obj[2]>2016:
               return 'Closed Won'
            elif obj[2]<=2016:
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[3] == 'Binding':
            return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[0] == 'APAC':
         return 'Closed Lost'
      elif obj[0] == 'EMEA':
         return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_18':
      # {"feature": "Year Created", "instances": 306, "metric_value": 0.9721, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 219, "metric_value": 0.9506, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Quote_Type", "instances": 219, "metric_value": 0.9506, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 87, "metric_value": 0.9991, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Quote_Type", "instances": 86, "metric_value": 0.9984, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Japan':
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Won'
   elif obj[1] == 'Person_Name_3':
      # {"feature": "Year Created", "instances": 256, "metric_value": 0.8518, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 146, "metric_value": 0.9395, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Quote_Type", "instances": 146, "metric_value": 0.9395, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 110, "metric_value": 0.6639, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Quote_Type", "instances": 110, "metric_value": 0.6639, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_4':
      # {"feature": "Year Created", "instances": 210, "metric_value": 0.9958, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Quote_Type", "instances": 159, "metric_value": 0.9993, "depth": 3}
         if obj[3] == 'Non Binding':
            # {"feature": "Region", "instances": 156, "metric_value": 0.9989, "depth": 4}
            if obj[0] == 'EMEA':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[3] == 'Binding':
            # {"feature": "Region", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[0] == 'EMEA':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 51, "metric_value": 0.9662, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Quote_Type", "instances": 50, "metric_value": 0.971, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'APAC':
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_65':
      # {"feature": "Quote_Type", "instances": 195, "metric_value": 0.7219, "depth": 2}
      if obj[3] == 'Non Binding':
         # {"feature": "Year Created", "instances": 192, "metric_value": 0.7281, "depth": 3}
         if obj[2]>2016:
            # {"feature": "Region", "instances": 145, "metric_value": 0.7355, "depth": 4}
            if obj[0] == 'APAC':
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[2]<=2016:
            # {"feature": "Region", "instances": 47, "metric_value": 0.7046, "depth": 4}
            if obj[0] == 'APAC':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[3] == 'Binding':
         return 'Closed Won'
      else:
         return 'Closed Won'
   elif obj[1] == 'Person_Name_32':
      # {"feature": "Year Created", "instances": 194, "metric_value": 0.5399, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 111, "metric_value": 0.6395, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Quote_Type", "instances": 111, "metric_value": 0.6395, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[2]<=2016:
         # {"feature": "Quote_Type", "instances": 83, "metric_value": 0.3744, "depth": 3}
         if obj[3] == 'Non Binding':
            # {"feature": "Region", "instances": 78, "metric_value": 0.3912, "depth": 4}
            if obj[0] == 'Japan':
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[3] == 'Binding':
            return 'Closed Won'
         else:
            return 'Closed Won'
      else:
         return 'Closed Won'
   elif obj[1] == 'Person_Name_64':
      # {"feature": "Year Created", "instances": 160, "metric_value": 0.9224, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 133, "metric_value": 0.9079, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Quote_Type", "instances": 133, "metric_value": 0.9079, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 27, "metric_value": 0.9751, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Quote_Type", "instances": 27, "metric_value": 0.9751, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      else:
         return 'Closed Won'
   elif obj[1] == 'Person_Name_16':
      # {"feature": "Year Created", "instances": 143, "metric_value": 0.8735, "depth": 2}
      if obj[2]<=2016:
         # {"feature": "Quote_Type", "instances": 74, "metric_value": 0.8218, "depth": 3}
         if obj[3] == 'Non Binding':
            # {"feature": "Region", "instances": 73, "metric_value": 0.8272, "depth": 4}
            if obj[0] == 'EMEA':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[3] == 'Binding':
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]>2016:
         # {"feature": "Region", "instances": 69, "metric_value": 0.9183, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Quote_Type", "instances": 69, "metric_value": 0.9183, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_45':
      # {"feature": "Quote_Type", "instances": 119, "metric_value": 0.9291, "depth": 2}
      if obj[3] == 'Non Binding':
         # {"feature": "Year Created", "instances": 118, "metric_value": 0.9318, "depth": 3}
         if obj[2]>2016:
            # {"feature": "Region", "instances": 114, "metric_value": 0.9268, "depth": 4}
            if obj[0] == 'Americas':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[2]<=2016:
            # {"feature": "Region", "instances": 4, "metric_value": 1.0, "depth": 4}
            if obj[0] == 'Americas':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[3] == 'Binding':
         return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_46':
      # {"feature": "Year Created", "instances": 116, "metric_value": 0.9033, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 87, "metric_value": 0.9576, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Quote_Type", "instances": 87, "metric_value": 0.9576, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 29, "metric_value": 0.5788, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Quote_Type", "instances": 29, "metric_value": 0.5788, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_2':
      # {"feature": "Year Created", "instances": 112, "metric_value": 0.9813, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 95, "metric_value": 0.9495, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Quote_Type", "instances": 95, "metric_value": 0.9495, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 17, "metric_value": 0.874, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Quote_Type", "instances": 17, "metric_value": 0.874, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_38':
      # {"feature": "Year Created", "instances": 95, "metric_value": 0.9317, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 83, "metric_value": 0.9223, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Quote_Type", "instances": 83, "metric_value": 0.9223, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 12, "metric_value": 0.9799, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Quote_Type", "instances": 12, "metric_value": 0.9799, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_42':
      # {"feature": "Year Created", "instances": 89, "metric_value": 0.9106, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 61, "metric_value": 0.8949, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Quote_Type", "instances": 61, "metric_value": 0.8949, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 28, "metric_value": 0.9403, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Quote_Type", "instances": 28, "metric_value": 0.9403, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      else:
         return 'Closed Won'
   elif obj[1] == 'Person_Name_66':
      # {"feature": "Year Created", "instances": 73, "metric_value": 0.8989, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 41, "metric_value": 0.9892, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Quote_Type", "instances": 41, "metric_value": 0.9892, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 32, "metric_value": 0.6253, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Quote_Type", "instances": 32, "metric_value": 0.6253, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      else:
         return 'Closed Won'
   elif obj[1] == 'Person_Name_60':
      # {"feature": "Year Created", "instances": 71, "metric_value": 0.8577, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 57, "metric_value": 0.8564, "depth": 3}
         if obj[0] == 'APAC':
            # {"feature": "Quote_Type", "instances": 57, "metric_value": 0.8564, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 14, "metric_value": 0.8631, "depth": 3}
         if obj[0] == 'APAC':
            # {"feature": "Quote_Type", "instances": 14, "metric_value": 0.8631, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_59':
      # {"feature": "Year Created", "instances": 61, "metric_value": 0.8537, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 54, "metric_value": 0.8767, "depth": 3}
         if obj[0] == 'APAC':
            # {"feature": "Quote_Type", "instances": 54, "metric_value": 0.8767, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 7, "metric_value": 0.5917, "depth": 3}
         if obj[0] == 'APAC':
            # {"feature": "Quote_Type", "instances": 7, "metric_value": 0.5917, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_49':
      # {"feature": "Year Created", "instances": 61, "metric_value": 0.9983, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 33, "metric_value": 0.9993, "depth": 3}
         if obj[0] == 'APAC':
            # {"feature": "Quote_Type", "instances": 33, "metric_value": 0.9993, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 28, "metric_value": 0.9963, "depth": 3}
         if obj[0] == 'APAC':
            # {"feature": "Quote_Type", "instances": 28, "metric_value": 0.9963, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_21':
      # {"feature": "Year Created", "instances": 53, "metric_value": 0.5631, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Quote_Type", "instances": 46, "metric_value": 0.496, "depth": 3}
         if obj[3] == 'Non Binding':
            # {"feature": "Region", "instances": 44, "metric_value": 0.5108, "depth": 4}
            if obj[0] == 'APAC':
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[3] == 'Binding':
            return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 7, "metric_value": 0.8631, "depth": 3}
         if obj[0] == 'APAC':
            # {"feature": "Quote_Type", "instances": 7, "metric_value": 0.8631, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      else:
         return 'Closed Won'
   elif obj[1] == 'Person_Name_52':
      # {"feature": "Quote_Type", "instances": 50, "metric_value": 0.6343, "depth": 2}
      if obj[3] == 'Non Binding':
         # {"feature": "Year Created", "instances": 48, "metric_value": 0.65, "depth": 3}
         if obj[2]>2016:
            # {"feature": "Region", "instances": 41, "metric_value": 0.6594, "depth": 4}
            if obj[0] == 'APAC':
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[2]<=2016:
            # {"feature": "Region", "instances": 7, "metric_value": 0.5917, "depth": 4}
            if obj[0] == 'APAC':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[3] == 'Binding':
         return 'Closed Won'
      else:
         return 'Closed Won'
   elif obj[1] == 'Person_Name_5':
      # {"feature": "Region", "instances": 49, "metric_value": 0.9633, "depth": 2}
      if obj[0] == 'Middle East':
         # {"feature": "Year Created", "instances": 47, "metric_value": 0.9441, "depth": 3}
         if obj[2]>2016:
            # {"feature": "Quote_Type", "instances": 46, "metric_value": 0.9503, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            elif obj[3] == 'Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[2]<=2016:
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[0] == 'EMEA':
         return 'Closed Won'
      else:
         return 'Closed Won'
   elif obj[1] == 'Person_Name_62':
      # {"feature": "Region", "instances": 46, "metric_value": 0.9503, "depth": 2}
      if obj[0] == 'EMEA':
         # {"feature": "Year Created", "instances": 45, "metric_value": 0.9389, "depth": 3}
         if obj[2]>2016:
            # {"feature": "Quote_Type", "instances": 42, "metric_value": 0.9183, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[2]<=2016:
            # {"feature": "Quote_Type", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[0] == 'Middle East':
         return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_54':
      # {"feature": "Quote_Type", "instances": 45, "metric_value": 0.9911, "depth": 2}
      if obj[3] == 'Non Binding':
         # {"feature": "Year Created", "instances": 35, "metric_value": 0.9947, "depth": 3}
         if obj[2]>2016:
            # {"feature": "Region", "instances": 31, "metric_value": 0.9932, "depth": 4}
            if obj[0] == 'APAC':
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[2]<=2016:
            # {"feature": "Region", "instances": 4, "metric_value": 1.0, "depth": 4}
            if obj[0] == 'APAC':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[3] == 'Binding':
         # {"feature": "Region", "instances": 10, "metric_value": 0.971, "depth": 3}
         if obj[0] == 'APAC':
            # {"feature": "Year Created", "instances": 10, "metric_value": 0.971, "depth": 4}
            if obj[2]<=2016:
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      else:
         return 'Closed Won'
   elif obj[1] == 'Person_Name_55':
      # {"feature": "Year Created", "instances": 36, "metric_value": 0.9911, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 31, "metric_value": 0.9629, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Quote_Type", "instances": 31, "metric_value": 0.9629, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 5, "metric_value": 0.7219, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Quote_Type", "instances": 5, "metric_value": 0.7219, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_63':
      # {"feature": "Year Created", "instances": 36, "metric_value": 0.9799, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 19, "metric_value": 0.8997, "depth": 3}
         if obj[0] == 'APAC':
            # {"feature": "Quote_Type", "instances": 19, "metric_value": 0.8997, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]<=2016:
         # {"feature": "Quote_Type", "instances": 17, "metric_value": 0.9975, "depth": 3}
         if obj[3] == 'Non Binding':
            # {"feature": "Region", "instances": 15, "metric_value": 0.9968, "depth": 4}
            if obj[0] == 'APAC':
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[3] == 'Binding':
            # {"feature": "Region", "instances": 2, "metric_value": 1.0, "depth": 4}
            if obj[0] == 'APAC':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Won'
   elif obj[1] == 'Person_Name_51':
      # {"feature": "Year Created", "instances": 35, "metric_value": 0.9275, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 23, "metric_value": 0.7554, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Quote_Type", "instances": 23, "metric_value": 0.7554, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 12, "metric_value": 0.9799, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Quote_Type", "instances": 12, "metric_value": 0.9799, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      else:
         return 'Closed Won'
   elif obj[1] == 'Person_Name_39':
      # {"feature": "Region", "instances": 29, "metric_value": 0.7355, "depth": 2}
      if obj[0] == 'EMEA':
         # {"feature": "Year Created", "instances": 27, "metric_value": 0.6913, "depth": 3}
         if obj[2]<=2016:
            # {"feature": "Quote_Type", "instances": 26, "metric_value": 0.7063, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[2]>2016:
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[0] == 'Middle East':
         # {"feature": "Year Created", "instances": 2, "metric_value": 1.0, "depth": 3}
         if obj[2]<=2016:
            # {"feature": "Quote_Type", "instances": 2, "metric_value": 1.0, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_33':
      # {"feature": "Year Created", "instances": 27, "metric_value": 0.9911, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 23, "metric_value": 0.9877, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Quote_Type", "instances": 23, "metric_value": 0.9877, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 4, "metric_value": 1.0, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Quote_Type", "instances": 4, "metric_value": 1.0, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_14':
      # {"feature": "Quote_Type", "instances": 27, "metric_value": 0.9751, "depth": 2}
      if obj[3] == 'Non Binding':
         # {"feature": "Region", "instances": 22, "metric_value": 1.0, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Year Created", "instances": 22, "metric_value": 1.0, "depth": 4}
            if obj[2]>2016:
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[3] == 'Binding':
         return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_44':
      # {"feature": "Year Created", "instances": 21, "metric_value": 0.4537, "depth": 2}
      if obj[2]<=2016:
         # {"feature": "Region", "instances": 16, "metric_value": 0.3373, "depth": 3}
         if obj[0] == 'APAC':
            # {"feature": "Quote_Type", "instances": 15, "metric_value": 0.3534, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            elif obj[3] == 'Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[0] == 'Japan':
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[2]>2016:
         # {"feature": "Region", "instances": 5, "metric_value": 0.7219, "depth": 3}
         if obj[0] == 'APAC':
            # {"feature": "Quote_Type", "instances": 5, "metric_value": 0.7219, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_61':
      # {"feature": "Year Created", "instances": 21, "metric_value": 0.7919, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 12, "metric_value": 0.9799, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Quote_Type", "instances": 12, "metric_value": 0.9799, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Won'
      elif obj[2]<=2016:
         return 'Closed Won'
      else:
         return 'Closed Won'
   elif obj[1] == 'Person_Name_41':
      return 'Closed Lost'
   elif obj[1] == 'Person_Name_9':
      # {"feature": "Region", "instances": 12, "metric_value": 0.9183, "depth": 2}
      if obj[0] == 'Americas':
         # {"feature": "Year Created", "instances": 12, "metric_value": 0.9183, "depth": 3}
         if obj[2]>2016:
            # {"feature": "Quote_Type", "instances": 12, "metric_value": 0.9183, "depth": 4}
            if obj[3] == 'Non Binding':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1] == 'Person_Name_26':
      return 'Closed Lost'
   elif obj[1] == 'Person_Name_11':
      return 'Closed Lost'
   elif obj[1] == 'Person_Name_58':
      return 'Closed Lost'
   elif obj[1] == 'Person_Name_29':
      return 'Closed Lost'
   elif obj[1] == 'Person_Name_17':
      return 'Closed Lost'
   elif obj[1] == 'Person_Name_35':
      return 'Closed Lost'
   elif obj[1] == 'Person_Name_23':
      return 'Closed Lost'
   elif obj[1] == 'Person_Name_36':
      return 'Closed Lost'
   elif obj[1] == 'Person_Name_25':
      return 'Closed Lost'
   elif obj[1] == 'Person_Name_47':
      return 'Closed Lost'
   elif obj[1] == 'Person_Name_34':
      return 'Closed Lost'
   else:
      return 'Closed Lost'
