# Appium 介绍 
## 1.特点  
#### appium 是一个自动化测试开源工具，支持 iOS 平台和 Android 平台上的原生应用，web应用和混合应用。

* “移动原生应用”是指那些用iOS或者 Android SDK 写的应用（Application简称app）。

* “移动web应用”是指使用移动浏览器访问的应用（appium支持iOS上的Safari和Android上的 Chrome）。
* “混合应用”是指原生代码封装网页视图——原生代码和 web 内容交互。比如，像 Phonegap，可以帮助开发者使用网页技术开发应用，然后用原生代码封装，这些就是混合应用。
重要的是，appium是一个跨平台的工具：它允许测试人员在不同的平台（iOS，Android）使用同一套API来写自动化测试脚本，这样大大增加了iOS和Android测试套件间代码的复用性。
## 2. appium 与 selenium 
* appium类库封装了标准Selenium客户端类库，为用户提供所有常见的JSON格式selenium命令以及额外的移动设备控制相关的命令，如多点触控手势和屏幕朝向。
appium客户端类库实现了Mobile JSON Wire Protocol（一个标准协议的官方扩展草稿）和W3C WebDriver spec（一个传输不可预知的自动化协议，该协议定义了MultiAction 接口）的元素。
* appium服务端定义了官方协议的扩展，为appium 用户提供了方便的接口来执行各种设备动作，例如在测试过程中安装/卸载App。这就是为什么我们需要appium特定的客户端，而不是通用的Selenium 客户端。当然，appium 客户端类库只是增加了一些功能，而实际上这些功能就是简单的扩展了Selenium 客户端，所以他们仍然可以用来运行通用的Selenium会话。
## 3. 工作原理
![](https://oss.v2url.com/2018/03/13/c1f3dc4f223a199b2c515d0c06b400f4.png)

# Appium 安装
## 1.安装Android SDK
Android Studio & Android SDK 下载地址：[下载地址](http://tools.android-studio.org/index.php/sdk)
下载完成后解压 
## 2.设置安卓环境变量

```

ANDROID_HOME	D:\android\Android\sdk

PATH	;%ANDROID_HOME%\platform-tools;%ANDROID_HOME%\tools;
```
## 3.安装Android版本
* 双击 SDK Manage.exe 启动SDK管理器，选择版本进行勾选安装
![](http://otfah9orz.bkt.clouddn.com/appium_sdk_manage.png)


* 双击 AVD Manage.exe 启动AVD管理器,创建虚拟机
![](http://otfah9orz.bkt.clouddn.com/appium_create_new_avd.png)

## 4.安装Appium 

* 安装node.js [官网](https://nodejs.org/en/)，安装成功后执行npm install -g appium 进行appium安装 

## 5.安装Appium Client
使用python编写脚本，需要安装python环境，版本自行选择
	
```
pip install Appium-Python-Client
```
## 6.配置项

* 启动appium：cmd中执行appium命令

![](https://oss.v2url.com/2018/03/13/f3905549b4ecb74531398ecefb420fd9.png)

* 打开模拟器或连接真机，打开usb调试，使用adb命令获取设备号及设备连接状态

![](https://oss.v2url.com/2018/03/13/18c3789a3a26f71cfe4cd5b011692308.png)

* Android 获取包名和 Activity 的方法[去查看](https://testerhome.com/topics/9209)

## 7.元素定位
* 打开sdk安装目录：D:\android-sdk\tools，执行uiautomatorviewer.bat

![](https://oss.v2url.com/2018/03/13/d4658cde2c904fa79b6eeb4e0e41eaea.png)

具体的捕捉方法详见：[元素定位](http://www.cnblogs.com/forcepush/p/6721828.html)

#### 脚本编写

```
#coding=utf-8
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'#设备系统
desired_caps['platformVersion'] = '4.4.2' #设备系统版本
desired_caps['deviceName'] = 'Android Emulator' #设备名称
desired_caps['appPackage'] = 'com.android.calculator2' 测试app包名
desired_caps['appActivity'] = '.Calculator' #测试appActivity

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_name("1").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("delete").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("+").click()

driver.find_element_by_name("6").click()

driver.find_element_by_name("=").click()

driver.quit()
```







