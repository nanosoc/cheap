import requests, json, random, re, time,selenium,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
TG_BOT_TOKEN = ''           # telegram bot token 自行申请
TG_USER_ID = ''             # telegram 用户ID
def get_email():
    a = random.randint(11, 99)
    b = random.randint(0, 20)
    email = 'lengtmp+{}no{}t@gmail.com'.format(a, b)
    return email
def send(email):
    data = {
        'email': email
    }
    s = requests.post(url='https://cv2.cheap/auth/send', data=data).text
    #print(s)
def get_num(email):
    global Driver
    #print(email)
    head = {
        'Cookie': 'csrf_gmailnator_cookie=9283eccf4672e233327c1d07cbde2fbe; __gads=ID=808c92a03a3667c7-2268f1463cc6007d:T=1614844196:RT=1614845007:S=ALNI_MaEB-hZfUPTo6kHkEmOBLzPe4nqTQ; cto_bundle=AGHOXV9XSVpTNzY3TlRHbldjMDY5RFhQTlU4Y2J1cUpIWGNLVU0xa3ZiWGRKV1duNHo5cXpJYSUyQm5mZ0ROVDJBRFlIa211cG85JTJCOElMV0ZGQUIzVCUyRjg4NTdQZmZSSW9xMzZmMVY5dXdXeDViUUFYeG51SWNibEhqZGxqWGU5NjBQZHpxMg; _ga=GA1.2.1618068840.1614844229; _gid=GA1.2.103981802.1614844229; ci_session=15d382f04f7b998cecd0f9158bfe3db2c8f32629; __cfduid=d1f9a21dd34e5060cfd24ea55f37149961614844181'}
    data = {'csrf_gmailnator_token': '9283eccf4672e233327c1d07cbde2fbe', 'action': 'LoadMailList',
            'Email_address': email}
    try:
        s = requests.post(url='https://www.gmailnator.com/mailbox/mailboxquery', data=data, headers=head).text
        id = re.findall(r'(?<=messageid\\/#).+(?=\\">\\n\\t\\t\\t\\t\\t<table class=\\"message_container)', s)[0]
        #print(id)
        data1 = {'csrf_gmailnator_token': '9283eccf4672e233327c1d07cbde2fbe', 'action': 'get_message', 'message_id': id,'email': 'varytmp'}
        mess = requests.post(url='https://www.gmailnator.com/mailbox/get_single_message/', headers=head, data=data1).text
        #print(mess)
        s_url = re.findall(r'(?<=\\uff1a\\r\\n\\r\\n).+(?=\\r\\n \\r\\n\\u795d\\u987a\\)', mess)[0].replace('\\','')

        #print(s_url)
        Driver.get(s_url)
        time.sleep(2)
        telegram_bot("梯子", '邀请成功！')
        Driver.quit()
    except Exception as e:
        print(e)
        Driver.close()


def register(email):
    global Driver
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--headless')  # 无界面化.
    chrome_opt.add_argument('--disable-gpu')  # 配合上面的无界面化.
    chrome_opt.add_argument('--window-size=1366,768')  # 设置窗口大小, 窗口大小会有影响.
    chrome_opt.add_argument("--no-sandbox")
    Driver = webdriver.Chrome(options=chrome_opt)
    try:
        #Driver = webdriver.Chrome()
        Driver.get('https://www.zionladdero.com/register')
        #driver.switch_to.frame('//*[@id="register"]/div/div')
        WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.ID, 'register')))
        time.sleep(5)
        Driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(email)
        Driver.find_element_by_xpath('//*[@id="id_password1"]').send_keys('refddr265rt!')
        Driver.find_element_by_xpath('//*[@id="id_password2"]').send_keys('refddr265rt!')
        Driver.find_element_by_xpath('//*[@id="register"]/div/div/div[2]/form/div[5]/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[11]/div/div[4]/div/button').click()
        time.sleep(1)
        Driver.find_element_by_xpath('//*[@id="send-confirm-email"]').click()
        ssr=Driver.find_element_by_xpath('/ html / body / div[1] / div / div / div[4] / div / div / p / strong[1]').text
        print(ssr)
        time.sleep(5)
        return ssr
    except Exception as e :
        print(e)
def register2(email,invite):
    global Driver
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--headless')  # 无界面化.
    chrome_opt.add_argument('--disable-gpu')  # 配合上面的无界面化.
    chrome_opt.add_argument('--window-size=1366,768')  # 设置窗口大小, 窗口大小会有影响.
    chrome_opt.add_argument("--no-sandbox")
    Driver = webdriver.Chrome(options=chrome_opt)
    try:
        #Driver = webdriver.Chrome()
        Driver.get(invite)
        #driver.switch_to.frame('//*[@id="register"]/div/div')
        time.sleep(2)
        Driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[1]/div/div[2]/a').click()

        WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.ID, 'register')))
        Driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(email)
        Driver.find_element_by_xpath('//*[@id="id_password1"]').send_keys('refddr265rt!')
        Driver.find_element_by_xpath('//*[@id="id_password2"]').send_keys('refddr265rt!')
        Driver.find_element_by_xpath('//*[@id="register"]/div/div/div/div[2]/form/div[5]/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[11]/div/div[4]/div/button').click()
        time.sleep(1)
        Driver.find_element_by_xpath('//*[@id="send-confirm-email"]').click()
        time.sleep(5)
    except Exception as e:
        print(e)
        telegram_bot("梯子", '邀请失败！')
def telegram_bot(title, content):
    print("\n")
    tg_bot_token = TG_BOT_TOKEN
    tg_user_id = TG_USER_ID
    if "TG_BOT_TOKEN" in os.environ and "TG_USER_ID" in os.environ:
        tg_bot_token = os.environ["TG_BOT_TOKEN"]
        tg_user_id = os.environ["TG_USER_ID"]
    if not tg_bot_token or not tg_user_id:
        print("Telegram推送的tg_bot_token或者tg_user_id未设置!!\n取消推送")
        return
    print("Telegram 推送开始")
    send_data = {"chat_id": tg_user_id, "text": title +
                 '\n\n'+content, "disable_web_page_preview": "true"}
    response = requests.post(
        url='https://api.telegram.org/bot%s/sendMessage' % (tg_bot_token), data=send_data)
    print(response.text)
def main():
    email=get_email()
    ssr=register(email)
    time.sleep(5)
    get_num(email)
    return ssr


def main2(invite):
    email = get_email()

    register2(email,invite)
    time.sleep(5)
    get_num(email)
    return True
if __name__ == "__main__":
    with open('invite.txt','r') as f:
        invite=random.choice(f.readlines()).replace('\n','')
        print(invite)
        main2(invite)
