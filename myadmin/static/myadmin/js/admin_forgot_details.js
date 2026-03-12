//Imports
function clicked() {
    window.alert("This element is sclicked")
}

// Constants for Document Objects
const UserNameDiv = document.getElementById("UsernameDiv");
const OtpVerificationDiv = document.getElementById("OtpBoxDiv");
const ChangePasswordDiv = document.getElementById("ChangePassword");
const ForgotPasswordVerifyDiv = document.getElementById("ForgotPassword");
const UsernameBox = document.querySelector("[name=Username]");
const GenerateOtpButton = document.getElementById("GenerateOtp");
const OtpBox = document.querySelector("[name=OTPBox]");
const VerifyEmailAddressButton = document.querySelector("#VerifyEmailAddress");
const MessageBox = document.getElementById("MessageBox");
const ResendOtp = document.querySelector("[name=ResendOtp]");
const SubmitPasswordButton = document.getElementById("SubmitPasswordButton")
const PasswordOne = document.getElementById("PasswordBox1")
const PasswordTwo = document.getElementById("PasswordBox2")
let request_type;

function ToggleDisable(object, innerhtml, type, message) {
    object.innerHTML = innerhtml;
    object.disabled = type;
    if (message) {
        MessageBox.innerHTML = message
    }

}
window.onload = () => {
    fetch("forgot_details", {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
            "Content-Type": "application/json"
        }, body: JSON.stringify({ request_type: "setup" })
    }).then(res => res.json()).then(server => {

        if (server.setup === "username_done") {
            ForgotPasswordVerifyDiv.classList.remove("hidden");
            UserNameDiv.classList.add("hidden");
            OtpVerificationDiv.classList.remove("hidden");
            OtpBox.classList.remove("hidden");
            MessageBox.innerHTML = server.message ? server.message : "";
            MessageBox.innerHTML = server.message ? server.message : "";
        }
        else if (server.setup === "otp_done") {
            ForgotPasswordVerifyDiv.classList.add("hidden");
            UserNameDiv.classList.add("hidden");
            OtpVerificationDiv.classList.add("hidden");
            ChangePasswordDiv.classList.remove("hidden");
            MessageBox.innerHTML = server.message ? server.message : "";
        }
        else {
            ForgotPasswordVerifyDiv.classList.remove("hidden");
            UserNameDiv.classList.remove("hidden");
            OtpVerificationDiv.classList.add("hidden");
            MessageBox.innerHTML = server.message ? server.message : "";
        }
    })
}
GenerateOtpButton.addEventListener("click", button => {
    button.preventDefault();
    request_type = "generate_otp"; request = "forgot_details";

    const UserName = UsernameBox.value
    const payload = {
        request_type: request_type,
        username: UserName, request: request
    }

    GenerateOtpButton.innerHTML = "Generating OTP..."
    GenerateOtpButton.disabled = true;


    fetch("forgot_details", {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
            "Content-Type": "application/json"
        }, body: JSON.stringify(payload)
    }).then(res => res.json()).then(server => {
        GenerateOtpButton.innerHTML = "Generate OTP"
        GenerateOtpButton.disabled = false;
        if (server.status === "ok") {
            UserNameDiv.classList.add("hidden")
            OtpVerificationDiv.classList.remove("hidden")
            MessageBox.innerHTML = server.message
        } else {
            MessageBox.innerHTML = server.message
        }
    })
})

/// for verify email address button
VerifyEmailAddressButton.addEventListener("click", cick => {
    cick.preventDefault();
    request_type = "verify_otp";
    if (OtpBox.value == "" || OtpBox.value == null){
        MessageBox.innerHTML = "Values cannot be empty in the inputs"
    }
    const otp = OtpBox.value;
    const data_pack = { request_type: request_type, otp: otp }

    VerifyEmailAddressButton.disabled = true;
    VerifyEmailAddressButton.innerHTML = "Verifying..."


    fetch(window.location.href, {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
            "content-type": "application/json"
        }, body: JSON.stringify(data_pack)
    })
        .then(res => res.json()).then(server => {
            VerifyEmailAddressButton.disabled = false;
            VerifyEmailAddressButton.innerHTML = "Submit"

            if (server.status === "ok") {
                UserNameDiv.classList.add("hidden");
                OtpVerificationDiv.classList.add("hidden");
                ChangePasswordDiv.classList.remove("hidden");
                MessageBox.innerHTML = server.message ? server.message : "";


            } else {
                MessageBox.innerHTML = server.message
            }
        }

        )
        .catch(error => {
            VerifyEmailAddressButton.disabled = false;
            VerifyEmailAddressButton.innerHTML = "Submit"
        })

})


/// For resend otp anchor tag
document.querySelector("[name=ResendOtp]").addEventListener("click", (Resend) => {
    Resend.preventDefault();
    ToggleDisable(ResendOtp, "Sending...", true);
    request_type = "generate_otp";
    request = "forgot_details";
    const payload = {
        request_type: request_type
        , request : request
    }
    fetch(window.location.href, {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
            "Content-Type": "application/json"
        }, body: JSON.stringify(payload)
    })
        .then(res => res.json()).then(server => {

            ToggleDisable(ResendOtp, "Sent...", false);
            setTimeout(1000)
            ToggleDisable(ResendOtp, "Resend OTP", false, server.message);
        }).catch(error => {
            ToggleDisable(ResendOtp, "Error...", false);
            setTimeout(1000)
            ToggleDisable(ResendOtp, "Resend OTP", false, "error");

        })
})

SubmitPasswordButton.addEventListener("click", SubmitPassword => {
    SubmitPassword.preventDefault();
    request_type = "submit_password";
    const password_one = PasswordOne.value;
    const password_two = PasswordTwo.value;
  if (!((password_one && password_two) && password_one != "" && password_two != "")) {
        MessageBox.innerHTML = "Fields cannot be empty!!"
    }  else  if (password_one != password_two) {
        MessageBox.innerHTML = "Both passwords must be same!!!";
        window.alert("The password fields doesnt match!!")
    }
    else {
        const password_pack = {
            request_type: request_type,
            password_one: password_one,
            password_two: password_two
        };


        fetch(window.location.href,{
            method : "POST",
            headers : {
                "X-CSRFToken" : document.querySelector("[name=csrfmiddlewaretoken]").value,
                "content-type" : "application/json"
            }, body : JSON.stringify (password_pack)
        }).then(res=>res.json).then(server=>{
          alert(JSON.stringify(server))
          alert("Response recieved")
          alert(server.status,server.message)
            if (server.status === "ok"){
                location.reload()
                UserNameDiv.classList.add("hidden");
                OtpVerificationDiv.classList.add("hidden");
                ChangePasswordDiv.classList.add("hidden");
                MessageBox.innerHTML = "<h1>Password was set successfully. Please return to login </h1>"

            }else{
                MessageBox.innerHTML = server.message;
            }
        }).catch( err=>{
          alert("console error" , err)
        })
    }
})