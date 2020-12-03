from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from mainpage.db import get_db
from mainpage.database import db_session
from mainpage.models import Sample, Machine, RawData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

bp = Blueprint('mainp', __name__)


@bp.route('/')
def index():
    '''
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    '''
    posts=None
    return render_template('index.html', posts=posts)

@bp.route('/ztron_upload', methods=['POST'])
def ztron_upload():
    data = request.json
    #print(data)
    ztron_insert(data)
    return "OK"



def ztron_insert(json_data):
    engine = create_engine("mysql+pymysql://root:2020@localhost:3306/test",echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    insert_data = []
    for i in json_data:
        #insert_data.append(RawData(sample_id=i['sample_id']))
        # 检查重复
        dup = session.query(Sample).filter(Sample.chip_name == i['chip_name'], Sample.lane_id == i['lane_id'], Sample.barcode == i['barcode']).first()
        if dup:
            # 增加log模块
            print("dup!!!!!!!!!!!!!")
            continue

        # 准备数据
        insert_data.append(Sample(sample_origin_code=i["sample_origin_code"], sample_dr_count=i["sample_dr_count"], \
            sample_origin_conc=i["sample_origin_conc"], zhijian_ban_code=i["zhijian_ban_code"], \
            zhijian_kongwei=i["zhijian_kongwei"], library_kit_code=i["library_kit_code"], \
            library_ban_code=i["library_ban_code"], library_kongwei=i["library_kongwei"], \
            library_name=i["library_name"], barcode=i["barcode"], adapter_conc=i["adapter_conc"], \
            library_conc=i["library_conc"], library_vol=i["library_vol"], \
            out_library_date=i["out_library_date"], jianku_beizhu=i["jianku_beizhu"], \
            shangji_kit_code=i["shangji_kit_code"], DNB_dr_count=i["DNB_dr_count"], \
            DNB_name=i["DNB_name"], DNB_conc=i["DNB_conc"], chip_name=i["chip_name"], \
            makeload_operator=i["makeload_operator"], makeload_date=i["makeload_date"], \
            makeload_beizhu=i["makeload_beizhu"], machine_id=i["machine_id"], lane_id=i["lane_id"], \
            seq_type=i["seq_type"], seq_operator=i["seq_operator"], seq_date=i["seq_date"], seq_beizhu=i["seq_beizhu"]))
    session.add_all(insert_data)
    session.commit()
    session.close()
