from fastapi import FastAPI, Path, Body, Depends
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Database setup
SQLALCHEMY_DATABASE_URL = "postgresql://twitter_clone_6ecg_user:acuzMrWei7et4n9Oqi0UjIYiaza51Izg@dpg-cq8ng0t6l47c73d1859g-a.oregon-postgres.render.com/twitter_clone_6ecg"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Car model
class Car(BaseModel):
    make: str
    model: str
    year: int
    price: float
    engine: Optional[str] = "V4"
    autonomous: bool
    sold: List[str]

# Database model
class CarDB(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    price = Column(Float)
    engine = Column(String)
    autonomous = Column(Boolean)
    sold = Column(ARRAY(String))

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"Welcome": "to JNNCE"}

@app.get("/cars")
def get_car_details(db: Session = Depends(get_db)):
    cars = db.query(CarDB).all()
    return cars

@app.get("/cars/{id}")
def get_car_by_id(id: int = Path(...), db: Session = Depends(get_db)):
    car = db.query(CarDB).filter(CarDB.id == id).first()
    return car

@app.post("/cars")
def add_cars(adding_cars: List[Car], db: Session = Depends(get_db)):
    for car in adding_cars:
        db_car = CarDB(**car.model_dump())
        db.add(db_car)
    db.commit()
    return {"message": "Cars added successfully"}

@app.put("/cars/{id}")
def update_car(id: int, car: Car, db: Session = Depends(get_db)):
    db_car = db.query(CarDB).filter(CarDB.id == id).first()
    for key, value in car.model_dump().items():
        setattr(db_car, key, value)
    db.commit()
    db.refresh(db_car)
    return db_car

@app.delete("/cars/{id}")
def delete_car(id: int, db: Session = Depends(get_db)):
    db_car = db.query(CarDB).filter(CarDB.id == id).first()
    db.delete(db_car)
    db.commit()
    return {"message": "Car deleted successfully"}
