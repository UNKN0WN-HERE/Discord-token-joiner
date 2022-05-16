import random, httpx, json, time
from colorama import Fore,Style

with open('./config.json') as fp:
    config = json.load(fp)
    
capapi = config["API"]
timeout=config["timeout"]
key=config["apikey"]

class TokenJoiner:
    def __init__(self, key, invitecode, token):
        self.key = key
        self.invitecode = invitecode
        
        with open("./Data/Proxies.txt") as fp:
            proxies = fp.read().splitlines()
            
        self.client = httpx.Client(timeout=timeout,headers={"Pragma": "no-cache", "Accept": "*/*", "Host": "discord.com", "Accept-Language": "en-US", "Cache-Control": "no-cache", "Accept-Encoding": "br, gzip, deflate", "Referer": "https://discord.com/", "Connection": "keep-alive", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
                                                                         "X-Track": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IlNhZmFyaSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi11cyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzEzXzYpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xMy4xLjIgU2FmYXJpLzYwNS4xLjE1IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTMuMS4yIiwib3NfdmVyc2lvbiI6IjEwLjEzLjYiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTEzNTQ5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}, cookies={"locale": "en-US"}, proxies=f"http://{random.choice(proxies)}") if config["Proxyless"] == False else httpx.Client(cookies={"locale": "en-US"}, headers={"Pragma": "no-cache", "Accept": "*/*", "Host": "discord.com", "Accept-Language": "en-US", "Cache-Control": "no-cache", "Accept-Encoding": "br, gzip, deflate", "Referer": "https://discord.com/", "Connection": "keep-alive", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
                                                                         "X-Track": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IlNhZmFyaSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi11cyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzEzXzYpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xMy4xLjIgU2FmYXJpLzYwNS4xLjE1IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTMuMS4yIiwib3NfdmVyc2lvbiI6IjEwLjEzLjYiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTEzNTQ5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="})
        
        self.client.headers["X-Fingerprint"] = self.client.get("https://canary.discord.com/api/v10/experiments", timeout=30).json()["fingerprint"]
        self.client.headers["X-Super-Properties"] = "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IlNhZmFyaSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi11cyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzEzXzYpIEFwcGxlV2ViS2l0LzYwNS4xLjE1IChLSFRNTCwgbGlrZSBHZWNrbykgVmVyc2lvbi8xMy4xLjIgU2FmYXJpLzYwNS4xLjE1IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTMuMS4yIiwib3NfdmVyc2lvbiI6IjEwLjEzLjYiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTE3OTE4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
        self.client.headers["Authorization"] = token
        self.client.headers["Origin"] = "https://discord.com"
        
    def JoinServer(self):
        time.sleep(config["delay"])
        joinreq = self.client.post(f"https://canary.discord.com/api/v10/invites/{self.invitecode}")
        if "captcha_key" not in joinreq.json():
            if "message" in joinreq.json() and joinreq["message"] == "You need to verify your account in order to perform this action.":
                print(f"{self.client.headers['Authorization']} - Locked Token")
                return "FailedJoin", joinreq.json()
            print(
                f"{Fore.GREEN}{self.client.headers['Authorization']} Successfully Joined discord.gg/{self.invitecode} {Style.RESET_ALL}")
            return "SuccessJoin", joinreq.json()
        captcha_rqtoken = joinreq.json()["captcha_rqtoken"]
        joinreq=self.client.post(f"https://canary.discord.com/api/v10/invites/{self.invitecode}", json={"captcha_key": self.solvecaptcha(), "captcha_rqtoken": captcha_rqtoken})
        if joinreq.status_code == 200:
            print(
                f"{Fore.GREEN}{self.client.headers['Authorization']} Successfully Joined discord.gg/{self.invitecode} {Style.RESET_ALL}")
            return "SuccessJoin", joinreq.json()
        else:
            print(
                f"{Fore.RED}{self.client.headers['Authorization']} Failed To Join discord.gg/{self.invitecode} {Style.RESET_ALL}")
            return "FailedJoin", joinreq.json()
        
    def solvecaptcha(self):
        capapi = config["API"]
        apikey = config["apikey"]
        solvedCaptcha = None
        taskId = ""
        taskId = httpx.post(f"https://api.{capapi}/createTask", json={"clientKey": apikey, "task": {"type": "HCaptchaTaskProxyless", "websiteURL": "https://discord.com/",
                            "websiteKey": "a9b5fb07-92ff-493f-86fe-352a2803b3df", "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"}}, timeout=30).json()
        if taskId.get("errorId") > 0:
            print(f"[-] createTask - {taskId.get('errorDescription')}!")
            return None
        taskId = taskId.get("taskId")

        while not solvedCaptcha:
            captchaData = httpx.post(f"https://api.{capapi}/getTaskResult", json={
                                     "clientKey": apikey, "taskId": taskId}, timeout=30).json()
            if captchaData.get("status") == "ready":
                solvedCaptcha = captchaData.get(
                    "solution").get("gRecaptchaResponse")
                return 
