import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='afdcli',  
    version='0.3.1',
    scripts=['bin/afdcli'] ,
    author="Yaman Özakin",
    author_email="",
    description="Seismic waveform downloading client",
    include_package_data=True,
    package_data={
        "": ['params.py','save_params.py'],
    },
    install_requires=[
        'requests',
        'numpy',
        'obspy',
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maratumba/afdcli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
    ],
 )