import json

data = '{"data":{"message":"ok","nu":"SF1403785112909","ischeck":"1","condition":"F00","com":"shunfeng","status":"200","state":"3","data":[{"time":"2022-09-05 15:31:30","ftime":"2022-09-05 15:31:30","context":"【秦皇岛市】已签收,签收人是拍照签收,感谢使用安能,期待再次为您服务","location":"秦皇岛市 河北秦皇岛开发区东部"},{"time":"2022-09-05 13:45:54","ftime":"2022-09-05 13:45:54","context":"【秦皇岛市】河北秦皇岛开发区东部派件员:霍江华13653363393正在为您派件","location":"秦皇岛市 河北秦皇岛开发区东部"},{"time":"2022-09-05 11:35:23","ftime":"2022-09-05 11:35:23","context":"【秦皇岛市】快件已到达河北秦皇岛开发区东部，电话【18630382665;03358395392】","location":"秦皇岛市 河北秦皇岛开发区东部"},{"time":"2022-09-05 08:41:27","ftime":"2022-09-05 08:41:27","context":"【秦皇岛市】秦皇岛分拨中心已发出,下一站河北秦皇岛开发区东部电话【18630382665;03358395392】","location":"秦皇岛市 秦皇岛分拨中心"},{"time":"2022-09-05 07:34:40","ftime":"2022-09-05 07:34:40","context":"【秦皇岛市】秦皇岛分拨中心快件已到达","location":"秦皇岛市 秦皇岛分拨中心"},{"time":"2022-09-05 02:25:12","ftime":"2022-09-05 02:25:12","context":"【廊坊市】廊坊分拨中心已发出,下一站秦皇岛分拨中心","location":"廊坊市 廊坊分拨中心"},{"time":"2022-09-02 21:21:27","ftime":"2022-09-02 21:21:27","context":"【太原市】太原分拨中心快件已到达","location":"太原市 太原分拨中心"},{"time":"2022-09-02 19:53:48","ftime":"2022-09-02 19:53:48","context":"【晋中市】榆次顺达已发出,下一站太原分拨中心","location":"晋中市 榆次顺达"},{"time":"2022-09-02 18:38:31","ftime":"2022-09-02 18:38:31","context":"【晋中市】榆次顺达收件员已揽件","location":"晋中市 榆次顺达"}]}}'


print(data)
print(type(data))
data1 = json.loads(data)
print(data1)
print(type(data1))


data2 = json.dumps(data1)
print(data2)
print(type(data2))