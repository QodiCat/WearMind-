from sqlalchemy import Column, Integer, String, Float, Enum, JSON, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum
from datetime import datetime

class ClothingType(str, enum.Enum):
    TOP = "top"
    BOTTOM = "bottom"
    DRESS = "dress"
    OUTERWEAR = "outerwear"
    SHOES = "shoes"
    ACCESSORY = "accessory"

class Season(str, enum.Enum):
    SPRING = "spring"
    SUMMER = "summer"
    FALL = "fall"
    WINTER = "winter"
    ALL_SEASON = "all_season"

class WardrobeItem(Base):
    __tablename__ = "wardrobe_items"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    # Basic information
    name = Column(String)
    type = Column(Enum(ClothingType))
    brand = Column(String, nullable=True)
    purchase_date = Column(DateTime, nullable=True)
    purchase_price = Column(Float, nullable=True)
    
    # Visual attributes
    image_path = Column(String)
    color = Column(String)
    pattern = Column(String, nullable=True)
    material = Column(String)
    
    # Usage information
    seasons = Column(JSON)  # List of Season
    weather_conditions = Column(JSON)  # List of suitable weather conditions
    last_worn = Column(DateTime, nullable=True)
    wear_count = Column(Integer, default=0)
    
    # AI-generated metadata
    style_tags = Column(JSON)  # List of style tags
    color_palette = Column(JSON)  # List of colors in the item
    fit_type = Column(String)  # e.g., "slim", "regular", "loose"
    
    # Virtual try-on data
    virtual_model_path = Column(String, nullable=True)
    
    # Relationships
    owner = relationship("User", back_populates="wardrobe")
    outfits = relationship("Outfit", secondary="outfit_items", back_populates="items")

class Outfit(Base):
    __tablename__ = "outfits"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    name = Column(String)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_worn = Column(DateTime, nullable=True)
    wear_count = Column(Integer, default=0)
    
    # Style attributes
    style_tags = Column(JSON)
    occasion = Column(String)
    season = Column(Enum(Season))
    
    # AI-generated attributes
    confidence_score = Column(Float)  # AI's confidence in the outfit
    style_explanation = Column(String)  # AI's explanation of the style
    
    # Relationships
    items = relationship("WardrobeItem", secondary="outfit_items", back_populates="outfits")

# Association table for outfit items
class OutfitItem(Base):
    __tablename__ = "outfit_items"
    
    outfit_id = Column(Integer, ForeignKey("outfits.id"), primary_key=True)
    item_id = Column(Integer, ForeignKey("wardrobe_items.id"), primary_key=True)
    position = Column(Integer)  # Order of items in the outfit 