from setuptools import setup, find_packages

with open('PYPI_SUMMARY.md', 'r') as f:
    long_description = f.read()

setup(name='qvantum',
    version='0.97',
    description='Python package for quantum computing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/vorpex/qvantum',
    author='Adam Sohonyai & Roland Sztaho',
    author_email='sohonyai.adam@gmail.com',
    maintainer='Adam Sohonyai',
    maintainer_email='sohonyai.adam@gmail.com',
    license='MIT',
    keywords='python quantum computing process',
    packages=find_packages(),
    # scripts=['bloch.py', 'check_bloch.py', 'check_circuit.py', 'check_gate.py', 'check_layer.py', \
    #     'check_qubit.py', 'check_register.py', 'circuit.py', 'gate.py', 'layer.py', 'qubit.py', \
    #     'register.py'],
    # install_requires=['collections', 'itertools', 'math', 'matplotlib', 'mpl_toolkits', 'numpy', 'unicodedata'],
    install_requires=['matplotlib', 'numpy'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'],
    zip_safe=False)
