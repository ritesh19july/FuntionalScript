import time
def addTestCaseData(dummyFilePath,totalTestCase,totalReportData,htmlfolderPath):
	text=""
	global testcaseNO
	with open(dummyFilePath) as ins:   
		for line in ins:
			text=text+line+"\n"
	now = time.strftime("%c")	
	animatedcollapse=""
	for i in range(1, totalTestCase+3) :
		animatedcollapse+="animatedcollapse.addDiv('"+str(i)+"', 'fade=1')\n"		
	text=text.replace("#@ExecutionDate@#",now)	
	text=text.replace("#@animatedcollapseDiv@#",animatedcollapse)	  
	replaceData=text.replace("@#generateREPORT#@",totalReportData)		
	target1 = open(htmlfolderPath+"/WWE_Result.html", 'w')
	target1.truncate()
	target1.write(replaceData)	
	target1.close()	
    
	
	
def testcaseMethod(testcaseNO,testCaseName,status):
	if(status==False):
		color="#FA5858";		
	else:
	   color="#D0F5A9";
	TestCaseReportVar="<table width=100% border=1 cellspacing=2 cellpadding=3 bgcolor=\"#C7D7DE\">\n"
	TestCaseReportVar+="<tbody>\n"
	TestCaseReportVar+="<tr>\n"
	TestCaseReportVar+="<td width=\"12%\">\n"
	TestCaseReportVar+="<a style=\"text-decoration:underline; color:#000BBF;\" href=\"javascript:animatedcollapse.toggle('"+str(testcaseNO)+"')\">\n"
	TestCaseReportVar+="<strong>"+str(testcaseNO)+"</strong>\n"
	TestCaseReportVar+="</a>\n"
	TestCaseReportVar+="</td>\n"
	TestCaseReportVar+="<td width=\"25%\">"+testCaseName+"</td>\n"
	TestCaseReportVar+="<td width=\"15%\">"+" "+"</td>\n"
	TestCaseReportVar+="<td width=\"35%\">"+" "+"</td>\n"
	TestCaseReportVar+="<td width=\"15%\" bgcolor=\""+color+"\">"+str(status)+"</td>\n"
	TestCaseReportVar+="</tr>\n"
	TestCaseReportVar+="</tbody>\n"
	TestCaseReportVar+="</table>\n"
	TestCaseReportVar+="<div id=\""+str(testcaseNO)+"\" class=\"table_con\"  style=\"display: none;\" fade=\"1\">\n"
	TestCaseReportVar+="<table style=\"margin-left:20px;\" width=\"97%\" cellspacing=\"0\" cellpadding=\"3\" border=\"1\" bgcolor=\"#AF5B1F\" >\n"
	TestCaseReportVar+="<tbody><tr>\n"
	TestCaseReportVar+="<td width=05% style=\"color:#FFFFFF;\">Step#</td>\n"
	TestCaseReportVar+="<td width=10% style=\"color:#FFFFFF;\">DeviceName</td>\n"
	TestCaseReportVar+="<td width=25% style=\"color:#FFFFFF;\">OrginalSrc</td>\n"
	TestCaseReportVar+="<td width=25% style=\"color:#FFFFFF;\">SecondSrc</td>\n"
	TestCaseReportVar+="<td width=25% style=\"color:#FFFFFF;\">CaptureImage</td>\n"
	TestCaseReportVar+="<td width=10% style=\"color:#FFFFFF;\">Status</td></tr>\n"
	return TestCaseReportVar


def keywordReportMethod(result,kewordNO,orgSrc,SecondSrc,imagePath,DeviceName):
        print result
	if(result==False):
		color="#FA5858";
	else:
                color="#D0F5A9"
	keywordReportVarLo="<tr bgcolor=\"#E4D4C8\" border=\"1\">\n"
	keywordReportVarLo+="<td width=05%>"+str(kewordNO)+"</td>\n"
	keywordReportVarLo+="<td width=10%>"+DeviceName+"</td>\n"
	keywordReportVarLo+="<td width=25%>"+orgSrc+"</td>\n"
	keywordReportVarLo+="<td width=25%>"+SecondSrc+"</a></td>\n"
	keywordReportVarLo+="<td width=25%><a href=\"file:./"+imagePath+"\" target='_blank'><img IMG HEIGHT=150 WIDTH=150 src=\"file:./"+imagePath+"\" alt='Click'></img></a></td>\n"
	keywordReportVarLo+="<td width=10% bgcolor=\""+color+"\">"+str(result)+"</td>\n"
	keywordReportVarLo+="</tr>\n"
	#keywordReportVar=keywordReportVarLo
	return keywordReportVarLo;



def CaptureSnapshot(driver,strSnapshot):
	print driver
	print "C:\\wwe\\wsx\\"+strSnapshot
	driver.save_screenshot("C:\\wwe\\wsx\\"+strSnapshot)
	return "/wsx/"+strSnapshot


def ValidateTheSearchInDiffTabs(driver):

	Arr = []
	FetchedText =  driver.find_element_by_xpath("//div[@id='wwe_search_gsa_results1']/div[5]/div/div[2]/a").text
	FetchedText2 = driver.find_element_by_xpath("//div[@id='wwe_search_gsa_results1']/div[5]/div[2]/div[2]/a").text
	#	FetchedText3 = driver.find_element_by_xpath("//*[@id='wwe_search_gsa_results1']/div[5]/div[3]/div[2]/a").text
	#	FetchedText4 = driver.find_element_by_xpath("//*[@id='wwe_search_gsa_results1']/div[5]/div[4]/div[2]/a").text
	Arr.append(FetchedText)
	Arr.append(FetchedText2)
	return Arr
	