from mozurestsdk.security.appauthenticator import default as default_auth;
from mozurestsdk.security.authenticationscope import AuthenticationScope;
#from mozurestsdk.config import __baseUrl__;
#from mozurestsdk import util;
from mozurestsdk.headers import Headers;
from mozurestsdk.platform.developer.developeradminuserauthticket import DeveloperAdminUserAuthTicket;
from mozurestsdk.platform.adminuser.tenantadminuserauthticket import TenantAdminUserAuthTicket;

class UserAuthenticator(object):
	"""Generate user claims for tenant or developer"""
	
	def __init__(self, username, password, tenantId = None, devAccountId = None):
		self.username = username;
		self.password = password;

		if (tenantId is not None):
			self.id = tenantId;
			self.scope = AuthenticationScope.Tenant;
		elif (devAccountId is not None):
			self.id = devAccountId;
			self.scope = AuthenticationScope.Developer;
		else:
			raise Exception("TenantId or Dev AccountId is needed for user authentication");
	

	def authenticate(self):
		#appAuth = default_auth();
		data = {"emailAddress" : self.username, "password" : self.password};
		#resourceUrl = None;
		if (self.scope is AuthenticationScope.Tenant):
			self.auth = TenantAdminUserAuthTicket().createUserAuthTicket(data, self.id);
			#resourceUrl = self.baseAuthUrl + "/api/platform/adminuser/authtickets/tenants?tenantId="+str(self.id);
		else:
			self.auth = DeveloperAdminUserAuthTicket().createDeveloperUserAuthTicket(data, self.id);
			#resourceUrl = self.baseAuthUrl + "/api/platform/developer/authtickets/?developerAccountId="+str(self.id);
		#headers = {};
		#headers[Headers.X_VOL_APP_CLAIMS] = appAuth.getAccessToken();
		
		#response = util.http_call(resourceUrl, "POST", data=data, headers=headers, verify=False);
		#self.auth = response.json();

	def refreshAuth(self):
		appAuth = default_auth();
		data = {"refreshToken" : self.auth["refreshToken"]};
		#resourceUrl = None;
		if (self.scope is AuthenticationScope.Tenant):
			self.auth = TenantAdminUserAuthTicket().refreshAuthTicket(data, self.id);
			#resourceUrl = self.baseAuthUrl + "/api/platform/adminuser/authtickets/tenants?tenantId="+str(self.id);
		else:
			self.auth = DeveloperAdminUserAuthTicket().refreshDeveloperAuthTicket(data, self.id);
			#resourceUrl = self.baseAuthUrl + "/api/platform/developer/authtickets/?developerAccountId="+str(self.id);
		#headers = {};
		#headers[Headers.X_VOL_APP_CLAIMS] = appAuth.getAccessToken();
		#data = {"refreshToken" : self.auth["refreshToken"]};
		#response = util.http_call(resourceUrl, "PUT", data=data, headers=headers, verify=False);
		#self.auth = response.json();

	def getAccessToken(self):
		accessTokenExpiry =  datetime.datetime.strptime(self.auth["accessTokenExpiration"],'%Y-%m-%dT%H:%M:%S.%fZ');
		refreshTokenExpiry = datetime.datetime.strptime(self.auth["refreshTokenExpiration"],'%Y-%m-%dT%H:%M:%S.%fZ');
		timeNow = datetime.datetime.utcnow() + datetime.timedelta(0,180);
		if ( timeNow > refreshTokenExpiry):
			self.authenticate();
		elif ( timeNow > accessTokenExpiry):
			self.refreshAuth();	
		return self.auth["accessToken"];