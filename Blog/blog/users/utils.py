import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from blog import mail


def save_picture(form_picture):
    random_hex= secrets.token_hex(8)
    _, f_ext =os.path.splitext(form_picture.filename)
    picture_file_name=random_hex + f_ext
    picture_path = os.path.join(current_app.root_path,'static/profile_pics' , picture_file_name)
    output_size=(125, 125)
    i= Image.open(form_picture)
    i.thumbnail(output_size)
    form_picture.save(i)
    return picture_file_name

def send_reset_email(user):
    token= user.get_reset_token()
    msg = Message('Password reset Request',sender='noreply@mc.com',recipients=[user.email])
    msg.body = f''' To reset your password, visit the followig link:
{url_for('users.reset_token', token = token ,_extrenal=True)}
 '''  
    mail.send(msg)
