from requests_html import HTMLSession

url = "https://explorer.duinocoin.com/"

s = HTMLSession()
r = s.get(url)
r.html.render(sleep = 1)

a = r.html.xpath('//*[@id="hashrate"]', first=True)
b = r.html.xpath('//*[@id="registeredusers"]', first=True)
c = r.html.xpath('//*[@id="allmined"]', first=True)
d = r.html.xpath('//*[@id="watt_usage"]', first=True)
e = r.html.xpath('//*[@id="shares"]', first=True)
f = r.html.xpath('//*[@id="workercount"]', first=True)

Hash_Rate = a.text
Users = b.text
Circulation = c.text
Net_Energy = d.text
Mined_Shares = e.text
Active_Workers = f.text

print(f"Hash_Rate = {Hash_Rate}")
print(f"Users = {Users}")
print(f"Circulation = {Circulation}")
print(f"Net_Energy = {Net_Energy}")
print(f"Mined_Shares = {Mined_Shares}")
print(f"Active_Workers = {Active_Workers}")

with open("data.txt",'w', encoding="utf-8")as f:
    f.write((f"Hash_Rate = {Hash_Rate}"))
    f.write("\n")
    f.write(f"Users = {Users}")
    f.write("\n")
    f.write(f"Circulation = {Circulation}")
    f.write("\n")
    f.write(f"Net_Energy = {Net_Energy}")
    f.write("\n")
    f.write(f"Mined_Shares = {Mined_Shares}")
    f.write("\n")
    f.write(f"Active_Workers = {Active_Workers}")
    f.write("\n")
