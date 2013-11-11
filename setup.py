from setuptools import setup

setup(
    name='Plotrique',
    version='0.0.1',
    author='Juraj Niznan',
    author_email='jniznan@redhat.com',
    packages=['plotrique'],
    scripts=[],
    description='Convenience plotting tools.',
    install_requires=[
        "pandas >= 0.12.0",
    ],
)
