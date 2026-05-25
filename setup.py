from setuptools import setup, find_packages

setup(
    name="brain_tumor_classification",
    version="1.0.0",
    author="Manu",
    description="Hybrid Deep Learning and Machine Learning Framework for Brain Tumor Classification using MRI Images",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "opencv-python",
        "scikit-learn",
        "xgboost",
        "tensorflow",
        "keras",
        "torch",
        "torchvision",
        "tqdm",
        "Pillow",
        "joblib",
        "albumentations",
        "efficientnet_pytorch"
    ],
    python_requires=">=3.9",
)