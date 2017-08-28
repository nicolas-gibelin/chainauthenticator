from setuptools import setup

setup(
    name='jupyterhub-chainauthenticator',
    version='1.0',
    description='Chain Authenticator for JupyterHub',
    url='https://github.com/.../chainauthenticator',
    author='Nicolas Gibelin',
    author_email='Nicolas.Gibelin@univ-grenoble-alpes.fr',
    license='3 Clause BSD',
    packages=['chainauthenticator'],
    install_requires=[
        'jupyterhub',
    ]
)
