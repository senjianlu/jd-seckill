#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: E:\Github\jd-seckill-selenium\main.py
# @DATE: 2021/02/10 周三
# @TIME: 20:06:44
#
# @DESCRIPTION: 京东秒杀脚本 Selenium 版本


import time
import jd_login
from rab_python_packages import rab_chrome
from rab_python_packages import rab_logging


# 日志记录
main_logger = rab_logging.build_rab_logger()


"""
@description: 主方法
-------
@param:
-------
@return:
"""
if __name__ == '__main__':
    main_logger.info("京东秒杀脚本 Selenium 版本启动...")
    # Selenium 所接管浏览器所在的端口
    port_num = 9999
    # 建立浏览器
    rab_chrome.build_chrome(port_num)
    driver = rab_chrome.get_driver(port_num)
    # 开始主线程
    try:
        # 前往 JD 登录页面
        driver.get("https://www.jd.com/")
        jd_login.login(driver)
        time.sleep(10)
    except Exception as e:
        rab_chrome.close_chrome(port_num)
        main_logger.error("京东秒杀脚本出错！错误信息：" + str(e))

