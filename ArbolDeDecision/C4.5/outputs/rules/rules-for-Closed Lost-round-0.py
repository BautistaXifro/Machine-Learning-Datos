def findDecision(obj): #obj[0]: Region, obj[1]: Total_Amount, obj[2]: Delivery_Year, obj[3]: Delivery_Quarter, obj[4]: Pricing, Delivery_Terms_Approved, obj[5]: Pricing, Delivery_Terms_Quote_Appr
   # {"feature": "Total_Amount", "instances": 15083, "metric_value": 0.0317, "depth": 1}
   if obj[1]<=959840.9042772575:
      # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 13132, "metric_value": 0.0174, "depth": 2}
      if obj[4]>0:
         # {"feature": "Region", "instances": 7594, "metric_value": 0.0604, "depth": 3}
         if obj[0] == 'Japan':
            # {"feature": "Delivery_Year", "instances": 3137, "metric_value": 0.0172, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 2200, "metric_value": 0.0006, "depth": 5}
               if obj[3] == 'Q2':
                  return 0.06134969325153374
               elif obj[3] == 'Q1':
                  return 0.08273381294964029
               elif obj[3] == 'Q4':
                  return 0.07733812949640288
               elif obj[3] == 'Q3':
                  return 0.08256880733944955
               else:
                  return 0.08256880733944955
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 937, "metric_value": 0.0163, "depth": 5}
               if obj[3] == 'Q4':
                  return 0.0
               elif obj[3] == 'Q1':
                  return 0.013513513513513514
               elif obj[3] == 'Q3':
                  return 0.013824884792626729
               elif obj[3] == 'Q2':
                  return 0.004784688995215311
               else:
                  return 0.004784688995215311
            else:
               return 0.007470651013874066
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 1775, "metric_value": 0.0019, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 690, "metric_value": 0.004, "depth": 5}
               if obj[2]>2016:
                  return 0.3205574912891986
               elif obj[2]<=2016:
                  return 0.4827586206896552
               else:
                  return 0.4827586206896552
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 482, "metric_value": 0.004, "depth": 5}
               if obj[2]>2016:
                  return 0.4767123287671233
               elif obj[2]<=2016:
                  return 0.3333333333333333
               else:
                  return 0.3333333333333333
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 391, "metric_value": 0.0, "depth": 5}
               if obj[2]>2016:
                  return 0.43023255813953487
               elif obj[2]<=2016:
                  return 0.44680851063829785
               else:
                  return 0.44680851063829785
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 212, "metric_value": 0.018, "depth": 5}
               if obj[2]<=2016:
                  return 0.487012987012987
               elif obj[2]>2016:
                  return 0.20689655172413793
               else:
                  return 0.20689655172413793
            else:
               return 0.41037735849056606
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Year", "instances": 1292, "metric_value": 0.0109, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 940, "metric_value": 0.0024, "depth": 5}
               if obj[3] == 'Q2':
                  return 0.3136645962732919
               elif obj[3] == 'Q1':
                  return 0.4007220216606498
               elif obj[3] == 'Q3':
                  return 0.3153846153846154
               elif obj[3] == 'Q4':
                  return 0.25925925925925924
               else:
                  return 0.25925925925925924
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 352, "metric_value": 0.0143, "depth": 5}
               if obj[3] == 'Q4':
                  return 0.12598425196850394
               elif obj[3] == 'Q3':
                  return 0.08130081300813008
               elif obj[3] == 'Q2':
                  return 0.21875
               elif obj[3] == 'Q1':
                  return 0.3157894736842105
               else:
                  return 0.3157894736842105
            else:
               return 0.14772727272727273
         elif obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 1277, "metric_value": 0.0021, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 412, "metric_value": 0.0006, "depth": 5}
               if obj[2]>2016:
                  return 0.5378378378378378
               elif obj[2]<=2016:
                  return 0.6190476190476191
               else:
                  return 0.6190476190476191
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 366, "metric_value": 0.0009, "depth": 5}
               if obj[2]>2016:
                  return 0.4186851211072664
               elif obj[2]<=2016:
                  return 0.4935064935064935
               else:
                  return 0.4935064935064935
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 277, "metric_value": 0.005, "depth": 5}
               if obj[2]>2016:
                  return 0.4859437751004016
               elif obj[2]<=2016:
                  return 0.7142857142857143
               else:
                  return 0.7142857142857143
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 222, "metric_value": 0.0021, "depth": 5}
               if obj[2]>2016:
                  return 0.42948717948717946
               elif obj[2]<=2016:
                  return 0.5303030303030303
               else:
                  return 0.5303030303030303
            else:
               return 0.4594594594594595
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 113, "metric_value": 0.0132, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 49, "metric_value": 0.0, "depth": 5}
               if obj[2]>2016:
                  return 0.6122448979591837
               else:
                  return 0.6122448979591837
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 27, "metric_value": 0.0, "depth": 5}
               if obj[2]>2016:
                  return 0.6666666666666666
               else:
                  return 0.6666666666666666
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 20, "metric_value": 0.0, "depth": 5}
               if obj[2]>2016:
                  return 0.85
               else:
                  return 0.85
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 17, "metric_value": 0.0005, "depth": 5}
               if obj[2]<=2016:
                  return 0.5454545454545454
               elif obj[2]>2016:
                  return 0.5
               else:
                  return 0.5
            else:
               return 0.5294117647058824
         else:
            return 0.6548672566371682
      elif obj[4]<=0:
         # {"feature": "Region", "instances": 5538, "metric_value": 0.0543, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 1523, "metric_value": 0.0046, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 979, "metric_value": 0.004, "depth": 5}
               if obj[3] == 'Q3':
                  return 0.24850299401197604
               elif obj[3] == 'Q1':
                  return 0.2695035460992908
               elif obj[3] == 'Q2':
                  return 0.38990825688073394
               elif obj[3] == 'Q4':
                  return 0.33793103448275863
               else:
                  return 0.33793103448275863
            elif obj[5]>0:
               # {"feature": "Delivery_Year", "instances": 544, "metric_value": 0.0258, "depth": 5}
               if obj[2]>2016:
                  return 0.367170626349892
               elif obj[2]<=2016:
                  return 0.8024691358024691
               else:
                  return 0.8024691358024691
            else:
               return 0.4319852941176471
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 1462, "metric_value": 0.1122, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Year", "instances": 1286, "metric_value": 0.079, "depth": 5}
               if obj[2]<=2016:
                  return 0.9938434476693052
               elif obj[2]>2016:
                  return 0.6778523489932886
               else:
                  return 0.6778523489932886
            elif obj[5]<=0:
               # {"feature": "Delivery_Year", "instances": 176, "metric_value": 0.0156, "depth": 5}
               if obj[2]>2016:
                  return 0.2556390977443609
               elif obj[2]<=2016:
                  return 0.06976744186046512
               else:
                  return 0.06976744186046512
            else:
               return 0.21022727272727273
         elif obj[0] == 'Americas':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 1296, "metric_value": 0.0092, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Year", "instances": 862, "metric_value": 0.0035, "depth": 5}
               if obj[2]>2016:
                  return 0.3788300835654596
               elif obj[2]<=2016:
                  return 0.2361111111111111
               else:
                  return 0.2361111111111111
            elif obj[5]>0:
               # {"feature": "Delivery_Year", "instances": 434, "metric_value": 0.0081, "depth": 5}
               if obj[2]>2016:
                  return 0.5115606936416185
               elif obj[2]<=2016:
                  return 0.7272727272727273
               else:
                  return 0.7272727272727273
            else:
               return 0.5552995391705069
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 1235, "metric_value": 0.0107, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 854, "metric_value": 0.0134, "depth": 5}
               if obj[3] == 'Q2':
                  return 0.4406779661016949
               elif obj[3] == 'Q4':
                  return 0.2876712328767123
               elif obj[3] == 'Q3':
                  return 0.1625615763546798
               elif obj[3] == 'Q1':
                  return 0.30612244897959184
               else:
                  return 0.30612244897959184
            elif obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 381, "metric_value": 0.0123, "depth": 5}
               if obj[3] == 'Q2':
                  return 0.5092592592592593
               elif obj[3] == 'Q1':
                  return 0.4537037037037037
               elif obj[3] == 'Q3':
                  return 0.6862745098039216
               elif obj[3] == 'Q4':
                  return 0.38095238095238093
               else:
                  return 0.38095238095238093
            else:
               return 0.5196850393700787
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 22, "metric_value": 0.1256, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 15, "metric_value": 0.0, "depth": 5}
               if obj[2]>2016:
                  return 0.5333333333333333
               else:
                  return 0.5333333333333333
            elif obj[3] == 'Q2':
               return 1
            elif obj[3] == 'Q4':
               return 1
            else:
               return 1.0
         else:
            return 0.6818181818181818
      else:
         return 0.5084868183459733
   elif obj[1]>959840.9042772575:
      # {"feature": "Delivery_Year", "instances": 1951, "metric_value": 0.0168, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 1363, "metric_value": 0.0068, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 567, "metric_value": 0.0123, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 512, "metric_value": 0.0024, "depth": 5}
               if obj[3] == 'Q3':
                  return 0.9464285714285714
               elif obj[3] == 'Q1':
                  return 0.9693251533742331
               elif obj[3] == 'Q2':
                  return 0.9354838709677419
               elif obj[3] == 'Q4':
                  return 0.9473684210526315
               else:
                  return 0.9473684210526315
            elif obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 55, "metric_value": 0.0601, "depth": 5}
               if obj[3] == 'Q4':
                  return 0.6
               elif obj[3] == 'Q2':
                  return 0.9375
               elif obj[3] == 'Q1':
                  return 0.9333333333333333
               elif obj[3] == 'Q3':
                  return 0.5
               else:
                  return 0.5
            else:
               return 0.7818181818181819
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 476, "metric_value": 0.0051, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 159, "metric_value": 0.0061, "depth": 5}
               if obj[4]>0:
                  return 0.9183673469387755
               elif obj[4]<=0:
                  return 0.8360655737704918
               else:
                  return 0.8360655737704918
            elif obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 141, "metric_value": 0.0066, "depth": 5}
               if obj[5]>0:
                  return 0.9111111111111111
               elif obj[5]<=0:
                  return 1.0
               else:
                  return 1.0
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 122, "metric_value": 0.0009, "depth": 5}
               if obj[5]>0:
                  return 0.8660714285714286
               elif obj[5]<=0:
                  return 0.8
               else:
                  return 0.8
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 54, "metric_value": 0.0203, "depth": 5}
               if obj[5]>0:
                  return 0.76
               elif obj[5]<=0:
                  return 1.0
               else:
                  return 1.0
            else:
               return 0.7777777777777778
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 272, "metric_value": 0.0073, "depth": 4}
            if obj[4]<=0:
               # {"feature": "Delivery_Quarter", "instances": 143, "metric_value": 0.0063, "depth": 5}
               if obj[3] == 'Q3':
                  return 0.9130434782608695
               elif obj[3] == 'Q2':
                  return 0.8780487804878049
               elif obj[3] == 'Q4':
                  return 0.9655172413793104
               elif obj[3] == 'Q1':
                  return 0.9259259259259259
               else:
                  return 0.9259259259259259
            elif obj[4]>0:
               # {"feature": "Delivery_Quarter", "instances": 129, "metric_value": 0.031, "depth": 5}
               if obj[3] == 'Q2':
                  return 0.975
               elif obj[3] == 'Q3':
                  return 1.0
               elif obj[3] == 'Q1':
                  return 0.9444444444444444
               elif obj[3] == 'Q4':
                  return 0.9375
               else:
                  return 0.9375
            else:
               return 0.9689922480620154
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 30, "metric_value": 0.109, "depth": 4}
            if obj[4]>0:
               # {"feature": "Delivery_Quarter", "instances": 16, "metric_value": 0.0634, "depth": 5}
               if obj[3] == 'Q1':
                  return 0.6
               elif obj[3] == 'Q2':
                  return 0.75
               elif obj[3] == 'Q3':
                  return 0.75
               elif obj[3] == 'Q4':
                  return 1.0
               else:
                  return 1.0
            elif obj[4]<=0:
               return 1
            else:
               return 1.0
         elif obj[0] == 'Middle East':
            return 1
         else:
            return 1.0
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 588, "metric_value": 0.011, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 267, "metric_value": 0.0141, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 86, "metric_value": 0.0303, "depth": 5}
               if obj[4]>0:
                  return 0.5
               elif obj[4]<=0:
                  return 0.8235294117647058
               else:
                  return 0.8235294117647058
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 80, "metric_value": 0.0493, "depth": 5}
               if obj[5]>0:
                  return 0.8157894736842105
               elif obj[5]<=0:
                  return 0.0
               else:
                  return 0.0
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 61, "metric_value": 0.0136, "depth": 5}
               if obj[5]>0:
                  return 0.7586206896551724
               elif obj[5]<=0:
                  return 1.0
               else:
                  return 1.0
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 40, "metric_value": 0.0126, "depth": 5}
               if obj[4]<=0:
                  return 0.42424242424242425
               elif obj[4]>0:
                  return 0.7142857142857143
               else:
                  return 0.7142857142857143
            else:
               return 0.475
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 223, "metric_value": 0.008, "depth": 4}
            if obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 71, "metric_value": 0.0114, "depth": 5}
               if obj[5]>0:
                  return 0.7285714285714285
               elif obj[5]<=0:
                  return 0.0
               else:
                  return 0.0
            elif obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 61, "metric_value": 0.0069, "depth": 5}
               if obj[5]>0:
                  return 0.847457627118644
               elif obj[5]<=0:
                  return 1.0
               else:
                  return 1.0
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 51, "metric_value": 0.0553, "depth": 5}
               if obj[4]>0:
                  return 0.8157894736842105
               elif obj[4]<=0:
                  return 1.0
               else:
                  return 1.0
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 40, "metric_value": 0.0072, "depth": 5}
               if obj[4]>0:
                  return 0.71875
               elif obj[4]<=0:
                  return 0.875
               else:
                  return 0.875
            else:
               return 0.75
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 81, "metric_value": 0.1259, "depth": 4}
            if obj[4]<=0:
               return 1
            elif obj[4]>0:
               # {"feature": "Delivery_Quarter", "instances": 39, "metric_value": 0.1481, "depth": 5}
               if obj[3] == 'Q4':
                  return 0.6111111111111112
               elif obj[3] == 'Q1':
                  return 0.9
               elif obj[3] == 'Q2':
                  return 1.0
               elif obj[3] == 'Q3':
                  return 0.0
               else:
                  return 0.0
            else:
               return 0.717948717948718
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 15, "metric_value": 0.0773, "depth": 4}
            if obj[4]>0:
               # {"feature": "Delivery_Quarter", "instances": 13, "metric_value": 0.1676, "depth": 5}
               if obj[3] == 'Q3':
                  return 0.75
               elif obj[3] == 'Q1':
                  return 0.0
               elif obj[3] == 'Q2':
                  return 0.3333333333333333
               elif obj[3] == 'Q4':
                  return 0.5
               else:
                  return 0.5
            elif obj[4]<=0:
               return 1
            else:
               return 1.0
         elif obj[0] == 'Middle East':
            return 1
         else:
            return 1.0
      else:
         return 0.7448979591836735
   else:
      return 0.8636596617119426
