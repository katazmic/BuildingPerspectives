import os
import datetime
import urllib
import time
import xlrd
import xlwt

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from cStringIO import StringIO

#----------GLOBAL SETTINGS------------#

# USE FORWARD SLASHES IN DIRECTORIES ONLY

os.path.abspath("mydir/myfile.txt")

readPath = os.path.abspath("mydir/myfile.txt")


#----------LAUNCH DRIVER--------------#
driver = webdriver.Firefox()

#----------DEFINITIONS----------------#

def startFirefox():
	return webdriver.Firefox()
	
def getPortalInfo (row_index, boroughInput, blockInput, lotInput, try_num, num_rows):
	return



#----------ACTIONS----------------#

