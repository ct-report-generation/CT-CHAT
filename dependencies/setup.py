from setuptools import setup, find_packages

setup(
  name = 'dependencies',
  install_requires=[
    'accelerate',
    'einops>=0.6',
    'ema-pytorch>=0.2.2',
    'opencv-python',
    'pillow',
    'numpy',
    'sentencepiece',
    #'torch==2.0.1',
    'torchtyping',
    #'transformers==4.30.1',
    'tqdm',
    'vector-quantize-pytorch==1.1.2',
    'nibabel',
    'openpyxl',
    'beartype',
    'einops>=0.6',
    'ftfy',
    'regex',
    #'torch==2.0.1',
    'torchvision',
    "XlsxWriter",
    "h5py",
    "matplotlib",
    "seaborn",
    "wilds",
    'ImageNetV2_pytorch @ git+https://github.com/modestyachts/ImageNetV2_pytorch.git',
    "click",
    "appdirs",
    "attr",
    "nltk"
  ],
)
