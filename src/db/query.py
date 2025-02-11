from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


# creat database
engine = create_engine('sqlite:///data/wal.db')
base = declarative_base()
session = sessionmaker(bind=engine)()

class admins(base):
    __tablename__ = 'admins'

    chat_id = Column('chat_id', Integer, unique=True)
    user_name = Column('user_name', String, unique=True, primary_key=True)
    password = Column('password', String)
    traffic = Column('traffic', Integer)
    inb_id = Column('inb_id', Integer)

class priceing(base):
    __tablename__ = 'priceing'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    traffic = Column('traffic', Integer)
    price = Column('price', Integer)
    
base.metadata.create_all(engine)

# pricing query
class PriceQuery:
    def add_plan(self, traffic, price):
        try:
            new_plan = priceing(
                traffic=traffic,
                price=price
            )
            session.add(new_plan)
            session.commit()
            return True
        except:
            return False
    
    def delete_plan(self, id):
        try:
            delete = session.query(priceing).filter(priceing.id==id).first()
            session.delete(delete)
            session.commit()
            self.reorder_ids()
            return True
        except:
            return False
        
    def edite_plan(self, id, traffic, price):
        try:
            update = session.query(priceing).filter(priceing.id==id).update({'traffic':traffic, 'price':price})
            session.commit()
            if update:
                return True
            else:
                return False
        except:
            return False
    
    def reorder_ids(self):
        try:
            plans = session.query(priceing).order_by(priceing.id).all()
            for index, plan in enumerate(plans, start=1):
                plan.id = index
            session.commit()
            return True
        except:
            return False
        
    def show_plans(self):
        try:
            plans = session.query(priceing).all()
            pricing_list = [
                {"id": price.id, "traffic": price.traffic,"price":price.price}
                for price in plans
            ]
            return pricing_list
        except:
            False
        
    def get_plan(self,id):
        try:
            plan = session.query(priceing).filter(priceing.id==id).first()
            if not plan:
                return False
            data = {
                "traffic": plan.traffic,
                "price": plan.price,
            }
            return data
        except:
            return False
price_query = PriceQuery()


# admins query
class AdminsQuery:
    def add_admin(self, user_name, password, traffic, inb_id):
        try:
            new_admin = admins(
                user_name=user_name,
                password=password,
                traffic=traffic,
                inb_id=inb_id
            )
            session.add(new_admin)
            session.commit()
            return True
        except:
            return False
        
    def change_inb(self, user_name, inb_id):
        try:
            update = session.query(admins).filter(admins.user_name==user_name).update({'inb_id':inb_id})
            session.commit()
            return True
        except:
            return False
        
    def add_traffic(self, user_name, traffic):
        try:
            admin = session.query(admins).filter(admins.user_name==user_name).first()
            if admin:
                admin.traffic += traffic
                session.commit()
                return True
            return False
        except:
            return False
        
    def delete_admin(self, user_name):
        try:
            delete = session.query(admins).filter(admins.user_name==user_name).first()
            session.delete(delete)
            session.commit()
            return True
        except:
            return False
        
    def show_admins(self):
        try:
            select_admins = session.query(admins).all()
            admins_list = [
                {"user_name": admin.user_name,"password":admin.password, "traffic": admin.traffic, "inb_id": admin.inb_id}
                for admin in select_admins
            ]
            return admins_list
        except:
            False

    def add_chat_id(self, user_name, password, chat_id):
        try:
            check = check = session.query(admins).filter_by(user_name=user_name, password=password).all()
            if check:
                update = session.query(admins).filter(admins.user_name==user_name).update({'chat_id':chat_id})
                session.commit()
                return True
            else:
                return False
        except:
            False
    
    def remove_chat_id(self, chat_id):
        try:
            update = session.query(admins).filter(admins.chat_id==chat_id).update({'chat_id':None})
            session.commit()
            return True
        except:
            return False
        
    def admin_data(self, chat_id):
        try:
            admin = session.query(admins).filter(admins.chat_id == chat_id).first()
            if not admin:
                return False
            data = {
                "user_name": admin.user_name,
                "password": admin.password,
                "traffic": admin.traffic,
                "inb_id": admin.inb_id
            }
            return data
        except:
            return False
        
    def reduce_traffic(self, chat_id, delta):
        try:
            admin_list = session.query(admins).filter(admins.chat_id==chat_id).all()
            if not admin_list:
                return False
            else:
                admin = admin_list[0]
                traffic = admin.traffic
                new_traffic = traffic + delta
                if new_traffic < 0:
                    new_traffic = 0
                session.query(admins).filter(admins.chat_id==chat_id).update({'traffic': new_traffic})
                session.commit()
                return True
        except:
            return False


        
    def admin_approval(self, chat_id):
        try:
            approv = session.query(admins).filter(admins.chat_id==chat_id).all()
            if approv:
                return True
            else:
                return False
        except:
            return False

admins_query = AdminsQuery()

