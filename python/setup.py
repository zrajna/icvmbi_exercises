# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


long_description = (here / "README.md").read_text(encoding="utf-8")

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name="icvmbi_exercises",  # Required
    version="0.0.1",  # Required
    description="ICVMBI exercises",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/zrajna/icvmbi_exercises",  # Optional
    author="Zalan Rajna",  # Optional
    author_email="zalan.rajna@oulu.fi",  # Optional
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Image Processing",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    # packages=find_packages(where='.'),  # Required
    py_modules=["ex1", "ex1_functions", "ex2", "ex2_functions", "ex3", "ex3_functions"],
    python_requires=">=3.5, <4",
    install_requires=["numpy"],  # Optional
    entry_points={  # Optional
        "console_scripts": [
            "icvmbi_ex1=ex1:main",
            "icvmbi_ex2=ex2:main",
            "icvmbi_ex3=ex3:main",
        ]
    },
)
