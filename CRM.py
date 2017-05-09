# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:52:25 2017

@author: Elias Ayrey
"""

#import fme
#import fmeobjects
import math
import numpy as np

###################################################################################
## Stump DOB and DIB coefs                                                       #
##################################################################################
Stump_coefs={'SM':[0.12798,0.92267,0.12506],'YB':[0.11585,0.94181,0.1074],'PB':[0.11585,0.94181,0.1074], 'BEAL':[0.11585,0.94181,0.1074],
                'BEPA':[0.11585,0.94181,0.1074],'GB':[0.11585,0.94181,0.1074], 'SB':[0.11585,0.94181,0.1074], 'RM':[0.11585,0.94181,0.1074],
                'MM':[0.11585,0.94181,0.1074], 'ACRU':[0.11585,0.94181,0.1074], 'GA': [0.12766,0.91979,0.12152], 'WA':[0.12766,0.91979,0.12152],
                'BT':[0.09658,0.91882,0.08593], 'BTA':[0.09658,0.91882,0.08593], 'QA':[0.09658,0.91882,0.08593],'BP':[0.09658,0.91882,0.08593],
                'BE':[0.12798,0.92267,0.12506], 'AB':[0.12798,0.92267,0.12506],'RO':[0.12798,0.92267,0.12506],'WO':[0.12798,0.92267,0.12506],
                'CO':[0.12798,0.92267,0.12506],'BC':[0.12798,0.92267,0.12506],'BF':[0.12667,0.914,0.11975], 'ABBA':[0.12667,0.914,0.11975], 
                'RS':[0.14525,0.94804,0.13722],'PIRU':[0.14525,0.94804,0.13722],'WS':[0.14525,0.94804,0.13722],'BS':[0.14525,0.94804,0.13722],
                'WP':[0.08091,0.90698,0.08469], 'PIST':[0.08091,0.90698,0.08469], 'TA':[0.12667,0.914,0.11975],'NS':[0.14525,0.94804,0.13722],
                'JP':[0.08091,0.90698,0.08469],'PP':[0.08091,0.90698,0.08469], 'NC':[0.12667,0.914,0.11975], 'THOC':[0.12667,0.914,0.11975],
                'WC':[0.12667,0.914,0.11975],'NWC':[0.12667,0.914,0.11975],'RP':[0.08091,0.90698,0.08469], 'EH':[0.12667,0.914,0.11975],
                'TSCA':[0.12667,0.914,0.11975], 'HE':[0.12667,0.914,0.11975], 'BW':[0.12766,0.91979,0.12152], 'HH':[0.12766,0.91979,0.12152],
                'OH':[0.12766,0.91979,0.12152]}

###################################################################################
## Jenkins simplified ratio equations                                            #
##################################################################################
JENKINS_STEM_WOOD_RATIO_B1={'SM':-0.3065,'YB':-0.3065, 'PB':-0.3065, 'BEAL':-0.3065,'BEPA':-0.3065,'GB':-0.3065, 'SB':-0.3065, 'RM':-0.3065,
                'MM':-0.3065, 'ACRU':-0.3065, 'GA': -0.3065, 'WA':-0.3065, 'BT':-0.3065, 'BTA':-0.3065, 'QA':-0.3065,'BP':-0.3065,
                'BE':-0.3065, 'AB':-0.3065,'RO':-0.3065,'WO':-0.3065,'CO':-0.3065,'BC':-0.3065,'BF':-0.3737, 'ABBA':-0.3737, 'RS':-0.3737,
                'PIRU':-0.3737,'WS':-0.3737,'BS':-0.3737,'WP':-0.3737, 'PIST':-0.3737, 'TA':-0.3737,'NS':-0.3737, 'JP':-0.3737,'PP':-0.3737,
                'NC':-0.3737, 'THOC':-0.3737,'WC':-0.3737,'NWC':-0.3737,'RP':-0.3737, 'EH':-0.3737, 'TSCA':-0.3737, 'HE':-0.3737, 
                'BW':-0.3065, 'HH':-0.3065, 'OH':-0.3065}

JENKINS_STEM_WOOD_RATIO_B2={'SM':-5.424,'YB':-5.424, 'PB':-5.424, 'BEAL':-5.424,'BEPA':-5.424,'GB':-5.424, 'SB':-5.424, 'RM':-5.424,
                'MM':-5.424, 'ACRU':-5.424, 'GA': -5.424, 'WA':-5.424, 'BT':-5.424, 'BTA':-5.424, 'QA':-5.424,'BP':-5.424,
                'BE':-5.424, 'AB':-5.424,'RO':-5.424,'WO':-5.424,'CO':-5.424,'BC':-5.424,'BF':-1.8055, 'ABBA':-1.8055, 'RS':-1.8055,
                'PIRU':-1.8055,'WS':-1.8055,'BS':-1.8055,'WP':-1.8055, 'PIST':-1.8055, 'TA':-1.8055,'NS':-1.8055, 'JP':-1.8055,'PP':-1.8055,
                'NC':-1.8055, 'THOC':-1.8055,'WC':-1.8055,'NWC':-1.8055,'RP':-1.8055, 'EH':-1.8055, 'TSCA':-1.8055, 'HE':-1.8055, 
                'BW':-5.424, 'HH':-5.424, 'OH':-5.424}
                
JENKINS_STEM_BARK_RATIO_B1={'SM':-2.0129,'YB':-2.0129, 'PB':-2.0129, 'BEAL':-2.0129,'BEPA':-2.0129,'GB':-2.0129, 'SB':-2.0129, 'RM':-2.0129,
                'MM':-2.0129, 'ACRU':-2.0129, 'GA': -2.0129, 'WA':-2.0129, 'BT':-2.0129, 'BTA':-2.0129, 'QA':-2.0129,'BP':-2.0129,
                'BE':-2.0129, 'AB':-2.0129,'RO':-2.0129,'WO':-2.0129,'CO':-2.0129,'BC':-2.0129,'BF':-2.098, 'ABBA':-2.098, 'RS':-2.098,
                'PIRU':-2.098,'WS':-2.098,'BS':-2.098,'WP':-2.098, 'PIST':-2.098, 'TA':-2.098,'NS':-2.098, 'JP':-2.098,'PP':-2.098,
                'NC':-2.098, 'THOC':-2.098,'WC':-2.098,'NWC':-2.098,'RP':-2.098, 'EH':-2.098, 'TSCA':-2.098, 'HE':-2.098, 
                'BW':-2.0129, 'HH':-2.0129, 'OH':-2.0129}

JENKINS_STEM_BARK_RATIO_B2={'SM':-1.6805,'YB':-1.6805, 'PB':-1.6805, 'BEAL':-1.6805,'BEPA':-1.6805,'GB':-1.6805, 'SB':-1.6805, 'RM':-1.6805,
                'MM':-1.6805, 'ACRU':-1.6805, 'GA': -1.6805, 'WA':-1.6805, 'BT':-1.6805, 'BTA':-1.6805, 'QA':-1.6805,'BP':-1.6805,
                'BE':-1.6805, 'AB':-1.6805,'RO':-1.6805,'WO':-1.6805,'CO':-1.6805,'BC':-1.6805,'BF':-1.1432, 'ABBA':-1.1432, 'RS':-1.1432,
                'PIRU':-1.1432,'WS':-1.1432,'BS':-1.1432,'WP':-1.1432, 'PIST':-1.1432, 'TA':-1.1432,'NS':-1.1432, 'JP':-1.1432,'PP':-1.1432,
                'NC':-1.1432, 'THOC':-1.1432,'WC':-1.1432,'NWC':-1.1432,'RP':-1.1432, 'EH':-1.1432, 'TSCA':-1.1432, 'HE':-1.1432, 
                'BW':-1.6805, 'HH':-1.6805, 'OH':-1.6805}
                
JENKINS_TOTAL_B1 ={'SM':-2.0127,'YB':-1.9123, 'PB':-1.9123, 'BEAL':-1.9123,'BEPA':-1.9123,'GB':-1.9123, 'SB':-1.9123, 'RM':-1.9123,
                'MM':-1.9123, 'ACRU':-1.9123, 'GA': -2.48, 'WA':-2.48, 'BT':-2.2094, 'BTA':-2.2094, 'QA':-2.2094,'BP':-2.2094,
                'BE':-2.0127, 'AB':-2.48,'RO':-2.0127,'WO':-2.0127,'CO':-2.0127,'BC':-2.48,'BF':-2.5384, 'ABBA':-2.5384, 'RS':-2.0773,
                'PIRU':-2.0773,'WS':-2.0773,'BS':-2.0773,'WP':-2.5356, 'PIST':-2.5356, 'TA':-2.0336,'NS':-2.0773, 'JP':-2.5356,'PP':-2.5356,
                'NC':-2.0336, 'THOC':-2.0336,'WC':-2.0336,'NWC':-2.0336,'RP':-2.5356, 'EH':-2.5384, 'TSCA':-2.5384, 'HE':-2.5384, 
                'BW':-2.48, 'HH':-2.48, 'OH':-2.48}    

JENKINS_TOTAL_B2 ={'SM':2.4342,'YB':2.3651, 'PB':2.3651, 'BEAL':2.3651,'BEPA':2.3651,'GB':2.3651, 'SB':2.3651, 'RM':2.3651,
                'MM':2.3651, 'ACRU':2.3651, 'GA': 2.4835, 'WA':2.4835, 'BT':2.3867, 'BTA':2.3867, 'QA':2.3867,'BP':2.3867,
                'BE':2.4342, 'AB':2.4835,'RO':2.4342,'WO':2.4342,'CO':2.4342,'BC':2.4835,'BF':2.4814, 'ABBA':2.4814, 'RS':2.3323,
                'PIRU':2.3323,'WS':2.3323,'BS':2.3323,'WP':2.4349, 'PIST':2.4349, 'TA':2.2592,'NS':2.3323, 'JP':2.4349,'PP':2.4349,
                'NC':2.2592, 'THOC':2.2592,'WC':2.2592,'NWC':2.2592,'RP':2.4349, 'EH':2.4814, 'TSCA':2.4814, 'HE':2.4814, 
                'BW':2.4835, 'HH':2.4835, 'OH':2.4835}   
                
JENKINS_FOLIAGE_RATIO_B1 ={'SM':-4.0813,'YB':-4.0813, 'PB':-4.0813, 'BEAL':-4.0813,'BEPA':-4.0813,'GB':-4.0813, 'SB':-4.0813, 'RM':-4.0813,
                'MM':-4.0813, 'ACRU':-4.0813, 'GA': -4.0813, 'WA':-4.0813, 'BT':-4.0813, 'BTA':-4.0813, 'QA':-4.0813,'BP':-4.0813,
                'BE':-4.0813, 'AB':-4.0813,'RO':-4.0813,'WO':-4.0813,'CO':-4.0813,'BC':-4.0813,'BF':-2.9584, 'ABBA':-2.9584, 'RS':-2.9584,
                'PIRU':-2.9584,'WS':-2.9584,'BS':-2.9584,'WP':-2.9584, 'PIST':-2.9584, 'TA':-2.9584,'NS':-2.9584, 'JP':-2.9584,'PP':-2.9584,
                'NC':-2.9584, 'THOC':-2.9584,'WC':-2.9584,'NWC':-2.9584,'RP':-2.9584, 'EH':-2.9584, 'TSCA':-2.9584, 'HE':-2.9584, 
                'BW':-4.0813, 'HH':-4.0813, 'OH':-4.0813} 

JENKINS_FOLIAGE_RATIO_B2 ={'SM':5.8816,'YB':5.8816, 'PB':5.8816, 'BEAL':5.8816,'BEPA':5.8816,'GB':5.8816, 'SB':5.8816, 'RM':5.8816,
                'MM':5.8816, 'ACRU':5.8816, 'GA': 5.8816, 'WA':5.8816, 'BT':5.8816, 'BTA':5.8816, 'QA':5.8816,'BP':5.8816,
                'BE':5.8816, 'AB':5.8816,'RO':5.8816,'WO':5.8816,'CO':5.8816,'BC':5.8816,'BF':4.4766, 'ABBA':4.4766, 'RS':4.4766,
                'PIRU':4.4766,'WS':4.4766,'BS':4.4766,'WP':4.4766, 'PIST':4.4766, 'TA':4.4766,'NS':4.4766, 'JP':4.4766,'PP':4.4766,
                'NC':4.4766, 'THOC':4.4766,'WC':4.4766,'NWC':4.4766,'RP':4.4766, 'EH':4.4766, 'TSCA':4.4766, 'HE':4.4766, 
                'BW':5.8816, 'HH':5.8816, 'OH':5.8816} 

JENKINS_ROOT_RATIO_B1 ={'SM':-1.6911,'YB':-1.6911, 'PB':-1.6911, 'BEAL':-1.6911,'BEPA':-1.6911,'GB':-1.6911, 'SB':-1.6911, 'RM':-1.6911,
                'MM':-1.6911, 'ACRU':-1.6911, 'GA': -1.6911, 'WA':-1.6911, 'BT':-1.6911, 'BTA':-1.6911, 'QA':-1.6911,'BP':-1.6911,
                'BE':-1.6911, 'AB':-1.6911,'RO':-1.6911,'WO':-1.6911,'CO':-1.6911,'BC':-1.6911,'BF':-1.5619, 'ABBA':-1.5619, 'RS':-1.5619,
                'PIRU':-1.5619,'WS':-1.5619,'BS':-1.5619,'WP':-1.5619, 'PIST':-1.5619, 'TA':-1.5619,'NS':-1.5619, 'JP':-1.5619,'PP':-1.5619,
                'NC':-1.5619, 'THOC':-1.5619,'WC':-1.5619,'NWC':-1.5619,'RP':-1.5619, 'EH':-1.5619, 'TSCA':-1.5619, 'HE':-1.5619, 
                'BW':-1.6911, 'HH':-1.6911, 'OH':-1.6911} 

JENKINS_ROOT_RATIO_B2 ={'SM':0.816,'YB':0.816, 'PB':0.816, 'BEAL':0.816,'BEPA':0.816,'GB':0.816, 'SB':0.816, 'RM':0.816,
                'MM':0.816, 'ACRU':0.816, 'GA': 0.816, 'WA':0.816, 'BT':0.816, 'BTA':0.816, 'QA':0.816,'BP':0.816,
                'BE':0.816, 'AB':0.816,'RO':0.816,'WO':0.816,'CO':0.816,'BC':0.816,'BF':0.6614, 'ABBA':0.6614, 'RS':0.6614,
                'PIRU':0.6614,'WS':0.6614,'BS':0.6614,'WP':0.6614, 'PIST':0.6614, 'TA':0.6614,'NS':0.6614, 'JP':0.6614,'PP':0.6614,
                'NC':0.6614, 'THOC':0.6614,'WC':0.6614,'NWC':0.6614,'RP':0.6614, 'EH':0.6614, 'TSCA':0.6614, 'HE':0.6614, 
                'BW':0.816, 'HH':0.816, 'OH':0.816} 
                
###################################################################################
## FIA wood gravities, see REF_SPECIES, Miles and Smith 2009                     #
##################################################################################
wood_gravities={'SM':.56,'YB':.55, 'PB':.48, 'BEAL':.55,'BEPA':.48,'GB':.45, 'SB':.6, 'RM':.49,
                'MM':.44, 'ACRU':.49, 'GA': .53, 'WA':.55, 'BT':.36, 'BTA':.36, 'QA':.35,'BP':.31,
                'BE':.56, 'AB':.56,'RO':.56,'WO':.6,'CO':.57,'BC':.47,'BF':.33, 'ABBA':.33, 'RS':.37,
                'PIRU':.37,'WS':.37,'BS':.38,'WP':.34, 'PIST':.34, 'TA':.49,'NS':.36, 'JP':.4,'PP':.47,
                'NC':.29, 'THOC':.29,'WC':.29,'NWC':.29,'RP':.41, 'EH':.38, 'TSCA':.38, 'HE':.38, 
                'BW':.32, 'HH':.63, 'OH':.52}
                
bark_gravities={'SM':.54,'YB':.62, 'PB':.56, 'BEAL':.62,'BEPA':.56,'GB':.55, 'SB':.62, 'RM':.6,
                'MM':.5, 'ACRU':.6, 'GA': .48, 'WA':.5, 'BT':.59, 'BTA':.59, 'QA':.5,'BP':.5,
                'BE':.67, 'AB':.67,'RO':.68,'WO':.56,'CO':.54,'BC':.63,'BF':.4, 'ABBA':.4, 'RS':.32,
                'PIRU':.32,'WS':.39,'BS':.42,'WP':.47, 'PIST':.47, 'TA':.3,'NS':.44, 'JP':.41,'PP':.34,
                'NC':.42, 'THOC':.42,'WC':.42,'NWC':.42,'RP':.27, 'EH':.46, 'TSCA':.46, 'HE':.46, 
                'BW':.48, 'HH':.5, 'OH':.53}

bark_percents={'SM':.156,'YB':.098, 'PB':.126, 'BEAL':.098,'BEPA':.126,'GB':.126, 'SB':.098, 'RM':.086,
                'MM':.086, 'ACRU':.086, 'GA': .16, 'WA':.16, 'BT':.144, 'BTA':.144, 'QA':.144,'BP':.22,
                'BE':.06, 'AB':.06,'RO':.2,'WO':.16,'CO':.23,'BC':.092,'BF':.12, 'ABBA':.12, 'RS':.13,
                'PIRU':.13,'WS':.13,'BS':.13,'WP':.16, 'PIST':.16, 'TA':.14,'NS':.126, 'JP':.14,'PP':.134,
                'NC':.14, 'THOC':.14,'WC':.14,'NWC':.14,'RP':.16, 'EH':.17, 'TSCA':.17, 'HE':.17, 
                'BW':.105, 'HH':.15, 'OH':.152}

#Westfall is metric
###################################################################################
## Westfall & Scott 2010 Forest Science (56, 515-582)  FIA taper equations       #
##################################################################################
def WestfallScottn(SPP,h,H,dbh):
  if(SPP=='SM'):         #sugar maple
    th1  =  6.5790
    th2  =  0.0111
    a1    =  1.0682
    a2    =  1.1833
    gm1  =  0.1031
    gm2  =  0.2624
    phi  =  0.1516
    lmd  =  1.1482
    bet1  =  0.6637
    bet2  =  3.0996
  
  elif(SPP=='YB' or SPP=='PB' or SPP=='GB' or SPP=='SB' or SPP== 'BEAL ' or SPP== 'BEPA' ): #birches
    th1 =  7.5437
    th2 =  0.0103
    a1 =  0.9961
    a2  =  1.1042
    gm1  =  0.1313
    gm2  =  0.3539
    phi  =  0.2091
    lmd  =  0.9478
    bet1  =  0.5995
    bet2  =  3.4205
  
  elif(SPP=='RM' or SPP=='ACRU'): #red maple
    th1  =  7.5707
    th2  =  0.0105
    a1    =  1.5273
    a2    =  0.7684
    gm1  =  0.0931
    gm2  =  0.4223
    phi  =  0.1441
    lmd  =  1.3910
    bet1  =  0.6453
    bet2  =  4.0737
  
  elif(SPP=='GA' or SPP=='WA' or SPP=='BT' or SPP=='QA' or SPP=='BP' or SPP== 'BTA '): #ash, quaking aspen, balsam poplar
    th1  =  3.3085
    th2  =  0.0276
    a1    =  1.2634
    a2    =  0.9088
    gm1   =  0.1098
    gm2  =  0.5198
    phi  =  0.1840
    lmd  =  1.7842
    bet1  =  0.6719
    bet2  =  5.1178
  
  elif(SPP=='AB' or SPP=='BE'): #American beech
    th1  =  8.9843
    th2  =  0.0107
    a1    =  0.7621
    a2    =  1.3734
    gm1  =  0.0956
    gm2  =  0.1650
    phi  =  0.1924
    lmd  =  1.2237
    bet1  =  0.4626
    bet2  =  1.0954
  
  elif(SPP=='RO' or SPP=='WO' or SPP=='CO'): #red and white and chestnut oak
    th1  =  12.8336
    th2  =  0.0125
    a1    =  0.9038
    a2    =  1.0950
    gm1  =  0.0935
    gm2  =  0.3971
    phi  =  0.2038
    lmd  =  1.0457
    bet1  =  0.5508
    bet2  =  3.4681
  
  elif(SPP=='BC'):           #black cherry
    th1  =  3.2042
    th2  =  0.0479
    a1    =  1.2507
    a2    =  0.8075
    gm1  =  0.0800
    gm2  =  0.4170
    phi  =  0.2227
    lmd  =  2.7226
    bet1  =  0.7065
    bet2  =  4.6476
  
  elif(SPP=='BF' or SPP=='ABBA'):                        #balsam fir
    th1  =  5.3693
    th2  =  0.0171
    a1    =  1.4212
    a2    =  0.3003
    gm1  =  0.0890
    gm2  =  0.6485
    phi  =  0.1916
    lmd  =  1.8873
    bet1  =  0.4764
    bet2  =  2.6383
  
  elif(SPP=='RS' or SPP=='BS' or SPP=='WS' or SPP== 'PIRU'):           #spruces
    th1  =  6.8745
    th2  =  0.0110
    a1    =  1.1241
    a2    =  0.4107
    gm1  =  0.1376
    gm2  =  0.4842
    phi  =  0.2038
    lmd  =  1.2598
    bet1  =  0.4986
    bet2  =  2.7865
  
  elif(SPP=='WP'or SPP== 'PIST'): #white pine
    th1  =  7.1438
    th2  =  0.0123
    a1    =  0.8978
    a2    =  0.7872
    gm1  =  0.0989
    gm2  =  0.4985
    phi  =  0.2049
    lmd  =  0.9247
    bet1  =  0.5715
    bet2  =  2.0482
  
  elif(SPP=='TA' or SPP=='NS' or SPP=='JP'): #larch, Norway spruce, jack pine
    th1  =  5.2913
    th2  =  0.0411
    a1    =  1.1291
    a2    =  0.6831
    gm1  =  0.0745
    gm2  =  0.5798
    phi  =  0.1896
    lmd  =  1.5776
    bet1  =  0.6616
    bet2  =  6.0645
  
  elif(SPP== 'NC' or SPP== 'THOC 'or SPP== 'WC' or SPP== 'NWC'): #northern white cedar
    th1  =  5.400
    th2  =  0.0256
    a1    =  1.9295
    a2    =  0.8142
    gm1  =  0.0943
    gm2  =  0.9642
    phi  =  0.2761
    lmd  =  1.8605
    bet1  =  1.3432
    bet2  =  1.3438
  
  elif(SPP=='RP'): #red pine
    th1  =  7.6044
    th2  =  0.0148
    a1    =  1.2379
    a2    =  0.3304
    gm1  =  0.0759
    gm2  =  0.6611
    phi  =  0.3008
    lmd  =  1.1569
    bet1  =  0.5462
    bet2  =  3.0627
  
  elif(SPP=='EH' or SPP=='TSCA' or SPP=='HE'): #eastern hemlock
    th1  =  7.2442
    th2  =  0.0152
    a1    =  1.4008
    a2    =  0.8306
    gm1  =  0.0856
    gm2  =  0.4724
    phi  =  0.2011
    lmd  =  1.5776
    bet1  =  0.6616
    bet2  =  6.0645
  
  elif(SPP=='OH'or SPP=='BW' or SPP=='MM' or SPP=='HH'):
    th1  =  9.0505
    th2  =  0.0241
    a1   =  1.298
    a2    =  0.7684
    gm1  =  0.0684
    gm2  =  0.4555
    phi  =  0.1769
    lmd  =  1.6684
    bet1  =  0.5408
    bet2  =  4.1821
  elif(SPP=='OS' or SPP== 'PP' or SPP=='JP'): #composite of all conifers
    th1  =  6.418214286
    th2  =  0.019585714
    a1    =  1.305771429
    a2    =  0.593785714
    gm1  =  0.093685714
    gm2  =  0.615528571
    phi  =  0.223985714
    lmd  =  1.462628571
    bet1  =  0.685271429
    bet2  =  2.842342857
  else : #composite of all species
    th1  =  7.114957895
    th2  =  0.016836842
    a1    =  1.148384211
    a2    =  0.857194737
    gm1  =  0.101226316
    gm2  =  0.460905263
    phi  =  0.195610526
    lmd  =  1.351415789
    bet1  =  0.634036842
    bet2  =  3.302584211
  x=dbh/H
  z=h/H
  S1=th1/(1+(z/th2)**lmd)
  S2=(z/bet1)**(bet2*x)/(1+(z/bet1)**(bet2*x))
  d=math.sqrt(dbh**2*(1.37/H/gm1)**phi*((1-z)/(1-gm1))**(a1+S1)*((1-z)/(1-gm2))**(a2*S2))
  return d

#Scott's imperial (/sigh)
###################################################################################
## Scott's 1982 FIA volume equations                                             #
##################################################################################
def scottseq(SP,dbh,bowl_ht):
    #white and red pine
    if SP== 'WP' or SP== 'RP' or SP== 'PIST':
        b0=0.11
        b1=-.05977
        b2=2.0498
        b3=0.04965
        b4=2.0198
        b5=0.3468
    #all the spruces.. which is stupid
    elif SP== 'RS' or SP== 'BS' or SP== 'WS' or SP== 'PR' or SP== 'PIRU':
        b0=0.17
        b1=-.06315
        b2=2.0654
        b3=0.05122
        b4=2.0264
        b5=0.3508
    #balsalm fir
    elif SP== 'BF' or SP== 'ABBA':
        b0=-.1
        b1=-.05444
        b2=2.1194
        b3=0.04821
        b4=2.0427
        b5=0.3579
    #Hemlock
    elif SP== 'EH' or SP== 'TSCA' or SP== 'HE':
        b0=0.24
        b1=-.05895
        b2=2.0362
        b3=0.04947
        b4=2.00172
        b5=0.3366
    #Basically other conifers
    elif SP== 'TA' or SP== 'PP' or SP== 'NS' or SP== 'JP':
        b0=-0.03
        b1=-.05604
        b2=2.0473
        b3=0.05022
        b4=2.0198
        b5=0.3242
    #Cedar
    elif SP== 'NC' or SP== 'THOC 'or SP== 'WC' or SP== 'NWC':
        b0=.19
        b1=-.05904
        b2=1.9935
        b3=0.04981
        b4=2.0027
        b5=0.3214 
    #sugar maple
    elif SP== 'SM':
        b0=-.19
        b1=-.01171
        b2=1.8949
        b3=0.01340
        b4=1.9928
        b5=0.6471
    #other maple/tulip poplar
    elif SP== 'RM' or SP== 'ACRU ' or SP== 'MM ':
        b0=-.45
        b1=-.00523
        b2=2.2323
        b3=0.01338
        b4=2.0093
        b5=0.6384  
    #all ash and aspen.. its not me, its the equations!
    elif SP== 'WA' or SP== 'BA ' or SP== 'BT ' or SP== 'QA 'or SP== 'BTA ':
        b0=0.06
        b1=-.02437
        b2=1.5419
        b3=0.01299
        b4=1.9885
        b5=0.6453     
    #black cherry
    elif SP== 'BC':
        b0=-0.04
        b1=-.01783
        b2=1.8109
        b3=0.01358
        b4=1.9905
        b5=0.6553  
    #All birch
    elif SP== 'YB' or SP== 'BEAL ' or SP== 'BEPA' or SP== 'PB' or SP== 'GB':
        b0=-0.27
        b1=-.00675
        b2=1.9728
        b3=0.01327
        b4=1.9967
        b5=0.6407  
    #Beech
    elif SP== 'BE' or SP== 'AB':
        b0=-0.6
        b1=-.00711
        b2=2.2693
        b3=0.01399
        b4=2.019
        b5=0.6518  
    #Basswood  
    elif SP== 'BW':
        b0=-0.6
        b1=-.00711
        b2=2.2693
        b3=0.01399
        b4=2.019
        b5=0.6518  
    #Oaks and gums 
    elif SP== 'RO' or SP== 'WO':
        b0=-0.13
        b1=-.00536
        b2=1.9172
        b3=0.01131
        b4=1.9975
        b5=0.6549 
    #Chestnut oak 
    elif SP== 'CO':
        b0=-.26
        b1=.00038
        b2=2
        b3=0.01068
        b4=1.998
        b5=0.6438
    #Other hardwoods
    elif SP== 'OH':
        b0=.13
        b1=-.00183
        b2=2.36
        b3=0.00944
        b4=2.0608
        b5=0.6516
    
    return b0+b1*(dbh**b2)+b3*(dbh**b4)*(bowl_ht**b5)

#Everything is imperial units
def biomasser(SP,HT,DBH,rot=0):
    #The species included are as follows, all others will be 'Other Hardwoods'
    #Sugar Maple, Yellow Birch, Grey Birch, Paper Birch, Sweet Birch, Red Maple, Striped Maple,
    #Green Ash, White Ash, Bigtooth Aspen, Quaking Aspen, Balsam Poplar, Beech, Red Oak, White Oak,
    #Chestnut Oak, Black Cherry, Balsam Fir, Red Spruce, White Spruce, Black SPruce, White Pine
    #Tamarack, Norway Spruce, Jack Pine, Pitch Pine, Northern White Cedar, Red Pine, Eastern Hemlock,
    #BassWood, Hophorn Beem
    species_list=['SM','YB', 'PB', 'BEAL','BEPA','GB', 'SB', 'RM','MM', 'ACRU', 'GA', 'WA', 'BT', 'BTA', 'QA','BP',
        'BE', 'AB','RO','WO','CO','BC','BF', 'ABBA', 'RS',
        'PIRU','WS','BS','WP', 'PIST', 'TA','NS', 'JP','PP',
        'NC', 'THOC','WC','NWC','RP', 'EH', 'TSCA', 'HE', 
        'BW', 'HH', 'OH']
    
    ######STEP 1, get bole height (from DBH and HT) using taper equations
    diam=WestfallScottn(SP,HT,HT,DBH)
    BoleHT=HT
    while diam<10.16:
        BoleHT=BoleHT-BoleHT/500
        diam=WestfallScottn(SP,BoleHT,HT,DBH)
        #if the tree is never more than 4 inches wide, you shouldn't be using these equations
        #but lets assume its bole height is at breast height then.
        if BoleHT == 0:
            diam=10.16
            BoleHT=1.37
    #Scott assumes ft and 1ft stump
    BoleHT=BoleHT*3.28084-1
        
    #######STEP 2, get stem volume from archaic volume equations
    VOLCFGRS=scottseq(SP,DBH/2.54,BoleHT)
        
    #######STEP 3, if availible, take into account percent rot
    VOLCFSND=VOLCFGRS*(1-rot/100)
        
    #######STEP 4, Calculate biomass of bole (vol*water weight*specific grav + barkstuff)
    if SP not in species_list :
        SP='OH'
    woodMass=VOLCFSND*62.4*wood_gravities[SP]
    barkMass=VOLCFSND*62.4*bark_gravities[SP]*bark_percents[SP]
    BoleMass=woodMass+barkMass
    
    #######STEP 5, Calculate the Jenkins total biomass and the adjustment factor
    stem_ratio=np.exp(JENKINS_STEM_WOOD_RATIO_B1[SP]+JENKINS_STEM_WOOD_RATIO_B2[SP]/(DBH))
    bark_ratio=np.exp(JENKINS_STEM_BARK_RATIO_B1[SP]+JENKINS_STEM_BARK_RATIO_B2[SP]/(DBH))
    
    Jenkins_Tot=np.exp(JENKINS_TOTAL_B1[SP]+JENKINS_TOTAL_B2[SP]*np.log(DBH))*2.2046
    Jenkins_wood=stem_ratio*Jenkins_Tot
    Jenkins_bark=bark_ratio*Jenkins_Tot
    Jenkins_BoleMass=Jenkins_bark+Jenkins_wood
                       
    AdjFac=BoleMass/Jenkins_BoleMass
    
    #######STEP 6, leaf and root biomass
    foliage_ratio=np.exp(JENKINS_FOLIAGE_RATIO_B1[SP]+JENKINS_FOLIAGE_RATIO_B2[SP]/(DBH))
    root_ratio=np.exp(JENKINS_ROOT_RATIO_B1[SP]+JENKINS_ROOT_RATIO_B2[SP]/(DBH))
    
    Jenkins_Foliage=foliage_ratio*Jenkins_Tot
    
    Jenkins_roots=Jenkins_Tot*root_ratio
    
    #######STEP 7, Stump biomass
    VDIB=0.005454153*((DBH/2.54)**2)*((Stump_coefs[SP][1]**2)+(5.62462*Stump_coefs[SP][1]*Stump_coefs[SP][2])+(8.50038*(Stump_coefs[SP][2]**2)))
    VDOB=0.005454153*((DBH/2.54)**2)*((1+(5.62462*Stump_coefs[SP][0])+(8.50038*(Stump_coefs[SP][0]**2))))
    
    stump_wood_mass=VDIB*62.4*wood_gravities[SP]
    stump_bark_mass=(VDOB-VDIB)*62.4*bark_gravities[SP]
    stump_biomass=(stump_wood_mass+stump_bark_mass)
    
    #######STEP 8, Top and branch biomass
    Jenkins_Top=Jenkins_Tot-Jenkins_BoleMass-Jenkins_Foliage-stump_biomass
    
    #######STEP 9, Combine them, convert to kg
    AG_Biomass=(Jenkins_Top*AdjFac+stump_biomass*AdjFac+BoleMass)*0.453592
    BG_Biomass=(Jenkins_roots*AdjFac)*0.453592
    
    Total_Biomass = AG_Biomass + BG_Biomass
    return AG_Biomass, Total_Biomass
    

#test tree
#Requires metric measurements, returns kg
SP='PB'
HT=42*.3048
DBH=5.7*2.54
rot=0

AG_Biomass, Total_Biomass=biomasser(SP,HT,DBH,rot=0)
print AG_Biomass