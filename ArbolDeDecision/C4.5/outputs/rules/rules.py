def findDecision(obj): #obj[0]: Region, obj[1]: Total_Amount, obj[2]: TRF
   # {"feature": "TRF", "instances": 16883, "metric_value": 0.9879, "depth": 1}
   if obj[2]<=2.3358407865900612:
      # {"feature": "Total_Amount", "instances": 14740, "metric_value": 0.9516, "depth": 2}
      if obj[1]<=1003967.3752647843:
         # {"feature": "Region", "instances": 14610, "metric_value": 0.9488, "depth": 3}
         if obj[0] == 'Japan':
            return 'Closed Won'
         elif obj[0] == 'EMEA':
            return 'Closed Won'
         elif obj[0] == 'Americas':
            return 'Closed Won'
         elif obj[0] == 'APAC':
            return 'Closed Won'
         elif obj[0] == 'Middle East':
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[1]>1003967.3752647843:
         # {"feature": "Region", "instances": 130, "metric_value": 0.7793, "depth": 3}
         if obj[0] == 'Americas':
            return 'Closed Lost'
         elif obj[0] == 'EMEA':
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
   elif obj[2]>2.3358407865900612:
      # {"feature": "Region", "instances": 2143, "metric_value": 0.5385, "depth": 2}
      if obj[0] == 'Americas':
         # {"feature": "Total_Amount", "instances": 903, "metric_value": 0.5742, "depth": 3}
         if obj[1]>1003967.3752647843:
            return 'Closed Lost'
         elif obj[1]<=1003967.3752647843:
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[0] == 'EMEA':
         # {"feature": "Total_Amount", "instances": 733, "metric_value": 0.5856, "depth": 3}
         if obj[1]>1003967.3752647843:
            return 'Closed Lost'
         elif obj[1]<=1003967.3752647843:
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[0] == 'APAC':
         # {"feature": "Total_Amount", "instances": 436, "metric_value": 0.3528, "depth": 3}
         if obj[1]>1003967.3752647843:
            return 'Closed Lost'
         elif obj[1]<=1003967.3752647843:
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[0] == 'Japan':
         # {"feature": "Total_Amount", "instances": 51, "metric_value": 0.6723, "depth": 3}
         if obj[1]>1003967.3752647843:
            return 'Closed Lost'
         elif obj[1]<=1003967.3752647843:
            return 'Closed Lost'
         else:
            return 'Closed Lost'
      elif obj[0] == 'Middle East':
         return 'Closed Lost'
      else:
         return 'Closed Lost'
   else:
      return 'Closed Lost'
