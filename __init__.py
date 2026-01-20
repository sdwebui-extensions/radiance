"""
═══════════════════════════════════════════════════════════════════════════════
                    FXTD STUDIO RADIANCE
              Professional HDR Image Processing Suite
                     FXTD Studios © 2024-2026
                     
GPU-accelerated nodes for HDR, color grading, film effects, and upscaling.
═══════════════════════════════════════════════════════════════════════════════
"""

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# ═══════════════════════════════════════════════════════════════════════════════
#                       DEPENDENCY VALIDATION
# ═══════════════════════════════════════════════════════════════════════════════

# Import all node modules
from .nodes_hdr import NODE_CLASS_MAPPINGS as HDR_NODES, NODE_DISPLAY_NAME_MAPPINGS as HDR_NAMES
from .nodes_grade import NODE_CLASS_MAPPINGS as GRADE_NODES, NODE_DISPLAY_NAME_MAPPINGS as GRADE_NAMES
from .nodes_upscale import NODE_CLASS_MAPPINGS as UPSCALE_NODES, NODE_DISPLAY_NAME_MAPPINGS as UPSCALE_NAMES
from .nodes_filmgrain import NODE_CLASS_MAPPINGS as FILM_NODES, NODE_DISPLAY_NAME_MAPPINGS as FILM_NAMES
from .nodes_exr import NODE_CLASS_MAPPINGS as EXR_NODES, NODE_DISPLAY_NAME_MAPPINGS as EXR_NAMES
from .nodes_prompt import FXTDCinematicPromptEncoder
from .nodes_camera import NODE_CLASS_MAPPINGS as CAMERA_NODES, NODE_DISPLAY_NAME_MAPPINGS as CAMERA_NAMES
from .nodes_sampler import NODE_CLASS_MAPPINGS as SAMPLER_NODES, NODE_DISPLAY_NAME_MAPPINGS as SAMPLER_NAMES
from .nodes_radiance_viewer import NODE_CLASS_MAPPINGS as RADIANCE_VIEWER_NODES, NODE_DISPLAY_NAME_MAPPINGS as RADIANCE_VIEWER_NAMES
from .nodes_help import NODE_CLASS_MAPPINGS as HELP_NODES, NODE_DISPLAY_NAME_MAPPINGS as HELP_NAMES
from .nodes_depth import NODE_CLASS_MAPPINGS as DEPTH_NODES, NODE_DISPLAY_NAME_MAPPINGS as DEPTH_NAMES


# ═══════════════════════════════════════════════════════════════════════════════
#                       WEB EXTENSION DIRECTORY
# ═══════════════════════════════════════════════════════════════════════════════
# This tells ComfyUI to load JavaScript extensions from our js/ folder
WEB_DIRECTORY = "./js"

# Merge all node mappings
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# Add HDR nodes
NODE_CLASS_MAPPINGS.update(HDR_NODES)
NODE_DISPLAY_NAME_MAPPINGS.update(HDR_NAMES)

# Add Grade node (Color Grading)
NODE_CLASS_MAPPINGS.update(GRADE_NODES)
NODE_DISPLAY_NAME_MAPPINGS.update(GRADE_NAMES)


# Add Radiance Viewer (VFX Industry Standard)
NODE_CLASS_MAPPINGS.update(RADIANCE_VIEWER_NODES)
NODE_DISPLAY_NAME_MAPPINGS.update(RADIANCE_VIEWER_NAMES)

# Add Upscale nodes
NODE_CLASS_MAPPINGS.update(UPSCALE_NODES)
NODE_DISPLAY_NAME_MAPPINGS.update(UPSCALE_NAMES)

# Add Film grain nodes
NODE_CLASS_MAPPINGS.update(FILM_NODES)
NODE_DISPLAY_NAME_MAPPINGS.update(FILM_NAMES)

# Add EXR nodes
NODE_CLASS_MAPPINGS.update(EXR_NODES)
NODE_DISPLAY_NAME_MAPPINGS.update(EXR_NAMES)

# Add Camera simulation nodes
NODE_CLASS_MAPPINGS.update(CAMERA_NODES)
NODE_DISPLAY_NAME_MAPPINGS.update(CAMERA_NAMES)

# Add Sampler nodes
NODE_CLASS_MAPPINGS.update(SAMPLER_NODES)
NODE_DISPLAY_NAME_MAPPINGS.update(SAMPLER_NAMES)

# Add Prompt nodes
NODE_CLASS_MAPPINGS.update({
    "FXTDCinematicPromptEncoder": FXTDCinematicPromptEncoder,
})
NODE_DISPLAY_NAME_MAPPINGS.update({
    "FXTDCinematicPromptEncoder": "🎬 Radiance Cinematic Encoder",
})

# Add Help node
NODE_CLASS_MAPPINGS.update(HELP_NODES)
NODE_DISPLAY_NAME_MAPPINGS.update(HELP_NAMES)

# Add Depth Map Generator
NODE_CLASS_MAPPINGS.update(DEPTH_NODES)
NODE_DISPLAY_NAME_MAPPINGS.update(DEPTH_NAMES)





# Add DNA nodes (Signature Architecture)
from .nodes_dna import FXTDDNAReader
NODE_CLASS_MAPPINGS.update({
    "FXTD_DNA_Reader": FXTDDNAReader
})
NODE_DISPLAY_NAME_MAPPINGS.update({
    "FXTD_DNA_Reader": "🧬 Radiance DNA Reader"
})

# Add Resolution node (Industry-standard presets)
from .nodes_resolution import NODE_CLASS_MAPPINGS as RESOLUTION_NODES, NODE_DISPLAY_NAME_MAPPINGS as RESOLUTION_NAMES
NODE_CLASS_MAPPINGS.update(RESOLUTION_NODES)
NODE_DISPLAY_NAME_MAPPINGS.update(RESOLUTION_NAMES)


# Add Radiance Unified Loader
from .nodes_loader import NODE_CLASS_MAPPINGS as LOADER_NODES, NODE_DISPLAY_NAME_MAPPINGS as LOADER_NAMES
NODE_CLASS_MAPPINGS.update(LOADER_NODES)
NODE_DISPLAY_NAME_MAPPINGS.update(LOADER_NAMES)


# Package info
__version__ = "1.0.0"
__author__ = "FXTD Studios"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']

print(f"[FXTDStudio Radiance] Loaded {len(NODE_CLASS_MAPPINGS)} nodes (v{__version__})")
print(f"[FXTDStudio Radiance] Radiance Viewer JavaScript extension enabled")
