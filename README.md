# Component-Ratio-Method (CRM)
An implementation of the USFS's FIA component ratio method for estimating biomass of a tree

The component ratio method is how the US Forest Service's Forest Inventory and Analysis program estimates how much biomass is in a given tree. Ultimately its used for US's carbon monitoring.

The CRM is a hot mess. It uses local equations to correct biases in national equations for different parts of the tree, then combines them. A thorough walkthrough can be found here:

https://www.nrs.fs.fed.us/pubs/gtr/gtr_nrs88.pdf

Equations from the North East are used to make biomass estimates of the following species: 

#The species included are as follows, all others will be 'Other Hardwoods'
Sugar Maple(SM), Yellow Birch(YB), Grey Birch(GB), Paper Birch(PB), Sweet Birch(SB), Red Maple(RM), Striped Maple(MM),
Green Ash(GA), White Ash(WA), Bigtooth Aspen(BT), Quaking Aspen(QA), Balsam Poplar(BP), Beech(BE, BA), Red Oak(RO), White Oak (WO),
Chestnut Oak(CO), Black Cherry(BC), Balsam Fir(BF), Red Spruce(RS), White Spruce(WS), Black Spruce(BS), White Pine(WP)
Tamarack(TA), Norway Spruce(NS), Jack Pine(JP), Pitch Pine(PP), Northern White Cedar(NC), Red Pine(RP), Eastern Hemlock(EH),
BassWood(BW), Hophorn Beem(HH)

Run everything, then use the 'biomasser' function to get biomass using Species, DBH(cm), and HT(m).
