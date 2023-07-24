from models import CouponCode

def create_coupon(db,coupon):
 
    coupon_exists = db.query(CouponCode).filter_by(name=coupon.name).first()
   
    if coupon_exists:
            raise Exception(f"Coupon Code already exists")
    else:
            coupon = CouponCode(name=coupon.name,price=coupon.price)     
            db.add(coupon)
            db.commit()
            db.refresh(coupon) 
            return coupon

def get_all_coupons(db):

    coupons = db.query(CouponCode).all()
    return coupons

def update_coupon(db,id,coupon_req):

    coupon = db.query(CouponCode).filter_by(id=id).first()
    if not coupon:
        raise Exception(f"Coupon Code not found ")
    else:
        coupon.name=coupon_req.name
        coupon.price=coupon_req.price

        updated_coupon= db.query(CouponCode).get(id)
        db.commit()
        db.close()


def delete_coupon(db,coupon_id):

    coupon = db.query(CouponCode).filter(CouponCode.id==coupon_id).first()
    if not coupon:
        raise Exception(f"Coupon Code not found ")
    else:
        db.delete(coupon)
        db.commit()
        db.close()