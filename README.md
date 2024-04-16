![image](https://github.com/itwizardo/leetmailer/assets/32465924/3f15e197-9e94-4583-be31-38225051671b)


### LeetMailer

LeetMailer is a powerful tool for sending personalized emails in bulk. Below are instructions on how to set up and use LeetMailer effectively:

---

#### Configuration Files

Ensure you customize the following files according to your requirements:

- **emaillist.txt:** This file should contain a list of email addresses along with corresponding first and last names, separated by commas. For example:
  ```
  example@gmail.com,john,doe
  ```

- **smtp.txt:** This file holds SMTP configuration details.

- **letter.html:** Customize the email template here. You can use placeholders like `{{2}}` for the first name and `{{3}}` for the last name.

- **dummy.config:** Here, you can configure the email subject, sender details, and other settings.

---

#### Macros

In the `letter.html` template or the dummy.config, you can utilize the following macros:

- `{{email}}` recipient's mail.
- `{{email_b64}}`recipient's email, encoded in base64. Useful when you pass it as a parameter to your marketing.
- `{{email_user}}` a fragment of the recipient's mail that comes before @. For example, for the mailbox john@apple.com it will be John (the first letter will be replaced with a capital one). Useful if we don’t have the recipient’s name in the database, but need to contact him by name or nickname.
- `{{email_host}}` recipient's email domain. In our example this is apple.com .
- `{{email_l2_domain}}` in our case it’s just apple . Useful if you want to put in the letter the name of the company where the recipient of the letter works.
- `{{smtp_user}}`: user of the smtp server used to send a specific letter. It's useful to include it in the From field to make the recipient less suspicious.
- `{{smtp_host}}`: smtp server domain. It is useful to indicate it as the sending company.
- `{{url}}`: Use this to insert a button link. Links specified in `redirect.txt` will change every 100th message.
- `{{random_name}}`: Random female first and last name. Useful if you need a random sender name.
- `{{random_fname}}`: Picks a random first name.
- `{{random_lname}}`: Picks a random last name.

---

#### Installation (Ubuntu/Debian)

1. Install Python 3:
   ```
   apt install python3
   ```

2. Clone the LeetMailer repository:
   ```
   git clone https://github.com/itwizardo/leetmailer.git
   ```

3. Navigate to the LeetMailer directory:
   ```
   cd leetmailer
   ```

4. Run LeetMailer:
   ```
   python3 leetmailer.py
   ```

5. Follow the prompts.

---

#### Things to do

Ensure to update GlockApp for inbox placement tracking.

---

Please use LeetMailer for educational purposes only. Feel free to reach out if you need further assistance or customization options. Happy emailing!
