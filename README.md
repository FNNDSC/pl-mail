# pl_mail

A ChRIS Plugin for sending email.

* rcpt: Comma separated receipients. It can be specified with `-r`, `--rcpt`, or in `[inputdir]/rcpt`
* title: Title of the email. It can be specified with `-t`, `--title`, or in `[inputdir]/title`
* content: Content of the email. It can be specified with `-c`, `--content`, or in `[inputdir]/content`.
* sender: Sender of the email (default: `noreply@fnndsc.org`). It can be specified in `[inputdir]/sender`, or with `-s`, `--sender`.
* mailserver: Mail server (default: `postfix.postfix.svc.k8s.galena.fnndsc`). It can be speicified in `[inputdir]/mailserver`, or with `-m`, `--mailserver`.
