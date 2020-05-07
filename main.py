
from flask import Flask
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import csv
import json
import datetime


app = Flask(__name__)

@app.route("/")
def rehtml():
	"""
	#最後に必ずdriver.quit()を入れること！
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	driver = webdriver.Chrome(options=options)

	text = driver.implicitly_wait(30)

	driver.get('http://jra.jp/keiba/')
	WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located)
	html = driver.page_source.encode('utf-8')
	soup = BeautifulSoup(html, "lxml", from_encoding="utf-8")

	ozzu_js = soup.find(text="オッズ").parent.parent.get("onclick")

	
	driver.execute_script(ozzu_js)

	WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located)
	html2 = driver.page_source.encode('utf-8')
	soup2 = BeautifulSoup(html2, "lxml", from_encoding="utf-8")
	race_links = []
	link_list_ul = soup2.find_all("ul", class_="link_list")
	for ul in link_list_ul:
		print(ul.parent.parent.find("h3").text)
		lis = ul.find_all("li")
		for li in lis:
			race_links.append(li.find("a").get("onclick"))
			print("\t"+li.find("a").text)

	count = 0
	tanpuku_js_list = []
	umaren_js_list = []
	wide_js_list = []
	umatan_js_list = []
	sanpuku_js_list = []
	santan_js_list = []
	for race_link in race_links:
		driver.execute_script(race_link)

		WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located)
		html3 = driver.page_source.encode('utf-8')
		soup3 = BeautifulSoup(html3, "lxml", from_encoding="utf-8")
		btn_lists = soup3.find_all("ul", class_="btn_list")
		
		for btn_list in btn_lists:
			tanpuku_js_list.append([])
			umaren_js_list.append([])
			wide_js_list.append([])
			umatan_js_list.append([])
			sanpuku_js_list.append([])
			santan_js_list.append([])
			tanpuku_url = btn_list.find("li", class_="tanpuku").find("a").get("onclick")
			umaren_url = btn_list.find("li", class_="umaren").find("a").get("onclick")
			wide_url = btn_list.find("li", class_="umaren").find("a").get("onclick")
			umatan_url = btn_list.find("li", class_="umaren").find("a").get("onclick")
			sanpuku_url = btn_list.find("li", class_="umaren").find("a").get("onclick")
			santan_url = btn_list.find("li", class_="umaren").find("a").get("onclick")
			tanpuku_js_list[count].append(tanpuku_url)
			umaren_js_list[count].append(umaren_url)
			wide_js_list[count].append(wide_url)
			umatan_js_list[count].append(umatan_url)
			sanpuku_js_list[count].append(sanpuku_url)
			santan_js_list[count].append(santan_url)
			#print(btn_list.find("li", class_="umaren").find("a").text)

		count += 1
	"""
	dt_now = datetime.datetime.now()
	year = dt_now.year
	month = dt_now.month
	day = dt_now.day
	hour = dt_now.hour
	minute = dt_now.minute
	second = dt_now.second

	year = str(dt_now.year)
	month = str(dt_now.month)
	day = str(dt_now.day)
	hour = str(dt_now.hour)
	minute = str(dt_now.minute)
	second = str(dt_now.second)

	dic = {
		"date" : {
			"year" : year,
			"month" : month,
			"day" : day
		},
		"time" : {
			"hour" : hour,
			"minute" : minute,
			"second" : second
		}
	}
	"""
	driver.quit()
	with open("result.csv", "a", encoding="utf-8") as fw:
		writer = csv.writer(fw, lineterminator="\n")
		writer.writerow([ozzu_js])

	with open("result.csv", "r", encoding="utf-8") as fr:
		#reader = csv.reader(fr)
		return fr.read()
	"""
	return json.dumps(dic)
	
	#return "\n".join(reader)

if __name__ == '__main__':
	app.run(debug=False)
