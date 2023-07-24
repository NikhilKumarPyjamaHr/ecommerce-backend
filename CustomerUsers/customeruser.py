
from models import CustomerUser

def create_user(db,user_req):
    duplicate_customer_user = db.query(CustomerUser).filter_by(email=user_req.email).first()
    if duplicate_customer_user:
            return duplicate_customer_user
    else:
            customer_user = CustomerUser(name=user_req.name, email=user_req.email)
            
            db.add(customer_user)
            db.commit()
            db.refresh(customer_user) 
            return customer_user

def get_all_users(db):
      customers = db.query(CustomerUser).all()
      return customers

def get_user_by_email(db,email:str):
      customer = db.query(CustomerUser).filter_by(email=email).first()
      if not customer:
        raise Exception(f"Customer with email {email} does not exists")

      return customer
