#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser, Namespace

import os
import os.path

import smtplib
from email.message import EmailMessage

from chris_plugin import chris_plugin
from pflog import pflog


parser = ArgumentParser(description='A ChRIS plugin to send email')
parser.add_argument('-r', '--rcpt', type=str, required=False, default='', help='comma separated receipients. [inputdir]/rcpt if not specified in argument.')
parser.add_argument('-t', '--title', type=str, required=False, default='', help='email title. [inputdir]/title if not specified in argument.')
parser.add_argument('-c', '--content', type=str, required=False, default='', help='content. [inputdir]/content if not specified in argument.')

parser.add_argument('-s', '--sender', type=str, required=False, default='noreply@fnndsc.org', help='sender (from). use [inputdir]/sender if exists.')
parser.add_argument('-m', '--mailserver', type=str, required=False, default='postfix.postfix.svc.k8s.galena.fnndsc', help='email server. use [inputdir]/mailserver if exists.')


@chris_plugin(
    parser=parser,
    title='A ChRIS plugin to send email',
    category='',  # ref. https://chrisstore.co/plugins
    min_memory_limit='500Mi',  # supported units: Mi, Gi
    min_cpu_limit='1000m',  # millicores, e.g. "1000m" = 1 CPU core
    min_gpu_limit=0,  # set min_gpu_limit=1 to enable GPU
)
@pflog.tel_logTime(
    event       = 'email',
    log         = 'Email',
)
def main(options: Namespace, inputdir: Path, outputdir: Path):
    filename = os.sep.join([inputdir, 'rcpt'])
    rcpt = _args_or_filename(options.rcpt, filename, 'Email: no --rcpt and no [inputdir]/rcpt')

    filename = os.sep.join([inputdir, 'title'])
    title = _args_or_filename(options.title, filename, 'Email: no --title and no [inputdir]/title')

    filename = os.sep.join([inputdir, 'content'])
    content = _args_or_filename(options.content, filename, 'Email: no --content and no [inputdir]/content')

    filename = os.sep.join([inputdir, 'sender'])
    sender = _filename_or_args(options.sender, filename, 'Email: no --sender and no [inputdir]/sender')

    filename = os.sep.join([inputdir, 'mailserver'])
    mail_server = _filename_or_args(options.mailserver, filename, 'Email: no --mailserver and no [inputdir]/mailserver')

    _send_email(title=title, content=content, recipients=rcpt, mail_server=mail_server, sender=sender)


def _args_or_filename(arg, filename, err_msg):
    if arg:
        return arg

    if not os.path.exists(filename):
        raise RuntimeError(err_msg)

    with open(filename, 'r') as f:
        return f.read().strip()


def _filename_or_args(arg, filename, err_msg):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return f.read().strip()

    if arg:
        return arg

    raise RuntimeError(err_msg)


def _send_email(title, content, recipients, mail_server, sender):
    if not recipients:
        raise RuntimeError('Email: no --rcpt and no [inputdir]/rcpt')

    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = sender
    msg['To'] = recipients
    msg.set_content(content)

    s = smtplib.SMTP(mail_server)
    s.send_message(msg)
    s.quit()


if __name__ == '__main__':
    main()
