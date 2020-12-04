from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from mainpage.db import get_db
from mainpage.database import db_session
from mainpage.models import Sample, Machine, RawData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from mainpage.config import MYSQLconfig

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
    engine = create_engine(MYSQLconfig,echo=True)
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
            makeload_beizhu=i["makeload_beizhu"], machine_code=i["machine_code"], lane_id=i["lane_id"], \
            seq_type=i["seq_type"], seq_operator=i["seq_operator"], seq_date=i["seq_date"], seq_beizhu=i["seq_beizhu"]))
    session.add_all(insert_data)
    session.commit()

    insert_data = []
    for i in json_data:
        res = session.query(Sample).filter(Sample.chip_name == i['chip_name'], Sample.lane_id == i['lane_id'], Sample.barcode == i['barcode']).first()
        insert_data.append(RawData(sample_id=res.id, xiaji_date=i["xiaji_date"], split_rate=i["split_rate"], esr=i["esr"], basenun_G=i["basenun_G"], \
            GC=i["GC"], Q30_read2=i["Q30_read2"], Q30_total=i["Q30_total"], Q20=i["Q20"], totalreads_M=i["totalreads_M"], Lag=i["Lag"], \
            Runon=i["Runon"], cycle_N_max=i["cycle_N_max"], Error_rate_est=i["Error_rate_est"], ChipProductivity=i["ChipProductivity"], \
            ImageAre=i["ImageAre"], MaxOffsetX_MaxOffsetY=i["MaxOffsetX_MaxOffsetY"], InitialOffsetX_InitialOffsetY=i["InitialOffsetX_InitialOffsetY"], \
            RecoverValue_A_G_T_C_AVG=i["RecoverValue_A_G_T_C_AVG"], Intensity_of_All_DNB=i["Intensity_of_All_DNB"], RHO_Intensity=i["RHO_Intensity"], \
            Background_Intensity=i["Background_Intensity"], SNR=i["SNR"], BIC=i["BIC"], FIT=i["FIT"]))
    session.add_all(insert_data)
    session.commit()
    session.close()
