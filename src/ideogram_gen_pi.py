# Code written on 10-Aug-2020. This code generates the files
# required to generate the circos plot for the digits of pi

# There are no input files
# Output files are stored in the directory karyotype

# function call
# python ideogram_gen_pi.py

# Author: SMU Abdullah
# Email: umer_973@hotmail.com

import time
import os

start_time=time.time()

mainoutdir='karyotype'
if(not os.path.isdir(mainoutdir)):    #check if output directory exists
    os.mkdir(mainoutdir)              #create output directory

pivec='31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989'
color=["117,107,177",
    "197,27,138",
    "67,162,202",
    "49,163,84",
    "255,247,188",
    "217,95,14",
    "240,59,32",
    "173,221,142",
    "158,188,218",
    "158,202,225"]

numdigits=200 # number of digits to use
numrows=4 # number of rows in the plot
digitsperfile=numdigits/numrows

foutfile=open(mainoutdir+'/pi.txt','w')
for coliter in range(0,digitsperfile):
    colval=pivec[coliter]
    colorval=color[int(colval)]
    wrtstr='chr - '+str(coliter+1)+' '+colval+' '+str(coliter)+' '+str(coliter+1)+' '+colorval
    foutfile.write(wrtstr)
    foutfile.write('\n')
        
for fileiter in range(1,numrows):
    foutfile=open(mainoutdir+'/pi_'+str(fileiter)+'.txt','w')
    for coliter in range(digitsperfile*fileiter,digitsperfile*fileiter+digitsperfile):
        colval=pivec[coliter]
        colorval=color[int(colval)]
        wrtstr=str(coliter-digitsperfile*fileiter+1)+' '+str(coliter-digitsperfile*fileiter+1)+' '+str(coliter-digitsperfile*fileiter)+' '+colval+' fill_color='+colorval
        foutfile.write(wrtstr)
        foutfile.write('\n')
    foutfile.close()
print("--- %s seconds ---" % (time.time() - start_time))
