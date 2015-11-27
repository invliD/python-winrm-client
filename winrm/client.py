import re
from xml.etree import ElementTree

import pywsman

from winrm import uris
from winrm.error import WinRMError

class Client(object):

	def __init__(self, host, user, password, protocol='http', port=None, path='/wsman',
		timeout=30, verify_ssl=True):
		if port is None:
			if protocol == 'http':
				port = 5985
			elif protocol == 'https':
				port = 5986
		self.client = pywsman.Client(
			host,
			port,
			path,
			protocol,
			user,
			password,
		)
		self.client.transport().set_auth_method(pywsman.BASIC_AUTH_STR)
		self.client.transport().set_timeout(timeout)
		self.client.transport().set_verify_peer(verify_ssl)
		self.client.transport().set_verify_host(verify_ssl)

	def enumerate(self, cls):
		options = pywsman.ClientOptions()

		result = []

		resource_uri = cls.resource_uri()
		doc = self.client.enumerate(options, None, resource_uri)
		if doc is None:
			error_code = self.client.last_error()
			error_msg = self.client.transport().error_string(error_code)
			raise WinRMError(error_code, error_msg)
		root = _get_root(doc)
		result += self._parse_items(cls, root)

		while doc.context() is not None:
			doc = self.client.pull(options, None, resource_uri, str(doc.context()))
			root = _get_root(doc)
			result += self._parse_items(cls, root)

		return result

	def _parse_items(self, cls, root):
		items = root.find('.//{{{}}}Items'.format(uris.SOAP_ENUM_URI))
		if items is None:
			return []

		result = []
		for item in items:
			attributes = {}
			for attr in item:
				tag_name = re.sub(r'\{.*\}', '', attr.tag, 1)
				nil_str = attr.get('{{{}}}nil'.format(uris.XSI_URI))
				if nil_str == 'true':
					attributes[tag_name] = None
				else:
					attributes[tag_name] = attr.text
			obj = cls.from_dict(attributes)
			result.append(obj)
		return result


def _get_root(doc):
	root = doc.root()
	return ElementTree.fromstring(root.string())
