import requests
import json
from datetime import datetime

# host = open('/usr/src/app/hostname')
# for line in host:
#     print(line)
# print('tentei')
matricula = '51007731'
hostname = 'brbelrasp118'

urlLogin = 'http://brbelm0itqa01/OJT/ojtws/Authentication/LoginByWorker'
urlMetrics = 'http://brbelm0itqa01/AIOService_AIODashboard/Prodash/GetActualUserAttributes/'
urlLpa = 'http://brbelm0apps02/AIOService/Lpa/GetOpenActionsByPost/?parameters='
urlImagens = 'http://brbelm0itqa01/AIOServiceSTG/Images5S/'
urlAvatar = 'http://brbelm0apps01/UserImage/'
start = datetime.now()


p = requests.post(urlLogin,data = {'HostName':hostname,'Badge':matricula})
print(p.json())
print("Tempo request Login: " + str(p.elapsed.total_seconds()))

r = requests.get(urlMetrics+hostname)
print(r.json())
print("Tempo request metrics: " + str(r.elapsed.total_seconds()))

q = requests.get(urlLpa+hostname)
print(q.json())
print("Tempo request ações lpa: " + str(q.elapsed.total_seconds()))

x = requests.get(urlImagens+'Frame1.png')
print(x)
print("tempo request mural1: " + str(x.elapsed.total_seconds()))

z = requests.get(urlImagens+'Frame2.png')
print(z)
print("Tempo request mural2 " + str(z.elapsed.total_seconds()))

w = requests.get(urlAvatar+'1008294.jpg')
print(w)
print("Tempo request avatar: " + str(w.elapsed.total_seconds()))

end = datetime.now()

print(f"Tempo total (hh:mm:ss.ms): {end - start}")