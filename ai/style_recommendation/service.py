import torch
import torch.nn as nn
import numpy as np
from typing import List, Dict, Any
import os
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

class StyleRecommendationService:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self._load_model()
        self.scaler = StandardScaler()
        self.style_clusters = None
        
        # Style categories
        self.style_categories = {
            "casual": 0,
            "formal": 1,
            "streetwear": 2,
            "minimalist": 3,
            "vintage": 4,
            "y2k": 5,
            "bohemian": 6
        }
        
        # Color compatibility rules
        self.color_rules = {
            "red": ["black", "white", "navy", "gray"],
            "blue": ["white", "gray", "black", "beige"],
            "green": ["white", "black", "brown", "gray"],
            "yellow": ["black", "white", "gray", "navy"],
            "black": ["white", "gray", "red", "blue"],
            "white": ["black", "navy", "red", "gray"],
            "gray": ["black", "white", "navy", "red"],
            "brown": ["beige", "white", "black", "navy"],
            "pink": ["white", "black", "gray", "navy"],
            "purple": ["white", "black", "gray", "navy"]
        }
    
    def _load_model(self) -> nn.Module:
        """Load pre-trained style recommendation model."""
        model = StyleNet()
        model.load_state_dict(torch.load("models/style_recommender.pth"))
        model = model.to(self.device)
        model.eval()
        return model
    
    def recommend_outfits(
        self,
        user_profile: Dict[str, Any],
        weather: Dict[str, Any],
        occasion: str,
        num_recommendations: int = 5
    ) -> List[Dict[str, Any]]:
        """Generate outfit recommendations based on user profile and context."""
        # Prepare input features
        features = self._prepare_features(user_profile, weather, occasion)
        
        # Get style predictions
        with torch.no_grad():
            features_tensor = torch.FloatTensor(features).unsqueeze(0).to(self.device)
            style_scores = self.model(features_tensor)
            style_probs = torch.softmax(style_scores, dim=1)
        
        # Get top style categories
        top_styles = torch.topk(style_probs, k=3, dim=1)[1].squeeze().tolist()
        
        # Generate outfit recommendations
        recommendations = []
        for style_idx in top_styles:
            style_name = list(self.style_categories.keys())[style_idx]
            outfits = self._generate_outfits_for_style(
                style_name,
                user_profile,
                weather,
                occasion,
                num_recommendations
            )
            recommendations.extend(outfits)
        
        return recommendations[:num_recommendations]
    
    def _prepare_features(
        self,
        user_profile: Dict[str, Any],
        weather: Dict[str, Any],
        occasion: str
    ) -> np.ndarray:
        """Prepare input features for the model."""
        # Combine user profile, weather, and occasion features
        features = []
        
        # User profile features
        features.extend([
            user_profile.get("height", 0),
            user_profile.get("weight", 0),
            self.style_categories.get(user_profile.get("preferred_style", "casual"), 0)
        ])
        
        # Weather features
        features.extend([
            weather.get("temperature", 20),
            weather.get("humidity", 50),
            weather.get("precipitation", 0)
        ])
        
        # Occasion feature
        features.append(self._get_occasion_score(occasion))
        
        return np.array(features)
    
    def _get_occasion_score(self, occasion: str) -> float:
        """Convert occasion to numerical score."""
        occasion_scores = {
            "casual": 0.0,
            "business_casual": 0.3,
            "business": 0.6,
            "formal": 0.9
        }
        return occasion_scores.get(occasion.lower(), 0.0)
    
    def _generate_outfits_for_style(
        self,
        style: str,
        user_profile: Dict[str, Any],
        weather: Dict[str, Any],
        occasion: str,
        num_outfits: int
    ) -> List[Dict[str, Any]]:
        """Generate outfit combinations for a specific style."""
        outfits = []
        
        # Get user's wardrobe items
        wardrobe_items = user_profile.get("wardrobe", [])
        
        # Filter items by style
        style_items = [
            item for item in wardrobe_items
            if style in item.get("style_tags", [])
        ]
        
        # Generate outfit combinations
        for _ in range(num_outfits):
            outfit = self._create_outfit(
                style_items,
                style,
                weather,
                occasion
            )
            if outfit:
                outfits.append(outfit)
        
        return outfits
    
    def _create_outfit(
        self,
        items: List[Dict[str, Any]],
        style: str,
        weather: Dict[str, Any],
        occasion: str
    ) -> Dict[str, Any]:
        """Create a single outfit combination."""
        # Select items based on weather and occasion
        temperature = weather.get("temperature", 20)
        
        outfit = {
            "top": None,
            "bottom": None,
            "outerwear": None,
            "shoes": None,
            "accessories": []
        }
        
        # Select top
        tops = [item for item in items if item["category"] == "top"]
        if tops:
            outfit["top"] = np.random.choice(tops)
        
        # Select bottom
        bottoms = [item for item in items if item["category"] == "bottom"]
        if bottoms:
            outfit["bottom"] = np.random.choice(bottoms)
        
        # Select outerwear based on temperature
        if temperature < 15:
            outerwear = [item for item in items if item["category"] == "outerwear"]
            if outerwear:
                outfit["outerwear"] = np.random.choice(outerwear)
        
        # Select shoes
        shoes = [item for item in items if item["category"] == "shoes"]
        if shoes:
            outfit["shoes"] = np.random.choice(shoes)
        
        # Select accessories
        accessories = [item for item in items if item["category"] == "accessory"]
        if accessories:
            num_accessories = min(3, len(accessories))
            outfit["accessories"] = list(np.random.choice(
                accessories,
                size=num_accessories,
                replace=False
            ))
        
        # Add style explanation
        outfit["style_explanation"] = self._generate_style_explanation(
            outfit,
            style,
            weather,
            occasion
        )
        
        return outfit
    
    def _generate_style_explanation(
        self,
        outfit: Dict[str, Any],
        style: str,
        weather: Dict[str, Any],
        occasion: str
    ) -> str:
        """Generate explanation for the outfit style."""
        temperature = weather.get("temperature", 20)
        
        explanation = f"This {style} outfit is perfect for {occasion}. "
        
        if temperature < 15:
            explanation += "The outerwear keeps you warm while maintaining style. "
        
        if outfit.get("accessories"):
            explanation += "The accessories add a stylish touch. "
        
        return explanation.strip()

class StyleNet(nn.Module):
    def __init__(self, input_size: int = 7, hidden_size: int = 64, num_classes: int = 7):
        super(StyleNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
    
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)
        return x 