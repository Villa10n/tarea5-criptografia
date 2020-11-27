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

# EXTRAEMOS DATOS DEL ARCHIVO
archivo = open("datos.txt", 'r')
array = []
for linea in archivo:
    dato = linea.rstrip()
    array.append(dato)
correo = array[1]
typ, msgnums = mail.search(None, 'FROM ' + correo)

# OBTENEMOS LOS MESSAGE-ID Y COMPROBAMOS SI SON VALIDOS
largo = len(msgnums[0].split())
expresion_regular = array[0]
i = 0
j = 1
while (i < 20):
    correo = msgnums[0].split()[largo - i - 1]
    typ2, raw_data = mail.fetch(correo, '(RFC822)')
    message = email.message_from_string(raw_data[0][1].decode('utf-8'))
    message_id = message['message-id'][1:-1]
    x = re.search(expresion_regular, message_id)
    if x:
        print(j, ': ', message_id, '(coincide)')
    else:
        print(j, ': ',message_id, '(no coincide)')
    i += 1
    j += 1