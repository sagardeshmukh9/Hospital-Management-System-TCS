from HMS import db

class Userstore(db.Document):
    username = db.StringField(unique = True, max_length=50)
    password = db.StringField(min_length=10,max_length=50)



class Patient_info(db.Document):
    ws_ssn = db.StringField(min_length=9,max_length=9)
    ws_pat_id = db.StringField(min_length=9,max_length=9)
    ws_pat_name = db.StringField(max_length=50)
    ws_adrs = db.StringField(max_length=255)
    ws_state = db.StringField(max_length=50)
    ws_city = db.StringField(max_lenth=50)
    ws_age = db.IntField()
    ws_doj = db.DateField()
    ws_rtype = db.StringField()
    ws_status = db.StringField()


class Medicine_issued(db.Document):
    ws_pat_id = db.IntField()
    ws_med_id = db.StringField()
    ws_qty = db.IntField()

class Medicine_info(db.Document):
    ws_med_id = db.IntField(unique = True)
    ws_med_name = db.StringField()
    ws_qty_avail = db.IntField()
    ws_med_rate = db.IntField()


class Diagnostics_issued(db.Document):
    ws_pat_id = db.IntField()
    ws_test_id = db.StringField()



class Diagnostics_info(db.Document):
    ws_test_id = db.IntField(unique=True)
    ws_test_name = db.StringField()
    ws_test_rate = db.IntField()
