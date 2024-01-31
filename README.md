# pl_mail

A ChRIS Plugin for sending email.

* rcpt: Comma separated receipients. It can be specified in `[inputdir]/rcpt` , or with `-r`, `--rcpt`.
* title: Title of the email. It can be specified in `[inputdir]/title`, or with `-t`, `--title`.
* content: Content of the email. It can be specified in `[inputdir]/content`, or with `-c`, `--content`.
* sender: Sender of the email (default: `noreply@fnndsc.org`). It can be specified in `[inputdir]/sender`, or with `-s`, `--sender`.
* mailserver: Mail server (default: `postfix.postfix.svc.k8s.galena.fnndsc`). It can be specified in `[inputdir]/mailserver`, or with `-m`, `--mailserver`.
