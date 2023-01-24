from django.shortcuts import render
from . import Pool
from . import PoolDict

def userinterface(request):
    return render(request,"userregister.html")

def userregister(request):
    try:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        birthdate = request.POST['birthdate']
        mobilenumber = request.POST['mobileno']
        emailaddress = request.POST['email']
        password=request.POST['pass']
        cpassword=request.POST['cpass']

        q = "insert into user(firstname,lastname,gender,dob,email,mobileno,password,confirmpassword)values('{}','{}','{}','{}','{}','{}','{}','{}')".format(
            firstname, lastname, gender, birthdate, emailaddress, mobilenumber, password,cpassword)
        print(q)
        db, cmd = Pool.ConnectionPool()
        cmd.execute(q)
        db.commit()
        db.close()

        return render(request, 'userregister.html', {'msg': 'Record Succesfully Submitted'})

    except Exception as e:

        print("error:", e)
        return render(request, 'userregister.html', {'msg': 'Fail to Submit Record'})


def userlogin(request):
    try:
        emailaddress=request.POST['your_email']
        password=request.POST['your_pass']
        q="select * from user where email='{}'  and password='{}'".format(emailaddress,password)
        print(q)
        db,cmd=PoolDict.ConnectionPool()
        cmd.execute(q)
        result=cmd.fetchone()
        print(result)
        if(result):
            #request.session['EMPLOYEE'] = result
            return render(request,'userlogin.html',{'msg':'Login Succesfully'})
        else:
            return render(request,'userlogin.html',{'msg':'Invalid Email or Password'})
    except Exception as e:
     print("error:",e)
     return render(request, 'userlogin.html', {'result': {},'msg':'Server Error'})
