const UserNameDiv = document.getElementById("UsernameDiv");
const OtpVerificationDiv = document.getElementById("OtpBoxDiv");
const ChangePasswordDiv = document.getElementById("ChangePassword");
const ForgotPasswordVerifyDiv = document.getElementById("ForgotPassword");
const UsernameBox = document.querySelector("[name=Username]");
const GenerateOtpButton = document.getElementById("GenerateOtp");
const OtpBox = document.querySelector("[name=OTPBox]");
const VerifyEmailAddressButton = document.querySelector("#VerifyEmailAddress");
const MessageBox = document.getElementById("MessageBox");
let request_type;

window.onload = () =>{
    fetch("forgot_details",{
        method : "POST",
        headers : {
            "X-CSRFToken" : document.querySelector("[name=csrfmiddlewaretoken]").value,
            "Content-Type" : "application/json"
        }, body : JSON.stringify ({ request_type : "setup"})
    }).then (res => res.json()).then(server=>{
        
        if (server.setup === "username_done"){
            ForgotPasswordVerifyDiv.classList.remove("hidden");
            UserNameDiv.classList.add("hidden");
            OtpVerificationDiv.classList.remove("hidden");
            OtpBox.classList.remove("hidden");
                MessageBox.innerHTML = server.message ? server.message : "";
            MessageBox.innerHTML = server.message ? server.message : "";
        }
        else if (server.setup === "otp_done"){
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
GenerateOtpButton.addEventListener("click", cick=>{
    cick.preventDefault();
    request_type = "generate_otp";
    const UserName = UsernameBox.value
    const payload = {
        request_type : request_type,
        username : UserName
    }

    GenerateOtpButton.innerHTML = "Generating OTP..."
    GenerateOtpButton.disabled = true;


    fetch("forgot_details",{
        method : "POST",
        headers : {
            "X-CSRFToken" : document.querySelector("[name=csrfmiddlewaretoken]").value,
            "Content-Type" : "application/json"
        }, body : JSON.stringify (payload)
    }).then (res => res.json()).then(server=>{
        GenerateOtpButton.innerHTML = "Generate OTP"
        GenerateOtpButton.disabled = false;
        if (server.status === "ok"){
            UserNameDiv.classList.add("hidden")
            OtpVerificationDiv.classList.remove("hidden")
            MessageBox.innerHTML = server.message
        }else {
            MessageBox.innerHTML = server.message
        }
    })
})


VerifyEmailAddressButton.addEventListener("click", cick=>{
    cick.preventDefault();
    request_type = "verify_otp";
    const otp  = OtpBox.value;
    const data_pack = { request_type : request_type , otp : otp }
    

    fetch(window.location.href,{
        method : "POST",
        headers : {
            "X-CSRFToken" : document.querySelector("[name=csrfmiddlewaretoken]").value,
            "content-type" : "application/json"
        }, body : JSON.stringify(data_pack)
        .then(res => res.json()).then( server=>{
            alert(server.email)

            if (server.status === "ok"){
                UserNameDiv.classList.add("hidden");
                OtpVerificationDiv.classList.add("hidden");
                ChangePasswordDiv.classList.remove("hidden");
                MessageBox.innerHTML = server.message ? server.message : "";

                
            } else {
                MessageBox.innerHTML = server.message
            }
        }
            
        )
    })


})