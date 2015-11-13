# python-winrm-client

This Python package provides a convenient interface to WinRM using the WSMan SOAP protocol.

## Usage
### Create a client
```python
from winrm import Client

client = Client('hostname', 'user', 'password')
```

### Create a client using HTTPS
```python
client = Client('hostname', 'user', 'password', protocol='https')
```

### Enumerate a class
```python
from winrm.models import Volume

volumes = client.enumerate(Volume)
```

## Contributing
If you want to contribute to this project:

- Fork the repository
- Hack your changes
- Submit a Pull Request
