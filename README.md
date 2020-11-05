# VisualLab
### 依赖
```shell
pip install flask
```
### 初始化
进入项目目录
``` bash
cd VisualLab
export FLASK_APP=mainpage
export FLASK_ENV=development
flask init-db
```
### 数据库
schema.sql是生成数据库表的脚本，修改此脚本可以修改表结构
gener_tool_data.sql是插入tool data的sql脚本，可以通过修改auto_db.py来修改生成此脚本
### 运行
``` shell
flask run
```
```
 * Serving Flask app "mainpage" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 194-248-006
```
### 开发

在mainp.py中补充sql语句获取需要的数据，以json格式传给posts

前端页面为templates/index.html 遵循jinja2的传参规则，这部分主要修改js