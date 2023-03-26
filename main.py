import pickle
import numpy as np
import numpy as np
from flask import Flask, request

app = Flask(__name__)
# 从文件中加载模型
with open('rf_model.pkl', 'rb') as f:
    clf_rf_loaded = pickle.load(f)
@app.route('/predict', methods=['POST'])
def controller():
    #获取请求体中的参数
    data = request.json
    #将字典转换为数组
    param = np.array(list(data.values())).reshape(1, -1)
    # 进行预测
    return str(clf_rf_loaded.predict(param)[0])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)


