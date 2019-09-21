import yagmail


sender_email = 'smtpforletslearnabout@gmail.com'
receiver_email = 'smtpforletslearnabout@gmail.com'
subject = "Check THIS out"
sender_password = input(f'Please, enter the password for {sender_email}:\n')

yag = yagmail.SMTP(user='smtpforletslearnabout@gmail.com', password=sender_password)

contents = [
  "This is the first paragraph in our email",
  "As you can see, we can send a list of strings,",
  "being this our third one",
  "BTW, here you have two pictures of dogs and cats. You need them:\n",
  "C:\\Users\\Void\\Desktop\\Codi\\Python\\yagmail\\dogs.jpg",
  "C:\\Users\\Void\\Desktop\\Codi\\Python\\yagmail\\cats.jpg",
]

# yag.send(sender_email, subject, contents)

# yag.send([sender_email, sender_email, sender_email, sender_email], subject, contents)

# yag.send([sender_email, sender_email, sender_email, sender_email], subject, contents, ["C:\\Users\\Void\\Desktop\\Codi\\Python\\yagmail\\dogs.jpg", "C:\\Users\\Void\\Desktop\\Codi\\Python\\yagmail\\cats.jpg"])
