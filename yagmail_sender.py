import yagmail


sender_email = 'smtpforletslearnabout@gmail.com'
receiver_emails = ['smtpforletslearnabout@gmail.com', 'smtpforletslearnabout@gmail.com', 'smtpforletslearnabout@gmail.com']
subject = "Check THIS out"
sender_password = input(f'Please, enter the password for {sender_email}:\n')

try: 
  yag = yagmail.SMTP(user='smtpforletslearnabout@gmail.com', password=sender_password)

  contents = [
    "This is the first paragraph in our email",
    "As you can see, we can send a list of strings,",
    "being this our third one",
    "C:\\Users\\Void\\Desktop\\Codi\\Python\\yagmail\\dodgs.jpg",
    "C:\\Users\\Void\\Desktop\\Codi\\Python\\yagmail\\cats.jpg"
  ]

  yag.send(receiver_emails, subject, contents)

except Exception as e:
  print(f'Something went wrong!\n{e}')