import requests
import json

#根据学生id和courseid获取任务完成数
def get_task(personid, courseid):
    url = 'localhost:8080/?personid={}&courseid={}'.format((personid, courseid))
    response = requests.get(url)
    data = response.json()
    count = 0
    for item in data:
        ++count
    return count



#根据学生id和courseid获取考试成绩



#根据学生id和courseid获取综合成绩


#根据学生id和courseid获取综合成绩



#根据学生id和courseid获取学生参与讨论次数



#根据学生id和courseid获取学生完成任务次数



#根据学生id和courseid获取学生参与同步课堂次数



#根据学生id和courseid获取学生参与课堂直播次数





#根据学生id和courseid获取学生参与选人次数




#根据学生id和courseid获取学生参与问卷次数





#根据学生id和courseid获取学生参与分组任务活动次数



#根据班级id返回所有学生id



#根据班级id返回所有学生成绩
