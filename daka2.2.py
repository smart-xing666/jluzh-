from playwright.sync_api import Playwright, sync_playwright, expect
import time
import requests
import threading


def run1(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    page.wait_for_timeout(10000)
    # Go to https://authserver.zcst.edu.cn/cas/login?service=https%3A%2F%2Fwork.zcst.edu.cn%2Fdefault%2Fwork%2Fjlzh%2Fjkxxtb%2Fjkxxcj.jsp
    page.goto("https://authserver.zcst.edu.cn/cas/login?service=https%3A%2F%2Fwork.zcst.edu.cn%2Fdefault%2Fwork%2Fjlzh%2Fjkxxtb%2Fjkxxcj.jsp")
    time.sleep(5)
    # Click [placeholder="用户名\/手机号\/邮箱"]
    page.locator("[placeholder=\"用户名\\/手机号\\/邮箱\"]").click()

    # Fill [placeholder="用户名\/手机号\/邮箱"]
    page.locator("[placeholder=\"用户名\\/手机号\\/邮箱\"]").fill("xxxxxxxx")

    # Click [placeholder="密码"]
    page.locator("[placeholder=\"密码\"]").click()

    # Fill [placeholder="密码"]
    page.locator("[placeholder=\"密码\"]").fill("xxxxxx")

    # Click text=5天内自动登录 登 录 >> input[name="submit"]
    page.locator("text=5天内自动登录 登 录 >> input[name=\"submit\"]").click()
    # expect(page).to_have_url("https://work.zcst.edu.cn/default/work/jlzh/jkxxtb/jkxxcj.jsp")

    # Click text=为了全力做好学校新型冠状病毒感染的肺炎疫情防控工作，我承诺以下内容填写属实。 30s 已阅读并同意 >> ins
    page.locator("text=为了全力做好学校新型冠状病毒感染的肺炎疫情防控工作，我承诺以下内容填写属实。 30s 已阅读并同意 >> ins").click()

    # Click text=下一步
    page.locator("text=下一步").click()

    # Click #select2-select_pcode-container
    page.locator("#select2-select_pcode-container").click()
    time.sleep(1)
    # Click li[role="treeitem"]:has-text("广东省")
    page.locator("li[role=\"treeitem\"]:has-text(\"xxx\")").click()

    # Click #select2-select_ccode-container
    page.locator("#select2-select_ccode-container").click()

    # Click li[role="treeitem"]:has-text("珠海市")
    page.locator("li[role=\"treeitem\"]:has-text(\"xxx\")").click()

    # Click #select2-select_dcode-container
    page.locator("#select2-select_dcode-container").click()

    # Click li[role="treeitem"]:has-text("金湾区")
    page.locator("li[role=\"treeitem\"]:has-text(\"xxx\")").click()

    # Click input[name="jtdz"]
    page.locator("input[name=\"jtdz\"]").click()
    time.sleep(1)
    # Fill input[name="jtdz"]
    page.locator("input[name=\"jtdz\"]").fill("xxxx")

    # Click #hsjcsj div >> nth=1
    page.locator("#hsjcsj div").nth(1).click()

    # Click text=确定 >> nth=1
    page.locator("text=确定").nth(1).click()

    # Click text=本人承诺登记后、到校前不再前往其他地区 >> ins
    page.locator("text=本人承诺登记后、到校前不再前往其他地区 >> ins").click()

    # Click button:has-text("提交")
    page.locator("button:has-text(\"提交\")").click()

    # Click a:has-text("确定")
    page.locator("a:has-text(\"确定\")").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run1(playwright)

requests.packages.urllib3.disable_warnings()
requests.get("https://sctapi.ftqq.com/SCT153582TgKo3b6dteqGcVJyw6mCQCPYh.send?title=%E6%89%93%E5%8D%A1%E6%88%90%E5%8A%9F",verify=False)




