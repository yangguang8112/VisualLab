# VisualLab
### 依赖
```shell
pip install flask
pip install sqlalchemy
pip install pymysql
```
使用mysql数据库，本地调试建议构建一个本地mysql数据库，不建议直接在阿里云上的MySQL直接调试
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


展示的内容

如何展示

=========

生产监控

仪器，仪器性能，仪器使用率2

累计生产，柱状图，按机器分颜色，加平均值辅助线，理想状态下产能辅助线

=========

质量控制

一段时间内质量统计
