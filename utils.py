import pickle

with open('rf_model.pkl', 'rb') as f:
    clf_rf_loaded = pickle.load(f)

#预测综合函数
def predict_score(paramlist):
    return str(clf_rf_loaded.predict(paramlist)[0])

#预测学生学习投入值
def engagement(job_finish, bbs_log, stat_work):
    return 0.95238*job_finish + 0.9764*bbs_log + 0.9449*stat_work


#预测学生学习互动值
def interaction(job_finish, bbs_log, preemptive_answer, topic_count):
    return 0.9142*job_finish + 0.9339*bbs_log + 1.49*preemptive_answer + 1.33*topic_count

#预测学生学习偏好值
def preferences(job_finish, bbs_log, stat_work):
    return 0.95238*job_finish + 0.9764*bbs_log + 0.9449*stat_work


#预测学生学习效果值
def effect(exam_score, final_score):
    return 1.0339 * exam_score + 2.1579 * final_score