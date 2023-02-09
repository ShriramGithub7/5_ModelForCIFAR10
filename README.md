# Problem Statement:
Build a CNN which satisfies below conditions:
  - total RF must be more than 44
  - use Depthwise Separable Convolution, Dilated Convolution, GAP (compulsory), albumentation with techniques
    -  horizontal flip
    -  shiftScaleRotate
    -  coarseDropout
    -  
# Expected Output:
  - Achieve 85% accuracy, with less than 200k parameters. No restrictions on number of epochs



# Training logs





             [1    6000] loss: 1.886 
             [1   12000] loss: 1.646 
             Test set: Average loss: 0.3907   Accuracy: 4305/10000 (43.05%)     
            
             [2    6000] loss: 1.525     
             [2   12000] loss: 1.446     
             Test set: Average loss: 0.3535   Accuracy: 4912/10000 (49.12%)     
                  
             [3    6000] loss: 1.375     
             [3   12000] loss: 1.332         
             Test set: Average loss: 0.3201   Accuracy: 5378/10000 (53.78%)     
                  
             [4    6000] loss: 1.274     
             [4   12000] loss: 1.253     
             Test set: Average loss: 0.3158   Accuracy: 5513/10000 (55.13%)     
                  
             [5    6000] loss: 1.214     
             [5   12000] loss: 1.202     
             Test set: Average loss: 0.2946   Accuracy: 5797/10000 (57.97%)     
             [6    6000] loss: 1.171     
             [6   12000] loss: 1.154     
             Test set: Average loss: 0.2859   Accuracy: 5928/10000 (59.28%)     
                  
             [7    6000] loss: 1.132     
             [7   12000] loss: 1.124     
             Test set: Average loss: 0.2894   Accuracy: 5908/10000 (59.08%)     
                  
             [8    6000] loss: 1.106     
             [8   12000] loss: 1.098     
             Test set: Average loss: 0.2755   Accuracy: 6056/10000 (60.56%)     
                  
             [9    6000] loss: 1.068     
             [9   12000] loss: 1.064     
             Test set: Average loss: 0.2680   Accuracy: 6154/10000 (61.54%)     
                  
             [10    6000] loss: 1.051     
             [10   12000] loss: 1.049     
             Test set: Average loss: 0.2646   Accuracy: 6251/10000 (62.51%)     
                  
             [11    6000] loss: 1.029     
             [11   12000] loss: 1.030     
             Test set: Average loss: 0.2581   Accuracy: 6335/10000 (63.35%)     
                  
             [12    6000] loss: 1.012     
             [12   12000] loss: 1.015     
             Test set: Average loss: 0.2523   Accuracy: 6466/10000 (64.66%)     
                  
             [13    6000] loss: 1.004     
             [13   12000] loss: 0.982     
             Test set: Average loss: 0.2516   Accuracy: 6444/10000 (64.44%)     
                  
             [14    6000] loss: 0.982     
             [14   12000] loss: 0.985     
             Test set: Average loss: 0.2536   Accuracy: 6441/10000 (64.41%)     
                  
             [15    6000] loss: 0.971     
             [15   12000] loss: 0.976     
             Test set: Average loss: 0.2541   Accuracy: 6462/10000 (64.62%)     
                  
             [16    6000] loss: 0.955     
             [16   12000] loss: 0.955     
             Test set: Average loss: 0.2441   Accuracy: 6561/10000 (65.61%)     
                  
             [17    6000] loss: 0.945     
             [17   12000] loss: 0.942     
             Test set: Average loss: 0.2382   Accuracy: 6604/10000 (66.04%)     
                  
             [18    6000] loss: 0.941     
             [18   12000] loss: 0.930     
             Test set: Average loss: 0.2421   Accuracy: 6672/10000 (66.72%)     
                  
             [19    6000] loss: 0.923     
             [19   12000] loss: 0.930     
             Test set: Average loss: 0.2386   Accuracy: 6627/10000 (66.27%)     
                  
             [20    6000] loss: 0.916     
             [20   12000] loss: 0.924     
             Test set: Average loss: 0.2466   Accuracy: 6531/10000 (65.31%)     
                  
             [21    6000] loss: 0.898     
             [21   12000] loss: 0.920     
             Test set: Average loss: 0.2309   Accuracy: 6736/10000 (67.36%)     
                  
             [22    6000] loss: 0.900     
             [22   12000] loss: 0.890     
             Test set: Average loss: 0.2325   Accuracy: 6671/10000 (66.71%)     
                  
             [23    6000] loss: 0.894     
             [23   12000] loss: 0.888     
             Test set: Average loss: 0.2360   Accuracy: 6706/10000 (67.06%)     
                  
             [24    6000] loss: 0.882     
             [24   12000] loss: 0.901     
             Test set: Average loss: 0.2309   Accuracy: 6773/10000 (67.73%)     
                  
             [25    6000] loss: 0.880     
             [25   12000] loss: 0.875     
             Test set: Average loss: 0.2248   Accuracy: 6834/10000 (68.34%)     
                  
             [26    6000] loss: 0.878     
             [26   12000] loss: 0.883     
             Test set: Average loss: 0.2325   Accuracy: 6789/10000 (67.89%)     
                  
             [27    6000] loss: 0.872     
             [27   12000] loss: 0.865     
             Test set: Average loss: 0.2268   Accuracy: 6817/10000 (68.17%)     
                  
             [28    6000] loss: 0.852     
             [28   12000] loss: 0.862     
             Test set: Average loss: 0.2267   Accuracy: 6801/10000 (68.01%)     
                  
             [29    6000] loss: 0.856     
             [29   12000] loss: 0.854     
             Test set: Average loss: 0.2279   Accuracy: 6809/10000 (68.09%)     
                  
             [30    6000] loss: 0.853     
             [30   12000] loss: 0.851     
             Test set: Average loss: 0.2283   Accuracy: 6773/10000 (67.73%)     
                  
             [31    6000] loss: 0.841     
             [31   12000] loss: 0.855     
             Test set: Average loss: 0.2211   Accuracy: 6911/10000 (69.11%)     
                  
             [32    6000] loss: 0.843     
             [32   12000] loss: 0.836     
             Test set: Average loss: 0.2273   Accuracy: 6891/10000 (68.91%)     
                  
             [33    6000] loss: 0.841     
             [33   12000] loss: 0.835     
             Test set: Average loss: 0.2267   Accuracy: 6815/10000 (68.15%)     
                  
             [34    6000] loss: 0.827     
             [34   12000] loss: 0.838     
             Test set: Average loss: 0.2226   Accuracy: 6909/10000 (69.09%)     
                  
             [35    6000] loss: 0.819     
             [35   12000] loss: 0.829     
             Test set: Average loss: 0.2184   Accuracy: 6911/10000 (69.11%)     
                  
             [36    6000] loss: 0.817     
             [36   12000] loss: 0.819     
             Test set: Average loss: 0.2193   Accuracy: 6949/10000 (69.49%)     
                  
             [37    6000] loss: 0.819     
             [37   12000] loss: 0.829     
             Test set: Average loss: 0.2257   Accuracy: 6851/10000 (68.51%)     
                  
             [38    6000] loss: 0.818     
             [38   12000] loss: 0.803     
             Test set: Average loss: 0.2187   Accuracy: 6964/10000 (69.64%)     
                  
             [39    6000] loss: 0.817     
             [39   12000] loss: 0.806     
             Test set: Average loss: 0.2200   Accuracy: 6889/10000 (68.89%)     
                  
             [40    6000] loss: 0.809     
             [40   12000] loss: 0.804     
             Test set: Average loss: 0.2236   Accuracy: 6877/10000 (68.77%)     
                  
             [41    6000] loss: 0.807     
             [41   12000] loss: 0.799     
             Test set: Average loss: 0.2184   Accuracy: 6948/10000 (69.48%)     
                  
             [42    6000] loss: 0.794     
             [42   12000] loss: 0.802     
             Test set: Average loss: 0.2291   Accuracy: 6848/10000 (68.48%)     
                  
             [43    6000] loss: 0.788     
             [43   12000] loss: 0.811     
             Test set: Average loss: 0.2176   Accuracy: 6914/10000 (69.14%)     
                  
             [44    6000] loss: 0.795     
             [44   12000] loss: 0.790     
             Test set: Average loss: 0.2147   Accuracy: 7002/10000 (70.02%)     
                  
             [45    6000] loss: 0.783     
             [45   12000] loss: 0.784     
             Test set: Average loss: 0.2131   Accuracy: 7072/10000 (70.72%)     
                  
             [46    6000] loss: 0.784     
             [46   12000] loss: 0.783     
             Test set: Average loss: 0.2171   Accuracy: 7018/10000 (70.18%)     
                  
             [47    6000] loss: 0.787     
             [47   12000] loss: 0.786     
             Test set: Average loss: 0.2125   Accuracy: 7030/10000 (70.30%)     
                  
             [48    6000] loss: 0.777     
             [48   12000] loss: 0.780     
             Test set: Average loss: 0.2119   Accuracy: 7042/10000 (70.42%)     
                  
             [49    6000] loss: 0.778     
             [49   12000] loss: 0.774     
             Test set: Average loss: 0.2164   Accuracy: 6983/10000 (69.83%)     
                  
             [50    6000] loss: 0.785     
             [50   12000] loss: 0.771     
             Test set: Average loss: 0.2083   Accuracy: 7129/10000 (71.29%)     
                  
             [51    6000] loss: 0.769     
             [51   12000] loss: 0.777     
             Test set: Average loss: 0.2120   Accuracy: 7044/10000 (70.44%)     
                  
             [52    6000] loss: 0.773     
             [52   12000] loss: 0.773     
             Test set: Average loss: 0.2110   Accuracy: 6994/10000 (69.94%)     
                  
             [53    6000] loss: 0.771     
             [53   12000] loss: 0.767     
             Test set: Average loss: 0.2079   Accuracy: 7106/10000 (71.06%)     
                  
             [54    6000] loss: 0.751     
             [54   12000] loss: 0.774     
             Test set: Average loss: 0.2086   Accuracy: 7121/10000 (71.21%)     
                  
             [55    6000] loss: 0.762     
             [55   12000] loss: 0.771     
             Test set: Average loss: 0.2077   Accuracy: 7099/10000 (70.99%)     
                  
             [56    6000] loss: 0.760     
             [56   12000] loss: 0.763     
             Test set: Average loss: 0.2137   Accuracy: 7100/10000 (71.00%)     
                  
             [57    6000] loss: 0.756     
             [57   12000] loss: 0.763     
             Test set: Average loss: 0.2078   Accuracy: 7110/10000 (71.10%)     
                  
             [58    6000] loss: 0.754     
             [58   12000] loss: 0.757     
             Test set: Average loss: 0.2090   Accuracy: 7097/10000 (70.97%)     
                  
             [59    6000] loss: 0.762     
             [59   12000] loss: 0.752     
             Test set: Average loss: 0.2085   Accuracy: 7107/10000 (71.07%)     
                  
             [60    6000] loss: 0.752     
             [60   12000] loss: 0.752     
             Test set: Average loss: 0.2065   Accuracy: 7125/10000 (71.25%)     
                  
             [61    6000] loss: 0.742     
             [61   12000] loss: 0.745     
             Test set: Average loss: 0.2052   Accuracy: 7078/10000 (70.78%)     
                  
             [62    6000] loss: 0.752     
             [62   12000] loss: 0.756     
             Test set: Average loss: 0.2081   Accuracy: 7154/10000 (71.54%)     
                  
             [63    6000] loss: 0.736     
             [63   12000] loss: 0.736     
             Test set: Average loss: 0.2043   Accuracy: 7150/10000 (71.50%)     
                  
             [64    6000] loss: 0.737     
             [64   12000] loss: 0.742     
             Test set: Average loss: 0.2053   Accuracy: 7127/10000 (71.27%)     
                  
             [65    6000] loss: 0.737     
             [65   12000] loss: 0.738     
             Test set: Average loss: 0.2076   Accuracy: 7111/10000 (71.11%)     
                  
             [66    6000] loss: 0.738     
             [66   12000] loss: 0.742     
             Test set: Average loss: 0.2092   Accuracy: 7129/10000 (71.29%)     
                  
             [67    6000] loss: 0.734     
             [67   12000] loss: 0.736     
             Test set: Average loss: 0.2052   Accuracy: 7194/10000 (71.94%)     
                  
             [68    6000] loss: 0.723     
             [68   12000] loss: 0.738     
             Test set: Average loss: 0.2019   Accuracy: 7211/10000 (72.11%)     
                  
             [69    6000] loss: 0.731     
             [69   12000] loss: 0.737     
             Test set: Average loss: 0.1998   Accuracy: 7234/10000 (72.34%)     
                  
             [70    6000] loss: 0.730     
             [70   12000] loss: 0.726     
             Test set: Average loss: 0.2057   Accuracy: 7180/10000 (71.80%)     
                
         
# Graphs: Test Accuracy

![image](https://user-images.githubusercontent.com/93775361/217713950-4fbc796c-85e3-4b13-9f56-e976fdc20426.png)

