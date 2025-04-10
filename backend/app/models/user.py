from sqlalchemy import Column, Integer, String, Float, Enum, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class BodyType(str, enum.Enum):
    HOURGLASS = "hourglass"
    PEAR = "pear"
    APPLE = "apple"
    RECTANGLE = "rectangle"
    INVERTED_TRIANGLE = "inverted_triangle"

class StylePreference(str, enum.Enum):
    CASUAL = "casual"
    FORMAL = "formal"
    STREETWEAR = "streetwear"
    MINIMALIST = "minimalist"
    VINTAGE = "vintage"
    Y2K = "y2k"
    BOHEMIAN = "bohemian"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    profile = relationship("UserProfile", back_populates="user", uselist=False)
    wardrobe = relationship("WardrobeItem", back_populates="owner")

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Physical attributes
    gender = Column(String)
    height = Column(Float)  # in cm
    weight = Column(Float)  # in kg
    body_type = Column(Enum(BodyType))
    skin_tone = Column(String)
    measurements = Column(JSON)  # Store bust, waist, hip measurements
    
    # Style preferences
    preferred_styles = Column(JSON)  # List of StylePreference
    color_preferences = Column(JSON)  # List of preferred colors
    brand_preferences = Column(JSON)  # List of preferred brands
    
    # Virtual model
    virtual_model_path = Column(String, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="profile") 