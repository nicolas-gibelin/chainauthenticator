# chainauthenticator

## Installation ##

You can install it from pip with:

```
```

## Usage ##

You can enable this authenticator with the following lines in your
`jupyter_config.py`:

```python
c.JupyterHub.authenticator_class = 'chainauthenticator.ChainAuthenticator'
```

#### `ChainAuthenticator.authenticators` ####

c.ChainAuthenticator.authenticators = [
  'casauthenticator.CASAuthenticator',
  'jupyterhub.auth.PAMAuthenticator',
]

