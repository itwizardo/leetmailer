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

In the `letter.html` template, you can utilize the following macros:

- `{{email}}`
- `{{email_b64}}`
- `{{email_user}}`
- `{{email_host}}`
- `{{email_l2_domain}}`
- `{{smtp_user}}`: SMTP user.
- `{{smtp_host}}`: SMTP host.
- `{{url}}`: Use this to insert a button link. Links specified in `redirect.txt` will change every 100th message.
- `{{random_Fname}}`: Generates a random first name.
- `{{random_Lname}}`: Generates a random last name.
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
