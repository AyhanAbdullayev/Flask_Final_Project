from Extensions import My_db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

class Products(My_db.Model):
    __tablename__ = "Products"
    id = My_db.Column(My_db.Integer, primary_key = True, auto_increment = True)
    Name = My_db.Column(My_db.String(100),nullable = False)
    Category_Id = My_db.Column(My_db.Integer, My_db.ForeignKey("Category.id"))
    Price = My_db.Column(My_db.Float,nullable = False)
    Discount = My_db.Column(My_db.Float, nullable = False)
    Image = My_db.Column(My_db.Text,default = "pr-1.webp")

    Category = My_db.relationship("Category", backref = My_db.backref('Products', uselist = True))

    def __repr__(self):
        return f"{self.id},{self.Name},{self.Category_Id},{self.Price},{self.Discount}"
    
    def save(self):
        My_db.session.add(self)
        My_db.session.commit()



class Category(My_db.Model):
    __tablename__ = "Category"
    id = My_db.Column(My_db.Integer,primary_key = True,auto_increment = True)
    Name = My_db.Column(My_db.String(100), nullable = False)
    Parent_Id = My_db.Column(My_db.Integer, My_db.ForeignKey("Category.id"), nullable = True )

    parent = My_db.relationship("Category", remote_side = [id] ,backref = My_db.backref("Child", uselist = True))

    

    def __repr__(self):
        return f"{self.id},{self.Name}"

    def save(self):
        My_db.session.add(self)
        My_db.session.commit()





class User(My_db.Model,UserMixin):
    __tablename__ = "Users"
    id = My_db.Column(My_db.Integer, primary_key = True , auto_increment = True)
    Full_Name = My_db.Column(My_db.String(100), nullable = False )
    Email = My_db.Column(My_db.String(100), nullable = False)
    Password = My_db.Column(My_db.Text, nullable = False)

    def __repr__(self):
        return f"{self.id},{self.Name},{self.Email},{self.Password}"
    


    def __init__(self,Full_Name,Email,Password):
        self.Full_Name = Full_Name
        self.Email = Email
        self.Password = generate_password_hash(Password)
    
    def save(self):
        My_db.session.add(self)
        My_db.session.commit()


@login_manager.user_loader
def load_User(User_Id):
    return User.query.get(User_Id)


class Reviews(My_db.Model):
    __tablename__ = "Reviews"
    id = My_db.Column(My_db.Integer,primary_key = True,auto_increment = True)
    Product_Id = My_db.Column(My_db.Integer, My_db.ForeignKey("Products.id"))
    User_Id = My_db.Column(My_db.Integer, My_db.ForeignKey("Users.id"))
    Review = My_db.Column(My_db.Text, nullable = False)

    Product = My_db.relationship("Products", backref = My_db.backref("Product", uselist = True))
    # User  = My_db.relationship("Users", backref = My_db.backref("user", uselist = True))

    def __repr__(self):
        return f"{self.id},{self.Product_Id},{self.User_Id},{self.Review}"
    
    def save(self):
        My_db.session.add(self)
        My_db.session.commit()
        
 

