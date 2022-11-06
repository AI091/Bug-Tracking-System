
from controller import db 
from datetime import datetime
from sqlalchemy import Model ,Column , Integer , String , Text , DateTime , ForeignKey ,Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Model): 
    id = Column(Integer , primary_key= True)
    username = Column(String(20) , unique = True , nullable = False)
    email = Column(String(120) , unique = True , nullable = False)
    profile_pic = Column(String(20) , nullable = False , default = 'to_be_added')
    password = Column(String(60) , nullable = False)
    tickets = relationship('Ticket' , backref='author' , lazy=True)
    managed_projects = relationship('Projects' , backref= 'manager' , lazy =True ) 
    
    

    def __repr__(self): 
        return f"User('{self.username}',{self.email}' , {self.profile_pic}')"
    

class Ticket(Model):   
    id = Column(Integer , primary_key= True)
    title = Column(String(100), nullable = False)
    date_posted = Column(DateTime , nullable= False , default= datetime.utcnow )
    content = Column(Text , nullable = False)
    user_id = Column(Integer , ForeignKey('user.id'), nullable= False)
    
    def __repr__(self): 
        return f"Ticket('{self.title}',{self.date_posted}')"
    
association_table = Table(
    "association_table",
    Base.metadata,
    Column("left_id", ForeignKey("user.id")),
    Column("right_id", ForeignKey("project.id")),
)

class Project(Model): 
    id = Column(Integer , primary_key= True)
    title = Column(String(100), nullable = False)
    date_posted = Column(DateTime , nullable= False , default= datetime.utcnow )
    manager_id = Column(Integer , ForeignKey('user.id'), nullable= False)
    assigned_users = relationship("User", secondary=association_table)


