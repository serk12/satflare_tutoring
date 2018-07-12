from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxBinary
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from PIL import Image, ImageFont, ImageDraw

import time
import os

import pyvirtualdisplay


with pyvirtualdisplay.Display(visible=False, size=(1417,1073)):
    url = 'http://www.satflare.com/track.asp?q=41732'
    binary = FirefoxBinary()
    browser = webdriver.Firefox(None, binary)
    browser.get(url)

    try:
        WebDriverWait(browser, 3).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        alert.accept()
    except:
        print("no alert_is_present")

    try:
        element = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.ID, "TabFullScreen")))
        element.click()
    except:
        print("no TabFullScreen")

    try:
        element = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='sc_thispolicy']/child::button[1]")))
        element.click()
    except:
        print("no sc_thispolicy")

    banner = "3Cat-2 NanoSat Lab"
    fontFile = "data/arial.ttf"
    infoText = "The 3Cat-2 (spelled 'cube-cat-two') is the second satellite in" \
                + "the 3Cat series and the second satellite developed in  \nCatalonia " \
                + "at UPC's NanoSat Lab. This spacecraft carries the PYCARO main payload" \
                + ", a novel dual-band and \ndual-polarization GNSS Reflectometer (GNSS-R) which" \
                + " has been designed and manufactured at UPC's Remote\nSensing Lab and NanoSat Lab." \
                + " It also integrates the Mirabilis Star Tracker, an experimental star tracker for " \
                + "attitude\ndetermination and the AMR eLISA magnetometer designed and manufactured at" \
                + " IEEC for the future ESA's LISA mission"
    pictureFile = 'data/picture.png'
    tempImage = "data/building_pic.png"

    print("start loop")

    while(True):
        browser.save_screenshot(tempImage)
        img = Image.open(tempImage)
        draw = ImageDraw.Draw(img)

        draw.rectangle((205, 687, 1060, 889), fill=(255,255,255), outline=(255,0,0))

        font = ImageFont.truetype(fontFile, 36)
        draw.text((300, 700),banner,(0,0,0),font=font)

        font = ImageFont.truetype(fontFile, 16)
        draw.text((215, 750),infoText,(0,0,0),font=font)

        img.save(tempImage)
        os.rename(tempImage, pictureFile)
        time.sleep(1)
    browser.quit()
