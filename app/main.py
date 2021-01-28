import requests
import json
# host = open('/usr/src/app/hostname')
# for line in host:
#     print(line)
# print('tentei')

urlMetrics = 'http://brbelm0itqa01/AIOService_AIODashboard/Prodash/GetActualUserAttributes/'
hostname = 'brbelrasp103'
r = requests.get(urlMetrics+hostname)

print(r.json())
