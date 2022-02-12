import requests
from lxml import etree
import re
import time


def icp(domain,line):
	try:
		url="http://icp.chinaz.com/"+domain
		res = requests.get(url=url)
		tree = etree.HTML(res.content.decode('utf-8'))
		icp_name = tree.xpath('//a/text()')[368]
		icp_type = tree.xpath('//strong/text()')[0]
		print(icp_name+"    "+icp_type+"      "+line)
		f = open('result.txt','a+')
		f.write(icp_name+"    "+icp_type+"      "+line+"\n")
		f.close()
		time.sleep(2)
	except:
		pass
	
if __name__ == "__main__":
	for line in open('domain.txt'):
		domain=re.findall('[^/"><\.]{1,}\.com|[^/"><\.]{1,}\.cn|[^/"><\.]{1,}\.net\.cn\.top', line)
		if domain:
			icp(domain[0],line.replace('\n',''))
        	
