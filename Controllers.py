from Web_app import Web_app
from flask import render_template,request,redirect,url_for,flash
from Models import Products,User,Category,Reviews
from Forms import  Reg_Pag,Login_Pag
import re
from werkzeug.security import check_password_hash 
from flask_login import login_user 
from sqlalchemy import or_



@Web_app.route("/", methods = ["GET"])

def Shop_Page():

    categ = request.args.get("category")
    products = Products.query.all()


    if categ:
        categ_list = categ.split(",")
        categ_list = [ int(x) for x in categ_list ]
        products = []
        for i in categ_list:
            products += Products.query.filter_by(Category_Id =  i).all()

    
    category = Category.query.all()

    Search = request.args.get("Search")


    if Search:
        products = Products.query.filter(or_(Products.Name.like(f"%{Search}%"))).all()



    
    context = {
            "Category": category,
            "Products":products
    }
        
        
    return render_template("shop.html" ,**context,products=products,Search=Search)




@Web_app.route("/Detail/")


def Detail_Page():
    
    category = Category.query.all()
    products = Products.query.all()
    context = {
        "Category": category,
        "Products":products
    }




    return  render_template("detail.html",**context)




@Web_app.route("/Register/", methods=["GET","POST"])

def Register_Page():
    register_form =  Reg_Pag()

    category = Category.query.all()



    context = {
            "Category": category,
    }

    Message = None
    if request.method == "POST":
        if register_form.validate_on_submit():
            user = User(
                Full_Name = register_form.Full_Name.data,
                Email = register_form.Email.data,
                Password = register_form.Password.data
            )
            Password_pattern = "^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)...[0-9a-zA-Z!@#$%&]{3,}$"
            Password_Id = str(register_form.Password.data)
            Valid = re.match(Password_pattern,Password_Id)
            if not Valid:
                Message = "Password must be at least one numeric character, lowercase letter,capital letter special character between @#$"
                return render_template("register.html", register_form = register_form, Message = Message)
            user.save()
            return redirect(url_for("Login_Page"))
        
    return render_template("register.html", register_form = register_form,**context)


@Web_app.route("/Login/", methods = ["GET","POST"])


def Login_Page():
    category = Category.query.all()
    context = {
        "Category": category,
    }

    login_form = Login_Pag()
    Message = None
    if request.method == "POST":
        if login_form.validate_on_submit:
            Email = login_form.Email.data
            user = User.query.filter_by(Email=Email).first()
            if user:
                if not check_password_hash(user.Password, login_form.Password.data)   :
                    Message = "Password or Email incorrect"
                    return render_template("login.html",login_form = login_form, Message = Message)
                login_user(user)
                return render_template("shop.html")
            else:
                Message = "User Dont Registered or Password is  Incorrect "
                return render_template("login.html",login_form = login_form, Message = Message)
            
        
    return render_template("login.html",login_form = login_form,**context)


@Web_app.route("/Favourites/")

def Favourites_Page():
    category = Category.query.all()



    context = {
            "Category": category
    }
    return render_template("favorites.html",**context)


@Web_app.route("/Contact/")

def Contact_Page():
    category = Category.query.all()
    context = {
            "Category": category,
            "Products":Products
    }

    return render_template("contact.html",**context)

@Web_app.route("/Delete/", methods=["GET","POST"])

def delete():
    return render_template("favorites.html")
    




