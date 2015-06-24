import logging
import unittest
from mozurestsdk import mozuclient
from mozurestsdk.platform.tenant import Tenant
from mozurestsdk.apiexception import ApiException;

class Tenant_Test(unittest.TestCase):

	def setUp(self):
		logging.basicConfig(level=logging.INFO);
		client = mozuclient.configure(config="c:\projects\mozuconfig.txt");

	def test_getTenantUnauthorized(self):
		try:
			tenant = Tenant().getTenant(1234);
		except ApiException as apiException:
			logging.error(apiException.message);
			self.assertEqual(apiException.errorCode, "UNAUTHORIZED");

	def test_getTenant(self):
		tenantId = 10236;
		try:
			tenant = Tenant().getTenant(tenantId);
			self.assertIsNotNone(tenant);
			self.assertEqual(tenantId, tenant["id"]);
		except ApiException as e:
			self.fail(e.message);

if __name__ == '__main__':
    unittest.main()
