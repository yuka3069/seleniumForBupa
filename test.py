from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import smtplib#导入smtp模块
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header 

#smtp的服务类型，我的是QQ，其他比如136邮箱可改成smtp.136.com,或者谷歌邮箱smtp.gmail.com
SMTP_SERVER = 'smtp.qq.com'
#这个端口一般没什么问题所有邮箱都是25，谷歌的587也可以
SMTP_PORT = 465
#自己的qq邮箱，如果你是136的话可以改成xxxxxx@136.com
QQMAIL_USER = 'yourqq@qq.com'
#smtp服务的授权码，根据上面的操作就可以获得
QQMAIL_PASS = 'yourQQmailPass'




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


#需要填写 recipient,subject,和邮件内容，recipient为收件人的邮箱地址。，text为邮件内容
def send_email(recipient,subject,text):
    smtpserver = smtplib.SMTP_SSL(SMTP_SERVER,465)
    smtpserver.login(QQMAIL_USER,QQMAIL_PASS)
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = QQMAIL_USER
    msg['To'] = recipient

    smtpserver.sendmail(QQMAIL_USER,recipient,msg)
    smtpserver.quit()


#查看是否有空位
status_text = driver.find_element(By.ID,"ContentPlaceHolder1_SelectTime1_divNoAvailSlots").text
print(status_text)
if 'no available' in status_text:
    print("no!")
else:
    print("yes!")




