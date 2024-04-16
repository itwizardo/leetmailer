<img width="1000" alt="Screenshot 2024-04-16 at 06 34 18" src="https://github.com/itwizardo/leetmailer/assets/32465924/e59c2d3c-d068-4789-ad6a-3ede258ea6cb">



![image](https://github.com/itwizardo/leetmailer/assets/32465924/4447fd50-fbc6-402d-acf6-0e32e9016dd6)

### LeetMailer

LeetMailer is a powerful tool for sending personalized emails in bulk. Below are instructions on how to set up and use LeetMailer effectively:

---

Yes, mailers differ not only in the convenience of the interface. The inbox rate depends on their internal structure.

For my mailer I chose Python and its smtplib library. It is popular among white-label sites and sends many clean emails, but (like Go and Javascript) is rarely used for sending spam.

Depending on the programming language in which the mailers are written, they use different libraries to work with SMTP or, without the use of third-party libraries, they communicate with the SMTP server through raw sockets, trying to imitate popular email clients ( but usually they fail in this task with a bang).

It is also designed to run on Linux or MacOS. I did not add socks proxy support to it, because if a proxy is used, the percentage of letters that end up in the inbox will depend on the purity of the proxy IP address, and not the purity of the IP server on which we ran our smtp checker and checked for delivery to inbox our smtp servers.

The mailer runs at 40 threads, which is enough to send 100,000 emails without heavy attachments in ~30 minutes. Without any problems, you can run it with 100 threads, but then it will simply be inconvenient to control them, because they won't fit on the screen.

Smtp servers will be disabled as they reach the daily limits of sent letters. And the mailer itself will stop when it finishes sending or if there are no more available smtp servers. If you want to forcefully stop it, press `[Ctrl]+[C]`on the keyboard.

Key Features:

- IP blacklist checker
- SMTP rotation
- Removal of potentially hazardous email addresses
- Macros for personalized content
- Inbox testing capabilities



#### Configuration Files

Make sure you edit the dummy.config files for the subject from mail ect the `mails_to_verify:` function will send test emails to for each new smtp server used. Used to carry inbox-rate statistics.

In the working directory from where the mailer will be launched, you can have as many .config-files as you like. The mailer will choose to use the config that was last edited.


#### Email list

If in your list of mails, in addition to the mails themselves, there is additional data (for example, name, company, position, telephone numbers, etc.), with any separator (for example, ,or |or ;or :), then the recipient's email is automatically extracted from each line of your mail file , regardless of its position among other data. The mailer will also automatically load the remaining data from each row, and each column will be available in macros {{1}}, {{2}}, {{3}}and so on (starting with number 1), depending on the number of columns.

- **emaillist.txt:** This file should contain a list of email addresses along with corresponding first and last names, separated by commas. For example:
  ```
  example@gmail.com,john,doe
  ```

- **smtp.txt:** This file holds SMTP configuration details. example:server|port|username|password" smtp will rotate

- **letter.html:** Customize the email template here. You can use placeholders like `{{2}}` for the first name and `{{3}}` for the last name.

---

#### Macros

In the `letter.html` template or the `dummy.config`, you can utilize the following macros:

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

---

#### Things to do

Ensure to update GlockApp for inbox placement tracking.

---

Please use LeetMailer for educational purposes only. Feel free to reach out if you need further assistance or customization options. Happy emailing!
