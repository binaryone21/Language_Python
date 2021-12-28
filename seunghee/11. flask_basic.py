from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello() :
    return "<h1>Hello World!</h1>"


# https://blog.naver.com/PostView.nhn?blogId=ysc89&logNo=221850770046&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView