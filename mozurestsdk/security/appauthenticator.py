import datetime;
import logging;
import json;
from mozurestsdk import util;


class AppAuthenticator(object):
	
	def __init__(self,applicationKey, sharedSecret, authUrl, verifySSL):
		self.applicationKey = applicationKey;
		self.sharedSecret = sharedSecret;
		self.authUrl = authUrl;
		self.verifySSL = verifySSL;

	def authenticate(self):
		auth_url = self.authUrl + "/api/platform/applications/authtickets";
		headers = {'Content-type': 'application/json', 'Accept-Encoding': 'gzip, deflate'}
		auth_request = {'applicationId' : self.applicationKey, 'sharedSecret' : self.sharedSecret};
		
		auth_response = util.http_call(auth_url,"POST", data=json.dumps(auth_request), headers=headers, verify=self.verifySSL);
		self.auth = auth_response.json();
		logging.info("Auth Token : %s" % self.auth["accessToken"]);
		logging.info("Refresh Token : %s" % self.auth["refreshToken"]);
		logging.info("Access Token Expiration: %s" % self.auth["accessTokenExpiration"])
		logging.info("Refresh Token Expiration: %s" % self.auth["refreshTokenExpiration"])

	def refreshAuth(self):
		auth_url = self.authUrl + "/api/platform/applications/authtickets/refresh-ticket";
		headers = {'Content-type': 'application/json', 'Accept-Encoding': 'gzip, deflate'}
		auth_request = {'refreshToken' : self.auth["refreshToken"]};
		
		auth_response = util.http_call(auth_url,"PUT", data=json.dumps(auth_request), headers=headers, verify=self.verifySSL);
		self.auth = auth_response.json();

	def getAccessToken(self):
		accessTokenExpiry =  datetime.datetime.strptime(self.auth["accessTokenExpiration"],'%Y-%m-%dT%H:%M:%S.%fZ');
		refreshTokenExpiry = datetime.datetime.strptime(self.auth["refreshTokenExpiration"],'%Y-%m-%dT%H:%M:%S.%fZ');
		timeNow = datetime.datetime.utcnow() + datetime.timedelta(0,180);
		if ( timeNow > refreshTokenExpiry):
			self.authenticate();
		elif ( timeNow > accessTokenExpiry):
			self.refreshAuth();	
		return self.auth["accessToken"];