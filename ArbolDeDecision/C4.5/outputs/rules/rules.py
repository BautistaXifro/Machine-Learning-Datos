def findDecision(obj): #obj[0]: Region, obj[1]: Total_Amount, obj[2]: Delivery_Year, obj[3]: Delivery_Quarter
   # {"feature": "Total_Amount", "instances": 15448, "metric_value": 0.9875, "depth": 1}
   if obj[1]<=1037643.413886339:
      # {"feature": "Delivery_Year", "instances": 13429, "metric_value": 0.9501, "depth": 2}
      if obj[2]<=2018:
         # {"feature": "Region", "instances": 13202, "metric_value": 0.947, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Delivery_Quarter", "instances": 4600, "metric_value": 0.8967, "depth": 4}
            if obj[3] == 'Q1':
               return 'Closed Won'
            elif obj[3] == 'Q2':
               return 'Closed Won'
            elif obj[3] == 'Q4':
               return 'Closed Won'
            elif obj[3] == 'Q3':
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 3330, "metric_value": 0.9582, "depth": 4}
            if obj[3] == 'Q2':
               return 'Closed Won'
            elif obj[3] == 'Q3':
               return 'Closed Won'
            elif obj[3] == 'Q1':
               return 'Closed Won'
            elif obj[3] == 'Q4':
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 2601, "metric_value": 0.9952, "depth": 4}
            if obj[3] == 'Q3':
               return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Won'
            elif obj[3] == 'Q1':
               return 'Closed Won'
            elif obj[3] == 'Q4':
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Quarter", "instances": 2535, "metric_value": 0.9127, "depth": 4}
            if obj[3] == 'Q2':
               return 'Closed Won'
            elif obj[3] == 'Q3':
               return 'Closed Won'
            elif obj[3] == 'Q1':
               return 'Closed Won'
            elif obj[3] == 'Q4':
               return 'Closed Won'
            else:
               return 'Closed Won'
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 136, "metric_value": 0.9231, "depth": 4}
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
      elif obj[2]>2018:
         # {"feature": "Delivery_Quarter", "instances": 227, "metric_value": 0.9689, "depth": 3}
         if obj[3] == 'Q1':
            # {"feature": "Region", "instances": 197, "metric_value": 0.9884, "depth": 4}
            if obj[0] == 'EMEA':
               return 'Closed Won'
            elif obj[0] == 'Japan':
               return 'Closed Lost'
            elif obj[0] == 'APAC':
               return 'Closed Lost'
            elif obj[0] == 'Americas':
               return 'Closed Lost'
            elif obj[0] == 'Middle East':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[3] == 'Q2':
            # {"feature": "Region", "instances": 21, "metric_value": 0.5917, "depth": 4}
            if obj[0] == 'Japan':
               return 'Closed Lost'
            elif obj[0] == 'Americas':
               return 'Closed Lost'
            elif obj[0] == 'APAC':
               return 'Closed Lost'
            elif obj[0] == 'EMEA':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[3] == 'Q4':
            return 'Closed Lost'
         elif obj[3] == 'Q3':
            # {"feature": "Region", "instances": 4, "metric_value": 0.8113, "depth": 4}
            if obj[0] == 'Japan':
               return 'Closed Lost'
            elif obj[0] == 'Americas':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Lost'
      else:
         return 'Closed Lost'
   elif obj[1]>1037643.413886339:
      # {"feature": "Region", "instances": 2019, "metric_value": 0.5649, "depth": 2}
      if obj[0] == 'Americas':
         # {"feature": "Delivery_Year", "instances": 861, "metric_value": 0.6123, "depth": 3}
         if obj[2]<=2018:
            # {"feature": "Delivery_Quarter", "instances": 806, "metric_value": 0.5912, "depth": 4}
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
         elif obj[2]>2018:
            # {"feature": "Delivery_Quarter", "instances": 55, "metric_value": 0.8454, "depth": 4}
            if obj[3] == 'Q1':
               return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            elif obj[3] == 'Q3':
               return 'Closed Won'
            else:
               return 'Closed Won'
         else:
            return 'Closed Lost'
      elif obj[0] == 'EMEA':
         # {"feature": "Delivery_Year", "instances": 699, "metric_value": 0.5995, "depth": 3}
         if obj[2]<=2018:
            # {"feature": "Delivery_Quarter", "instances": 667, "metric_value": 0.6171, "depth": 4}
            if obj[3] == 'Q2':
               return 'Closed Lost'
            elif obj[3] == 'Q3':
               return 'Closed Lost'
            elif obj[3] == 'Q1':
               return 'Closed Lost'
            elif obj[3] == 'Q4':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[2]>2018:
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[0] == 'APAC':
         # {"feature": "Delivery_Year", "instances": 392, "metric_value": 0.3423, "depth": 3}
         if obj[2]<=2018:
            # {"feature": "Delivery_Quarter", "instances": 345, "metric_value": 0.3751, "depth": 4}
            if obj[3] == 'Q3':
               return 'Closed Lost'
            elif obj[3] == 'Q2':
               return 'Closed Lost'
            elif obj[3] == 'Q4':
               return 'Closed Lost'
            elif obj[3] == 'Q1':
               return 'Closed Lost'
            else:
               return 'Closed Lost'
         elif obj[2]>2018:
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[0] == 'Japan':
         # {"feature": "Delivery_Year", "instances": 48, "metric_value": 0.7766, "depth": 3}
         if obj[2]<=2018:
            # {"feature": "Delivery_Quarter", "instances": 44, "metric_value": 0.8113, "depth": 4}
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
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[0] == 'Middle East':
         return 'Closed Lost'
      else:
         return 'Closed Lost'
   else:
      return 'Closed Lost'
