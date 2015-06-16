import sys
import time

htmlfolderPath=sys.argv[1]
xmlPath=sys.argv[2]
DummyReportPath=sys.argv[3]
capturefolderPath=sys.argv[4]
repofolderPath=sys.argv[5]
difffolderPath=sys.argv[6]
i=0
TestCaseReportVar=""
keywordReportVar=""
mainGlobalArray=""
def addTestCaseData():
	text=""
	global testcaseNO
	with open("C:\\wwe\\dummy.txt") as ins:   
		for line in ins:
			text=text+line+"\n"
	now = time.strftime("%c")	
	animatedcollapse=""
	for i in range(1, testcaseNO+3) :
		animatedcollapse+="animatedcollapse.addDiv('"+str(i)+"', 'fade=1')\n"		
	text=text.replace("#@ExecutionDate@#",now)	
	print animatedcollapse
	text=text.replace("#@animatedcollapseDiv@#",animatedcollapse)	  
	replaceData=text.replace("@#generateREPORT#@",mainGlobalArray)		
	target1 = open(htmlfolderPath+"/WWEhtmlFile.html", 'w')
	target1.truncate()
	target1.write(replaceData)	
	target1.close()	
    
	
	
def testcaseMethod():
	#if(status==false)
	#	color="#FA5858";		
	#else
	color="#D0F5A9";
	global mainDataArray
	global TestCaseReportVar
	global testcaseNO
	localmindataArray =mainDataArray
	localTestCaseReportVar=""
	TestCaseReportVar="<table width=100% border=1 cellspacing=2 cellpadding=3 bgcolor=\"#C7D7DE\">\n"
	TestCaseReportVar+="<tbody>\n"
	TestCaseReportVar+="<tr>\n"
	TestCaseReportVar+="<td width=\"12%\">\n"
	TestCaseReportVar+="<a style=\"text-decoration:underline; color:#000BBF;\" href=\"javascript:animatedcollapse.toggle('"+str(testcaseNO)+"')\">\n"
	TestCaseReportVar+="<strong>"+str(testcaseNO)+"</strong>\n"
	TestCaseReportVar+="</a>\n"
	TestCaseReportVar+="</td>\n"
	TestCaseReportVar+="<td width=\"25%\">"+localmindataArray[2]+"</td>\n"
	TestCaseReportVar+="<td width=\"15%\">"+" "+"</td>\n"
	TestCaseReportVar+="<td width=\"35%\">"+" "+"</td>\n"
	TestCaseReportVar+="<td width=\"15%\" bgcolor=\""+color+"\">"+" "+"</td>\n"
	TestCaseReportVar+="</tr>\n"
	TestCaseReportVar+="</tbody>\n"
	TestCaseReportVar+="</table>\n"
	TestCaseReportVar+="<div id=\""+str(testcaseNO)+"\" class=\"table_con\"  style=\"display: none;\" fade=\"1\">\n"
	TestCaseReportVar+="<table style=\"margin-left:20px;\" width=\"97%\" cellspacing=\"0\" cellpadding=\"3\" border=\"1\" bgcolor=\"#AF5B1F\" >\n"
	TestCaseReportVar+="<tbody><tr>\n"
	TestCaseReportVar+="<td width=05% style=\"color:#FFFFFF;\">Step#</td>\n"
	TestCaseReportVar+="<td width=10% style=\"color:#FFFFFF;\">DeviceName</td>\n"
	TestCaseReportVar+="<td width=25% style=\"color:#FFFFFF;\">RunTimeImage</td>\n"
	TestCaseReportVar+="<td width=25% style=\"color:#FFFFFF;\">baseLineImage  </td>\n"
	TestCaseReportVar+="<td width=25% style=\"color:#FFFFFF;\">CompareImage</td>\n"
	TestCaseReportVar+="<td width=10% style=\"color:#FFFFFF;\">Status</td></tr>\n"
	TestCaseReportVar=TestCaseReportVar


def keywordReportMethod():
	global keywordReportVar
	global deviceNO
	global mainDataArray
	color="#D0F5A9";
	# if(result==false)
		# color="#FA5858";
	# else if(result==true)
		# color="#D0F5A9";
	# else
		# color="#D0F5B8";
	global capturefolderPath	
	global repofolderPath
	global difffolderPath
	mainimage=mainDataArray[1]
	mainimage=mainimage.strip()
	mainimageSp=mainimage.split(".")
	repoImage=mainimageSp[0]+"-repo.png"
	compImage=mainimageSp[0]+"-diff.png"
	mainimage=capturefolderPath+"/"+mainimage	
	repoImage=repofolderPath+"/"+repoImage
	compImage=difffolderPath+"/"+compImage
	keywordReportVarLo="<tr bgcolor=\"#E4D4C8\" border=\"1\">\n"
	keywordReportVarLo+=	"<td width=05%>"+str(deviceNO)+"</td>\n"
	keywordReportVarLo+=	"<td width=10%>"+mainDataArray[3]+"</td>\n"
	keywordReportVarLo+=	"<td width=25%><a href=\"file:./"+mainimage+"\" target='_blank'><img IMG HEIGHT=150 WIDTH=150 src=\"file:./"+mainimage+"\" alt='Click'></img></a></td>\n"
	keywordReportVarLo+=	"<td width=25%><a href=\"file:./"+repoImage+"\" target='_blank'><img IMG HEIGHT=150 WIDTH=150 src=\"file:./"+repoImage+"\" alt='Click'></img></a></td>\n"
	keywordReportVarLo+=	"<td width=25%><a href=\"file:./"+compImage+"\" target='_blank'><img IMG HEIGHT=150 WIDTH=150 src=\"file:./"+compImage+"\" alt='Click'></img></a></td>\n"
	keywordReportVarLo+=	"<td width=10% bgcolor=\""+color+"\">"+"false"+"</td>\n"
#	keywordReportVarLo+=	"<td width=10%><a href=\"file:./"+mainDataArray[0]+"\" target='_blank'><img IMG HEIGHT=150 WIDTH=150 src=\"file:./"+mainDataArray[0]+"\" alt='Click'></img></a></td>\n"

	keywordReportVarLo+="</tr>\n"
	keywordReportVar=keywordReportVarLo
	return keywordReportVar;


# main Script
#target = open(folderPath+"/htmlFile.txt", 'w')
#target.truncate()
text=""
with open(xmlPath) as ins:   
    for line in ins:
	   text=text+line+"\n"
previousTestCase=""
newTestCase=""

testcaseNO=0
deviceNO=0
for fail in text.split("<failure"):
	if "</failure" not in fail: continue
	data=fail.split("failure>")
	newdata=data[0].split("))")
	if  data[0]=="": 
		print "inside\n"
		continue
	
     
	arrayData=newdata[0].split("array(")
	replaceData=arrayData[1].replace("'","")
	mainDataArray=replaceData.split(",")
	
	if previousTestCase==mainDataArray[2] : 	        
			deviceNO=deviceNO+1
			keywordReportMethod()
			mainGlobalArray+=keywordReportVar
	#		target.write(keywordReportVar)
	else:
		testcaseNO=testcaseNO+1
		deviceNO=1
		if previousTestCase !="" :		    
			mainGlobalArray+="</tbody></table></div>"
	#		target.write("</tbody></table></div>")
		testcaseMethod()
		mainGlobalArray+=TestCaseReportVar
	#	target.write(TestCaseReportVar)
		keywordReportMethod()
		mainGlobalArray+=keywordReportVar
	#	target.write(keywordReportVar)	
		previousTestCase=mainDataArray[2]

mainGlobalArray+="</tbody></table></div>"
#target.write("</tbody></table></div>")		
addTestCaseData()
#target.close()	
