from typing import Union

from fastapi import FastAPI,status,HTTPException


from database import SessionLocal, Base, Product
from models import CustomerUser
import pdb
from CustomerUsers import customeruser,customerpydantic
from Products import products,productpydantic
from CouponCodes import couponcode,couponpydantic
from AdminUser import adminuser,adminuserpydantic
from Cart import cartpydantic,cart
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

db = SessionLocal()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#CUSTOMER USER SECTION

@app.post("/customerusers/", response_model=customerpydantic.CustomerUserResponse, status_code=status.HTTP_201_CREATED)
def create_customer_user(user:customerpydantic.CustomerUserRequest):
  
    try:
      
        customer_user=customeruser.create_user(db,user)
        db.close()
        return customer_user

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating customer user")
    


@app.get("/customerusers/",response_model=customerpydantic.CustomerUserList)
def get_customer_users():
   
   
    try:
        customer_user_list=customeruser.get_all_users(db)
        db.close()
        return{"customers":customer_user_list}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error fetching customer users")
    

@app.get("/customeruserbyemail/",response_model=customerpydantic.CustomerUserResponse)
def get_customer_user_by_email(email:str):
   
   
    try:
        customer_user_by_email=customeruser.get_user_by_email(db,email)
        db.close()
        return customer_user_by_email
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error fetching customer user")


#ADMIN SECTION

@app.post("/adminusers/", response_model=adminuserpydantic.AdminUserResponse, status_code=status.HTTP_201_CREATED)
def create_customer_user(user:adminuserpydantic.AdminUserRequest):
  
    try:
      
        admin_user=adminuser.create_admin(db,user)
        db.close()
        return admin_user

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except:
        
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating admin user")
    




#PRODUCT SECTION  

@app.post("/products/", response_model=productpydantic.ProductsList, status_code=status.HTTP_201_CREATED)
def create_product(productdict: productpydantic.ProductRequest):
    
    try:
        product=products.create_product(db,productdict)
        db.close()
        productlist=get_products()
        return productlist

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating product")


@app.get("/products/",response_model=productpydantic.ProductsList)
def get_products():

    try:
        product_list=products.get_all_products(db)
        db.close()
        return{"products":product_list}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error fetching products")
    
@app.put("/products/{id}",response_model=productpydantic.ProductsList)
def update_product(id: int, product: productpydantic.ProductRequest):

    try:
        products.update_product(db,id,product)
       
        return get_products()

    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error updating product")

@app.delete("/products/{id}",response_model=productpydantic.ProductsList)
def delete_product(id: int):

    try:
        products.delete_product(db,id)

        return get_products()

    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting product")
    

#COUPON CODE SECTION

@app.post("/couponcodes/", response_model=couponpydantic.CouponCodeList, status_code=status.HTTP_201_CREATED)
def create_coupon(coupondict: couponpydantic.CouponCodeRequest):
    
    try:
        coupon=couponcode.create_coupon(db,coupondict)
        db.close()
        return get_coupons()

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating coupon")


@app.get("/couponcodes/",response_model=couponpydantic.CouponCodeList)
def get_coupons():

    try:
        coupon_list=couponcode.get_all_coupons(db)
        db.close()
        return{"couponcodes":coupon_list}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error fetching coupons")
    
@app.put("/couponcodes/{id}",response_model=couponpydantic.CouponCodeList)
def update_coupon(id: int, coupon: couponpydantic.CouponCodeRequest):

    try:
        couponcode.update_coupon(db,id,coupon)
        return get_coupons()

    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error updating coupon")

@app.delete("/couponcodes/{id}",response_model=couponpydantic.CouponCodeList)
def delete_coupon(id: int):

    try:
        couponcode.delete_coupon(db,id)
        return get_coupons()

    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting coupon")
    

#CART SECTION


@app.post("/cart/", response_model=cartpydantic.CartResponse, status_code=status.HTTP_201_CREATED)
def create_cart(cartdict: cartpydantic.CartRequest):
    
    try:
  
        updated_cart=cart.create_cart(db,cartdict)
        db.close()
        return updated_cart

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating/updating cart")



@app.delete("/cart/{id}")
def delete_cart(id:int):

    try:
        cart.delete_cart(db,id)
        return "deleted successfully"

    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting cart")


#PAYMENT SECTION

@app.get("/payment/")
def payment():
    
    try:

        return "Payment Success" 

    except Exception as e:
      
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error doing payment")