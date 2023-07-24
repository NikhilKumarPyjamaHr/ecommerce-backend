from models import Cart
from models import CustomerUser

def create_cart(db,cart):
 
  
 
    customer_user_exists = db.query(CustomerUser).filter_by(email=cart.customer_user_id).first()
   
    cart_exists = db.query(Cart).filter_by(customer_user_id=cart.customer_user_id).first()
  

   
    if not customer_user_exists:
            raise Exception(f"Customer with email {cart.customer_user_id} not found ")
    else:
        if cart_exists:
            cart_exists.items=cart.items
            cart_exists.totalprice=cart.totalprice
            cart_exists.purchasestatus=cart.purchasestatus
            cart_exists.is_active=cart.is_active
            cart_exists.customer_user_id=cart.customer_user_id
          
            updated_cart = db.query(Cart).get(cart_exists.id)
            return updated_cart 

        else:
            cart = Cart(items=cart.items,totalprice=cart.totalprice,purchasestatus=cart.purchasestatus, is_active=cart.is_active,customer_user_id=cart.customer_user_id)
            # customer_user_exists.cart.append(cart)
            
            db.add(cart)
            db.commit()
            db.refresh(cart) 
            return cart



def delete_cart(db,id):

    cart = db.query(Cart).filter(Cart.id==id).first()
    if not cart:
        raise Exception(f"Cart  not found ")
    else:
        db.delete(cart)
        db.commit()
        db.close()
