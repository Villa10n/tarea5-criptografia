import imaplib
import email
import re

# DATOS INICIO DE SESION
email_host = ''
email_user = ''
email_pass = ''

# INICIAMOS SESION
mail = imaplib.IMAP4_SSL(email_host)
mail.login(email_user, email_pass)

# SELECCIONAMOS INBOX
mail.select('INBOX')

# AGREGAMOS EL CORREO EMISOR
typ, msgnums = mail.search(None, 'FROM gitkraken@axosoft.com')

# OBTENEMOS LOS MESSAGE-ID
largo = len(msgnums[0].split())
i = 0
j = 1
while (i < 20):
    correo = msgnums[0].split()[largo - i - 1]
    typ2, raw_data = mail.fetch(correo, '(RFC822)')
    message = email.message_from_string(raw_data[0][1].decode('utf-8'))
    message_id = message['message-id'][1:-1]
    print(j, ': ', message_id)
    i += 1
    j += 1