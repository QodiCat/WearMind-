import torch
import torchvision
import cv2
import numpy as np
from PIL import Image
from typing import List, Dict, Any
import os

class ClothingRecognitionService:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self._load_model()
        self.preprocess = torchvision.transforms.Compose([
            torchvision.transforms.Resize(256),
            torchvision.transforms.CenterCrop(224),
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])
        
        # Clothing categories
        self.categories = {
            0: "top",
            1: "bottom",
            2: "dress",
            3: "outerwear",
            4: "shoes",
            5: "accessory"
        }
        
        # Color names
        self.colors = {
            "red": (255, 0, 0),
            "blue": (0, 0, 255),
            "green": (0, 255, 0),
            "yellow": (255, 255, 0),
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "gray": (128, 128, 128),
            "brown": (165, 42, 42),
            "pink": (255, 192, 203),
            "purple": (128, 0, 128)
        }

    def _load_model(self) -> torch.nn.Module:
        """Load pre-trained ResNet model for clothing classification."""
        model = torchvision.models.resnet50(pretrained=True)
        # Modify the last layer for our clothing categories
        num_ftrs = model.fc.in_features
        model.fc = torch.nn.Linear(num_ftrs, len(self.categories))
        model.load_state_dict(torch.load("models/clothing_classifier.pth"))
        model = model.to(self.device)
        model.eval()
        return model

    def detect_clothing(self, image_path: str) -> Dict[str, Any]:
        """Detect and classify clothing in an image."""
        # Load and preprocess image
        image = Image.open(image_path).convert('RGB')
        input_tensor = self.preprocess(image)
        input_batch = input_tensor.unsqueeze(0).to(self.device)

        # Get model predictions
        with torch.no_grad():
            output = self.model(input_batch)
            probabilities = torch.nn.functional.softmax(output[0], dim=0)
            category_idx = torch.argmax(probabilities).item()
            confidence = probabilities[category_idx].item()

        # Get dominant colors
        colors = self._get_dominant_colors(image_path)

        # Get pattern
        pattern = self._detect_pattern(image_path)

        return {
            "category": self.categories[category_idx],
            "confidence": confidence,
            "colors": colors,
            "pattern": pattern
        }

    def _get_dominant_colors(self, image_path: str, num_colors: int = 3) -> List[str]:
        """Extract dominant colors from the image."""
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Reshape the image to be a list of pixels
        pixels = image.reshape(-1, 3)
        
        # Perform k-means clustering
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
        _, labels, centers = cv2.kmeans(
            np.float32(pixels),
            num_colors,
            None,
            criteria,
            10,
            cv2.KMEANS_RANDOM_CENTERS
        )
        
        # Convert centers to RGB
        centers = np.uint8(centers)
        
        # Find closest color names
        dominant_colors = []
        for color in centers:
            min_dist = float('inf')
            closest_color = None
            for name, rgb in self.colors.items():
                dist = np.linalg.norm(color - rgb)
                if dist < min_dist:
                    min_dist = dist
                    closest_color = name
            dominant_colors.append(closest_color)
        
        return dominant_colors

    def _detect_pattern(self, image_path: str) -> str:
        """Detect patterns in the clothing."""
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply edge detection
        edges = cv2.Canny(gray, 100, 200)
        
        # Calculate pattern features
        edge_density = np.sum(edges) / (edges.shape[0] * edges.shape[1])
        
        if edge_density > 0.3:
            return "patterned"
        else:
            return "solid"

    def remove_background(self, image_path: str, output_path: str) -> None:
        """Remove background from clothing image."""
        image = cv2.imread(image_path)
        
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply threshold
        _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
        
        # Create transparent background
        b, g, r = cv2.split(image)
        rgba = [b, g, r, mask]
        dst = cv2.merge(rgba, 4)
        
        # Save result
        cv2.imwrite(output_path, dst) 