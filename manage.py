#!/usr/bin/env python3
import os
import sys
import uuid

#from django.contrib.auth.models import User
from django.core.management import execute_from_command_line

#from signup.models import Pcuser

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "infohub.settings")

    execute_from_command_line(sys.argv)

#    if sys.argv[1]== 'syncdb':
#        sys.argv.append('--noinput')
#        name='maccadmin'
#        email='macc@systers.com'
#        password = 'maccpassword'
#        user = User.objects.create_superuser(name,email,password)
#        user.first_name = ''
#        user.last_name = ''
#        user = Pcuser(user=user , location="", phone="",  gender="", reset_pass="", verified = uuid.uuid4().hex)
#        user.save()
