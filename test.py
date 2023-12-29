from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 启动浏览器（这里以 Chrome 为例，确保你已经下载了 ChromeDriver）
driver = webdriver.Chrome()

# 打开目标网页
driver.get("https://bmvs.onlineappointmentscheduling.net.au/oasis/Default.aspx")

# 定位并点击特定 ID 的按钮
button1 = driver.find_element(By.ID, "ContentPlaceHolder1_btnInd")
button1.click()

# 使用显式等待等待特定 ID 的input元素可见
wait1 = WebDriverWait(driver, 20)  # 等待最多20秒
input_element = wait1.until(EC.visibility_of_element_located((By.ID, "ContentPlaceHolder1_SelectLocation1_txtSuburb")))

# 填写input元素
input_element.send_keys("0832")
button2 = driver.find_element(By.CSS_SELECTOR, f'input[value="Search"]')
button2.click()

wait2 = WebDriverWait(driver, 20)
location_check = wait2.until(EC.visibility_of_element_located((By.ID, "rbLocation137")))
next_button = driver.find_element(By.ID, "ContentPlaceHolder1_btnCont")
location_check.click()
next_button.click()


wait3 = WebDriverWait(driver, 20)
medical_exam_check = wait3.until(EC.visibility_of_element_located((By.ID, "chkClass1_489")))
chest_x_ray_check = driver.find_element(By.ID, "chkClass1_492")
serum_check = driver.find_element(By.ID, "chkClass1_1266")
next_button2 = driver.find_element(By.ID,"ContentPlaceHolder1_btnCont")

medical_exam_check.click()
chest_x_ray_check.click()
serum_check.click()
next_button2.click()




