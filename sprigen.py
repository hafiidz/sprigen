import torch
import numpy as np
import rembg
from PIL import Image

# Define helper functions
# Tensor to PIL and PIL to Tensor functions are copied from MIT licensed repo by WASasquatch at https://github.com/WASasquatch/was-node-suite-comfyui/blob/main/WAS_Node_Suite.py

# Tensor to PIL
def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
    
# PIL to Tensor
def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class SprigenRemBG:
    @classmethod
    def INPUT_TYPES(s):
        return {
                    "required": {
                        "image": ("IMAGE", ),
                    },
                }

    RETURN_TYPES = ("IMAGE", )
    RETURN_NAMES = ("Image", )  
    FUNCTION = "rembg_remove_background"
    CATEGORY = "Sprigen/Image"

    def rembg_remove_background(self, image,):
        # convert to PIL
        image_pil = tensor2pil(image)
        # remove background
        image_rembg = rembg.remove(image_pil)
        # re-convert to tensor
        image_tensor = pil2tensor(image_rembg)
        return (image_tensor,)


# Register nodes in ComfyUI
NODE_CLASS_MAPPINGS = {
    "SprigenRemBG": SprigenRemBG,
}

# Human readable names for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "SprigenRemBG": "Sg Remove Background",
}