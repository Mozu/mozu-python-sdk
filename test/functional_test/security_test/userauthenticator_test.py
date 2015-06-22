import unittest
from mozurestsdk import mozuclient;
from mozurestsdk.security.userauthenticator import UserAuthenticator;
from mozurestsdk import util;

class UserAuthenticator_Test(unittest.TestCase):

	def setUp(self):
		self.config = util.readConfigFile("c:\projects\mozuconfig.txt");
		mozuclient.configure(config="c:\projects\mozuconfig.txt");

	def test_tenantAuth(self):
		userName = self.config.get("userName", None);
		password = self.config.get("password", None);
		tenantId = self.config.get("tenantId", None);
		userAuth = UserAuthenticator(userName, password,   tenantId=tenantId);
		userAuth.authenticate();
		userAuth.refreshAuth();
		self.assertIsNotNone(userAuth.auth);
		self.assertIsNotNone(userAuth.auth["accessToken"]);
		self.assertEqual(str(userAuth.auth["tenant"]["id"]), tenantId);

	def test_devAccountAuth(self):
		userName = self.config.get("userName", None);
		password = self.config.get("password", None);
		devAccountId = self.config.get("devAccountId", None);
		authUrl = self.config.get("baseAuthUrl", None);
		userAuth = UserAuthenticator(userName, password,  devAccountId=devAccountId);
		userAuth.authenticate();
		userAuth.refreshAuth();
		self.assertIsNotNone(userAuth.auth);
		self.assertIsNotNone(userAuth.auth["accessToken"]);
		self.assertEqual(str(userAuth.auth["account"]["id"]), devAccountId);
	

if __name__ == '__main__':
    unittest.main()
