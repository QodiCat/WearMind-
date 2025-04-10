import torch
from diffusers import StableDiffusionPipeline, ControlNetModel, UniPCMultistepScheduler
from diffusers.utils import load_image
import numpy as np
from PIL import Image
from typing import List, Dict, Any
import os

class VirtualTryOnService:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.controlnet = self._load_controlnet()
        self.pipeline = self._load_pipeline()
        
    def _load_controlnet(self) -> ControlNetModel:
        """Load ControlNet model for pose and body shape control."""
        controlnet = ControlNetModel.from_pretrained(
            "lllyasviel/ControlNet",
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        return controlnet.to(self.device)
    
    def _load_pipeline(self) -> StableDiffusionPipeline:
        """Load Stable Diffusion pipeline with ControlNet."""
        pipeline = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            controlnet=self.controlnet,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        pipeline.scheduler = UniPCMultistepScheduler.from_config(pipeline.scheduler.config)
        pipeline = pipeline.to(self.device)
        return pipeline
    
    def generate_tryon(
        self,
        person_image: str,
        clothing_image: str,
        prompt: str = "A person wearing the clothing item",
        negative_prompt: str = "ugly, blurry, bad anatomy, bad proportions",
        num_inference_steps: int = 20,
        guidance_scale: float = 7.5
    ) -> Image.Image:
        """Generate virtual try-on image."""
        # Load and preprocess images
        person_img = load_image(person_image)
        clothing_img = load_image(clothing_image)
        
        # Generate control image (pose estimation)
        control_image = self._get_control_image(person_img)
        
        # Generate try-on image
        image = self.pipeline(
            prompt=prompt,
            image=control_image,
            clothing_image=clothing_img,
            negative_prompt=negative_prompt,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale
        ).images[0]
        
        return image
    
    def _get_control_image(self, image: Image.Image) -> Image.Image:
        """Generate control image for pose and body shape."""
        # Convert to numpy array
        img_array = np.array(image)
        
        # Apply pose estimation (simplified version)
        # In practice, you would use a proper pose estimation model
        control_img = self._simulate_pose_estimation(img_array)
        
        return Image.fromarray(control_img)
    
    def _simulate_pose_estimation(self, image: np.ndarray) -> np.ndarray:
        """Simulate pose estimation (placeholder for actual pose estimation)."""
        # This is a simplified version
        # In practice, you would use OpenPose or similar
        height, width = image.shape[:2]
        control_img = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Draw skeleton-like lines
        cv2.line(control_img, (width//2, 0), (width//2, height), (255, 255, 255), 2)
        cv2.line(control_img, (width//2, height//3), (width//4, height//2), (255, 255, 255), 2)
        cv2.line(control_img, (width//2, height//3), (3*width//4, height//2), (255, 255, 255), 2)
        cv2.line(control_img, (width//2, 2*height//3), (width//4, height), (255, 255, 255), 2)
        cv2.line(control_img, (width//2, 2*height//3), (3*width//4, height), (255, 255, 255), 2)
        
        return control_img
    
    def generate_video(
        self,
        person_image: str,
        clothing_image: str,
        num_frames: int = 30,
        output_path: str = "output.mp4"
    ) -> None:
        """Generate try-on video with different poses."""
        frames = []
        
        for i in range(num_frames):
            # Generate frame with slightly different pose
            frame = self.generate_tryon(
                person_image,
                clothing_image,
                prompt=f"A person wearing the clothing item, pose {i+1}/{num_frames}"
            )
            frames.append(frame)
        
        # Save as video
        self._save_frames_as_video(frames, output_path)
    
    def _save_frames_as_video(
        self,
        frames: List[Image.Image],
        output_path: str,
        fps: int = 30
    ) -> None:
        """Save frames as video file."""
        import cv2
        import numpy as np
        
        # Get frame dimensions
        width, height = frames[0].size
        
        # Create video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        
        # Write frames
        for frame in frames:
            # Convert PIL Image to OpenCV format
            frame_cv = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
            video.write(frame_cv)
        
        # Release video writer
        video.release() 