from HMS import app
from flask import render_template, flash, session, redirect, url_for, request
from HMS.forms import LoginForm, UpdateForm, CreateForm
from HMS.models import Userstore, Patient_info, Medicine_info, Medicine_issued

@app.route("/", methods=["GET","POST"])
def home():
    Lform = LoginForm()
    if Lform.validate_on_submit():
        username = Lform.username.data
        password = Lform.password.data
        user = Userstore.objects(username=username).first()
        if user and user.password == password:
            flash("You've successfully Logged in!", "success")
            # creating a session
            session['username'] = user.username

            return redirect(url_for("index"))
        elif user and user.password != password:
            flash("The password you entered was incorrect!","danger")
        else:
            flash("This username is not valid!", "danger")

    return render_template("home.html", Lform=Lform)

@app.route("/logged_in")
def index():
    if session['username']:
        return render_template("index.html")
    else:
        flash("You need to log in to view the requested page","warning")
        return redirect(url_for("home"))

@app.route("/logged_in/patients_info")
def patients_info():
    if session['username']:
        Uform = UpdateForm()
        Cform = CreateForm()
        patients = Patient_info.objects(ws_status="active").all()
        return render_template("patients.html", patients=patients, Cform=Cform, Uform = Uform)
    else:
        flash("You need to log in to view the requested page","warning")
        return redirect(url_for("home"))

@app.route("/logged_in/patient_info/add_patient",  methods=["GET","POST"])
def add_patient():
    Cform = CreateForm()
    if Cform.validate_on_submit() and session['username']:
        ws_ssn = Cform.ws_ssn.data
        ws_pat_id = Cform.ws_pat_id.data
        ws_pat_name = Cform.ws_pat_name.data
        ws_adrs = Cform.ws_adrs.data
        ws_state = Cform.ws_state.data
        ws_city = Cform.ws_city.data
        ws_age = Cform.ws_age.data
        ws_doj = Cform.ws_doj.data
        ws_rtype = Cform.ws_rtype.data
        ws_status = "active"

        patient = Patient_info(ws_ssn=ws_ssn, ws_pat_id=ws_pat_id, ws_pat_name=ws_pat_name, ws_adrs=ws_adrs, ws_state=ws_state, ws_city=ws_city, ws_age=ws_age,ws_doj=ws_doj, ws_rtype=ws_rtype, ws_status=ws_status)
        if Patient_info.objects(ws_ssn=patient.ws_ssn,ws_status="active").first():
            flash("Patient with this SSN id has already been registered","danger")
        else:
            patient.save()
            flash("Data has been added successfully","success")
        return redirect(url_for("patients_info"))
    else:
        flash("You need to log in to view the requested page", "warning")
        return redirect(url_for("home"))


@app.route("/logged_in/patients_info/update", methods=["GET","POST"])
def update_patient_info():

    Uform = UpdateForm()
    if Uform.validate_on_submit():
        ws_pat_name = Uform.ws_pat_name.data
        ws_adrs = Uform.ws_adrs.data
        ws_state = Uform.ws_state.data
        ws_city = Uform.ws_city.data
        ws_age = Uform.ws_age.data
        ws_doj = Uform.ws_doj.data
        ws_rtype = Uform.ws_rtype.data

        Patient_info.objects(ws_pat_id = Uform.ws_pat_id.data).update(ws_pat_name=ws_pat_name, ws_adrs=ws_adrs,ws_state=ws_state,ws_city=ws_city, ws_age=ws_age, ws_doj=ws_doj, ws_rtype=ws_rtype)
        flash("Patient info updated successfully", "success")
    return redirect(url_for("patients_info", Uform=Uform))


@app.route("/logged_in/patients_info/delete", methods=["GET","POST"])
def delete_patient():
    if session['username']:
        if request.method == "POST":
            delpat = Patient_info.objects(ws_pat_id = request.form['patient_id']).first()
            delpat.delete()
            flash("Record deleted successfully","success")
        return redirect(url_for("patients_info"))
    flash("You need to log in to view the requested page", "warning")
    return redirect(url_for("home"))






@app.route("/logged_in/patients_info/search",methods=["GET","POST"])
def search():
    if session['username']:
        if request.method == "POST":
            Uform = UpdateForm()
            Cform = CreateForm()
            id = request.form['patient_id']
            pat = Patient_info.objects(ws_pat_id = id).first()
            if pat:
                flash("Patient found. Search successful!","success")
                return render_template("patients.html",pat=pat, Uform=Uform, Cform=Cform)
        flash("Patient not found.","danger")
        return redirect(url_for("patients_info"))
    else:
        flash("You need to log in to view the requested page","warning")
        return redirect(url_for("home"))


@app.route("/logged_out")
def logout():
    session['username'] = None
    return redirect(url_for("home"))

#
# @app.route("/search",methods=["GET","POST"])
# def search1():
#     if request.method == "POST":
#         patient = Patient_info.objects(ws_pat_id = patient_id).first()
#         med_issued = Medicine_issued.objects(ws_pat_id = patient_id).all()
#         meds_list=[]
#         for m in med_issued:
#             meds_list.append(Medicine_info.objects(ws_med_id = m.ws_med_id).first())
#
#
#         dictionary = {"patient_id":patient.ws_pat_id, "ssn_id":patient.ws_ssn, "Name":patient.ws_pat_name, "Age":patient.ws_age, "List_of_meds":meds_list}
#     return render_template("display.html",dictionary=dictionary)
