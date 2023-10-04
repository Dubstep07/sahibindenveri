from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import xlsxwriter

baslik_list=[]
fiyat_list=[]
ilan_no_list=[]
ilan_tarihi_list=[]
marka_list=[]
seri_list=[]
model_list=[]
yil_list=[]
yakit_list=[]
vites_list=[]
arac_durumu_list=[]
km_list=[]
kasa_tipi_list=[]
motor_gucu_list=[]
motor_hacmi_list=[]
cekis_list=[]
kapi_list=[]
renk_list=[]
garanti_list=[]
agir_hasar_kayitli_list=[]
plaka_uyruk_list=[]
kimden_list=[]
goruntu_list=[]
takas_list=[]

workbook = xlsxwriter.Workbook("SUV.xlsx")
worksheet = workbook.add_worksheet("AracBilgileri")

chop = webdriver.ChromeOptions()
chop.add_extension('extension_1_48_4_0.crx')
driver = webdriver.Chrome(chrome_options = chop)


sayfa = 0
driver.get("https://www.sahibinden.com/arazi-suv-pickup?pagingOffset={}&pagingSize=50".format(sayfa))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))).click()

while sayfa <= 950:
    driver.get("https://www.sahibinden.com/arazi-suv-pickup?pagingOffset={}&pagingSize=50")
    sayfa += 50
    sleep(1)
    ilan = 1
    while ilan <= 52:
        try:
            sleep(2)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchResultsTable > tbody > tr:nth-child({})".format(ilan)))).click()
            baslik=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailTitle > h1').text
            fiyat=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > h3').text.split('TL')[0]
            ilan_no=driver.find_element(By.CSS_SELECTOR, '#classifiedId').text
            ilan_tarihi=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(2) > span').text
            marka=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(3) > span').text
            seri=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(4) > span').text
            model=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(5) > span').text
            yil=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(6) > span').text
            yakit=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(7) > span').text
            vites=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(8) > span').text
            arac_durumu=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(9) > span').text
            km=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(10) > span').text
            kasa_tipi=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(11) > span').text
            motor_gucu=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(12) > span').text.split('hp')[0]
            motor_hacmi=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(13) > span').text.split('cc')[0]
            cekis=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(14) > span').text
            kapi=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(15) > span').text
            renk=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(16) > span').text
            garanti=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(17) > span').text
            agir_hasar_kayitli=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(18) > span').text
            plaka_uyruk=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(19) > span').text
            kimden=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(20) > span').text
            goruntu=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(21) > span').text
            takas=driver.find_element(By.CSS_SELECTOR, '#classifiedDetail > div > div.classifiedDetailContent > div.classifiedInfo > ul > li:nth-child(22) > span').text
            
            baslik_list.append(baslik)
            fiyat_list.append(fiyat)
            ilan_no_list.append(ilan_no)
            ilan_tarihi_list.append(ilan_tarihi)
            marka_list.append(marka)
            seri_list.append(seri)
            model_list.append(model)
            yil_list.append(yil)
            yakit_list.append(yakit)
            vites_list.append(vites)
            arac_durumu_list.append(arac_durumu)
            km_list.append(km)
            kasa_tipi_list.append(kasa_tipi)
            motor_gucu_list.append(motor_gucu)
            motor_hacmi_list.append(motor_hacmi)
            cekis_list.append(cekis)
            kapi_list.append(kapi)
            renk_list.append(renk)
            garanti_list.append(garanti)
            agir_hasar_kayitli_list.append(agir_hasar_kayitli)
            plaka_uyruk_list.append(plaka_uyruk)                
            kimden_list.append(kimden)
            goruntu_list.append(goruntu)
            takas_list.append(takas)
            
            ilan += 1
            sleep(1)
            driver.back()
        except:
            ilan += 1
            sleep(1)
            driver.get("https://www.sahibinden.com/arazi-suv-pickup?pagingOffset={}&pagingSize=50".format(sayfa))
            
            

for satir,veri in enumerate(baslik_list):
    worksheet.write(satir,0,veri) 
for satir,veri in enumerate(fiyat_list):
    worksheet.write(satir,1,veri)
for satir,veri in enumerate(ilan_no_list):
    worksheet.write(satir,2,veri)
for satir,veri in enumerate(ilan_tarihi_list):
    worksheet.write(satir,3,veri)
for satir,veri in enumerate(marka_list):
    worksheet.write(satir,4,veri)
for satir,veri in enumerate(seri_list):
    worksheet.write(satir,5,veri)
for satir,veri in enumerate(model_list):
    worksheet.write(satir,6,veri)
for satir,veri in enumerate(yil_list):
    worksheet.write(satir,7,veri)
for satir,veri in enumerate(yakit_list):
    worksheet.write(satir,8,veri)
for satir,veri in enumerate(vites_list):
    worksheet.write(satir,9,veri)
for satir,veri in enumerate(arac_durumu_list):
    worksheet.write(satir,10,veri)
for satir,veri in enumerate(km_list):
    worksheet.write(satir,11,veri)
for satir,veri in enumerate(kasa_tipi_list):
    worksheet.write(satir,12,veri)
for satir,veri in enumerate(motor_gucu_list):
    worksheet.write(satir,13,veri)
for satir,veri in enumerate(motor_hacmi_list):
    worksheet.write(satir,14,veri)
for satir,veri in enumerate(cekis_list):
    worksheet.write(satir,15,veri)
for satir,veri in enumerate(kapi_list):
    worksheet.write(satir,16,veri)
for satir,veri in enumerate(renk_list):
    worksheet.write(satir,17,veri)
for satir,veri in enumerate(garanti_list):
    worksheet.write(satir,18,veri)
for satir,veri in enumerate(agir_hasar_kayitli_list):
    worksheet.write(satir,19,veri)
for satir,veri in enumerate(plaka_uyruk_list):
    worksheet.write(satir,20,veri)
for satir,veri in enumerate(kimden_list):
    worksheet.write(satir,21,veri)
for satir,veri in enumerate(goruntu_list):
    worksheet.write(satir,22,veri)
for satir,veri in enumerate(takas_list):
    worksheet.write(satir,23,veri)

workbook.close()
driver.close()