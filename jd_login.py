#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: E:\Github\jd-seckill-selenium\jd_login.py
# @DATE: 2021/02/10 周三
# @TIME: 21:10:16
#
# @DESCRIPTION: 京东登录模块


import os
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rab_python_packages import rab_logging


# 登录模块日志记录
login_logger = rab_logging.build_rab_logger()


"""
@description: 从图片路径读取图片并解析成为二维码（存在登录风险，废弃）
-------
@param:
-------
@return:
"""
def decode_png_and_print_qrcode(png_path):
    login_logger.info("开始转换二维码...")
    # 读取图片中二维码的链接
    barcode_url = ''
    barcodes = decode(Image.open(png_path))
    for barcode in barcodes:
        barcode_url = barcode.data.decode("utf-8")
    # 将链接转回二维码并打印
    qr = qrcode.QRCode()
    qr.add_data(barcode_url)
    qr.print_ascii(invert=True)

"""
@description: 直接显示图片
-------
@param:
-------
@return:
"""
def show_png(png_path):
    png = Image.open(png_path)
    png.show()

"""
@description: 等待扫码登录完成
-------
@param:
-------
@return:
"""
def wait_for_qrcode_login():
    rab_logging.info("请在一分钟内扫码登录...")
    time.sleep(60)

"""
@description: 登录方法
-------
@param:
-------
@return:
"""
def login(driver):
    # 跳转至登录页
    login_a = driver.find_element_by_xpath(
        "//li[@id='ttbar-login']/a[contains(@class,'link-login')]")
    login_a.click()
    login_logger.info("已跳转至登录页面！")
    # 等待 QR 二维码出现
    qrcode_xpath = "//div[@id='J-qrcoderror']"
    element = WebDriverWait(driver, 10, 0.2).until(
            EC.presence_of_element_located((By.XPATH, qrcode_xpath)))
    login_logger.info("登录二维码加载完成！")
    # 登录界面临时保存文件名
    png_file_name = "login_screenshot.png"
    if (os.path.exists(png_file_name)):
        os.remove(png_file_name)
    driver.save_screenshot(png_file_name)
    login_logger.info("登录页面保存完成！路径：" + str(png_file_name))
    # 由于转换二维码后登录存在风险，因此改为保存本地直接访问
    # 如果在服务器上使用请提前使用 Nginx 设置路径
    # decode_png_and_print_qrcode(png_file_name)
    wait_for_qrcode_login()
    