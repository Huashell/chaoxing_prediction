import pandas as pd
import numpy as np
from flask import Flask, request
import utils as ut
import datautils as du

app = Flask(__name__)
df_job_finish = pd.read_excel('t_stat_job_finish.xls', sheet_name='Sheet1', usecols=['personid',  'jobid'])
df_exam = pd.read_excel('t_stat_exam_answer.xls', sheet_name='Sheet1', usecols=['personid', 'examscore'])
df_bbs = pd.read_excel('t_stat_bbs_log.xls', sheet_name='Sheet1', usecols=['personid'])
df_score = pd.read_excel('t_stat_student_score.xls', sheet_name='Sheet1', usecols=['personid', 'finalscore'])
df_job = pd.read_excel('t_stat_job_finish.xls', sheet_name='Sheet1', usecols=['personid'])

#预测综合成绩
@app.route('/predict', methods=['POST'])
def score_controller():
    #获取请求体中的参数
    data = request.json
    #将字典转换为数组
    param = np.array(list(data.values())).reshape(1, -1)
    return ut.predict_score(param)

#判断学生学习投入值
#param：  personid   学生id
#         courseid   课程id
@app.route('/learning/engagement')
def engagement_controller():
    data = request.json
    personid = int(data.get('personid'))
    courseid = int(data.get('courseid'))
    job_finish = du.get_task(personid, courseid)
    bbs_log = int(data.get('bbs_lob'))
    stat_work = int(data.get('stat_work'))
    return ut.engagement((job_finish, bbs_log, stat_work))


#判断学生学习互动值
#  param: personid 学生id
#         courseid 课程id
@app.route('/learning/interaction')
def interaction_controller():
    data = request.json
    personid = int(data.get('personid'))
    courseid = int(data.get('courseid'))
    job_finish = du.get_task(personid, courseid)
    return ut.interaction(job_finish, bbs_log, preemptive_answer, topic_count)

#判断学生学科偏好值
#  param: personid 学生id
@app.route('/learning/preferences/value')
def preferences_controller():
    data = request.json
    personid = int(data.get('personid'))
    courseid = int(data.get('courseid'))
    job_finish = du.get_task(personid, courseid)
    return ut.preferences(job_finish, bbs_log, stat_work)

#返回学生偏好学科
# param: personid
@app.route('/learning/preferences/subject')
def preferences_sub_controller():
    data = request.json
    personid = int(data.get('personid'))
    #查询数据获取courseid job bbs work数组
    courseid = []
    preferences_value = []
    for i in range(len(courseid)):
        preferences_value.append(ut.preferences())
    maxV = max(preferences_value)
    ind = preferences_value.index(maxV)
    return courseid[ind]


#判断学生学科产出值
# param: personid 学生id
#        courseid
@app.route('/learning/effect')
def effect_controller():
    data = request.json
    personid = int(data.get('personid'))
    courseid = int(data.get('courseid'))
    job_finish = du.get_task(personid, courseid)
    return ut.effect(exam_score, final_score)




#判断学生的学习风格
#param: personid
@app.route('/learning/character')
def character_controller():
    data = request.json


#返回某门课的学习进度
# param: personid
#        courseid



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)


