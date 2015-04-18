from splinter import Browser
import time
from datetime import datetime

browser = Browser('chrome')
browser.visit('https://egov.uscis.gov/cris/Dashboard/CaseStatus.do')
receipt_search = '000'
total_num = 0
while True:
    input = browser.find_by_id('receipt')
    button = browser.find_by_id('dashboardForm').find_by_name('submit')
    receipt_pre = 'EAC1490146'
    input.first.fill(receipt_pre + receipt_search)
    button.first.click()
    status = browser.find_by_id('caseStatus').find_by_xpath('//div/div/h4')
    details = browser.find_by_id('caseStatus').find_by_xpath('//div/div/p')
    target = False
    index_end = 3
    date = ""
    for detail in details:
        if 'we received this I765 APPLICATION FOR EMPLOYMENT AUTHORIZATION' in detail.value:
            target = True
            index_end = detail.value.index('we received this I765 APPLICATION FOR EMPLOYMENT AUTHORIZATION')
            date = detail.value[3:index_end-2]
            break
    #time.sleep(60)
    if target and 'Initial Review' in status[0].value:
        print receipt_pre+str(receipt_search)+"    "+date
	total_num = total_num + 1
    receipt_search = str(int(receipt_search) + 1).zfill(3)
    if int(receipt_search) >= 999:
        break
    browser.back()
print 'done'
print str(total_num)
