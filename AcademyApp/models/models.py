from sqlalchemy import Column, Integer, String
from AcademyApp.config.database import Base


class Faq1(Base):
    __tablename__ = 'faq1'
    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)


class Faq2(Base):
    __tablename__ = 'faq2'
    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)


class Form(Base):
    __tablename__ = 'forms'
    id = Column(Integer, primary_key=True)
    fulname = Column(String, nullable=True)
    contact = Column(String, nullable=True)


class WhyUs(Base):
    __tablename__ = 'why_us'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image_url = Column(String, nullable=True)


class ServicesUs(Base):
    __tablename__ = 'services_us'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)


class Certificate(Base):
    __tablename__ = 'certificates'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image_url = Column(String, nullable=True)


class OurTeam(Base):
    __tablename__ = 'our_team'
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=True)
    title = Column(String, nullable=True)
    experience = Column(String, nullable=True)
    image_url = Column(String, nullable=True)



class Partners(Base):
    __tablename__ = 'partners'
    id = Column(Integer, primary_key=True)
    image_url = Column(String, nullable=True)
    url = Column(String, nullable=True)


class WebsiteCreate(Base):
    __tablename__ = 'website_create'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    image_url = Column(String, nullable=True)

