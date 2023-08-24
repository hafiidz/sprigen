# SpriGen

Sprigen (Sprite Generator): AI 2D game asset generator

## Status

Currently in public beta stages
## Requirements

1. [ComfyUI](https://github.com/comfyanonymous/ComfyUI) installed
1. GPU with 8GB VRAM recommended

## Installation steps

0. This project is a custom workflow and should be installed within path/to/ComfyUI/custom_nodes folder
1. Navigate to ComfyUI/custom_nodes folder via terminal
1. Run `git clone https://github.com/hafiidz/sprigen.git sprigen` to clone this repository to the local folder
1. Navigate to sprigen folder via `cd sprigen`
1. Run `install.bat`
1. Alternatively, you can manually Install `rembg[gpu]` library as per details [below](##alternative-steps)
1. Open ComfyUI via `run_nvidia_gpu.bat`
1. Load `rembg` workflow by clicking Load button and navigate to `path/to/ComfyUI/custom_nodes/sprigen/workflow/remb.json`

## Alternative steps
1. Run `"path\to\ComfUI\python_embeded\python.exe" -s -m pip install rembg[gpu]`. See details for rembg version and installation guide at https://github.com/danielgatis/rembg#installation. Note to include double quote `"` on the path if there is spaces in one of the folders along the path and the typo (embeded instead of embedded as per ComfyUI current path naming, as of July 2023)

## Target Features

SpriGen aims to address 2D game asset generation with the following features:

1. MVP focus on basic character generation. Assets is in png with associated text file map.

## Example assets

Example assets as follows (note: that this example will be replaced with actual AI Generated image, placeholder example game assets from https://github.com/fishfolk/jumpy)

![Example Assets](https://user-images.githubusercontent.com/24392180/151969075-399e9fea-e2de-4340-96a4-0a0e5b79c281.gif)

## Acknowledgements

Some of the code snippets and functions are copied over from  custom_nodes repo by WASasquatch at https://github.com/WASasquatch/was-node-suite-comfyui/blob/main/WAS_Node_Suite.py [MIT License]
