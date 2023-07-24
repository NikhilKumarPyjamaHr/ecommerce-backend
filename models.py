from sqlalchemy import Column, Integer, String, JSON, DateTime, Boolean, ForeignKey,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class CustomerUser(Base):
    __tablename__ = "customerusers"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(50), index=True)
    email = Column(String(100),index=True,unique=True)
    createdat = Column(DateTime, default=func.now())

    cart = relationship("Cart", back_populates="customer_user")


class AdminUser(Base):
    __tablename__ = "adminusers"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(50), index=True)
    email = Column(String(100),index=True,unique=True)
    
    createdat = Column(DateTime, default=func.now())

    products = relationship("Product", back_populates="admin_user")
    

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(100), index=True)
    description = Column(String(250), index=True)
    price = Column(Integer, index=True)

    admin_user_id = Column(String(100), ForeignKey("adminusers.email"))
    
    admin_user = relationship("AdminUser", back_populates="products")

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    items = Column(JSON)
    totalprice = Column(Integer, index=True)
    createdat = Column(DateTime, default=func.now())
    purchasestatus = Column(Boolean, default=False) 
    is_active = Column(Boolean, default=True) 

    customer_user_id = Column(String(255), ForeignKey("customerusers.email"), unique=True)
    
    customer_user = relationship("CustomerUser", back_populates="cart", uselist=False)


class CouponCode(Base):
    __tablename__ = "couponcode"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(30),index=True,unique=True)
    price = Column(Integer,index=True)

   






