#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/10/5 16:00
# @Author:boyizhang
# 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

# make sure you're logged in with `huggingface-cli login`
from torch import autocast
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=True)


# pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
# pipe = StableDiffusionPipeline.from_pretrained("./stable-diffusion-v1-4")

pipe = pipe.to("cuda")

prompt = "a photo of an astronaut riding a horse on mars"
with autocast("cuda"):
    image = pipe(prompt).images[0]
    # b%6mT4bZs8@cz6A