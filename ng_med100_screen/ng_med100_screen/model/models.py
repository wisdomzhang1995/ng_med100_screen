# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime

from django.conf import settings
from django.db import models
from django.db.models import Count

from frame.tools.public_function import format_time
from model.base import BaseModel
from django.utils import timezone


class Slides(BaseModel):
    remark = models.TextField(db_collation='utf8mb3_general_ci', blank=True, null=True)
    scantime = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    barcode = models.TextField(blank=True, null=True)
    slideno = models.TextField(blank=True, null=True)
    size = models.BigIntegerField(blank=True, null=True)
    slidepath = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    appid = models.CharField(db_column='APPID', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slides'


class TAccount(BaseModel):
    account_id = models.AutoField(primary_key=True)
    center = models.ForeignKey('TCenter', models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey('TSite', models.DO_NOTHING, blank=True, null=True)
    original_site_id = models.IntegerField(blank=True, null=True)
    account_phone = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=200, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    group = models.IntegerField(blank=True, null=True)
    head_image = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    web_user_name = models.CharField(max_length=30, blank=True, null=True)
    invite_code = models.IntegerField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    signature = models.IntegerField(blank=True, null=True)
    is_disabled = models.IntegerField(blank=True, null=True)
    enterprice_wechat_user_id = models.CharField(max_length=50, blank=True, null=True)
    is_lock = models.IntegerField(blank=True, null=True)
    password_update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account'


class TAccountActionLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_action_log'


class TAccountAddress(BaseModel):
    address_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(TAccount, models.DO_NOTHING, blank=True, null=True)
    user_phone = models.CharField(max_length=20, blank=True, null=True)
    user_name = models.CharField(max_length=20, blank=True, null=True)
    user_address = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_address'


class TAccountAuth(BaseModel):
    auth_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    idno = models.CharField(max_length=20, blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_expert = models.IntegerField(blank=True, null=True)
    account_type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    audit_time = models.DateTimeField(blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_auth'


class TAccountAuthCallbackLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField(blank=True, null=True)
    auth_openid = models.CharField(max_length=100, blank=True, null=True)
    account_phone = models.CharField(max_length=20, blank=True, null=True)
    process = models.IntegerField(blank=True, null=True)
    opt_time = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    stamp = models.TextField(blank=True, null=True)
    stamp_status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_auth_callback_log'


class TAccountAuthImg(BaseModel):
    auth = models.ForeignKey(TAccountAuth, models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_auth_img'


class TAccountExpert(BaseModel):
    account = models.OneToOneField(TAccount, models.DO_NOTHING, primary_key=True)
    expert_title = models.CharField(max_length=20, blank=True, null=True)
    signature = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    site_doctor_type = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    is_top = models.IntegerField(blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    site_receipt_limit = models.IntegerField(blank=True, null=True)
    auth_doctor_id = models.CharField(max_length=100, blank=True, null=True)
    auth_idcard = models.CharField(max_length=100, blank=True, null=True)
    auth_openid = models.CharField(max_length=100, blank=True, null=True)
    auth_status = models.IntegerField(blank=True, null=True)
    is_use_auth = models.IntegerField(blank=True, null=True)
    auth_doctor_id_res = models.IntegerField(blank=True, null=True)
    auth_idcard_res1 = models.IntegerField(blank=True, null=True)
    auth_idcard_res2 = models.IntegerField(blank=True, null=True)
    auth_zhiye_id = models.CharField(max_length=100, blank=True, null=True)
    auth_zhiye_id_res = models.IntegerField(blank=True, null=True)
    auth_bankno = models.CharField(max_length=100, blank=True, null=True)
    auth_opening_bank = models.CharField(max_length=100, blank=True, null=True)
    auth_contract_expire_date = models.DateField(blank=True, null=True)
    auth_insurance_no = models.CharField(max_length=100, blank=True, null=True)
    auth_insurance_expire_date = models.DateField(blank=True, null=True)
    auth_title_id_res = models.IntegerField(blank=True, null=True)
    receive_order_count_general = models.IntegerField(blank=True, null=True)
    receive_order_count_cells = models.IntegerField(blank=True, null=True)
    receive_order_status = models.IntegerField(blank=True, null=True)
    is_ai = models.IntegerField(blank=True, null=True)
    auth_doctor_res_id = models.CharField(max_length=200, blank=True, null=True)
    auth_zhiye_res_id = models.CharField(max_length=200, blank=True, null=True)
    is_view_all_case = models.IntegerField(blank=True, null=True)
    score = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_expert'


class TAccountExpertContract(BaseModel):
    expert_contract_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    contract_file = models.IntegerField(blank=True, null=True)
    is_sign = models.IntegerField(blank=True, null=True)
    sign_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_expert_contract'


class TAccountExpertSpec(BaseModel):
    account = models.ForeignKey(TAccountExpert, models.DO_NOTHING, blank=True, null=True)
    spec = models.ForeignKey('TDictSpec', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_expert_spec'


class TAccountFollow(BaseModel):
    account_id = models.IntegerField(blank=True, null=True)
    follow_account_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_follow'


class TAccountLoginLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(TAccount, models.DO_NOTHING, blank=True, null=True)
    login_city = models.CharField(max_length=30, blank=True, null=True)
    login_time = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    login_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_login_log'


class TAccountMoney(BaseModel):
    account_id = models.IntegerField(primary_key=True)
    money = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_forzen = models.IntegerField(blank=True, null=True)
    security_code = models.CharField(max_length=10, blank=True, null=True)
    alipay_account = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_money'


class TAccountMoneyLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(TAccountMoney, models.DO_NOTHING, blank=True, null=True)
    change_money = models.FloatField(blank=True, null=True)
    cur_money = models.FloatField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    log_type = models.IntegerField(blank=True, null=True)
    alipay_account = models.CharField(max_length=100, blank=True, null=True)
    alipay_username = models.CharField(max_length=100, blank=True, null=True)
    log_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_money_log'


class TAccountPerformanceReport(BaseModel):
    account_performance_report_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    pdf_url = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_performance_report'


class TAccountPwderror(BaseModel):
    account_phone = models.CharField(max_length=20, blank=True, null=True)
    error_pwd = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    ipaddress = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_pwderror'


class TAccountRebate(BaseModel):
    rebate_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField(blank=True, null=True)
    extend_id = models.IntegerField(blank=True, null=True)
    extend_type = models.IntegerField(blank=True, null=True)
    is_pay = models.IntegerField(blank=True, null=True)
    suggest_price = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    post = models.ForeignKey('TPost', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_rebate'


class TAccountReleExpert(BaseModel):
    account = models.ForeignKey(TAccount, models.DO_NOTHING, blank=True, null=True)
    expert_account_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_rele_expert'


class TAccountRole(BaseModel):
    account_role_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(TAccount, models.DO_NOTHING, blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_audit_self = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_role'


class TAccountSearch(BaseModel):
    search_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField(blank=True, null=True)
    search_name = models.CharField(max_length=100, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_search'


class TAccountSearchField(BaseModel):
    search_field_id = models.AutoField(primary_key=True)
    search_id = models.IntegerField(blank=True, null=True)
    field_source = models.IntegerField(blank=True, null=True)
    field_name = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_search_field'


class TAccountSite(BaseModel):
    account = models.ForeignKey(TAccount, models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey('TSite', models.DO_NOTHING, blank=True, null=True)
    is_get_msg = models.IntegerField(blank=True, null=True)
    is_get_frozen = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_site'


class TAccountSpec(BaseModel):
    account_id = models.IntegerField(primary_key=True)
    role_id = models.IntegerField()
    spec_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_account_spec'
        unique_together = (('account_id', 'role_id', 'spec_id'),)


class TAccountToken(BaseModel):
    account = models.OneToOneField(TAccount, models.DO_NOTHING, primary_key=True)
    token = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_token'


class TAccountVercode(BaseModel):
    code_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    is_used = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_account_vercode'


class TAdvice(BaseModel):
    advice_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    pathology_no = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    apply_no = models.CharField(max_length=50, blank=True, null=True)
    info_patient_sex = models.IntegerField(blank=True, null=True)
    info_patient_age = models.IntegerField(blank=True, null=True)
    info_patient_age_unit = models.IntegerField(blank=True, null=True)
    info_pre_diagnosis = models.TextField(blank=True, null=True)
    express_name = models.CharField(max_length=20, blank=True, null=True)
    express_no = models.CharField(max_length=100, blank=True, null=True)
    sample_name = models.CharField(max_length=30, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    agreement_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_advice'


class TAdviceSample(BaseModel):
    advice_sample_id = models.AutoField(primary_key=True)
    advice_id = models.IntegerField(blank=True, null=True)
    sample_name = models.CharField(max_length=100, blank=True, null=True)
    sample_desc = models.CharField(max_length=100, blank=True, null=True)
    sample_id = models.IntegerField(blank=True, null=True)
    sample_position = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_advice_sample'


class TAdviceStatusLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    advice = models.ForeignKey(TAdvice, models.DO_NOTHING, blank=True, null=True)
    pre_status = models.IntegerField(blank=True, null=True)
    cur_status = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    action = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_advice_status_log'


class TAdviceTotal(BaseModel):
    advice = models.OneToOneField(TAdvice, models.DO_NOTHING, primary_key=True)
    submit_time = models.DateTimeField(blank=True, null=True)
    submit_account = models.IntegerField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    send_account = models.IntegerField(blank=True, null=True)
    receive_time = models.DateTimeField(blank=True, null=True)
    receive_account = models.IntegerField(blank=True, null=True)
    cancel_time = models.DateTimeField(blank=True, null=True)
    cancel_account = models.IntegerField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    finish_account = models.IntegerField(blank=True, null=True)
    people_pay_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_advice_total'


class TAdviceWaxblock(BaseModel):
    waxblock_id = models.AutoField(primary_key=True)
    advice = models.ForeignKey(TAdvice, models.DO_NOTHING, blank=True, null=True)
    waxblock_no = models.CharField(max_length=100, blank=True, null=True)
    advice_sample = models.ForeignKey(TAdviceSample, models.DO_NOTHING, blank=True, null=True)
    waxblock_name = models.CharField(max_length=100, blank=True, null=True)
    get_part = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=100, blank=True, null=True)
    material_count = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_advice_waxblock'


class TAdviceWaxblockItem(BaseModel):
    waxblock_item_id = models.AutoField(primary_key=True)
    waxblock = models.ForeignKey(TAdviceWaxblock, models.DO_NOTHING, blank=True, null=True)
    ihc_id = models.IntegerField(blank=True, null=True)
    dye = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    test_no = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_advice_waxblock_item'


class TAdviceWaxblockSlide(BaseModel):
    slide_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    waxblock_item = models.ForeignKey(TAdviceWaxblockItem, models.DO_NOTHING, blank=True, null=True)
    is_bind = models.IntegerField(blank=True, null=True)
    bind_time = models.DateTimeField(blank=True, null=True)
    bind_account_id = models.IntegerField(blank=True, null=True)
    is_upload = models.IntegerField(blank=True, null=True)
    upload_time = models.DateTimeField(blank=True, null=True)
    oss_url = models.CharField(max_length=100, blank=True, null=True)
    local_url = models.CharField(max_length=100, blank=True, null=True)
    file_name = models.CharField(max_length=200, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    slide_memo = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    scan_time = models.DateTimeField(blank=True, null=True)
    slide_label = models.IntegerField(blank=True, null=True)
    slide_preview = models.IntegerField(blank=True, null=True)
    mini_oss_url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_advice_waxblock_slide'


class TAliyunPhone(BaseModel):
    aliyun_phone_id = models.AutoField(primary_key=True)
    subs_id = models.CharField(max_length=100, blank=True, null=True)
    phone_no_a = models.CharField(max_length=20, blank=True, null=True)
    phone_no_x = models.CharField(max_length=20, blank=True, null=True)
    phone_no_b = models.CharField(max_length=20, blank=True, null=True)
    pool_key = models.CharField(max_length=50, blank=True, null=True)
    expiration = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_aliyun_phone'


class TAntibody(BaseModel):
    antibody_id = models.AutoField(primary_key=True)
    antibody_name = models.CharField(max_length=50, blank=True, null=True)
    other_name = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    expression = models.TextField(blank=True, null=True)
    positive = models.CharField(max_length=100, blank=True, null=True)
    utility = models.TextField(blank=True, null=True)
    create_user_name = models.CharField(max_length=20, blank=True, null=True)
    read_count = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_antibody'


class TArchiveCase(BaseModel):
    archive_case_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    case = models.ForeignKey('TCase', models.DO_NOTHING, blank=True, null=True)
    system_id = models.IntegerField(blank=True, null=True)
    organ_id = models.IntegerField(blank=True, null=True)
    lab_category = models.IntegerField(blank=True, null=True)
    diagnose_assess = models.IntegerField(blank=True, null=True)
    diagnose_assess_score = models.FloatField(blank=True, null=True)
    diagnose_assess_memo = models.CharField(max_length=200, blank=True, null=True)
    expert_account_id = models.IntegerField(blank=True, null=True)
    is_import_lab = models.IntegerField(blank=True, null=True)
    disease_type = models.IntegerField(blank=True, null=True)
    icd10_code = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_archive_case'


class TArchiveCaseTemp(BaseModel):
    case = models.OneToOneField('TCase', models.DO_NOTHING, primary_key=True)
    diagnose_assess = models.IntegerField(blank=True, null=True)
    diagnose_assess_score = models.FloatField(blank=True, null=True)
    diagnose_assess_memo = models.TextField(blank=True, null=True)
    expert_account_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_archive_case_temp'


class TArchiveIcd10(BaseModel):
    icd10_code = models.CharField(max_length=50, blank=True, null=True)
    icd10_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_archive_icd10'


class TArchiveScoreitem(BaseModel):
    scoreitem_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=20, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    slide_type = models.IntegerField(blank=True, null=True)
    total_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_archive_scoreitem'


class TArchiveSlide(BaseModel):
    archive_slide_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    slide_source = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    total_score = models.FloatField(blank=True, null=True)
    oas_url = models.CharField(max_length=100, blank=True, null=True)
    slide_status = models.IntegerField(blank=True, null=True)
    oas_archive_id = models.CharField(max_length=200, blank=True, null=True)
    callback_code = models.CharField(max_length=200, blank=True, null=True)
    is_ignore = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_archive_slide'


class TArchiveSlideScore(BaseModel):
    scoreitem = models.ForeignKey(TArchiveScoreitem, models.DO_NOTHING, blank=True, null=True)
    archive_slide = models.ForeignKey(TArchiveSlide, models.DO_NOTHING, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_archive_slide_score'


class TBacklogTask(BaseModel):
    site_id = models.IntegerField(blank=True, null=True)
    advance_site_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    task_type = models.IntegerField(blank=True, null=True)
    extend_id = models.IntegerField(blank=True, null=True)
    task_count = models.IntegerField(blank=True, null=True)
    is_finish = models.IntegerField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    finish_account_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_backlog_task'


class TBusinessTitle(BaseModel):
    business_title_id = models.AutoField(primary_key=True)
    business_title_name = models.CharField(max_length=20, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_business_title'


class TBusinessUser(BaseModel):
    business_user_id = models.AutoField(primary_key=True)
    business_title_id = models.IntegerField(blank=True, null=True)
    parent_business_user_id = models.IntegerField(blank=True, null=True)
    user_phone = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    head_image = models.IntegerField(blank=True, null=True)
    user_role_id = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_business_user'


class TBusinessUserArea(BaseModel):
    business_user_area_id = models.AutoField(primary_key=True)
    province_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    business_user_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_business_user_area'


class TCase(BaseModel):
    case_id = models.AutoField(primary_key=True)
    site = models.ForeignKey('TSite', models.DO_NOTHING, blank=True, null=True)
    system_no = models.CharField(max_length=100, blank=True, null=True)
    case_type = models.IntegerField(blank=True, null=True)
    pathology_no = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    business_type = models.ForeignKey('TMoneyBusinessType', models.DO_NOTHING, blank=True, null=True)
    can_edit = models.IntegerField(blank=True, null=True)
    consult_type = models.IntegerField(blank=True, null=True)
    case_advance_site_id = models.IntegerField(blank=True, null=True)
    apply_no = models.CharField(max_length=50, blank=True, null=True)
    frozen_type = models.IntegerField(blank=True, null=True)
    frozen_case_id = models.IntegerField(blank=True, null=True)
    frozen_prebook_no = models.IntegerField(blank=True, null=True)
    frozen_prebook_place = models.CharField(max_length=20, blank=True, null=True)
    frozen_prebook_date = models.DateTimeField(blank=True, null=True)
    frozen_prebook_type = models.IntegerField(blank=True, null=True)
    frozen_apply_date = models.DateTimeField(blank=True, null=True)
    frozen_apply_doctor = models.CharField(max_length=20, blank=True, null=True)
    frozen_apply_doctor_phone = models.CharField(max_length=20, blank=True, null=True)
    lab_inspect = models.TextField(blank=True, null=True)
    lab_inspect_options = models.TextField(blank=True, null=True)
    consultation_slide_count = models.IntegerField(blank=True, null=True)
    consultation_block_count = models.IntegerField(blank=True, null=True)
    consultation_orign_hospital = models.CharField(max_length=100, blank=True, null=True)
    consultation_pathology_no = models.CharField(max_length=100, blank=True, null=True)
    info_patient_is_menopause = models.IntegerField(blank=True, null=True)
    info_patient_name = models.CharField(max_length=200, blank=True, null=True)
    info_patient_sex = models.IntegerField(blank=True, null=True)
    info_patient_age = models.IntegerField(blank=True, null=True)
    info_patient_age_unit = models.IntegerField(blank=True, null=True)
    info_patient_id = models.CharField(max_length=100, blank=True, null=True)
    info_patient_job = models.CharField(max_length=20, blank=True, null=True)
    info_patient_addr = models.CharField(max_length=500, blank=True, null=True)
    info_patient_phone = models.CharField(max_length=100, blank=True, null=True)
    info_patient_menstruation = models.DateTimeField(blank=True, null=True)
    info_patient_nation = models.CharField(max_length=50, blank=True, null=True)
    info_patient_nation_place = models.CharField(max_length=20, blank=True, null=True)
    info_patient_is_married = models.IntegerField(blank=True, null=True)
    info_patient_area = models.CharField(max_length=20, blank=True, null=True)
    info_diagnosis_type = models.IntegerField(blank=True, null=True)
    info_diagnosis_no = models.CharField(max_length=50, blank=True, null=True)
    info_bed_no = models.CharField(max_length=50, blank=True, null=True)
    info_cost_type = models.IntegerField(blank=True, null=True)
    info_cost = models.FloatField(blank=True, null=True)
    info_clinical_diagnosis = models.TextField(blank=True, null=True)
    info_history = models.TextField(blank=True, null=True)
    info_surgery_see = models.TextField(blank=True, null=True)
    info_original_diagnosis = models.TextField(blank=True, null=True)
    info_pre_diagnosis = models.TextField(blank=True, null=True)
    sample_fixed_time = models.DateTimeField(blank=True, null=True)
    sample_vitro_time = models.DateTimeField(blank=True, null=True)
    sample_take_place = models.CharField(max_length=20, blank=True, null=True)
    sample_count = models.IntegerField(blank=True, null=True)
    sample_doctor = models.CharField(max_length=20, blank=True, null=True)
    sample_get_doctor = models.CharField(max_length=20, blank=True, null=True)
    sample_get_date = models.DateTimeField(blank=True, null=True)
    sample_send_doctor = models.CharField(max_length=20, blank=True, null=True)
    sample_send_doctor_phone = models.CharField(max_length=20, blank=True, null=True)
    sample_send_hos = models.CharField(max_length=30, blank=True, null=True)
    sample_send_dept = models.CharField(max_length=30, blank=True, null=True)
    sample_send_date = models.DateTimeField(blank=True, null=True)
    sample_type = models.IntegerField(blank=True, null=True)
    sample_fixed = models.IntegerField(blank=True, null=True)
    sample_collect_time = models.DateTimeField(blank=True, null=True)
    sample_collect_see = models.TextField(blank=True, null=True)
    sample_send_purpose = models.CharField(max_length=30, blank=True, null=True)
    express_name = models.CharField(max_length=20, blank=True, null=True)
    express_no = models.CharField(max_length=100, blank=True, null=True)
    express_time = models.DateTimeField(blank=True, null=True)
    express_phone = models.CharField(max_length=20, blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    submit_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    agreement_price = models.FloatField(blank=True, null=True)
    is_package = models.IntegerField(blank=True, null=True)
    sample_operator = models.CharField(max_length=20, blank=True, null=True)
    sample_time = models.DateTimeField(blank=True, null=True)
    lock_user = models.IntegerField(blank=True, null=True)
    lock_time = models.DateTimeField(blank=True, null=True)
    sample_doctor_id = models.IntegerField(blank=True, null=True)
    sample_operator_id = models.IntegerField(blank=True, null=True)
    operation_room_phone = models.CharField(max_length=20, blank=True, null=True)
    his_identification = models.CharField(db_column='his_Identification', max_length=100, blank=True, null=True)  # Field name made lowercase.
    disease_type = models.IntegerField(blank=True, null=True)
    clinical_diagnos_result = models.IntegerField(blank=True, null=True)
    sample_fixed_standard = models.IntegerField(blank=True, null=True)
    sample_fixed_reason = models.TextField(blank=True, null=True)
    sample_fixed_treatment = models.TextField(blank=True, null=True)
    borrowing_consultation_evaluation = models.IntegerField(blank=True, null=True)
    center = models.ForeignKey('TCenter', models.DO_NOTHING, blank=True, null=True)
    info_patient_company = models.CharField(max_length=50, blank=True, null=True)
    is_fast = models.IntegerField(blank=True, null=True)
    bv_status = models.IntegerField(blank=True, null=True)
    info_patient_name_s = models.TextField(blank=True, null=True)
    disease_id = models.IntegerField(blank=True, null=True)
    origin_case_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case'

    @classmethod
    def get_realtime_queryset(cls):
        if settings.DEBUG:
            return cls.search()
        start_time = timezone.now()
        print("QWWWWWWWWWWWWWWWWWWWWWW", start_time)
        end_time = start_time - datetime.timedelta(days=2)
        return cls.search(create_time__gte=format_time(start_time), create_time__lte=format_time(end_time))


class TCaseAdvice(BaseModel):
    advice_id = models.AutoField(primary_key=True)
    slide = models.ForeignKey('TCaseSlide', models.DO_NOTHING, blank=True, null=True)
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    msg_type = models.IntegerField(blank=True, null=True)
    waxblock_id = models.IntegerField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    execute_time = models.DateTimeField(blank=True, null=True)
    execute_account_id = models.IntegerField(blank=True, null=True)
    advice_submit_time = models.DateTimeField(blank=True, null=True)
    charge_time = models.DateTimeField(blank=True, null=True)
    advance_site_id = models.IntegerField(blank=True, null=True)
    advance_site_receive_time = models.DateTimeField(blank=True, null=True)
    advance_site_charge_time = models.DateTimeField(blank=True, null=True)
    case_report_time = models.DateTimeField(blank=True, null=True)
    make_type = models.IntegerField(blank=True, null=True)
    ihc = models.ForeignKey('TDictIhcItem', models.DO_NOTHING, blank=True, null=True)
    dye = models.IntegerField(blank=True, null=True)
    molecule = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    advice_business_type = models.IntegerField(blank=True, null=True)
    advice_result = models.CharField(max_length=20, blank=True, null=True)
    advice_source = models.IntegerField(blank=True, null=True)
    test_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_advice'


class TCaseAttachment(BaseModel):
    attachment_id = models.AutoField(primary_key=True)
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    memo = models.CharField(max_length=100, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    is_for_report = models.IntegerField(blank=True, null=True)
    case_sample = models.ForeignKey('TCaseSample', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_attachment'


class TCaseBorrow(BaseModel):
    case_borrow_id = models.AutoField(primary_key=True)
    case_id = models.IntegerField(blank=True, null=True)
    borrow_waxblock_id_str = models.CharField(max_length=200, blank=True, null=True)
    borrow_slide_id_str = models.CharField(max_length=200, blank=True, null=True)
    borrow_time = models.DateTimeField(blank=True, null=True)
    back_time = models.DateTimeField(blank=True, null=True)
    borrow_user_name = models.CharField(max_length=50, blank=True, null=True)
    borrow_phone = models.CharField(max_length=20, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_borrow'


class TCaseCa(BaseModel):
    case_id = models.IntegerField(primary_key=True)
    ca_status = models.IntegerField(blank=True, null=True)
    status_update_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca'


class TCaseCaJob(BaseModel):
    ca_job_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    ca_job_title = models.CharField(max_length=100, blank=True, null=True)
    ca_type = models.IntegerField(blank=True, null=True)
    case_type = models.IntegerField(blank=True, null=True)
    check_account_id = models.IntegerField(blank=True, null=True)
    check_ratio = models.FloatField(blank=True, null=True)
    job_no = models.CharField(max_length=10, blank=True, null=True)
    job_status = models.IntegerField(blank=True, null=True)
    total_count = models.IntegerField(blank=True, null=True)
    done_count = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    search_type = models.CharField(max_length=20, blank=True, null=True)
    spec_id = models.IntegerField(blank=True, null=True)
    sample_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_job'


class TCaseCaJobItem(BaseModel):
    ca_type = models.IntegerField(primary_key=True)
    extend_id = models.IntegerField()
    ca_job_id = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_job_item'
        unique_together = (('ca_type', 'extend_id'),)


class TCaseCaLine(BaseModel):
    case_ca_line_id = models.AutoField(primary_key=True)
    case_ca_line_status = models.IntegerField(blank=True, null=True)
    case_ca_line_status_update_time = models.DateTimeField(blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    is_excess_process = models.IntegerField(blank=True, null=True)
    consultation_post_time = models.DateTimeField(blank=True, null=True)
    consultation_post_detail = models.CharField(max_length=200, blank=True, null=True)
    consultation_express_no = models.CharField(max_length=200, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    case_ca_line_index = models.IntegerField(blank=True, null=True)
    improved_memo = models.CharField(max_length=200, blank=True, null=True)
    reject_memo_qucai_dengji = models.CharField(max_length=200, blank=True, null=True)
    reject_memo_regist = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_line'


class TCaseCaLineStatusLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    case_ca_line_id = models.IntegerField(blank=True, null=True)
    pre_status = models.IntegerField(blank=True, null=True)
    cur_status = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    extend_id = models.IntegerField(blank=True, null=True)
    log_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_line_status_log'


class TCaseCaRecord(BaseModel):
    case_ca_record_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    pdf_file = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_record'


class TCaseCaSample(BaseModel):
    case_sample_id = models.IntegerField(primary_key=True)
    case_ca_line_id = models.IntegerField(blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    case_sample_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_sample'


class TCaseCaScore(BaseModel):
    case_id = models.IntegerField(primary_key=True)
    case_creator_score = models.IntegerField(blank=True, null=True)
    case_creator_time = models.DateTimeField(blank=True, null=True)
    case_creator_score_user = models.IntegerField(blank=True, null=True)
    sample_operator = models.CharField(max_length=20, blank=True, null=True)
    sample_operator_score = models.IntegerField(blank=True, null=True)
    sample_operator_time = models.DateTimeField(blank=True, null=True)
    sample_operator_score_user = models.IntegerField(blank=True, null=True)
    sample_doctor = models.CharField(max_length=20, blank=True, null=True)
    sample_doctor_score = models.IntegerField(blank=True, null=True)
    sample_doctor_time = models.DateTimeField(blank=True, null=True)
    sample_doctor_score_user = models.IntegerField(blank=True, null=True)
    sample_operator_memo = models.CharField(max_length=100, blank=True, null=True)
    sample_doctor_memo = models.CharField(max_length=100, blank=True, null=True)
    case_creator_memo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_score'


class TCaseCaScoreReport(BaseModel):
    report_id = models.IntegerField(primary_key=True)
    case_id = models.IntegerField(blank=True, null=True)
    report_score = models.IntegerField(blank=True, null=True)
    report_score_user = models.IntegerField(blank=True, null=True)
    report_score_time = models.DateTimeField(blank=True, null=True)
    report_score_memo = models.CharField(max_length=100, blank=True, null=True)
    is_positive = models.IntegerField(blank=True, null=True)
    positive_type = models.IntegerField(blank=True, null=True)
    diagnosis_accurate = models.IntegerField(blank=True, null=True)
    diagnosis_accurate_time = models.DateTimeField(blank=True, null=True)
    diagnosis_accurate_user = models.IntegerField(blank=True, null=True)
    diagnosis_accurate_memo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_score_report'


class TCaseCaScoreSlide(BaseModel):
    slide_id = models.IntegerField(primary_key=True)
    case_id = models.IntegerField(blank=True, null=True)
    make_score = models.IntegerField(blank=True, null=True)
    make_score_time = models.DateTimeField(blank=True, null=True)
    make_score_user = models.IntegerField(blank=True, null=True)
    make_score_memo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_score_slide'


class TCaseCaScoreWaxblock(BaseModel):
    waxblock_id = models.IntegerField(primary_key=True)
    case_id = models.IntegerField(blank=True, null=True)
    embed_score = models.IntegerField(blank=True, null=True)
    embed_score_user = models.IntegerField(blank=True, null=True)
    embed_score_time = models.DateTimeField(blank=True, null=True)
    embed_score_memo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_score_waxblock'


class TCaseCaSlide(BaseModel):
    slide = models.OneToOneField('TCaseSlide', models.DO_NOTHING, primary_key=True)
    waxblock = models.ForeignKey('TCaseCaWaxblock', models.DO_NOTHING, blank=True, null=True)
    case = models.ForeignKey(TCaseCa, models.DO_NOTHING, blank=True, null=True)
    case_ca_line = models.ForeignKey(TCaseCaLine, models.DO_NOTHING, blank=True, null=True)
    case_slide_status = models.IntegerField(blank=True, null=True)
    case_sample_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_slide'


class TCaseCaStatusTime(BaseModel):
    case_ca_line_id = models.IntegerField()
    case_ca_line_status = models.IntegerField(primary_key=True)
    log_id = models.IntegerField(blank=True, null=True)
    status_change_time = models.DateTimeField(blank=True, null=True)
    receive_account_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_status_time'
        unique_together = (('case_ca_line_status', 'case_ca_line_id'),)


class TCaseCaStorage(BaseModel):
    case_ca_line_id = models.IntegerField()
    storage_cate = models.IntegerField(primary_key=True)
    storage_time = models.DateTimeField(blank=True, null=True)
    storage_pos = models.CharField(max_length=100, blank=True, null=True)
    expire_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_storage'
        unique_together = (('storage_cate', 'case_ca_line_id'),)


class TCaseCaSummary(BaseModel):
    summary_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    summary_time = models.CharField(max_length=20, blank=True, null=True)
    summary_type = models.IntegerField(blank=True, null=True)
    problem = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    improvement = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_summary'


class TCaseCaTask(BaseModel):
    case_ca_task_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    task_no = models.IntegerField(blank=True, null=True)
    task_item_type = models.IntegerField(blank=True, null=True)
    task_status = models.IntegerField(blank=True, null=True)
    task_action = models.IntegerField(blank=True, null=True)
    case_type = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    receive_account = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_task'


class TCaseCaTaskItem(BaseModel):
    ca_task_item_id = models.AutoField(primary_key=True)
    case_ca_task_id = models.IntegerField(blank=True, null=True)
    extend_id = models.IntegerField(blank=True, null=True)
    task_item_err_status = models.IntegerField(blank=True, null=True)
    case_ca_line_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_task_item'


class TCaseCaTaskStatusTime(BaseModel):
    case_ca_task_id = models.IntegerField(primary_key=True)
    task_status = models.IntegerField()
    log_id = models.IntegerField(blank=True, null=True)
    status_change_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_task_status_time'
        unique_together = (('case_ca_task_id', 'task_status'),)


class TCaseCaTuoshuiGroup(BaseModel):
    case_ca_tuoshui_group_id = models.AutoField(primary_key=True)
    lab_device_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    err_msg = models.CharField(max_length=500, blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_tuoshui_group'


class TCaseCaWaxblock(BaseModel):
    waxblock = models.OneToOneField('TCaseWaxblock', models.DO_NOTHING, primary_key=True)
    case = models.ForeignKey(TCaseCa, models.DO_NOTHING, blank=True, null=True)
    case_sample = models.ForeignKey(TCaseCaSample, models.DO_NOTHING, blank=True, null=True)
    case_ca_line_id = models.IntegerField(blank=True, null=True)
    case_waxblock_status = models.IntegerField(blank=True, null=True)
    case_ca_tuoshui_group_id = models.IntegerField(blank=True, null=True)
    dehydration_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ca_waxblock'


class TCaseChargingItem(BaseModel):
    case_charging_item_id = models.AutoField(primary_key=True)
    charging_item_id = models.IntegerField(blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_charging_item'


class TCaseComment(BaseModel):
    comment_id = models.AutoField(primary_key=True)
    type = models.IntegerField(blank=True, null=True)
    extend_id = models.IntegerField(blank=True, null=True)
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_comment'


class TCaseCommentImg(BaseModel):
    img_id = models.AutoField(primary_key=True)
    res_id = models.IntegerField(blank=True, null=True)
    comment = models.ForeignKey(TCaseComment, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_comment_img'


class TCaseDelay(BaseModel):
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    notice_content = models.TextField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    is_printed = models.IntegerField(blank=True, null=True)
    print_time = models.DateTimeField(blank=True, null=True)
    print_account_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_delay'


class TCaseDeptDiagnosis(BaseModel):
    dept_diagnosis_id = models.AutoField(primary_key=True)
    case_id = models.IntegerField(blank=True, null=True)
    expert_id = models.IntegerField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_dept_diagnosis'


class TCaseDeptDiagnosisExpert(BaseModel):
    case_id = models.IntegerField(blank=True, null=True)
    expert_id = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_dept_diagnosis_expert'


class TCaseDeptDiagnosisImg(BaseModel):
    img_id = models.AutoField(primary_key=True)
    dept_diagnosis_id = models.IntegerField(blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_dept_diagnosis_img'


class TCaseDiagnosisApply(BaseModel):
    case_diagnosis_apply_id = models.AutoField(primary_key=True)
    case_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    apply_reason = models.CharField(max_length=200, blank=True, null=True)
    apply_status = models.IntegerField(blank=True, null=True)
    apply_type = models.IntegerField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_diagnosis_apply'


class TCaseExpert(BaseModel):
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    case_status = models.IntegerField(blank=True, null=True)
    confirm_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_expert'


class TCaseFavorite(BaseModel):
    favorite_id = models.AutoField(primary_key=True)
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_favorite'


class TCaseFile(BaseModel):
    file_id = models.AutoField(primary_key=True)
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    memo = models.CharField(max_length=100, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    is_for_report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_file'


class TCaseFrozenDeviceTestLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    case_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=100, blank=True, null=True)
    test_time = models.DateTimeField(blank=True, null=True)
    device_type = models.IntegerField(blank=True, null=True)
    problem = models.TextField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_frozen_device_test_log'


class TCaseLibrary(BaseModel):
    case_library_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    library_name = models.CharField(max_length=100, blank=True, null=True)
    library_type = models.IntegerField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    is_enabled = models.IntegerField(blank=True, null=True)
    pre_str = models.CharField(max_length=10, blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_library'


class TCaseLibraryItem(BaseModel):
    case_library_id = models.IntegerField(blank=True, null=True)
    extend_id = models.IntegerField(blank=True, null=True)
    item_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_library_item'


class TCaseModify(BaseModel):
    case_modify_id = models.AutoField(primary_key=True)
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_modify'


class TCaseModifyLog(BaseModel):
    modify_log_id = models.AutoField(primary_key=True)
    case_modify = models.ForeignKey(TCaseModify, models.DO_NOTHING, blank=True, null=True)
    modify_position = models.IntegerField(blank=True, null=True)
    pre_value = models.TextField(blank=True, null=True)
    cur_value = models.TextField(blank=True, null=True)
    modify_field = models.CharField(max_length=100, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    extend_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_modify_log'


class TCasePathologyNo(BaseModel):
    site_id = models.IntegerField(blank=True, null=True)
    case_type = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    index_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_pathology_no'


class TCaseRef(BaseModel):
    ref_id = models.AutoField(primary_key=True)
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    ref_case_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    is_forzen_match = models.IntegerField(blank=True, null=True)
    forzen_match_memo = models.CharField(max_length=1000, blank=True, null=True)
    is_cell_match = models.IntegerField(blank=True, null=True)
    forzen_match_type = models.IntegerField(blank=True, null=True)
    general_result = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_ref'


class TCaseReport(BaseModel):
    report_id = models.AutoField(primary_key=True)
    report_serial_no = models.CharField(max_length=50, blank=True, null=True)
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    expert_account_id = models.IntegerField(blank=True, null=True)
    mirror_see = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    cell_memo = models.TextField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    is_valid = models.IntegerField(blank=True, null=True)
    print_count = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    audit_time = models.DateTimeField(blank=True, null=True)
    print_time = models.DateTimeField(blank=True, null=True)
    pdf_file = models.IntegerField(blank=True, null=True)
    audit_doctor = models.IntegerField(blank=True, null=True)
    pre_diagnosis = models.TextField(blank=True, null=True)
    value1 = models.TextField(blank=True, null=True)
    is_release = models.IntegerField(blank=True, null=True)
    release_account = models.IntegerField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)
    immuno_fluorescence = models.TextField(blank=True, null=True)
    electric_mirror_see = models.TextField(blank=True, null=True)
    report_type = models.IntegerField(blank=True, null=True)
    auth_status = models.IntegerField(blank=True, null=True)
    reject_time = models.DateTimeField(blank=True, null=True)
    reject_memo = models.CharField(max_length=500, blank=True, null=True)
    is_first_match = models.IntegerField(blank=True, null=True)
    is_cell_match = models.IntegerField(blank=True, null=True)
    report_template = models.IntegerField(blank=True, null=True)
    report_voice = models.IntegerField(blank=True, null=True)
    report_html = models.TextField(blank=True, null=True)
    is_structure_template = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_report'


class TCaseReportImage(BaseModel):
    report = models.ForeignKey(TCaseReport, models.DO_NOTHING, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_report_image'


class TCaseReportSignCallbackLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    report_id = models.IntegerField(blank=True, null=True)
    report_serial_no = models.CharField(max_length=50, blank=True, null=True)
    uniqueid = models.CharField(db_column='uniqueId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    signeddata = models.TextField(db_column='signedData', blank=True, null=True)  # Field name made lowercase.
    signedstamp = models.TextField(db_column='signedStamp', blank=True, null=True)  # Field name made lowercase.
    signedpdfbase64 = models.TextField(db_column='signedPdfBase64', blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(max_length=100, blank=True, null=True)
    openid = models.CharField(db_column='openId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_report_sign_callback_log'


class TCaseSample(BaseModel):
    case_sample_id = models.AutoField(primary_key=True)
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    organ_id = models.IntegerField(blank=True, null=True)
    sample_id = models.IntegerField(blank=True, null=True)
    sample_name = models.CharField(max_length=50, blank=True, null=True)
    sample_desc = models.CharField(max_length=100, blank=True, null=True)
    sample_index = models.IntegerField(blank=True, null=True)
    sample_take_site = models.CharField(max_length=20, blank=True, null=True)
    sample_take_time = models.DateTimeField(blank=True, null=True)
    generally_see = models.TextField(blank=True, null=True)
    frozen_surgery_see = models.TextField(blank=True, null=True)
    frozen_surgery_part = models.CharField(max_length=100, blank=True, null=True)
    frozen_get_date = models.DateTimeField(blank=True, null=True)
    cut_method = models.IntegerField(blank=True, null=True)
    sample_deal = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    sample_send_count = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_sample'


class TCaseSendRecord(BaseModel):
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    recommend_account = models.CharField(max_length=20, blank=True, null=True)
    send_account_id = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_send_record'


class TCaseSlide(BaseModel):
    slide_id = models.AutoField(primary_key=True)
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    case_sample_id = models.IntegerField(blank=True, null=True)
    waxblock = models.ForeignKey('TCaseWaxblock', models.DO_NOTHING, blank=True, null=True)
    slide_index = models.IntegerField(blank=True, null=True)
    is_print = models.IntegerField(blank=True, null=True)
    print_time = models.DateTimeField(blank=True, null=True)
    cut_time = models.DateTimeField(blank=True, null=True)
    cut_account_id = models.IntegerField(blank=True, null=True)
    is_made = models.IntegerField(blank=True, null=True)
    make_time = models.DateTimeField(blank=True, null=True)
    make_account_id = models.IntegerField(blank=True, null=True)
    is_bind = models.IntegerField(blank=True, null=True)
    bind_time = models.DateTimeField(blank=True, null=True)
    is_upload = models.IntegerField(blank=True, null=True)
    upload_time = models.DateTimeField(blank=True, null=True)
    oss_url = models.CharField(max_length=200, blank=True, null=True)
    local_url = models.CharField(max_length=100, blank=True, null=True)
    file_name = models.CharField(max_length=200, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    scan_time = models.DateTimeField(blank=True, null=True)
    bind_account_id = models.IntegerField(blank=True, null=True)
    slide_memo = models.CharField(max_length=500, blank=True, null=True)
    source_pathologyno = models.CharField(max_length=200, blank=True, null=True)
    slide_label = models.IntegerField(blank=True, null=True)
    slide_label_rotation = models.IntegerField(blank=True, null=True)
    slide_preview = models.IntegerField(blank=True, null=True)
    mini_oss_url = models.CharField(max_length=100, blank=True, null=True)
    is_label_miniprint = models.IntegerField(blank=True, null=True)
    is_bopian_miniprint = models.IntegerField(blank=True, null=True)
    consultation_slide_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_slide'


class TCaseSlideImage(BaseModel):
    slide = models.ForeignKey(TCaseSlide, models.DO_NOTHING, blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_slide_image'


class TCaseStatusLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    pre_status = models.IntegerField(blank=True, null=True)
    cur_status = models.IntegerField(blank=True, null=True)
    action = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_status_log'


class TCaseStatusTime(BaseModel):
    case_id = models.IntegerField()
    case_status = models.IntegerField(primary_key=True)
    log_id = models.IntegerField(blank=True, null=True)
    status_change_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_status_time'
        unique_together = (('case_status', 'case_id'),)


class TCaseTotal(BaseModel):
    case = models.OneToOneField(TCase, models.DO_NOTHING, primary_key=True)
    cs_account_id = models.IntegerField(blank=True, null=True)
    cs_check_time = models.DateTimeField(blank=True, null=True)
    expert_account_id = models.IntegerField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    report_time = models.DateTimeField(blank=True, null=True)
    report_time_last = models.DateTimeField(blank=True, null=True)
    ca_account_id = models.IntegerField(blank=True, null=True)
    ca_time = models.DateTimeField(blank=True, null=True)
    print_time = models.DateTimeField(blank=True, null=True)
    is_print = models.IntegerField(blank=True, null=True)
    print_account_id = models.IntegerField(blank=True, null=True)
    submit_center_time = models.DateTimeField(blank=True, null=True)
    send_advice_time = models.DateTimeField(blank=True, null=True)
    exec_advice_time = models.DateTimeField(blank=True, null=True)
    frozen_exec_submit_time = models.DateTimeField(blank=True, null=True)
    frozen_exec_time = models.DateTimeField(blank=True, null=True)
    across_center_time = models.DateTimeField(blank=True, null=True)
    across_center_id = models.IntegerField(blank=True, null=True)
    appoint_expert_id = models.IntegerField(blank=True, null=True)
    forzen_add_count = models.IntegerField(blank=True, null=True)
    turn_center_time = models.DateTimeField(blank=True, null=True)
    site_receive_time = models.DateTimeField(blank=True, null=True)
    followup_record = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_total'


class TCaseUpdateLog(BaseModel):
    case_id = models.IntegerField(blank=True, null=True)
    apply_account_id = models.IntegerField(blank=True, null=True)
    agree_account_id = models.IntegerField(blank=True, null=True)
    vercode = models.CharField(max_length=10, blank=True, null=True)
    is_used = models.TextField(blank=True, null=True)  # This field type is a guess.
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_update_log'


class TCaseWaxblock(BaseModel):
    waxblock_id = models.AutoField(primary_key=True)
    case = models.ForeignKey(TCase, models.DO_NOTHING, blank=True, null=True)
    waxblock_index = models.CharField(max_length=10, blank=True, null=True)
    case_sample = models.ForeignKey(TCaseSample, models.DO_NOTHING, blank=True, null=True)
    waxblock_name = models.CharField(max_length=20, blank=True, null=True)
    get_part = models.CharField(max_length=20, blank=True, null=True)
    material_count = models.IntegerField(blank=True, null=True)
    material_size = models.CharField(max_length=30, blank=True, null=True)
    material_source = models.IntegerField(blank=True, null=True)
    is_embed = models.IntegerField(blank=True, null=True)
    embed_time = models.DateTimeField(blank=True, null=True)
    embed_account_id = models.IntegerField(blank=True, null=True)
    cell_dye_type = models.IntegerField(blank=True, null=True)
    cell_make_type = models.IntegerField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_miniprint = models.IntegerField(blank=True, null=True)
    waxblock_deal = models.IntegerField(blank=True, null=True)
    waxblock_info = models.CharField(max_length=30, blank=True, null=True)
    lab_device_id = models.IntegerField(blank=True, null=True)
    dehydration_time = models.DateTimeField(blank=True, null=True)
    embed_memo = models.CharField(max_length=100, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_case_waxblock'


class TCenter(BaseModel):
    center_id = models.AutoField(primary_key=True)
    center_name = models.CharField(max_length=50, blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    center_type = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    logo = models.IntegerField(blank=True, null=True)
    people_site_id = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_center'


class TCriticalValue(BaseModel):
    critical_value_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    test_item = models.CharField(max_length=250, blank=True, null=True)
    clinic_receiver = models.CharField(max_length=20, blank=True, null=True)
    clinic_receiver_phone = models.CharField(max_length=20, blank=True, null=True)
    notifier = models.IntegerField(blank=True, null=True)
    notification_time = models.DateTimeField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_critical_value'


class TDiagnosisTemplate(BaseModel):
    diagnosis_template_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    tempate_content = models.TextField(blank=True, null=True)
    template_name = models.CharField(max_length=200, blank=True, null=True)
    parent_template_id = models.IntegerField(blank=True, null=True)
    extend_id = models.IntegerField(blank=True, null=True)
    sort_index = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_diagnosis_template'


class TDictIhcGroup(BaseModel):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dict_ihc_group'


class TDictIhcGroupItem(BaseModel):
    group = models.ForeignKey(TDictIhcGroup, models.DO_NOTHING, blank=True, null=True)
    ihc = models.ForeignKey('TDictIhcItem', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dict_ihc_group_item'


class TDictIhcItem(BaseModel):
    ihc_id = models.AutoField(primary_key=True)
    ihc_name_en = models.CharField(max_length=100, blank=True, null=True)
    ihc_name_ch = models.CharField(max_length=100, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dict_ihc_item'


class TDictOrgan(BaseModel):
    organ_id = models.AutoField(primary_key=True)
    system = models.ForeignKey('TDictSystem', models.DO_NOTHING, blank=True, null=True)
    organ_name = models.CharField(max_length=50, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    sort_index = models.FloatField(blank=True, null=True)
    generally_see = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dict_organ'


class TDictSample(BaseModel):
    sample_id = models.AutoField(primary_key=True)
    organ = models.ForeignKey(TDictOrgan, models.DO_NOTHING, blank=True, null=True)
    sample_name = models.CharField(max_length=50, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    sort_index = models.FloatField(blank=True, null=True)
    sample_tip = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dict_sample'


class TDictSampleCell(BaseModel):
    sample_id = models.AutoField(primary_key=True)
    sample_type = models.IntegerField(blank=True, null=True)
    sample_name = models.CharField(max_length=50, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dict_sample_cell'


class TDictSpec(BaseModel):
    spec_id = models.AutoField(primary_key=True)
    spec_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dict_spec'


class TDictSystem(BaseModel):
    system_id = models.AutoField(primary_key=True)
    system_name = models.CharField(max_length=50, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    sort_index = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dict_system'


class TDictTemplate(BaseModel):
    template_id = models.AutoField(primary_key=True)
    root_template_id = models.IntegerField(blank=True, null=True)
    parent_template_id = models.IntegerField(blank=True, null=True)
    template_type = models.IntegerField(blank=True, null=True)
    extend_id = models.IntegerField(blank=True, null=True)
    template_name = models.CharField(max_length=100, blank=True, null=True)
    mirror_see = models.TextField(blank=True, null=True)
    suggest_memo = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    sort_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_dict_template'


class TDisease(BaseModel):
    disease_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    disease_name = models.CharField(max_length=100, blank=True, null=True)
    parent_disease_id = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_disease'


class TExpertExportLog(BaseModel):
    export_log_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=10, blank=True, null=True)
    excel_resid = models.IntegerField(blank=True, null=True)
    moneyconfig_backup_resid = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_expert_export_log'


class TExportTask(BaseModel):
    export_task_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    export_task_type = models.IntegerField(blank=True, null=True)
    export_task_status = models.IntegerField(blank=True, null=True)
    params = models.TextField(blank=True, null=True)
    download_url = models.CharField(max_length=200, blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_export_task'


class TExpress(BaseModel):
    express_id = models.AutoField(primary_key=True)
    extend_id = models.IntegerField(blank=True, null=True)
    business_type = models.IntegerField(blank=True, null=True)
    express_name = models.CharField(max_length=20, blank=True, null=True)
    express_no = models.CharField(max_length=100, blank=True, null=True)
    express_time = models.DateTimeField(blank=True, null=True)
    user_phone = models.CharField(max_length=20, blank=True, null=True)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    user_address = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_express'


class TFeedback(BaseModel):
    feedback_id = models.AutoField(primary_key=True)
    feedback_type_id = models.IntegerField(blank=True, null=True)
    client = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    contact_phone = models.CharField(max_length=50, blank=True, null=True)
    device_info = models.TextField(blank=True, null=True)
    fault_time = models.DateTimeField(blank=True, null=True)
    is_deal = models.IntegerField(blank=True, null=True)
    deal_content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_feedback'


class TFeedbackImg(BaseModel):
    feedback_img_id = models.AutoField(primary_key=True)
    feedback_id = models.IntegerField(blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_feedback_img'


class TFeedbackType(BaseModel):
    feedback_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_feedback_type'


class TFileCategory(BaseModel):
    file_category_id = models.AutoField(primary_key=True)
    parent_file_category_id = models.IntegerField(blank=True, null=True)
    file_tpl_id = models.IntegerField(blank=True, null=True)
    file_category_type = models.IntegerField(blank=True, null=True)
    caption = models.CharField(max_length=50, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    sort_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file_category'


class TFileDetail(BaseModel):
    file_detail_id = models.AutoField(primary_key=True)
    file_category_id = models.IntegerField(blank=True, null=True)
    file_no = models.CharField(max_length=50, blank=True, null=True)
    file_caption = models.CharField(max_length=50, blank=True, null=True)
    file_version = models.CharField(max_length=20, blank=True, null=True)
    file_content = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    auditor = models.IntegerField(blank=True, null=True)
    audit_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file_detail'


class TFileExtend(BaseModel):
    file_extend_id = models.AutoField(primary_key=True)
    file_history_id = models.IntegerField(blank=True, null=True)
    extend_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file_extend'


class TFileForm(BaseModel):
    file_form_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    file_tpl_id = models.IntegerField(blank=True, null=True)
    file_detail_id = models.IntegerField(blank=True, null=True)
    form_name = models.CharField(max_length=100, blank=True, null=True)
    form_no = models.CharField(max_length=30, blank=True, null=True)
    form_type = models.IntegerField(blank=True, null=True)
    is_required = models.IntegerField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file_form'


class TFileFormFreq(BaseModel):
    file_form_freq_id = models.AutoField(primary_key=True)
    file_form_id = models.IntegerField(blank=True, null=True)
    form_type_freq = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file_form_freq'


class TFileFormFreqOption(BaseModel):
    file_form_freq_option_id = models.AutoField(primary_key=True)
    file_form_freq_question_id = models.IntegerField(blank=True, null=True)
    option_caption = models.CharField(max_length=200, blank=True, null=True)
    option_need_memo = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    sort_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file_form_freq_option'


class TFileFormFreqQuestion(BaseModel):
    file_form_freq_question_id = models.AutoField(primary_key=True)
    file_form_freq_id = models.IntegerField(blank=True, null=True)
    question_name = models.CharField(max_length=100, blank=True, null=True)
    question_type = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file_form_freq_question'


class TFileFormLink(BaseModel):
    link_id = models.AutoField(primary_key=True)
    file_detail_id = models.IntegerField(blank=True, null=True)
    file_form_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file_form_link'


class TFileHistory(BaseModel):
    file_history_id = models.AutoField(primary_key=True)
    file_detail_id = models.IntegerField(blank=True, null=True)
    history_version = models.CharField(max_length=20, blank=True, null=True)
    history_category_id = models.IntegerField(blank=True, null=True)
    history_caption = models.CharField(max_length=50, blank=True, null=True)
    history_content = models.IntegerField(blank=True, null=True)
    history_no = models.CharField(max_length=50, blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    auditor = models.IntegerField(blank=True, null=True)
    audit_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    enabling_time = models.DateTimeField(blank=True, null=True)
    history_update_memo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file_history'


class TFileIndex(BaseModel):
    file_index_id = models.AutoField(primary_key=True)
    file_history_id = models.IntegerField(blank=True, null=True)
    parent_file_index_id = models.IntegerField(blank=True, null=True)
    file_index_name = models.CharField(max_length=100, blank=True, null=True)
    file_index_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file_index'


class TFileLink(BaseModel):
    file_link_id = models.AutoField(primary_key=True)
    file_history_id = models.IntegerField(blank=True, null=True)
    link_type = models.IntegerField(blank=True, null=True)
    link_file_detail_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file_link'


class TFileStudy(BaseModel):
    file_study_id = models.AutoField(primary_key=True)
    file_history_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file_study'


class TFileTpl(BaseModel):
    file_tpl_id = models.AutoField(primary_key=True)
    parent_tpl_id = models.IntegerField(blank=True, null=True)
    center_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    tpl_name = models.CharField(max_length=20, blank=True, null=True)
    tpl_desc = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file_tpl'


class TFileUpdateLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    file_history_id = models.IntegerField(blank=True, null=True)
    update_user = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    log_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_file_update_log'


class TFqaiSlide(BaseModel):
    slide_id = models.IntegerField(primary_key=True)
    fq_slide_id = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_fqai_slide'


class TGlobalConfig(BaseModel):
    config_id = models.AutoField(primary_key=True)
    config_key = models.CharField(max_length=30, blank=True, null=True)
    config_value = models.CharField(max_length=200, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_global_config'


class THospital(BaseModel):
    hospital_id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=100, blank=True, null=True)
    provice = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    area = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_hospital'


class THospitalCode(BaseModel):
    hospital_name = models.CharField(max_length=200)
    region_code = models.CharField(max_length=50)
    site_code = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_hospital_code'


class THpv(BaseModel):
    hpv_id = models.AutoField(primary_key=True)
    system_no = models.CharField(max_length=100, blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    advance_site_id = models.IntegerField(blank=True, null=True)
    pathology_no = models.CharField(max_length=30, blank=True, null=True)
    apply_no = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    info_patient_name = models.CharField(max_length=100, blank=True, null=True)
    info_patient_sex = models.IntegerField(blank=True, null=True)
    info_patient_age = models.IntegerField(blank=True, null=True)
    info_patient_age_unit = models.IntegerField(blank=True, null=True)
    info_patient_phone = models.CharField(max_length=100, blank=True, null=True)
    info_patient_nation = models.CharField(max_length=50, blank=True, null=True)
    info_patient_is_married = models.IntegerField(blank=True, null=True)
    info_clinical_diagnosis = models.TextField(blank=True, null=True)
    info_diagnosis_type = models.IntegerField(blank=True, null=True)
    info_diagnosis_no = models.CharField(max_length=50, blank=True, null=True)
    info_patient_area = models.CharField(max_length=20, blank=True, null=True)
    info_bed_no = models.CharField(max_length=50, blank=True, null=True)
    info_patient_id = models.CharField(max_length=100, blank=True, null=True)
    info_patient_job = models.CharField(max_length=20, blank=True, null=True)
    info_patient_addr = models.CharField(max_length=500, blank=True, null=True)
    info_patient_nation_place = models.CharField(max_length=20, blank=True, null=True)
    info_cost_type = models.IntegerField(blank=True, null=True)
    info_cost = models.FloatField(blank=True, null=True)
    info_history = models.TextField(blank=True, null=True)
    info_patient_menstruation = models.DateTimeField(blank=True, null=True)
    info_patient_is_menopause = models.IntegerField(blank=True, null=True)
    operation_see = models.CharField(max_length=200, blank=True, null=True)
    sample_send_doctor = models.CharField(max_length=20, blank=True, null=True)
    sample_send_hos = models.CharField(max_length=30, blank=True, null=True)
    sample_send_dept = models.CharField(max_length=30, blank=True, null=True)
    sample_get_doctor = models.CharField(max_length=20, blank=True, null=True)
    sample_get_date = models.DateTimeField(blank=True, null=True)
    sample_send_date = models.DateTimeField(blank=True, null=True)
    report_address = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    express_name = models.CharField(max_length=20, blank=True, null=True)
    express_no = models.CharField(max_length=100, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    agreement_price = models.FloatField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    search_string = models.CharField(max_length=50, blank=True, null=True)
    sample_send_doctor_phone = models.CharField(max_length=20, blank=True, null=True)
    report_temp_type = models.IntegerField(blank=True, null=True)
    info_patient_name_s = models.TextField(blank=True, null=True)
    origin_hpv_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_hpv'


class THpvAttachment(BaseModel):
    hpv_attachment_id = models.AutoField(primary_key=True)
    hpv_id = models.IntegerField(blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_hpv_attachment'


class THpvCaseRef(BaseModel):
    hpv_id = models.IntegerField(primary_key=True)
    case_id = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_hpv_case_ref'
        unique_together = (('hpv_id', 'case_id'),)


class THpvChargingItem(BaseModel):
    hpv_charging_item_id = models.AutoField(primary_key=True)
    charging_item_id = models.IntegerField(blank=True, null=True)
    hpv_id = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_hpv_charging_item'


class THpvReport(BaseModel):
    hpv_report_id = models.AutoField(primary_key=True)
    hpv_id = models.IntegerField(blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    is_audit = models.IntegerField(blank=True, null=True)
    hpv_result = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    auditor = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    release_account = models.IntegerField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)
    print_count = models.IntegerField(blank=True, null=True)
    is_release = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_hpv_report'


class THpvSample(BaseModel):
    hpv_sample_id = models.AutoField(primary_key=True)
    hpv_id = models.IntegerField(blank=True, null=True)
    sample_name = models.CharField(max_length=30, blank=True, null=True)
    sample_memo = models.CharField(max_length=50, blank=True, null=True)
    sample_get_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_hpv_sample'


class THpvStatusLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    hpv_id = models.IntegerField(blank=True, null=True)
    pre_status = models.IntegerField(blank=True, null=True)
    cur_status = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    action = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_hpv_status_log'


class THpvTotal(BaseModel):
    hpv_id = models.IntegerField(primary_key=True)
    hpv_status = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)
    update_account = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_hpv_total'
        unique_together = (('hpv_id', 'hpv_status'),)


class TJpushLog(BaseModel):
    platform = models.CharField(max_length=100, blank=True, null=True)
    audience = models.TextField(blank=True, null=True)
    notification = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)
    result_msg = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_jpush_log'


class TLabDevice(BaseModel):
    lab_device_id = models.AutoField(primary_key=True)
    lab_device_type_id = models.IntegerField(blank=True, null=True)
    lab_room_id = models.IntegerField(blank=True, null=True)
    lab_device_caption = models.CharField(max_length=200, blank=True, null=True)
    extend_field = models.TextField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_used = models.IntegerField(blank=True, null=True)
    is_fixed_assets = models.IntegerField(blank=True, null=True)
    asset_no = models.CharField(max_length=100, blank=True, null=True)
    device_cate = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lab_device'


class TLabDeviceLog(BaseModel):
    lab_device_log_id = models.AutoField(primary_key=True)
    lab_device_id = models.IntegerField(blank=True, null=True)
    lab_device_type_freq_id = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lab_device_log'


class TLabDeviceLogAnswer(BaseModel):
    lab_device_log_answer_id = models.AutoField(primary_key=True)
    lab_device_log_id = models.IntegerField(blank=True, null=True)
    lab_device_type_freq_question_id = models.IntegerField(blank=True, null=True)
    answer_memo = models.TextField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lab_device_log_answer'


class TLabDeviceRes(BaseModel):
    lab_device_res_id = models.AutoField(primary_key=True)
    lab_device_id = models.IntegerField(blank=True, null=True)
    lab_device_res_caption = models.CharField(max_length=100, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lab_device_res'


class TLabDeviceType(BaseModel):
    lab_device_type_id = models.AutoField(primary_key=True)
    lab_device_type_caption = models.CharField(max_length=200, db_collation='utf8mb3_bin', blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    device_cate = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    item_type = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lab_device_type'


class TLabDeviceTypeFreq(BaseModel):
    lab_device_type_freq_id = models.AutoField(primary_key=True)
    lab_device_type_id = models.IntegerField(blank=True, null=True)
    device_type_freq = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lab_device_type_freq'


class TLabDeviceTypeFreqOption(BaseModel):
    lab_device_type_freq_option_id = models.AutoField(primary_key=True)
    lab_device_type_freq_question_id = models.IntegerField(blank=True, null=True)
    option_caption = models.CharField(max_length=200, blank=True, null=True)
    option_need_memo = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    sort_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lab_device_type_freq_option'


class TLabDeviceTypeFreqQuestion(BaseModel):
    lab_device_type_freq_question_id = models.AutoField(primary_key=True)
    lab_device_type_freq_id = models.IntegerField(blank=True, null=True)
    question_name = models.CharField(max_length=100, blank=True, null=True)
    question_type = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lab_device_type_freq_question'


class TLabForm(BaseModel):
    lab_form_id = models.AutoField(primary_key=True)
    lab_form_title = models.CharField(max_length=100, blank=True, null=True)
    lab_form_no = models.CharField(max_length=50, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lab_form'


class TLabRoom(BaseModel):
    lab_room_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    room_name = models.CharField(max_length=100, blank=True, null=True)
    parent_room_id = models.IntegerField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    lab_room_type = models.IntegerField(blank=True, null=True)
    lab_room_area = models.FloatField(blank=True, null=True)
    lab_room_owner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lab_room'


class TLabRoomForm(BaseModel):
    lab_room_form_id = models.AutoField(primary_key=True)
    lab_form_id = models.IntegerField(blank=True, null=True)
    lab_room_id = models.IntegerField(blank=True, null=True)
    is_check = models.IntegerField(blank=True, null=True)
    check_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lab_room_form'


class TLabRoomFormUser(BaseModel):
    lab_room_form_user = models.AutoField(primary_key=True)
    lab_room_form_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lab_room_form_user'


class TLocalserviceSiteMachine(BaseModel):
    machine_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    machine_title = models.CharField(max_length=50, blank=True, null=True)
    machine_interface = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    os_type = models.IntegerField(blank=True, null=True)
    teamview_id = models.CharField(max_length=20, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_localservice_site_machine'


class TLocalserviceSiteSvr(BaseModel):
    site_svr_id = models.AutoField(primary_key=True)
    svr_id = models.IntegerField(blank=True, null=True)
    machine_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    svr_status = models.IntegerField(blank=True, null=True)
    svr_root = models.CharField(max_length=100, blank=True, null=True)
    svr_path = models.CharField(max_length=50, blank=True, null=True)
    svr_conf = models.TextField(blank=True, null=True)
    site_svr_version = models.CharField(max_length=20, blank=True, null=True)
    version_update_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_localservice_site_svr'


class TLocalserviceSvr(BaseModel):
    svr_id = models.AutoField(primary_key=True)
    svr_type = models.IntegerField(blank=True, null=True)
    svr_name = models.CharField(max_length=50, blank=True, null=True)
    svr_version = models.CharField(max_length=20, blank=True, null=True)
    svr_res_url = models.CharField(max_length=100, blank=True, null=True)
    version_update_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    svr_port = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_localservice_svr'


class TLocalserviceSvrHistory(BaseModel):
    history_id = models.AutoField(primary_key=True)
    svr_id = models.IntegerField(blank=True, null=True)
    history_version = models.CharField(max_length=20, blank=True, null=True)
    history_res_url = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    os_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_localservice_svr_history'


class TLocalserviceSvrVersion(BaseModel):
    svr_id = models.IntegerField(primary_key=True)
    os_type = models.IntegerField()
    svr_version = models.CharField(max_length=20, blank=True, null=True)
    svr_res_url = models.CharField(max_length=100, blank=True, null=True)
    version_update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_localservice_svr_version'
        unique_together = (('svr_id', 'os_type'),)


class TLocationArea(BaseModel):
    area_id = models.IntegerField(primary_key=True)
    area_name = models.CharField(max_length=60, blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_location_area'


class TLocationCity(BaseModel):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=50, blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_location_city'


class TLocationProvince(BaseModel):
    province_id = models.IntegerField(primary_key=True)
    province_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_location_province'


class TMember(BaseModel):
    member_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    parent_member_id = models.IntegerField(blank=True, null=True)
    member_role_id = models.IntegerField(blank=True, null=True)
    member_name = models.CharField(max_length=20, blank=True, null=True)
    member_title = models.IntegerField(blank=True, null=True)
    education = models.CharField(max_length=20, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    member_role = models.CharField(max_length=100, blank=True, null=True)
    member_teach_title = models.IntegerField(blank=True, null=True)
    extend_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_member'


class TMemberEditLimitsConfig(BaseModel):
    member_info_cate = models.IntegerField(primary_key=True)
    account_id = models.IntegerField()
    site_id = models.IntegerField()
    is_open = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_member_edit_limits_config'
        unique_together = (('member_info_cate', 'account_id', 'site_id'),)


class TMemberIntroduce(BaseModel):
    member_introduce_id = models.AutoField(primary_key=True)
    member_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_member_introduce'


class TMemberMeeting(BaseModel):
    member_meeting_id = models.AutoField(primary_key=True)
    member_id = models.IntegerField(blank=True, null=True)
    meeting_name = models.CharField(max_length=100, blank=True, null=True)
    meeting_org = models.CharField(max_length=100, blank=True, null=True)
    meeting_date = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_member_meeting'


class TMemberPaper(BaseModel):
    member_paper_id = models.AutoField(primary_key=True)
    member_id = models.IntegerField(blank=True, null=True)
    paper_title = models.CharField(max_length=100, blank=True, null=True)
    paper_post = models.CharField(max_length=100, blank=True, null=True)
    post_time = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_member_paper'


class TMemberRole(BaseModel):
    member_role_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    member_role_name = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_member_role'


class TMemberTraining(BaseModel):
    member_training_id = models.AutoField(primary_key=True)
    member_id = models.IntegerField(blank=True, null=True)
    training_name = models.CharField(max_length=100, blank=True, null=True)
    training_org = models.CharField(max_length=100, blank=True, null=True)
    training_time = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_member_training'


class TMenu(BaseModel):
    menu_id = models.AutoField(primary_key=True)
    menu_title = models.CharField(max_length=20, blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    menu_type = models.IntegerField(blank=True, null=True)
    page_src = models.CharField(max_length=100, blank=True, null=True)
    sort_index = models.IntegerField(blank=True, null=True)
    parent_menu_id = models.IntegerField(blank=True, null=True)
    remind_field = models.CharField(max_length=100, blank=True, null=True)
    menu_key = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_menu'


class TMenuAccount(BaseModel):
    account_id = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    menu = models.ForeignKey(TMenu, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_menu_account'


class TMiniprintLog(BaseModel):
    extend_id = models.IntegerField(primary_key=True)
    print_type = models.IntegerField()
    print_time = models.DateTimeField(blank=True, null=True)
    print_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_miniprint_log'
        unique_together = (('extend_id', 'print_type'),)


class TMolecular(BaseModel):
    molecular_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    pathology_no = models.CharField(max_length=30, blank=True, null=True)
    apply_no = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    info_patient_name = models.CharField(max_length=100, blank=True, null=True)
    info_patient_sex = models.IntegerField(blank=True, null=True)
    info_patient_age = models.IntegerField(blank=True, null=True)
    info_patient_age_unit = models.IntegerField(blank=True, null=True)
    info_patient_phone = models.CharField(max_length=100, blank=True, null=True)
    info_patient_is_married = models.IntegerField(blank=True, null=True)
    info_patient_email = models.CharField(max_length=30, blank=True, null=True)
    info_clinical_diagnosis = models.TextField(blank=True, null=True)
    info_pathology_diagnosis = models.TextField(blank=True, null=True)
    sample_send_doctor = models.CharField(max_length=20, blank=True, null=True)
    sample_send_doctor_phone = models.CharField(max_length=20, blank=True, null=True)
    sample_send_hos = models.CharField(max_length=30, blank=True, null=True)
    sample_send_dept = models.CharField(max_length=30, blank=True, null=True)
    sample_collect_time = models.DateTimeField(blank=True, null=True)
    sample_collect_type = models.CharField(max_length=100, blank=True, null=True)
    sample_collect_type_other = models.CharField(max_length=100, blank=True, null=True)
    sample_focus = models.CharField(max_length=100, blank=True, null=True)
    sample_focus_other = models.CharField(max_length=100, blank=True, null=True)
    sample_count = models.IntegerField(blank=True, null=True)
    report_address = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    express_name = models.CharField(max_length=20, blank=True, null=True)
    express_no = models.CharField(max_length=100, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    agreement_price = models.FloatField(blank=True, null=True)
    info_diagnosis_no = models.CharField(max_length=50, blank=True, null=True)
    info_bed_no = models.CharField(max_length=50, blank=True, null=True)
    info_patient_memo = models.TextField(blank=True, null=True)
    info_patient_name_s = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular'


class TMolecularCategory(BaseModel):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular_category'


class TMolecularItem(BaseModel):
    item_id = models.AutoField(primary_key=True)
    parent_item_id = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(TMolecularCategory, models.DO_NOTHING, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular_item'


class TMolecularItemCenterPrice(BaseModel):
    item = models.ForeignKey(TMolecularItem, models.DO_NOTHING, blank=True, null=True)
    center_id = models.IntegerField(blank=True, null=True)
    site_price = models.FloatField(blank=True, null=True)
    suggest_price = models.FloatField(blank=True, null=True)
    people_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular_item_center_price'


class TMolecularItemSitePrice(BaseModel):
    item = models.ForeignKey(TMolecularItem, models.DO_NOTHING, blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    site_price = models.FloatField(blank=True, null=True)
    suggest_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular_item_site_price'


class TMolecularPackage(BaseModel):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular_package'


class TMolecularPackageItem(BaseModel):
    package_item_id = models.AutoField(primary_key=True)
    package = models.ForeignKey(TMolecularPackage, models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(TMolecularItem, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular_package_item'


class TMolecularReport(BaseModel):
    report_id = models.AutoField(primary_key=True)
    molecular = models.ForeignKey(TMolecular, models.DO_NOTHING, blank=True, null=True)
    report_file = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular_report'


class TMolecularSample(BaseModel):
    molecular_sample_id = models.AutoField(primary_key=True)
    molecular_id = models.IntegerField(blank=True, null=True)
    sample_name = models.CharField(max_length=100, blank=True, null=True)
    sample_desc = models.CharField(max_length=100, blank=True, null=True)
    sample_id = models.IntegerField(blank=True, null=True)
    sample_position = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular_sample'


class TMolecularSlide(BaseModel):
    slide_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    molecular_id = models.IntegerField(blank=True, null=True)
    molecular_sample_id = models.IntegerField(blank=True, null=True)
    waxblock_id = models.IntegerField(blank=True, null=True)
    is_bind = models.IntegerField(blank=True, null=True)
    bind_time = models.DateTimeField(blank=True, null=True)
    bind_account_id = models.IntegerField(blank=True, null=True)
    is_upload = models.IntegerField(blank=True, null=True)
    upload_time = models.DateTimeField(blank=True, null=True)
    oss_url = models.CharField(max_length=100, blank=True, null=True)
    local_url = models.CharField(max_length=200, blank=True, null=True)
    file_name = models.CharField(max_length=200, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=100, blank=True, null=True)
    scan_time = models.DateTimeField(blank=True, null=True)
    slide_label = models.IntegerField(blank=True, null=True)
    slide_preview = models.IntegerField(blank=True, null=True)
    mini_oss_url = models.IntegerField(blank=True, null=True)
    read_result = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular_slide'


class TMolecularStatusLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    molecular = models.ForeignKey(TMolecular, models.DO_NOTHING, blank=True, null=True)
    pre_status = models.IntegerField(blank=True, null=True)
    cur_status = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    action = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular_status_log'


class TMolecularTotal(BaseModel):
    molecular = models.OneToOneField(TMolecular, models.DO_NOTHING, primary_key=True)
    submit_time = models.DateTimeField(blank=True, null=True)
    submit_account = models.IntegerField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    send_account = models.IntegerField(blank=True, null=True)
    receive_time = models.DateTimeField(blank=True, null=True)
    receive_account = models.IntegerField(blank=True, null=True)
    cancel_time = models.DateTimeField(blank=True, null=True)
    cancel_account = models.IntegerField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    finish_account = models.IntegerField(blank=True, null=True)
    people_pay_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular_total'


class TMolecularWaxblock(BaseModel):
    waxblock_id = models.AutoField(primary_key=True)
    molecular = models.ForeignKey(TMolecular, models.DO_NOTHING, blank=True, null=True)
    molecular_sample_id = models.IntegerField(blank=True, null=True)
    waxblock_no = models.CharField(max_length=100, blank=True, null=True)
    waxblock_type = models.IntegerField(blank=True, null=True)
    waxblock_memo = models.CharField(max_length=100, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular_waxblock'


class TMolecularWaxblockItem(BaseModel):
    waxblock_item_id = models.AutoField(primary_key=True)
    molecular = models.ForeignKey(TMolecular, models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey(TMolecularItem, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular_waxblock_item'


class TMolecularWaxblockItemRecord(BaseModel):
    record_id = models.AutoField(primary_key=True)
    waxblock_item_id = models.IntegerField(blank=True, null=True)
    ct_positive = models.IntegerField(blank=True, null=True)
    ct_positive_memo = models.CharField(max_length=100, blank=True, null=True)
    ct_negative = models.IntegerField(blank=True, null=True)
    ct_negative_memo = models.CharField(max_length=100, blank=True, null=True)
    finally_result = models.IntegerField(blank=True, null=True)
    finally_result_memo = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_molecular_waxblock_item_record'


class TMoneyBusinessType(BaseModel):
    business_type_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    case_type = models.IntegerField(blank=True, null=True)
    business_name = models.CharField(max_length=20, blank=True, null=True)
    business_memo = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    pay_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_business_type'


class TMoneyCaseConfig(BaseModel):
    case_id = models.IntegerField(primary_key=True)
    business_config = models.TextField(blank=True, null=True)
    advice_config = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_free = models.IntegerField(blank=True, null=True)
    is_people_deal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_case_config'


class TMoneyConfigAdviceExpert(BaseModel):
    config_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    advice_business_type = models.IntegerField(blank=True, null=True)
    expert_amount = models.FloatField(blank=True, null=True)
    suggest_amount = models.FloatField(blank=True, null=True)
    people_amount = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_config_advice_expert'


class TMoneyConfigAdviceSite(BaseModel):
    config_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    advice_business_type = models.IntegerField(blank=True, null=True)
    site_amount = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_config_advice_site'


class TMoneyConfigAudit(BaseModel):
    config_id = models.AutoField(primary_key=True)
    business_type_id = models.IntegerField(blank=True, null=True)
    center_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    audit_amount = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_config_audit'


class TMoneyConfigBusiness(BaseModel):
    config_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    province_amount = models.FloatField(blank=True, null=True)
    city_amount = models.FloatField(blank=True, null=True)
    area_amount = models.FloatField(blank=True, null=True)
    business_type = models.ForeignKey(TMoneyBusinessType, models.DO_NOTHING, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    province_suggest_amount = models.FloatField(blank=True, null=True)
    city_suggest_amount = models.FloatField(blank=True, null=True)
    area_suggest_amount = models.FloatField(blank=True, null=True)
    people_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_config_business'


class TMoneyConfigBusinessSite(BaseModel):
    config_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    site = models.ForeignKey('TMoneyConfigSite', models.DO_NOTHING, blank=True, null=True)
    site_amount = models.FloatField(blank=True, null=True)
    business_type = models.ForeignKey(TMoneyBusinessType, models.DO_NOTHING, blank=True, null=True)
    site_business_name = models.CharField(max_length=50, blank=True, null=True)
    free_count = models.IntegerField(blank=True, null=True)
    free_count_used = models.IntegerField(blank=True, null=True)
    is_enable = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    site_suggest_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_config_business_site'


class TMoneyConfigCaSite(BaseModel):
    ca_account_id = models.IntegerField(primary_key=True)
    role_id = models.IntegerField()
    site_id = models.IntegerField()
    site_ca_amount = models.FloatField(blank=True, null=True)
    ca_amount_config = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    updator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_config_ca_site'
        unique_together = (('ca_account_id', 'role_id', 'site_id'),)


class TMoneyConfigExpert(BaseModel):
    config_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    business_type = models.ForeignKey(TMoneyBusinessType, models.DO_NOTHING, blank=True, null=True)
    expert_amount = models.FloatField(blank=True, null=True)
    is_enable = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_config_expert'


class TMoneyConfigExpertSite(BaseModel):
    expert_account_id = models.IntegerField(primary_key=True)
    site_id = models.IntegerField()
    site_expert_amount = models.FloatField(blank=True, null=True)
    amount_config = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    updator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_config_expert_site'
        unique_together = (('expert_account_id', 'site_id'),)


class TMoneyConfigSite(BaseModel):
    site_id = models.IntegerField(primary_key=True)
    province_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    signing_date = models.DateField(blank=True, null=True)
    money_date = models.DateField(blank=True, null=True)
    money_cycle = models.IntegerField(blank=True, null=True)
    money_cycle_old = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_config_site'


class TMoneyExpertCycle(BaseModel):
    cycle_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    expert_count = models.IntegerField(blank=True, null=True)
    expert_confirm_count = models.IntegerField(blank=True, null=True)
    case_count = models.IntegerField(blank=True, null=True)
    total_amount_case = models.FloatField(blank=True, null=True)
    total_amount_advice = models.FloatField(blank=True, null=True)
    confirm_total_amount = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_expert_cycle'


class TMoneyExpertReport(BaseModel):
    report_id = models.AutoField(primary_key=True)
    cycle = models.ForeignKey(TMoneyExpertCycle, models.DO_NOTHING, blank=True, null=True)
    center_id = models.IntegerField(blank=True, null=True)
    expert_account_id = models.IntegerField(blank=True, null=True)
    case_count = models.IntegerField(blank=True, null=True)
    business_amount = models.FloatField(blank=True, null=True)
    advice_amount = models.FloatField(blank=True, null=True)
    is_confirm = models.IntegerField(blank=True, null=True)
    confirm_time = models.DateTimeField(blank=True, null=True)
    confirm_account_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_expert_report'


class TMoneyExpertReportLog(BaseModel):
    report = models.ForeignKey(TMoneyExpertReport, models.DO_NOTHING, blank=True, null=True)
    log_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_expert_report_log'


class TMoneyLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    money_type = models.IntegerField(blank=True, null=True)
    advice_id = models.IntegerField(blank=True, null=True)
    expert_account_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    memo = models.CharField(max_length=100, blank=True, null=True)
    extend_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_deal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_log'


class TMoneyOrder(BaseModel):
    order_id = models.AutoField(primary_key=True)
    extend_id = models.IntegerField(blank=True, null=True)
    order_type = models.IntegerField(blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    order_price = models.FloatField(blank=True, null=True)
    order_no = models.CharField(max_length=50, blank=True, null=True)
    pay_type = models.IntegerField(blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    pay_url = models.TextField(blank=True, null=True)
    is_pay = models.IntegerField(blank=True, null=True)
    notice_phone = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    p_order_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_order'


class TMoneySiteCycle(BaseModel):
    cycle_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    site_count = models.IntegerField(blank=True, null=True)
    site_confirm_count = models.IntegerField(blank=True, null=True)
    case_count = models.IntegerField(blank=True, null=True)
    total_amount_case = models.FloatField(blank=True, null=True)
    total_amount_advice = models.FloatField(blank=True, null=True)
    confirm_total_amount = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    sole_advice_count = models.IntegerField(blank=True, null=True)
    molecular_count = models.IntegerField(blank=True, null=True)
    total_amount_molecular = models.FloatField(blank=True, null=True)
    total_amount_soleadvice = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_site_cycle'


class TMoneySiteReport(BaseModel):
    report_id = models.AutoField(primary_key=True)
    cycle = models.ForeignKey(TMoneySiteCycle, models.DO_NOTHING, blank=True, null=True)
    center_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    money_cycle = models.IntegerField(blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    case_count = models.IntegerField(blank=True, null=True)
    business_amount = models.FloatField(blank=True, null=True)
    advice_amount = models.FloatField(blank=True, null=True)
    is_confirm = models.IntegerField(blank=True, null=True)
    confirm_time = models.DateTimeField(blank=True, null=True)
    confirm_account_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    molecular_count = models.IntegerField(blank=True, null=True)
    sole_advice_count = models.IntegerField(blank=True, null=True)
    molecular_amount = models.FloatField(blank=True, null=True)
    sole_advice_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_site_report'


class TMoneySiteReportLog(BaseModel):
    report = models.ForeignKey(TMoneySiteReport, models.DO_NOTHING, blank=True, null=True)
    log_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_site_report_log'


class TMoneyWithdraw(BaseModel):
    money_withdraw_id = models.AutoField(primary_key=True)
    withdraw_no = models.CharField(max_length=20, blank=True, null=True)
    withdraw_status = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_withdraw'


class TMoneyWithdrawItem(BaseModel):
    money_withdraw_id = models.IntegerField(blank=True, null=True)
    log_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_money_withdraw_item'


class TNotice(BaseModel):
    notice_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    notice_type = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_notice'


class TNoticeReadLog(BaseModel):
    notice_id = models.IntegerField()
    account_id = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_notice_read_log'


class TOauthApp(BaseModel):
    oauth_app_id = models.AutoField(primary_key=True)
    app_id = models.CharField(max_length=200, blank=True, null=True)
    app_secret = models.CharField(max_length=500, blank=True, null=True)
    memo = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_disabled = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_oauth_app'


class TOauthAppSite(BaseModel):
    oauth_app_site_id = models.AutoField(primary_key=True)
    oauth_app_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_oauth_app_site'


class TOauthLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    oauth_app_id = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_oauth_log'


class TOpenApp(BaseModel):
    open_app_id = models.CharField(primary_key=True, max_length=100)
    app_secret = models.CharField(max_length=500, blank=True, null=True)
    app_name = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_open_app'


class TPisApplicationArchive(BaseModel):
    case_id = models.AutoField(primary_key=True)
    pis_storage_position_id = models.IntegerField(blank=True, null=True)
    archive_date = models.DateTimeField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_application_archive'


class TPisBorrow(BaseModel):
    pis_borrow_id = models.AutoField(primary_key=True)
    borrow_no = models.CharField(max_length=100, blank=True, null=True)
    borrower = models.CharField(max_length=50, blank=True, null=True)
    borrower_idno = models.CharField(max_length=20, blank=True, null=True)
    borrower_phone = models.CharField(max_length=20, blank=True, null=True)
    borrow_use = models.IntegerField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    borrow_money = models.IntegerField(blank=True, null=True)
    need_return_date = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    acceptor = models.IntegerField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    borrow_expressnumber = models.CharField(max_length=50, blank=True, null=True)
    return_expressnumber = models.CharField(max_length=50, blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    borrow_type = models.IntegerField(blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_borrow'


class TPisBorrowItem(BaseModel):
    item_id = models.AutoField(primary_key=True)
    pis_borrow_id = models.IntegerField(blank=True, null=True)
    extend_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    borrow_type = models.IntegerField(blank=True, null=True)
    return_condition = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_borrow_item'


class TPisConsumable(BaseModel):
    consumable_id = models.AutoField(primary_key=True)
    consumable_category_id = models.IntegerField(blank=True, null=True)
    consumable_name = models.CharField(max_length=50, blank=True, null=True)
    specification = models.CharField(max_length=50, blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    remind_amount = models.IntegerField(blank=True, null=True)
    total_amount = models.IntegerField(blank=True, null=True)
    total_money = models.FloatField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_consumable'


class TPisConsumableCategory(BaseModel):
    consumable_category_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    category_name = models.CharField(max_length=20, blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_consumable_category'


class TPisConsumableLog(BaseModel):
    consumable_log_id = models.AutoField(primary_key=True)
    consumable_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    log_type = models.IntegerField(blank=True, null=True)
    related_name = models.CharField(max_length=50, blank=True, null=True)
    operate_time = models.DateTimeField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    left_amount = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    other_expenses = models.FloatField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    express_company = models.CharField(max_length=20, blank=True, null=True)
    express_no = models.CharField(max_length=50, blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    receive_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    batch_number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_consumable_log'


class TPisLabQuality(BaseModel):
    pis_lab_quality_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    project_name = models.CharField(max_length=100, blank=True, null=True)
    project_type = models.IntegerField(blank=True, null=True)
    organizer = models.CharField(max_length=100, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_lab_quality'


class TPisMenu(BaseModel):
    pis_menu_id = models.AutoField(primary_key=True)
    parent_menu_id = models.IntegerField(blank=True, null=True)
    menu_title = models.CharField(max_length=50, blank=True, null=True)
    menu_group = models.IntegerField(blank=True, null=True)
    role_id = models.CharField(max_length=100, blank=True, null=True)
    page_src = models.CharField(max_length=500, blank=True, null=True)
    main_icon_id = models.IntegerField(blank=True, null=True)
    tool_icon_id = models.IntegerField(blank=True, null=True)
    menu_type = models.IntegerField(blank=True, null=True)
    sort_index = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    menu_key = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_menu'


class TPisMenuAccount(BaseModel):
    pis_menu_account_id = models.AutoField(primary_key=True)
    pis_menu_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_menu_account'


class TPisPackage(BaseModel):
    pis_package_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    receive_site_id = models.IntegerField(blank=True, null=True)
    package_status = models.IntegerField(blank=True, null=True)
    courier = models.IntegerField(blank=True, null=True)
    tracking_no = models.CharField(max_length=50, blank=True, null=True)
    sender_name = models.CharField(max_length=20, blank=True, null=True)
    sender_phone = models.CharField(max_length=20, blank=True, null=True)
    sender_address = models.TextField(blank=True, null=True)
    receiver = models.CharField(max_length=20, blank=True, null=True)
    receiver_phone = models.CharField(max_length=20, blank=True, null=True)
    receiver_address = models.TextField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_package'


class TPisPackageItem(BaseModel):
    pis_package_item_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    extend_id = models.IntegerField(blank=True, null=True)
    receive_site_id = models.IntegerField(blank=True, null=True)
    pis_package_id = models.IntegerField(blank=True, null=True)
    pathology_no = models.CharField(max_length=20, blank=True, null=True)
    item_source = models.IntegerField(blank=True, null=True)
    item_type = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    item_caption = models.CharField(max_length=100, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_package_item'


class TPisPackageStatusLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    pis_package_id = models.IntegerField(blank=True, null=True)
    package_status = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_package_status_log'


class TPisSlideArchive(BaseModel):
    slide_id = models.IntegerField(primary_key=True)
    pis_storage_position_id = models.IntegerField(blank=True, null=True)
    archive_date = models.DateTimeField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    slide_archive_memo = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_slide_archive'


class TPisStoragePosition(BaseModel):
    pis_storage_position_id = models.AutoField(primary_key=True)
    storage_position_type = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_storage_position'


class TPisWaxblockArchive(BaseModel):
    waxblock_id = models.IntegerField(primary_key=True)
    pis_storage_position_id = models.IntegerField(blank=True, null=True)
    archive_date = models.DateTimeField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    waxblock_archive_memo = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_pis_waxblock_archive'


class TPost(BaseModel):
    post_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField(blank=True, null=True)
    post_type = models.IntegerField(blank=True, null=True)
    show_account_id = models.IntegerField(blank=True, null=True)
    post_title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    info_patient_sex = models.IntegerField(blank=True, null=True)
    info_patient_age = models.IntegerField(blank=True, null=True)
    info_system = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    ding = models.IntegerField(blank=True, null=True)
    read_count = models.IntegerField(blank=True, null=True)
    share_count = models.IntegerField(blank=True, null=True)
    last_reply_time = models.DateTimeField(blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    bbs_post_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_post'


class TPostFavorite(BaseModel):
    post = models.ForeignKey(TPost, models.DO_NOTHING, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_post_favorite'


class TPostImg(BaseModel):
    post_img_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(TPost, models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_post_img'


class TPostReply(BaseModel):
    reply_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(TPost, models.DO_NOTHING, blank=True, null=True)
    parent_reply_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    ding = models.IntegerField(blank=True, null=True)
    is_get = models.IntegerField(blank=True, null=True)
    bbs_reply_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_post_reply'


class TPurchaseApply(BaseModel):
    purchase_apply_id = models.AutoField(primary_key=True)
    purchase_detail_id = models.IntegerField(blank=True, null=True)
    caption = models.CharField(max_length=50, blank=True, null=True)
    specs = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    total_count = models.IntegerField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    shipment_cost = models.FloatField(blank=True, null=True)
    visit_cost = models.FloatField(blank=True, null=True)
    install_cost = models.FloatField(blank=True, null=True)
    logistics_type = models.CharField(max_length=50, blank=True, null=True)
    logistics_number = models.CharField(max_length=50, blank=True, null=True)
    deliver_date = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_purchase_apply'


class TPurchaseDetail(BaseModel):
    purchase_detail_id = models.AutoField(primary_key=True)
    purchase_log_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    approval_number = models.CharField(max_length=50, blank=True, null=True)
    import_site_name = models.CharField(max_length=50, blank=True, null=True)
    purchase_type = models.CharField(max_length=100, blank=True, null=True)
    reason = models.CharField(max_length=500, blank=True, null=True)
    delivery_date = models.CharField(max_length=50, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    approval_status = models.IntegerField(blank=True, null=True)
    approval_result = models.TextField(blank=True, null=True)
    approval_user = models.CharField(max_length=50, blank=True, null=True)
    approval_log = models.TextField(blank=True, null=True)
    submit_user = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    submit_time = models.CharField(max_length=50, blank=True, null=True)
    finish_time = models.CharField(max_length=50, blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_purchase_detail'


class TPurchaseLog(BaseModel):
    purchase_log_id = models.AutoField(primary_key=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_purchase_log'


class TRegisterCertification(BaseModel):
    certification_id = models.AutoField(primary_key=True)
    register_info_id = models.IntegerField(blank=True, null=True)
    idnores_positive_id = models.IntegerField(blank=True, null=True)
    idnores_reverse_id = models.IntegerField(blank=True, null=True)
    qualification_no = models.CharField(max_length=50, blank=True, null=True)
    qualification_res_id = models.IntegerField(blank=True, null=True)
    licensed_res_id = models.IntegerField(blank=True, null=True)
    bank_no = models.CharField(max_length=50, blank=True, null=True)
    open_bank = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    head_image = models.IntegerField(blank=True, null=True)
    license_number = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_register_certification'


class TRegisterInfo(BaseModel):
    register_info_id = models.AutoField(primary_key=True)
    web_user_name = models.CharField(max_length=50, blank=True, null=True)
    true_name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    idno = models.CharField(max_length=20, blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=200, blank=True, null=True)
    work_units = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    work_year = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    expert_type = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    refuse_memo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_register_info'


class TRegisterInfoSpec(BaseModel):
    register_info_id = models.IntegerField(blank=True, null=True)
    spec_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_register_info_spec'


class TReportTemplate(BaseModel):
    report_template_id = models.AutoField(primary_key=True)
    center_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    organ_id = models.IntegerField(blank=True, null=True)
    case_type = models.IntegerField(blank=True, null=True)
    template_name = models.CharField(max_length=50, blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_template'


class TReportTemplateItem(BaseModel):
    template_item_id = models.AutoField(primary_key=True)
    template_line_id = models.IntegerField(blank=True, null=True)
    item_type = models.IntegerField(blank=True, null=True)
    item_code = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_template_item'


class TReportTemplateLine(BaseModel):
    template_line_id = models.AutoField(primary_key=True)
    report_template_id = models.IntegerField(blank=True, null=True)
    line_label = models.CharField(max_length=50, blank=True, null=True)
    is_must = models.IntegerField(blank=True, null=True)
    line_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_template_line'


class TReportWrite(BaseModel):
    report_write_id = models.AutoField(primary_key=True)
    case_report_id = models.IntegerField(blank=True, null=True)
    report_content = models.TextField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_write'


class TReportWriteItem(BaseModel):
    write_item_id = models.AutoField(primary_key=True)
    write_line_id = models.IntegerField(blank=True, null=True)
    item_type = models.IntegerField(blank=True, null=True)
    item_code = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_write_item'


class TReportWriteLine(BaseModel):
    write_line_id = models.AutoField(primary_key=True)
    report_template_id = models.IntegerField(blank=True, null=True)
    report_write_id = models.IntegerField(blank=True, null=True)
    line_label = models.CharField(max_length=50, blank=True, null=True)
    is_must = models.IntegerField(blank=True, null=True)
    line_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_write_line'


class TReportWriteLog(BaseModel):
    write_log_id = models.AutoField(primary_key=True)
    report_write_id = models.IntegerField(blank=True, null=True)
    report_data = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_report_write_log'


class TRes(BaseModel):
    res_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    is_used = models.IntegerField(blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_res'


class TSite(BaseModel):
    site_id = models.AutoField(primary_key=True)
    center = models.ForeignKey(TCenter, models.DO_NOTHING, blank=True, null=True)
    site_name = models.CharField(max_length=50, blank=True, null=True)
    logo = models.IntegerField(blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    nature = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    link_user = models.CharField(max_length=20, blank=True, null=True)
    link_phone = models.CharField(max_length=11, blank=True, null=True)
    local_interface = models.CharField(max_length=100, blank=True, null=True)
    is_advance = models.IntegerField(blank=True, null=True)
    advance_site_id = models.IntegerField(blank=True, null=True)
    is_self_run = models.IntegerField(blank=True, null=True)
    is_cs = models.IntegerField(blank=True, null=True)
    is_auto_make = models.IntegerField(blank=True, null=True)
    is_sign = models.IntegerField(blank=True, null=True)
    is_device_test = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    device_secret = models.CharField(max_length=100, blank=True, null=True)
    device_ip = models.CharField(max_length=20, blank=True, null=True)
    device_token = models.CharField(max_length=500, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    wx_chat_id = models.IntegerField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    is_archiving = models.IntegerField(blank=True, null=True)
    is_lock = models.IntegerField(blank=True, null=True)
    is_charging_item = models.IntegerField(blank=True, null=True)
    is_tuoguan = models.IntegerField(blank=True, null=True)
    enterprice_wechat_id = models.CharField(max_length=100, blank=True, null=True)
    vr_url = models.CharField(max_length=200, blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    discount_type = models.IntegerField(blank=True, null=True)
    discount_begin_date = models.DateField(blank=True, null=True)
    discount_end_date = models.DateField(blank=True, null=True)
    contract_begin_date = models.DateField(blank=True, null=True)
    contract_end_date = models.DateField(blank=True, null=True)
    hospital_type = models.IntegerField(blank=True, null=True)
    import_method = models.IntegerField(blank=True, null=True)
    import_method_host_name = models.CharField(max_length=100, blank=True, null=True)
    take_order_mode = models.IntegerField(blank=True, null=True)
    is_take_order_first_doctor = models.IntegerField(blank=True, null=True)
    is_p2p_slideview = models.IntegerField(blank=True, null=True)
    hpv_report_template = models.CharField(max_length=50, blank=True, null=True)
    is_two_day_weekend = models.IntegerField(blank=True, null=True)
    is_need_scan = models.IntegerField(blank=True, null=True)
    is_auth_code = models.IntegerField(blank=True, null=True)
    is_pis_enabled = models.IntegerField(blank=True, null=True)
    his_report_url = models.CharField(max_length=200, blank=True, null=True)
    is_pis_simple = models.IntegerField(blank=True, null=True)
    is_local_print = models.IntegerField(blank=True, null=True)
    no_frozen_call = models.IntegerField(blank=True, null=True)
    is_show_his_case = models.IntegerField(blank=True, null=True)
    is_send_advice = models.IntegerField(blank=True, null=True)
    is_allow_modify_report = models.IntegerField(blank=True, null=True)
    use_his_apply_no = models.IntegerField(blank=True, null=True)
    is_contract_terminated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site'


class TSiteAddress(BaseModel):
    site_address_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    contact_name = models.CharField(max_length=20, blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_address'


class TSiteAuthCode(BaseModel):
    auth_code_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    auth_code = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_used = models.IntegerField(blank=True, null=True)
    use_account_id = models.IntegerField(blank=True, null=True)
    auth_type = models.IntegerField(blank=True, null=True)
    extend_id = models.IntegerField(blank=True, null=True)
    use_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_auth_code'


class TSiteAuthCodeConf(BaseModel):
    site_id = models.IntegerField(primary_key=True)
    auth_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_site_auth_code_conf'
        unique_together = (('site_id', 'auth_type'),)


class TSiteCasetypePre(BaseModel):
    pre_id = models.AutoField(primary_key=True)
    site = models.ForeignKey(TSite, models.DO_NOTHING, blank=True, null=True)
    case_type = models.IntegerField(blank=True, null=True)
    pre_str = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_casetype_pre'


class TSiteChargingGroup(BaseModel):
    site_charging_group_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    label_str = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_charging_group'


class TSiteChargingGroupJoin(BaseModel):
    site_charging_group_id = models.IntegerField(blank=True, null=True)
    charging_item_id = models.IntegerField(blank=True, null=True)
    charging_package_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_charging_group_join'


class TSiteChargingItem(BaseModel):
    charging_item_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    charging_item_name = models.CharField(max_length=30, blank=True, null=True)
    charging_item_price = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    charging_item_code = models.CharField(max_length=20, blank=True, null=True)
    memo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_charging_item'


class TSiteChargingPackage(BaseModel):
    charging_package_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    charging_package_name = models.CharField(max_length=100, blank=True, null=True)
    charging_package_memo = models.CharField(max_length=100, blank=True, null=True)
    charging_items = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_charging_package'


class TSiteChargingPackageItem(BaseModel):
    charging_package_id = models.IntegerField(blank=True, null=True)
    charging_item_id = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_charging_package_item'


class TSiteDailyReport(BaseModel):
    site = models.OneToOneField(TSite, models.DO_NOTHING, primary_key=True)
    report_date = models.DateField()
    res_id = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_daily_report'
        unique_together = (('site', 'report_date'),)


class TSiteData(BaseModel):
    site = models.ForeignKey(TSite, models.DO_NOTHING, blank=True, null=True)
    data_type = models.IntegerField(blank=True, null=True)
    data_text = models.TextField(blank=True, null=True)
    data_memo = models.TextField(blank=True, null=True)
    parent_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_data'


class TSiteDevice(BaseModel):
    device_id = models.AutoField(primary_key=True)
    site = models.ForeignKey(TSite, models.DO_NOTHING, blank=True, null=True)
    device_name = models.CharField(max_length=100, blank=True, null=True)
    device_type = models.IntegerField(blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    extend_data = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_device'


class TSiteDiscount(BaseModel):
    site_id = models.IntegerField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_discount'


class TSiteExportLog(BaseModel):
    export_log_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=10, blank=True, null=True)
    excel_resid = models.IntegerField(blank=True, null=True)
    moneyconfig_backup_resid = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_export_log'


class TSiteIhc(BaseModel):
    site_ihc_id = models.AutoField(primary_key=True)
    site = models.ForeignKey(TSite, models.DO_NOTHING, blank=True, null=True)
    ihc_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_ihc'


class TSiteIhcStock(BaseModel):
    site_ihc_stock_id = models.AutoField(primary_key=True)
    site_ihc = models.ForeignKey(TSiteIhc, models.DO_NOTHING, blank=True, null=True)
    clone_no = models.CharField(max_length=20, blank=True, null=True)
    money = models.FloatField(blank=True, null=True)
    seller = models.CharField(max_length=50, blank=True, null=True)
    batch_number = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    reagent_type = models.CharField(max_length=20, blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    theory_times = models.IntegerField(blank=True, null=True)
    storage_time = models.DateTimeField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    is_empty = models.IntegerField(blank=True, null=True)
    memo = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    is_enable = models.IntegerField(blank=True, null=True)
    enable_time = models.DateTimeField(blank=True, null=True)
    is_valid = models.IntegerField(blank=True, null=True)
    test_result = models.CharField(max_length=50, blank=True, null=True)
    abolish = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_ihc_stock'


class TSiteIhcStockLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    site_ihc_stock = models.ForeignKey(TSiteIhcStock, models.DO_NOTHING, blank=True, null=True)
    use_date = models.DateField(blank=True, null=True)
    use_times = models.IntegerField(blank=True, null=True)
    advice_count = models.IntegerField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    advice_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_ihc_stock_log'


class TSiteIhcStockRes(BaseModel):
    site_ihc_stock_res_id = models.AutoField(primary_key=True)
    site_ihc_stock_id = models.IntegerField(blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_ihc_stock_res'


class TSiteInterface(BaseModel):
    interface_id = models.AutoField(primary_key=True)
    is_enabled = models.IntegerField(blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    interface_url = models.CharField(max_length=200, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    local_path = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_interface'


class TSiteJointLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    case_id = models.IntegerField(blank=True, null=True)
    hpv_id = models.IntegerField(blank=True, null=True)
    req_type = models.IntegerField(blank=True, null=True)
    req_data = models.TextField(blank=True, null=True)
    res_data = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_joint_log'


class TSiteMonthMoney(BaseModel):
    site_id = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=20, blank=True, null=True)
    total_money = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_month_money'


class TSiteReportTemp(BaseModel):
    temp_id = models.AutoField(primary_key=True)
    site = models.ForeignKey(TSite, models.DO_NOTHING, blank=True, null=True)
    temp_name = models.CharField(max_length=50, blank=True, null=True)
    temp_title = models.CharField(max_length=100, blank=True, null=True)
    temp_foot = models.CharField(max_length=500, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    temp_logo = models.IntegerField(blank=True, null=True)
    temp_extend = models.TextField(blank=True, null=True)
    is_show_generally_see = models.IntegerField(blank=True, null=True)
    audit_sign_pre = models.CharField(max_length=10, blank=True, null=True)
    is_show_info_patient_phone = models.IntegerField(blank=True, null=True)
    is_show_his_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_report_temp'


class TSiteStatisticsReportLog(BaseModel):
    site_statistics_report_log_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    pdf_file_url = models.CharField(max_length=50, blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_statistics_report_log'


class TSiteTime(BaseModel):
    time_id = models.AutoField(primary_key=True)
    site = models.ForeignKey(TSite, models.DO_NOTHING, blank=True, null=True)
    case_type = models.IntegerField(blank=True, null=True)
    time_config = models.IntegerField(blank=True, null=True)
    forzen_add_time = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    timely_rate_time = models.IntegerField(blank=True, null=True)
    time_config_biopsy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_time'


class TSiteTransferConf(BaseModel):
    site_id = models.IntegerField(primary_key=True)
    case_type = models.IntegerField()
    transfer_type = models.IntegerField()
    is_open = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_transfer_conf'
        unique_together = (('site_id', 'case_type', 'transfer_type'),)


class TSiteWeixinMsgLog(BaseModel):
    log_id = models.AutoField(primary_key=True)
    site_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_weixin_msg_log'


class TSiteWorkloadConfig(BaseModel):
    site_workload_config_id = models.AutoField(primary_key=True)
    site = models.ForeignKey(TSite, models.DO_NOTHING, blank=True, null=True)
    workload_key = models.CharField(max_length=30, blank=True, null=True)
    workload_value = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_site_workload_config'


class TSlideLabel(BaseModel):
    label_id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=190, blank=True, null=True)
    path = models.CharField(max_length=190, blank=True, null=True)
    label_name = models.CharField(max_length=190, blank=True, null=True)
    label_text = models.TextField(blank=True, null=True)
    label_content = models.TextField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_slide_label'


class TSlideReply(BaseModel):
    reply_id = models.AutoField(primary_key=True)
    slide_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    label_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_slide_reply'


class TSlideScreenshot(BaseModel):
    screenshot_id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=50, blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    screenshot = models.CharField(max_length=255, blank=True, null=True)
    screenshot_text = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_slide_screenshot'


class TSlideWaitingDelete(BaseModel):
    oss_url = models.CharField(max_length=100, blank=True, null=True)
    memo = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_slide_waiting_delete'


class TSmsLog(BaseModel):
    phone = models.CharField(max_length=15, blank=True, null=True)
    content = models.CharField(max_length=500, blank=True, null=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sms_log'


class TTrainingDocument(BaseModel):
    training_document_id = models.AutoField(primary_key=True)
    training_document_class_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_training_document'


class TTrainingDocumentClass(BaseModel):
    training_document_class_id = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=200, blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_training_document_class'


class TVersionLog(BaseModel):
    version = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_version_log'


class TWorkOrder(BaseModel):
    work_order_id = models.AutoField(primary_key=True)
    work_order_type = models.IntegerField(blank=True, null=True)
    extend_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creator = models.IntegerField(blank=True, null=True)
    deal_account_id = models.IntegerField(blank=True, null=True)
    deal_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_work_order'


class TWorkOrderAttachment(BaseModel):
    work_order_attachment_id = models.AutoField(primary_key=True)
    work_order_reply_id = models.IntegerField(blank=True, null=True)
    res_url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_work_order_attachment'


class TWorkOrderReply(BaseModel):
    work_order_reply_id = models.AutoField(primary_key=True)
    work_order_id = models.IntegerField(blank=True, null=True)
    sender = models.IntegerField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    content_type = models.IntegerField(blank=True, null=True)
    reply_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_work_order_reply'
