import pickle
import numpy as np
import numpy as np
from flask import Flask, request

app = Flask(__name__)
# 从文件中加载模型
with open('rf_model.pkl', 'rb') as f:
    clf_rf_loaded = pickle.load(f)

#预测综合成绩
@app.route('/predict', methods=['POST'])
def score_controller():
    #获取请求体中的参数
    data = request.json
    #将字典转换为数组
    param = np.array(list(data.values())).reshape(1, -1)
    # 进行预测
    return str(clf_rf_loaded.predict(param)[0])

#判断学生学习投入值
#param：job_finish   完成任务数
#       bbs_log    参与讨论数
#       stat_work   完成作业数
@app.route('/Learning/engagement')
def engagement_controller():
    data = request.json
    job_finish = int(data.get('job_finish'))
    bbs_log = int(data.get('bbs_lob'))
    stat_work = int(data.get('stat_work'))
    return 0.95238*job_finish + 0.9764*bbs_log + 0.9449*stat_work;


#判断学生学习互动值
#param：job_finish   完成任务数
#       bbs_log    参与讨论数
#       preemptive_answer  参与抢答数
#       topic_count    发帖数
@app.route('/Learning/interaction')
def engagement_controller():
    data = request.json
    job_finish = int(data.get('job_finish'))
    bbs_log = int(data.get('bbs_lob'))
    preemptive_answer = int(data.get('preemptive_answer'))
    topic_count = int(data.get('topic_count'))
    return 0.9142*job_finish + 0.9339*bbs_log + 1.49*preemptive_answer + 1.33*topic_count;

#判断学生学科偏好值
#param：job_finish   完成任务数
#       bbs_log    参与讨论数
#       stat_work   完成作业数
@app.route('/Learning/preferences')
def engagement_controller():
    data = request.json
    job_finish = int(data.get('job_finish'))
    bbs_log = int(data.get('bbs_lob'))
    stat_work = int(data.get('stat_work'))
    return 0.95238*job_finish + 0.9764*bbs_log + 0.9449*stat_work;

#判断学生学科效果值
#param：exam_score  平均考试成绩
#       fianl_score    综合成绩
@app.route('/Learning/effect')
def engagement_controller():
    data = request.json
    exam_score = int(data.get('exam_score'))
    final_score = int(data.get('final_score'))
    return 1.0339 * exam_score + 2.1579 * final_score

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)


