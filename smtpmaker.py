def get_smtp_server(email, smtp_mappings):
    domain = email.split('@')[-1]
    if domain in smtp_mappings:
        return smtp_mappings[domain]
    else:
        print(f"SMTP server for domain '{domain}' not found.")
        smtp_server = input(f"Please enter the SMTP server for {domain}: ")
        smtp_mappings[domain] = smtp_server  # Remember this server for any future references
        return smtp_server

def process_emails(file_path):
    output_lines = []
    smtp_mappings = {
  "gmail.com": "smtp.gmail.com",
  "yahoo.com": "smtp.mail.yahoo.com",
  "outlook.com": "smtp-mail.outlook.com",
  "hotmail.com": "smtp-mail.outlook.com",
  "aol.com": "smtp.aol.com",
  "icloud.com": "smtp.mail.me.com",
  "mail.com": "smtp.mail.com",
  "zoho.com": "smtp.zoho.com",
  "yandex.com": "smtp.yandex.com",
  "protonmail.com": "mail.protonmail.com",  # Note: ProtonMail requires specific setup
  "gmx.com": "smtp.gmx.com",
  "gmx.net": "smtp.gmx.net",
  "comcast.net": "smtp.comcast.net",
  "verizon.net": "outgoing.verizon.net",
  "att.net": "smtp.mail.att.net",
  "btinternet.com": "mail.btinternet.com",
  "cox.net": "smtp.cox.net",
  "orange.net": "smtp.orange.net",
  "sbcglobal.net": "smtp.sbcglobal.yahoo.com",
  "live.com": "smtp.live.com",
  "office365.com": "smtp.office365.com",
  "earthlink.net": "smtpauth.earthlink.net",
  "shaw.ca": "mail.shaw.ca",
  "telus.net": "smtp.telus.net",
  "qq.com": "smtp.qq.com",
  "naver.com": "smtp.naver.com",
  "skynet.be": "relay.skynet.be",
  "bellsouth.net": "mail.bellsouth.net",
  "blueyonder.co.uk": "smtp.blueyonder.co.uk",
  "charter.net": "mobile.charter.net",
  # New additions
  "yandex.ru": "smtp.yandex.ru",  # Russian Yandex
  "mail.ru": "smtp.mail.ru",  # Mail.ru
  "protonmail.ch": "mail.protonmail.ch",  # Alternative ProtonMail host
  "gandi.net": "smtp.gandi.net",
  "gmx.eu": "smtp.gmx.eu",  # European GMX
  "yahoo.co.jp": "smtp.mail.yahoo.co.jp",  # Japan Yahoo
  "googlemail.com": "smtp.gmail.com",  # Alternate Gmail domain
  "hotmail.fr": "smtp.live.com",  # French Hotmail
  "hotmail.de": "smtp.live.com",  # German Hotmail
  "hotmail.co.uk": "smtp.live.com",  # UK Hotmail
}
    port = "587"

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                email, password = line.strip().split(':')
                smtp_server = get_smtp_server(email, smtp_mappings)
                output_line = f"{smtp_server}|{port}|{email}|{password}"
                output_lines.append(output_line)
    except FileNotFoundError:
        print("The file was not found. Check the file path and try again.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    try:
        with open('smtpcomplete.txt', 'w') as file:
            for line in output_lines:
                file.write(line + '\n')
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")
        return
    
    print("Processing complete. Output saved to 'smtpcomplete.txt'.")

if __name__ == "__main__":
    file_path = input("Enter the path of your text file: ")
    process_emails(file_path)
