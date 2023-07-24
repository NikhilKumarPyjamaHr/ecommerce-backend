from models import AdminUser


def create_admin(db,admin_req):
    duplicate_admin_user = db.query(AdminUser).filter_by(email=admin_req.email).first()
    if duplicate_admin_user:
            raise Exception(f"Admin with email {admin_req.email} already exists.")
    else:
            admin_user = AdminUser(name=admin_req.name, email=admin_req.email)
            
            db.add(admin_user)
            db.commit()
            db.refresh(admin_user) 
            return admin_user