# Python 2.7 + Selenium
My first script
The task:
  1. Login to email.
  2. Send to myself on this email 15 mails with 10 random numbers and letters in topic and in body of message.
  3. Check that mails is sending.
  4. Grub text of messages from main page of email  and save it to dict. The key of dict is topic and value is text of message.
  5. Recived information send to yourself in one mail with next text:
	  "Received mail on theme {key} with message: {value}. It
	  contains {sum of letters in mail} letters and {sum of numbers in mail} numbers".
  Attention - values must be recived from dict! Not from memory! All messages must be in this format.
  6. Delete all mails besides last recived mail.

Use Python 2.7 and Selenium
