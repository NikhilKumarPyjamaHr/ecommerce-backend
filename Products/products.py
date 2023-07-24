from models import Product
from models import AdminUser

def create_product(db,product):
 
 
    admin_user_exists = db.query(AdminUser).filter_by(email=product.admin_user_id).first()
   
    if not admin_user_exists:
            raise Exception(f"Customer with email {product.admin_user_id} not found ")
    else:
            product = Product(name=product.name,description=product.description,price=product.price, admin_user_id=product.admin_user_id)
            admin_user_exists.products.append(product)
            
            db.add(product)
            db.commit()
            db.refresh(product) 
            return product

def get_all_products(db):

    products = db.query(Product).all()
    return products

def update_product(db,id,product_req):

    product = db.query(Product).filter_by(id=id).first()
    if not product:
        raise Exception(f"Product  not found ")
    else:
        product.name=product_req.name
        product.description=product_req.description
        product.price=product_req.price
        product.admin_user_id=product_req.admin_user_id
        updated_product = db.query(Product).get(id)
        db.commit()
        db.close()


def delete_product(db,product_id):

    product = db.query(Product).filter(Product.id==product_id).first()
    if not product:
        raise Exception(f"Product  not found ")
    else:
        db.delete(product)
        db.commit()
        db.close()




   