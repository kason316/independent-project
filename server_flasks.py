from flask import Flask, request, jsonify, render_template
from 浏览器维吉尼亚.cipher_clean import vigenere_encrypt_function, vigenere_decrypt_function

app = Flask(__name__)

@app.route('/')   #装饰器，“装饰”下面的函数，它的作用是告诉 Flask 框架：
#“当用户访问根路径 / 时，请调用下面这个 home() 函数。”
def home():
    return render_template('index.html')

# 定义加密API（应用程序接口）
@app.route('/encrypt', methods=['POST'])#当用户访问/encrypt路径时，执行encrypt_api()函数
def encrypt_api():  # 🎯 路由函数：处理HTTP请求
    data = request.json
    plaintext = data['text']
    key = data['key']
    ciphertext = vigenere_encrypt_function(plaintext, key)
    return jsonify({"密文": ciphertext})#把python字典转换成JSON格式返回给前端，前端javascript就能直接data.密文获取结果

# 添加解密API
@app.route('/decrypt', methods=['POST'])#指定只接受POST请求
def decrypt_api():  # 🎯 路由函数：处理HTTP请求
    data = request.json#request.json获取前端数据
    ciphertext = data['text']#像字典一样用data.密文取值
    key = data['key']
    plaintext = vigenere_decrypt_function(ciphertext, key)
    return jsonify({"明文": plaintext})

@app.route('/test')
def test():
    result = vigenere_encrypt_function("HELLO", "KEY")
    return f"算法测试: HELLO + KEY = {result}"

if __name__ == "__main__":
        app.run(debug=False, host='0.0.0.0', port=5000)

#代码执行流程：用户点击按钮→前端发送POST请求→FLASK路由接收→调用加密函数→返回JSON结果→前端显示结果