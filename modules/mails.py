import random, smtplib



def GenerateOTP(**details):
    Name = details.get("name")
    receiver_email = details.get("email")
    request_type = details.get("request")
    if not receiver_email:
        raise Exception("No email address input found")

    if not Name:
        Name = "**Name not defined**\n"
    
    otp = random.randint(100000,999999)
    sender_email = "otpmail.noreply@gmail.com"
    app_password = "dxrrnmilxweeznoz"

    if request_type == "registration":
        subject = "Your OTP for registration"
        
        message = f"""
        Hey Ms./Mr.{Name},
        This is your otp : {otp} for registration.
        Thankyou for registering.
        From : Mail Bot Service, login.
        """

    elif request_type == "forgot_details":
        subject = "Forgot Details | Your account Has been accessed"
        message = f"""
        Hey Mr/Ms. {Name},
        Is that you Trying to access Your account??
        Here is the otp: {otp},
        If its not you, Please once verify your password.
        Thankyou.

        From : MailBot.

        """
    else:
        subject = "otp"
        message = f"OTP : {otp}, Thankyou"
    text = f"Subject : {subject}\n\n{message}"
    print("Please wait... sending email")
    try :
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender_email,app_password)
        server.sendmail(sender_email,receiver_email,text )
        server.quit()
        print("Email has been successfully sent.\n")
        return otp
    
    except Exception as e :
        print(f"\n\033[31mError:\033[0m {e}\n")
        return "Error_exception"
    

def MaskEmail(email: str) -> str:
    name, domain = email.split("@")
    n = len(name)
    masked_name = name[0] + "*" * (n - 1) if n <= 6 else name[:3] + "*" * (n - 6) + name[-3:]
    return f"{masked_name}@{domain}"
