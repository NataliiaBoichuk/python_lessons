import os
import smtplib
import sys
from configparser import ConfigParser

SUBJECT = "Test email from Python"
TO = "some_recipient@gmail.com"
text_email = "Python 3.4 rules them all!"
user = 'some_sender@gmail.com'
pass_w = '12345678'


def send_email(subject, to, text, username, password):
    """
    Send an email
    """

    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "email.ini")

    if os.path.exists(config_path):
        cfg = ConfigParser()
        cfg.read(config_path)
    else:
        print("Config not found! Exiting!")
        sys.exit(1)

    host = cfg.get("smtp", "server")
    from_addr = cfg.get("smtp", "From")
    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to,
        "Subject: %s" % subject,
        "",
        text
    ))

    server = smtplib.SMTP(host)
    server.login(username, password)
    server.sendmail(from_addr, [to], BODY)
    server.quit()
