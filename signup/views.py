import jinja2
import smtplib
import uuid
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from jinja2.ext import loopcontrols
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from webhub.checker import check
from webhub.models import *
from webhub.serializers import *
from webhub import views as webhub_view


jinja_environ = jinja2.Environment(loader=jinja2.FileSystemLoader(['signup/templates/signup']), extensions=[loopcontrols])

# SMTP port for sending emails
SMTP_PORT = 465

#link for the localhost
website = "http://systerspcweb.herokuapp.com/"

#Calls the signup page. If the user us already logged in, s/he will be redirected to dashboard.
def signup_page(request):
    if request.user.is_authenticated():
        redirect_url = "/"
        if 'redirect_url' in request.REQUEST.keys():
            redirect_url = request.REQUEST['redirect_url']
        return HttpResponse(jinja_environ.get_template('redirect.html').render({"pcuser":None,"redirect_url":redirect_url}))

    else:
        return HttpResponse(jinja_environ.get_template('signup.html').render({"pcuser":None}))
    
    
#Called when a user clicks submit button in signup. Here a verification mail is also sent to the user.
@csrf_exempt
def signup_do(request):
    if request.user.is_authenticated():
        logout(request)
        redirect_url = "/"
        if 'redirect_url' in request.REQUEST.keys():
            redirect_url = request.REQUEST['redirect_url']
        return HttpResponse(jinja_environ.get_template('redirect.html').render({"pcuser":None,"redirect_url":redirect_url}))
    
    username = request.REQUEST['username']
    password = request.REQUEST['password']
    confirmpassword = request.REQUEST['confirmpassword']
        
    if password <> confirmpassword:
      return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                            "text":'<p>Passwords don\'t match. Please Enter again.</p><p>Click OK to go back to signup page.</p>',"link":'/signup_page/'}))
    
    first_name = request.REQUEST['first_name']
    last_name = request.REQUEST['last_name']
    phone = request.REQUEST['phone']
    email = request.REQUEST['email']
    gender = request.REQUEST['gender']
    location = request.REQUEST['location']

    try:
        if len(User.objects.filter(email=email))<>0:
            return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                                  "text":'<p>Someone has already registered using this email.</p><p>If you have forgotten your password, click <a href=\'/forgot_pass/\'</p><p>Click <a href=\'/signup_page/\'>here</a> to go back to signup page.</p>',"link":'0'}))
    except:
        pass
    
    if '@' not in email or '.' not in email:
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'<p>Invalid email, please Enter again.</p><p>Go Back or click OK to go to signup page.</p>',"link":"/signup_page/"}))
    
        
    if first_name == "":
        first_name = username
    
    user = User.objects.create_user(username, email, password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    entry = Pcuser(user=user, phone=phone, gender=gender, location=location, verified = uuid.uuid4().hex)
        
    entry.save()
    #send email to user
    webhub_view.login_do(request)
    send_verification_email(request)
    
    return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'<p>Verification email sent. check your inbox and verify the account.</p>',"text1":'<p>Go Back or click OK to go to signup page.</p>',"link":'/signup_page/'}))
    

    
#Function to send verification mail to user's email after he signs up.
def send_verification_email(request):
    if not request.user.is_authenticated():
        return HttpResponse(jinja_environ.get_template('index.html').render({"pcuser":None}))

    try:
        request.user.pcuser
    except:
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'No Pcuser associated!. Please go back or click  to go to the homepage' , "link": '/signup_page/'}))
    entry=request.user
    subject = 'Peace Corps Verification Email'
    msg = 'Subject: %s \n\nYour email has been registered on pchub.com.\nPlease\
    click on the following link to verify (or copy paste it in your browser if needed)\n\n\
    %s/verify?code=%s\n\nIf you have not registered on our website, please ignore.' % (subject, website, entry.pcuser.verified)
    
    x = send_email(msg, entry.email)
    if x[0]==0:
        return x[1]
    
    return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":request.user.pcuser, "text":'<p>Verification Email sent! Please Check your email inbox.</p><p>To re-send verification email, click <a href=\'/send_verification_email/\'>here</a>.</p><p>Click <a href=\'/logout_do/\'>here</a> to go to the homepage and log-in again</p>', "link":'0'}))



#Function to send emails using google smtplib. Takes email id and message as input.    
def send_email(msg, email):
    gmailLogin = 'pc.mobile.control.center'
    gmailPas = 'alphadeltaepsilon'
    fro = gmailLogin + "@gmail.com"
    
    to = email
    
    server = smtplib.SMTP_SSL('smtp.googlemail.com',SMTP_PORT)
    a = server.login( gmailLogin, gmailPas)
    server.sendmail(fro, to,msg)
    return (1,1)


#Called when a user enters verification code and clicks on submit. Checks the verification code with database.
def verify(request):
    if not request.user.is_authenticated():
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                              "text":'Verification Successful.',"text1":'Go to homepage' , "link": '/'}))
#        return HttpResponse(jinja_environ.get_template('index.html').render({"pcuser":Non,
#                                                                                   "code":request.REQUEST['code']}))
#        index(request)
    try:
        request.user.pcuser
    except:
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":None,
                                                                             "text":'<p>No Pcuser associated.</p>',"text1":'<p>Please click here to go to the homepage</p>',"link":'/'}))
    
    code = request.REQUEST['code']
    pcuser = request.user.pcuser
    if pcuser.verified == '1':
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":request.user.pcuser,
                                                                              "text":'<p>Verification successful.</p>',"text1":'<p>Click here to go to the homepage</p>',"link":'/'}))
    elif code == pcuser.verified:
        pcuser.verified = '1'
        pcuser.save()
        return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":request.user.pcuser,
                                                                              "text":'<p>Verification successful.</p>',"text1":'<p>Click here to go to the homepage</p>',"link":'/'}))
    
    return HttpResponse(jinja_environ.get_template('notice.html').render({"pcuser":request.user.pcuser,
                                                                          "text":'<p>Verification Failed.</p>',"text1":'<p>Please go back or click here to go to the homepage</p>',"link":'/'}))



