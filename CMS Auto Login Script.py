"""
================================================================================
📘 CMS AUTO LOGIN SCRIPT - SETUP AND USAGE GUIDE
================================================================================

🛠️ REQUIREMENTS:
-----------------
- Python 3.7 or higher
- Google Chrome browser installed
- ChromeDriver that matches your Chrome version

--------------------------------------------------------------------------------
📥 1. INSTALL PYTHON (If not already installed)
--------------------------------------------------------------------------------
- Download Python from: https://www.python.org/downloads/
- During installation, check ✅ "Add Python to PATH"

--------------------------------------------------------------------------------
💾 2. SAVE THIS SCRIPT
--------------------------------------------------------------------------------
- Save this file as: cms_auto_login.py

--------------------------------------------------------------------------------
📦 3. INSTALL REQUIRED PYTHON MODULES
--------------------------------------------------------------------------------
Open Command Prompt (or Terminal) and run:
    pip install selenium

(Note: 'tkinter' is built into Python, no need to install)

--------------------------------------------------------------------------------
🌐 4. DOWNLOAD & SET UP CHROMEDRIVER
--------------------------------------------------------------------------------
STEP 1: Check your Chrome version
    - Open Chrome > 3-dots menu > Help > About Google Chrome

STEP 2: Download matching ChromeDriver:
    https://sites.google.com/chromium.org/driver/

STEP 3: Extract it and either:
    - Add the folder containing chromedriver.exe to your system PATH
    OR
    - Place chromedriver.exe in the same folder as this script

--------------------------------------------------------------------------------
🚀 5. RUN THE SCRIPT
--------------------------------------------------------------------------------
Navigate to the folder where this script is saved and run:

    python cms_auto_login.py

--------------------------------------------------------------------------------
🔑 EXAMPLE INPUT:
--------------------------------------------------------------------------------
When prompted:
    CMS Code  : 58530
    Password  : 16-07-2003 (Format: dd-mm-yyyy)

--------------------------------------------------------------------------------
THIS SCRIPT DOES:
--------------------------------------------------------------------------------
- Opens the IPS CMS login page
- Asks for your CMS Code and Password using a GUI popup
- Logs you in
- Navigates the menu using hover actions
- Redirects to Student home page
- Logs out automatically
- Closes the browser

================================================================================
"""

import tkinter as tk
from tkinter import simpledialog, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# --- GUI Window Setup ---
root = tk.Tk()
root.withdraw()  # Hide the root window

# Show instruction message
messagebox.showinfo(
    "Login Instructions",
    "🔐 Example:\nComputer Code = 58530\nPassword = 16-07-2003\n\n📌 Note: Enter password in the format dd-mm-yyyy."
)

# Prompt for inputs
cms_code = simpledialog.askstring("CMS Login", "Enter your CMS Code:")
password = simpledialog.askstring("CMS Login", "Enter your Password (dd-mm-yyyy):", show='*')

# Validation
if not cms_code or not password:
    messagebox.showerror("Input Error", "CMS Code and Password are required!")
    exit()

# --- Selenium Automation ---
driver = webdriver.Chrome()

driver.get("https://cms2.ipsacademy.net/Login")
time.sleep(2)
driver.maximize_window()

# Click the link to redirect
driver.find_element(By.TAG_NAME, "a").click()
time.sleep(2)

# Login form
driver.find_element(By.NAME, "computer_code").send_keys(cms_code)
time.sleep(1)
driver.find_element(By.NAME, "password").send_keys(password)
time.sleep(1)
driver.find_element(By.CLASS_NAME, "login-button").click()
time.sleep(3)

# Hover and click on menu
mst = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/nav/ul/li[6]/a')
hover_obj = ActionChains(driver)
hover_obj.move_to_element(mst).perform()
time.sleep(1)
mst.click()
time.sleep(2)

# Go to student home page
driver.get("https://cms2.ipsacademy.net/Student")
time.sleep(2)

# Open dropdown menu
drop_down_ = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/ul/li/a/div/i[1]')
drop_down_.click()
time.sleep(2)

# Click logout
log_out = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/ul/li/ul/li[3]/a')
hover_obj.move_to_element(log_out).perform()
time.sleep(1)
log_out.click()

time.sleep(2)
driver.quit()
