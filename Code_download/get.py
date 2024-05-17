from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

data = pd.read_excel("C:/Users/15382/Desktop/p1.xlsx")
col_data = data["中成药"]
col_data = col_data.tolist()
print(col_data[0])

ser = Service()
ser.path=r"D:\miniconda3\envs\pytorch\chromedriver.exe"
browser = webdriver.Chrome(service=ser)

browser.get("http://www.tcmip.cn/ETCM2/front/#/browse/chinese_patent_drug")
time.sleep(10)
browser.find_element(By.LINK_TEXT,"简体中文").click()
time.sleep(10)
# data = browser.page_source
# dfs0 = pd.read_html(data)[1]
# dfs0 = pd.read_html(data)[3]
# dfs1 = dfs0.columns
# print(dfs1)
dfs = []
# time.sleep(10)
for i in range(454
               ):
    query = browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[1]/div[1]/div/input")
    query.send_keys(col_data[i])
    # query.send_keys(Keys.RETURN)
    time.sleep(2)
    data = browser.page_source
    df = pd.read_html(data)[1]
    df = df.iloc[0]
    print(df)
    dfs.append(df)
    time.sleep(2)
    query1 = browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[1]/div[1]/div/input")
    query1.send_keys(Keys.CONTROL, "a")
    query1.send_keys(Keys.BACKSPACE)
    time.sleep(3)
result = pd.concat(dfs)
# result.columns = dfs1
print(result)
result.to_excel(r"./all_drug.xlsx")

ser = Service()
ser.path = r'D:\miniconda3\envs\pytorch\chromedriver.exe'
browser = webdriver.Chrome(service=ser)

# browser = webdriver.Chrome()

browser.get("http://www.tcmip.cn/ETCM2/front/#/Detail/ingredient/Zosimin")
time.sleep(10)
# browser.find_element(By.LINK_TEXT,"简体中文").click()
# time.sleep(25)


data = browser.page_source  
# dfs0 = pd.read_html(data)[20]
# dfs0 = pd.read_html(data)[1]
# dfs1 = dfs0.columns
# print(dfs1)
dfs = []
for i in range(49
               ):
    time.sleep(4)
    data = browser.page_source
    df = pd.read_html(data)[21]
    # df = pd.read_html(data)[19]
    print(df)
    # df = pd.read_html(data)[2]
    browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[3]/div/button[2]").click()
    # browser.find_element(By.XPATH,"/html/body/div[1]/div/section/section/div/div/div[2]/div[3]/div[3]/div[2]/div[2]/div/div/div[3]/div/button[2]").click()
    dfs.append(df)
result = pd.concat(dfs)
# result.columns = dfs1
print(result)
result.to_excel(r"./ingredient-formula0.xlsx")

browser = webdriver.Chrome()

browser.get("http://www.tcmip.cn/ETCM2/front/#/Detail/target/KDM1A")
time.sleep(10)
# browser.find_element(By.LINK_TEXT,"简体中文").click()
time.sleep(25)


data = browser.page_source
dfs0 = pd.read_html(data)[1]
# dfs0 = pd.read_html(data)[3]
dfs1 = dfs0.columns
print(dfs1)
dfs = []
query = browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[1]/div[1]/div/input")

query.send_keys("huanglian")
query.send_keys(Keys.RETURN)
time.sleep(10)
for i in range(26
               ):
    time.sleep(4)
    data = browser.page_source
    df = pd.read_html(data)[2]
    # df = pd.read_html(data)[4]
    browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[3]/div/button[2]").click()
    # browser.find_element(By.XPATH,"/html/body/div[1]/div/section/section/div/div/div[2]/div[3]/div[3]/div[2]/div[2]/div/div/div[3]/div/button[2]").click()
    dfs.append(df)
result = pd.concat(dfs)
result.columns = dfs1
print(result)
result.to_excel(r"./target-formula0.xlsx")

# # ## 仅一面
# # time.sleep(1)
# # # element = browser.find_element(By.CSS_SELECTOR,'input[value="化学成分谱"]')
# # element = browser.find_element(By.CSS_SELECTOR,'input[value="Ingredients"]')
# # webdriver.ActionChains(browser).move_to_element(element ).click(element ).perform()
# # time.sleep(2)
# # data = browser.page_source
# # dfs0 = pd.read_html(data)[1]
# # dfs1 = dfs0.columns
# # dfs = []
# # df = pd.read_html(data)[2]
# # # browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[3]/div/button[2]").click()
# # dfs.append(df)
# # result = pd.concat(dfs)
# # result.columns = dfs1
# # print(result)
# # # result.to_excel(r"./爬取文件/化学成分谱.xlsx")
# # result.to_excel(r"./target-ingredient0.xlsx")

## 大于一面
time.sleep(1)
element = browser.find_element(By.CSS_SELECTOR,'input[value="Ingredients"]')
webdriver.ActionChains(browser).move_to_element(element ).click(element ).perform()
time.sleep(2)
data = browser.page_source
dfs0 = pd.read_html(data)[1]
# dfs0 = pd.read_html(data)[3]
dfs1 = dfs0.columns
dfs = []
for i in range(37
               ):
    time.sleep(6)
    data = browser.page_source
    df = pd.read_html(data)[2]
    # df = pd.read_html(data)[4]
    browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[3]/div/button[2]").click()
    # browser.find_element(By.XPATH,"/html/body/div[1]/div/section/section/div/div/div[2]/div[3]/div[3]/div[2]/div[5]/div/div/div[3]/div/button[2]").click()
    
    dfs.append(df)
result = pd.concat(dfs)
result.columns = dfs1
print(result)
result.to_excel(r"./target-ingredient0.xlsx")

time.sleep(5)
element = browser.find_element(By.CSS_SELECTOR,'input[value="Traditional Chinese Medicine Formulas"]')
webdriver.ActionChains(browser).move_to_element(element ).click(element ).perform()
time.sleep(3)
data = browser.page_source
dfs0 = pd.read_html(data)[1]
# dfs0 = pd.read_html(data)[3]
dfs1 = dfs0.columns
dfs = []
query = browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[1]/div[1]/div/input")
query.send_keys("huanglian")
query.send_keys(Keys.RETURN)
time.sleep(4)
for i in range(235
               ):
    time.sleep(5)
    data = browser.page_source
    df = pd.read_html(data)[2]
    # df = pd.read_html(data)[4]
    browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[3]/div/button[2]").click()
    # browser.find_element(By.XPATH,"/html/body/div[1]/div/section/section/div/div/div[2]/div[3]/div[3]/div[2]/div[3]/div/div/div[3]/div/button[2]").click()
    
    dfs.append(df)
result = pd.concat(dfs)
result.columns = dfs1
print(result)
result.to_excel(r"./target-traditional0.xlsx")

browser = webdriver.Chrome()

browser.get("http://www.tcmip.cn/ETCM2/front/#/Detail/target/KDM1A")
time.sleep(10)
browser.find_element(By.LINK_TEXT,"简体中文").click()
time.sleep(35)



data = browser.page_source
dfs0 = pd.read_html(data)[1]
# dfs0 = pd.read_html(data)[3]
dfs1 = dfs0.columns
print(dfs1)
dfs = []
query = browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[1]/div[1]/div/input")
query.send_keys("黄连")
query.send_keys(Keys.RETURN)
time.sleep(10)
for i in range(27
               ):
    time.sleep(4)
    data = browser.page_source
    df = pd.read_html(data)[2]
    # df = pd.read_html(data)[4]
    browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[3]/div/button[2]").click()
    # browser.find_element(By.XPATH,"/html/body/div[1]/div/section/section/div/div/div[2]/div[3]/div[3]/div[2]/div[2]/div/div/div[3]/div/button[2]").click()
    
    dfs.append(df)
result = pd.concat(dfs)
result.columns = dfs1
print(result)
result.to_excel(r"./CHN_target-formula0.xlsx")

time.sleep(4)
element = browser.find_element(By.CSS_SELECTOR,'input[value="相关中药古籍方剂列表"]')
webdriver.ActionChains(browser).move_to_element(element ).click(element ).perform()
time.sleep(3)
data = browser.page_source
dfs0 = pd.read_html(data)[1]
# dfs0 = pd.read_html(data)[3]
dfs1 = dfs0.columns
dfs = []
query = browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[1]/div[1]/div/input")
query.send_keys("黄连")
query.send_keys(Keys.RETURN)
time.sleep(12)
for i in range(235
               ):
    time.sleep(5)
    data = browser.page_source
    df = pd.read_html(data)[2]
    # df = pd.read_html(data)[4]
    browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[3]/div/button[2]").click()
    # browser.find_element(By.XPATH,"/html/body/div[1]/div/section/section/div/div/div[2]/div[3]/div[3]/div[2]/div[3]/div/div/div[3]/div/button[2]").click()
    
    dfs.append(df)
result = pd.concat(dfs)
result.columns = dfs1
print(result)
result.to_excel(r"./CHN_target-traditional0.xlsx")

time.sleep(1)
# element = browser.find_element(By.CSS_SELECTOR,'input[value="相关中药古籍方剂列表"]')
element = browser.find_element(By.CSS_SELECTOR,'input[value="Traditional Chinese Medicine Formulas"]')
webdriver.ActionChains(browser).move_to_element(element ).click(element ).perform()
time.sleep(2)
data = browser.page_source
dfs0 = pd.read_html(data)[1]
dfs1 = dfs0.columns
print(dfs1)
dfs = []
for i in range():
    time.sleep(2)
    data = browser.page_source
    df = pd.read_html(data)[2]
    browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[3]/div/button[2]").click()
    dfs.append(df)
result = pd.concat(dfs)
result.columns = dfs1
print(result)
# result.to_excel(r"./爬取文件/相关中药古籍方剂列表.xlsx")
result.to_excel(r"./爬取文件/Eng_相关中药古籍方剂列表.xlsx")

time.sleep(1)
# element = browser.find_element(By.CSS_SELECTOR,'input[value="化学成分谱"]')
element = browser.find_element(By.CSS_SELECTOR,'input[value="Ingredients"]')
webdriver.ActionChains(browser).move_to_element(element ).click(element ).perform()
time.sleep(2)
data = browser.page_source
dfs0 = pd.read_html(data)[1]
dfs1 = dfs0.columns
print(dfs1)
dfs = []
for i in range(3):
    time.sleep(2)
    data = browser.page_source
    df = pd.read_html(data)[2]
    browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[3]/div/button[2]").click()
    dfs.append(df)
result = pd.concat(dfs)
result.columns = dfs1
print(result)
# result.to_excel(r"./爬取文件/化学成分谱.xlsx")
result.to_excel(r"./爬取文件/Eng_化学成分谱.xlsx")

# 04 候选靶标谱
time.sleep(1)
# element = browser.find_element(By.CSS_SELECTOR,'input[value="候选靶标谱"]')
element = browser.find_element(By.CSS_SELECTOR,'input[value="Targets"]')
webdriver.ActionChains(browser).move_to_element(element ).click(element ).perform()
time.sleep(2)
data = browser.page_source
dfs0 = pd.read_html(data)[1]
dfs1 = dfs0.columns
print(dfs1)
dfs = []
for i in range(7):
    time.sleep(2)
    data = browser.page_source
    df = pd.read_html(data)[2]
    browser.find_element(By.XPATH,"//*[@id=\"alltable\"]/div[3]/div/button[2]").click()
    dfs.append(df)
result = pd.concat(dfs)
result.columns = dfs1
print(result)
# result.to_excel(r"./爬取文件/候选靶标谱.xlsx")
result.to_excel(r"./爬取文件/Eng_候选靶标谱.xlsx")