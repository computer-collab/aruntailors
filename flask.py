from flask import Flask, render_template, request, jsonify;

app = Flask(__name__)

profile_init = 0;
class Admin : 
    username : str
    password : str
    email :  str
    
    class Profile:
        Admin : bool # models.OneToOneField(User, on_delete=models.CASCADE , related_name="profile")
        Bio : str #= models.TextField(blank=True)
        DateOfBirth : str #= models.DateField(null=True, blank=True)
        PhoneNumber : str #= models.CharField(max_length=15)
        Address : str #= models.CharField(max_length=1000, null = True, blank= False)
        
    def __init__(self):
        
        profile_init = profile_init+1;
        self.profile_count = profile_init
        self.username = f"user_profile_{profile_init}"
        self.password = f"user_password_{profile_init}"
        self.email = f"{self.username}@email.com"
        self.Profile.Admin = True
        self.Profile.Bio = f"{self.username} is a good boy and this is his bio"
        self.Profile.PhoneNumber = f"{profile_init}999999999"
        self.Profile.Address = f"{self.username}'s address"

    def get_info(self):
        return jsonify(self)
        

    
    
profile_database[100] = Admin()

@app.route("/",methods = ["POST","GET"])
def root(user):
    if request.method == "GET": 

        return render_template("profiles.html",)
    elif request.method == "POST":
        pass