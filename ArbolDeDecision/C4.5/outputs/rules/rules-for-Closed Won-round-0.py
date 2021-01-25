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
                  return 0.9386503067484663
               elif obj[3] == 'Q1':
                  return 0.9172661870503597
               elif obj[3] == 'Q4':
                  return 0.9226618705035972
               elif obj[3] == 'Q3':
                  return 0.9174311926605505
               else:
                  return 0.9174311926605505
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 937, "metric_value": 0.0163, "depth": 5}
               if obj[3] == 'Q4':
                  return 1.0
               elif obj[3] == 'Q1':
                  return 0.9864864864864865
               elif obj[3] == 'Q3':
                  return 0.9861751152073732
               elif obj[3] == 'Q2':
                  return 0.9952153110047847
               else:
                  return 0.9952153110047847
            else:
               return 0.9925293489861259
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 1775, "metric_value": 0.0019, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 690, "metric_value": 0.004, "depth": 5}
               if obj[2]>2016:
                  return 0.6794425087108014
               elif obj[2]<=2016:
                  return 0.5172413793103449
               else:
                  return 0.5172413793103449
            elif obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 482, "metric_value": 0.004, "depth": 5}
               if obj[2]>2016:
                  return 0.5232876712328767
               elif obj[2]<=2016:
                  return 0.6666666666666666
               else:
                  return 0.6666666666666666
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 391, "metric_value": 0.0, "depth": 5}
               if obj[2]>2016:
                  return 0.5697674418604651
               elif obj[2]<=2016:
                  return 0.5531914893617021
               else:
                  return 0.5531914893617021
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 212, "metric_value": 0.018, "depth": 5}
               if obj[2]<=2016:
                  return 0.512987012987013
               elif obj[2]>2016:
                  return 0.7931034482758621
               else:
                  return 0.7931034482758621
            else:
               return 0.589622641509434
         elif obj[0] == 'APAC':
            # {"feature": "Delivery_Year", "instances": 1292, "metric_value": 0.0109, "depth": 4}
            if obj[2]>2016:
               # {"feature": "Delivery_Quarter", "instances": 940, "metric_value": 0.0024, "depth": 5}
               if obj[3] == 'Q2':
                  return 0.6863354037267081
               elif obj[3] == 'Q1':
                  return 0.5992779783393501
               elif obj[3] == 'Q3':
                  return 0.6846153846153846
               elif obj[3] == 'Q4':
                  return 0.7407407407407407
               else:
                  return 0.7407407407407407
            elif obj[2]<=2016:
               # {"feature": "Delivery_Quarter", "instances": 352, "metric_value": 0.0143, "depth": 5}
               if obj[3] == 'Q4':
                  return 0.8740157480314961
               elif obj[3] == 'Q3':
                  return 0.9186991869918699
               elif obj[3] == 'Q2':
                  return 0.78125
               elif obj[3] == 'Q1':
                  return 0.6842105263157895
               else:
                  return 0.6842105263157895
            else:
               return 0.8522727272727273
         elif obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 1277, "metric_value": 0.0021, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 412, "metric_value": 0.0006, "depth": 5}
               if obj[2]>2016:
                  return 0.46216216216216216
               elif obj[2]<=2016:
                  return 0.38095238095238093
               else:
                  return 0.38095238095238093
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 366, "metric_value": 0.0009, "depth": 5}
               if obj[2]>2016:
                  return 0.5813148788927336
               elif obj[2]<=2016:
                  return 0.5064935064935064
               else:
                  return 0.5064935064935064
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 277, "metric_value": 0.005, "depth": 5}
               if obj[2]>2016:
                  return 0.5140562248995983
               elif obj[2]<=2016:
                  return 0.2857142857142857
               else:
                  return 0.2857142857142857
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 222, "metric_value": 0.0021, "depth": 5}
               if obj[2]>2016:
                  return 0.5705128205128205
               elif obj[2]<=2016:
                  return 0.4696969696969697
               else:
                  return 0.4696969696969697
            else:
               return 0.5405405405405406
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 113, "metric_value": 0.0132, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 49, "metric_value": 0.0, "depth": 5}
               if obj[2]>2016:
                  return 0.3877551020408163
               else:
                  return 0.3877551020408163
            elif obj[3] == 'Q1':
               # {"feature": "Delivery_Year", "instances": 27, "metric_value": 0.0, "depth": 5}
               if obj[2]>2016:
                  return 0.3333333333333333
               else:
                  return 0.3333333333333333
            elif obj[3] == 'Q2':
               # {"feature": "Delivery_Year", "instances": 20, "metric_value": 0.0, "depth": 5}
               if obj[2]>2016:
                  return 0.15
               else:
                  return 0.15
            elif obj[3] == 'Q4':
               # {"feature": "Delivery_Year", "instances": 17, "metric_value": 0.0005, "depth": 5}
               if obj[2]<=2016:
                  return 0.45454545454545453
               elif obj[2]>2016:
                  return 0.5
               else:
                  return 0.5
            else:
               return 0.47058823529411764
         else:
            return 0.34513274336283184
      elif obj[4]<=0:
         # {"feature": "Region", "instances": 5538, "metric_value": 0.0543, "depth": 3}
         if obj[0] == 'EMEA':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 1523, "metric_value": 0.0046, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 979, "metric_value": 0.004, "depth": 5}
               if obj[3] == 'Q3':
                  return 0.7514970059880239
               elif obj[3] == 'Q1':
                  return 0.7304964539007093
               elif obj[3] == 'Q2':
                  return 0.6100917431192661
               elif obj[3] == 'Q4':
                  return 0.6620689655172414
               else:
                  return 0.6620689655172414
            elif obj[5]>0:
               # {"feature": "Delivery_Year", "instances": 544, "metric_value": 0.0258, "depth": 5}
               if obj[2]>2016:
                  return 0.6328293736501079
               elif obj[2]<=2016:
                  return 0.19753086419753085
               else:
                  return 0.19753086419753085
            else:
               return 0.5680147058823529
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 1462, "metric_value": 0.1122, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Year", "instances": 1286, "metric_value": 0.079, "depth": 5}
               if obj[2]<=2016:
                  return 0.006156552330694811
               elif obj[2]>2016:
                  return 0.3221476510067114
               else:
                  return 0.3221476510067114
            elif obj[5]<=0:
               # {"feature": "Delivery_Year", "instances": 176, "metric_value": 0.0156, "depth": 5}
               if obj[2]>2016:
                  return 0.7443609022556391
               elif obj[2]<=2016:
                  return 0.9302325581395349
               else:
                  return 0.9302325581395349
            else:
               return 0.7897727272727273
         elif obj[0] == 'Americas':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 1296, "metric_value": 0.0092, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Year", "instances": 862, "metric_value": 0.0035, "depth": 5}
               if obj[2]>2016:
                  return 0.6211699164345403
               elif obj[2]<=2016:
                  return 0.7638888888888888
               else:
                  return 0.7638888888888888
            elif obj[5]>0:
               # {"feature": "Delivery_Year", "instances": 434, "metric_value": 0.0081, "depth": 5}
               if obj[2]>2016:
                  return 0.4884393063583815
               elif obj[2]<=2016:
                  return 0.2727272727272727
               else:
                  return 0.2727272727272727
            else:
               return 0.4447004608294931
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 1235, "metric_value": 0.0107, "depth": 4}
            if obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 854, "metric_value": 0.0134, "depth": 5}
               if obj[3] == 'Q2':
                  return 0.559322033898305
               elif obj[3] == 'Q4':
                  return 0.7123287671232876
               elif obj[3] == 'Q3':
                  return 0.8374384236453202
               elif obj[3] == 'Q1':
                  return 0.6938775510204082
               else:
                  return 0.6938775510204082
            elif obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 381, "metric_value": 0.0123, "depth": 5}
               if obj[3] == 'Q2':
                  return 0.49074074074074076
               elif obj[3] == 'Q1':
                  return 0.5462962962962963
               elif obj[3] == 'Q3':
                  return 0.3137254901960784
               elif obj[3] == 'Q4':
                  return 0.6190476190476191
               else:
                  return 0.6190476190476191
            else:
               return 0.48031496062992124
         elif obj[0] == 'Middle East':
            # {"feature": "Delivery_Quarter", "instances": 22, "metric_value": 0.1256, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Delivery_Year", "instances": 15, "metric_value": 0.0, "depth": 5}
               if obj[2]>2016:
                  return 0.4666666666666667
               else:
                  return 0.4666666666666667
            elif obj[3] == 'Q2':
               return 0
            elif obj[3] == 'Q4':
               return 0
            else:
               return 0.0
         else:
            return 0.3181818181818182
      else:
         return 0.49151318165402674
   elif obj[1]>959840.9042772575:
      # {"feature": "Delivery_Year", "instances": 1951, "metric_value": 0.0168, "depth": 2}
      if obj[2]>2016:
         # {"feature": "Region", "instances": 1363, "metric_value": 0.0068, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 567, "metric_value": 0.0123, "depth": 4}
            if obj[5]>0:
               # {"feature": "Delivery_Quarter", "instances": 512, "metric_value": 0.0024, "depth": 5}
               if obj[3] == 'Q3':
                  return 0.05357142857142857
               elif obj[3] == 'Q1':
                  return 0.03067484662576687
               elif obj[3] == 'Q2':
                  return 0.06451612903225806
               elif obj[3] == 'Q4':
                  return 0.05263157894736842
               else:
                  return 0.05263157894736842
            elif obj[5]<=0:
               # {"feature": "Delivery_Quarter", "instances": 55, "metric_value": 0.0601, "depth": 5}
               if obj[3] == 'Q4':
                  return 0.4
               elif obj[3] == 'Q2':
                  return 0.0625
               elif obj[3] == 'Q1':
                  return 0.06666666666666667
               elif obj[3] == 'Q3':
                  return 0.5
               else:
                  return 0.5
            else:
               return 0.21818181818181817
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 476, "metric_value": 0.0051, "depth": 4}
            if obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 159, "metric_value": 0.0061, "depth": 5}
               if obj[4]>0:
                  return 0.08163265306122448
               elif obj[4]<=0:
                  return 0.16393442622950818
               else:
                  return 0.16393442622950818
            elif obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 141, "metric_value": 0.0066, "depth": 5}
               if obj[5]>0:
                  return 0.08888888888888889
               elif obj[5]<=0:
                  return 0.0
               else:
                  return 0.0
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 122, "metric_value": 0.0009, "depth": 5}
               if obj[5]>0:
                  return 0.13392857142857142
               elif obj[5]<=0:
                  return 0.2
               else:
                  return 0.2
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 54, "metric_value": 0.0203, "depth": 5}
               if obj[5]>0:
                  return 0.24
               elif obj[5]<=0:
                  return 0.0
               else:
                  return 0.0
            else:
               return 0.2222222222222222
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 272, "metric_value": 0.0073, "depth": 4}
            if obj[4]<=0:
               # {"feature": "Delivery_Quarter", "instances": 143, "metric_value": 0.0063, "depth": 5}
               if obj[3] == 'Q3':
                  return 0.08695652173913043
               elif obj[3] == 'Q2':
                  return 0.12195121951219512
               elif obj[3] == 'Q4':
                  return 0.034482758620689655
               elif obj[3] == 'Q1':
                  return 0.07407407407407407
               else:
                  return 0.07407407407407407
            elif obj[4]>0:
               # {"feature": "Delivery_Quarter", "instances": 129, "metric_value": 0.031, "depth": 5}
               if obj[3] == 'Q2':
                  return 0.025
               elif obj[3] == 'Q3':
                  return 0.0
               elif obj[3] == 'Q1':
                  return 0.05555555555555555
               elif obj[3] == 'Q4':
                  return 0.0625
               else:
                  return 0.0625
            else:
               return 0.031007751937984496
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 30, "metric_value": 0.109, "depth": 4}
            if obj[4]>0:
               # {"feature": "Delivery_Quarter", "instances": 16, "metric_value": 0.0634, "depth": 5}
               if obj[3] == 'Q1':
                  return 0.4
               elif obj[3] == 'Q2':
                  return 0.25
               elif obj[3] == 'Q3':
                  return 0.25
               elif obj[3] == 'Q4':
                  return 0.0
               else:
                  return 0.0
            elif obj[4]<=0:
               return 0
            else:
               return 0.0
         elif obj[0] == 'Middle East':
            return 0
         else:
            return 0.0
      elif obj[2]<=2016:
         # {"feature": "Region", "instances": 588, "metric_value": 0.011, "depth": 3}
         if obj[0] == 'Americas':
            # {"feature": "Delivery_Quarter", "instances": 267, "metric_value": 0.0141, "depth": 4}
            if obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 86, "metric_value": 0.0303, "depth": 5}
               if obj[4]>0:
                  return 0.5
               elif obj[4]<=0:
                  return 0.17647058823529413
               else:
                  return 0.17647058823529413
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 80, "metric_value": 0.0493, "depth": 5}
               if obj[5]>0:
                  return 0.18421052631578946
               elif obj[5]<=0:
                  return 1.0
               else:
                  return 1.0
            elif obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 61, "metric_value": 0.0136, "depth": 5}
               if obj[5]>0:
                  return 0.2413793103448276
               elif obj[5]<=0:
                  return 0.0
               else:
                  return 0.0
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 40, "metric_value": 0.0126, "depth": 5}
               if obj[4]<=0:
                  return 0.5757575757575758
               elif obj[4]>0:
                  return 0.2857142857142857
               else:
                  return 0.2857142857142857
            else:
               return 0.525
         elif obj[0] == 'EMEA':
            # {"feature": "Delivery_Quarter", "instances": 223, "metric_value": 0.008, "depth": 4}
            if obj[3] == 'Q4':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 71, "metric_value": 0.0114, "depth": 5}
               if obj[5]>0:
                  return 0.2714285714285714
               elif obj[5]<=0:
                  return 1.0
               else:
                  return 1.0
            elif obj[3] == 'Q2':
               # {"feature": "Pricing, Delivery_Terms_Quote_Appr", "instances": 61, "metric_value": 0.0069, "depth": 5}
               if obj[5]>0:
                  return 0.15254237288135594
               elif obj[5]<=0:
                  return 0.0
               else:
                  return 0.0
            elif obj[3] == 'Q3':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 51, "metric_value": 0.0553, "depth": 5}
               if obj[4]>0:
                  return 0.18421052631578946
               elif obj[4]<=0:
                  return 0.0
               else:
                  return 0.0
            elif obj[3] == 'Q1':
               # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 40, "metric_value": 0.0072, "depth": 5}
               if obj[4]>0:
                  return 0.28125
               elif obj[4]<=0:
                  return 0.125
               else:
                  return 0.125
            else:
               return 0.25
         elif obj[0] == 'APAC':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 81, "metric_value": 0.1259, "depth": 4}
            if obj[4]<=0:
               return 0
            elif obj[4]>0:
               # {"feature": "Delivery_Quarter", "instances": 39, "metric_value": 0.1481, "depth": 5}
               if obj[3] == 'Q4':
                  return 0.3888888888888889
               elif obj[3] == 'Q1':
                  return 0.1
               elif obj[3] == 'Q2':
                  return 0.0
               elif obj[3] == 'Q3':
                  return 1.0
               else:
                  return 1.0
            else:
               return 0.28205128205128205
         elif obj[0] == 'Japan':
            # {"feature": "Pricing, Delivery_Terms_Approved", "instances": 15, "metric_value": 0.0773, "depth": 4}
            if obj[4]>0:
               # {"feature": "Delivery_Quarter", "instances": 13, "metric_value": 0.1676, "depth": 5}
               if obj[3] == 'Q3':
                  return 0.25
               elif obj[3] == 'Q1':
                  return 1.0
               elif obj[3] == 'Q2':
                  return 0.6666666666666666
               elif obj[3] == 'Q4':
                  return 0.5
               else:
                  return 0.5
            elif obj[4]<=0:
               return 0
            else:
               return 0.0
         elif obj[0] == 'Middle East':
            return 0
         else:
            return 0.0
      else:
         return 0.25510204081632654
   else:
      return 0.13634033828805742
