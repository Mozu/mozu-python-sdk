import logging
import json
import configparser
from urllib.parse import urlparse;
from mozurestsdk.headers import Headers;
from mozurestsdk.security.appauthenticator import AppAuthenticator
from mozurestsdk import util
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.config import __basePciUrl__, __baseUrl__
from mozurestsdk.apicontext import ApiContext;

class MozuClient(object):
	__headers = {};
	__verb = None;
	__body = None;
	__resourceUrl = None;
	__baseAddress = None;
	__scheme = "https";
	__apiContext = None;
	__contentType = "application/json";
	__isJsonBody = True;

	def __init__(self, options=None, **args):
		"""Create Mozu Client object

		Usage::
			>>> import mozurestsdk
			>>> client = mozurestsdk.MozuClient(applicationKey='appKey', shareSecret='sharedsecret')
			>>> or
			>>> client = mozurestsdk.MozuClient(configFile='path to config')
		"""

		args = util.merge_dict(options or {}, args);

		configFile = args.get("config", None);
		if (configFile != None):
			config = configparser.ConfigParser();
			config.optionxform=str
			config.read(configFile);
			logging.info("Getting values from configFile : %s" % configFile);
			args = util.merge_dict(util.configSectionToDict(config, "MozuConfig") or {}, args)
			
		self.applicationKey = args.get("applicationKey", None);
		self.sharedSecret = args.get("sharedSecret", None);

		self.verifySSLCert = args.get("verifySSLCert", True) == 'True';
		if (self.applicationKey == None or self.sharedSecret == None):
			raise Exception("applicationKey or sharedSecret is missing");

		self.baseAuthUrl = args.get("baseAuthUrl", __baseUrl__);
		authScheme = urlparse(self.baseAuthUrl).scheme;
		if (not authScheme):
			self.__scheme = urlparse(self.baseAuthUrl).scheme;
		self.basePCIUrl = args.get("basePCIUrl", __basePciUrl__);
		self.appAuth = AppAuthenticator(self.applicationKey, self.sharedSecret, self.baseAuthUrl);
		self.appAuth.authenticate();
	
		tenantId = args.get("tenantId", None);
		if (tenantId is not None):
			self.__apiContext = ApiContext(**args);

	def withVerb(self, verb):
		self.verb = verb;
		return self;
		
	def withApiContext(self, apiContext: ApiContext):
		if (self.__apiContext is not None):
			apiContext = util.mergeProperties(self.__apiContext, apiContext);

		self.apicontext = apiContext;
		if (apiContext.tenantId is not None):
			self.__headers[Headers.X_VOL_TENANT] = apiContext.tenantId

		if (apiContext.siteId is not None):
			self.__headers[Headers.X_VOL_SITE] = apiContext.siteId;

		if (apiContext.catalogId is not None):
			self.__headers[Headers.X_VOL_CATALOG] = apiContext.catalogId;

		if (apiContext.masterCatalogId is not None):
			self.__headers[Headers.X_VOL_MASTER_CATALOG] = apiContext.masterCatalogId;

		if (apiContext.locale is not None):
			self.__headers[Headers.X_VOL_LOCALE] = apiContext.locale;

		if (apiContext.currency is not None):
			self.__headers[Headers.X_VOL_CURRENCY] = apiContext.currency;

		if (apiContext.dataViewMode is not None):
			self.__headers[Headers.X_VOL_DATAVIEW_MODE] = apiContext.dataViewMode;

		return self;

	def withHeader(self, header, value):
		self.__headers[header] = value;
		return self;

	def withUserClaim(self, userClaim):
		self.__headers[Headers.X_VOL_USER_CLAIMS] = userClaim;
		return self;

	def withBody(self, body):
		self.__body = body;
		return self;

	def withResourceUrl(self, url: MozuUrl):
		self.__resourceUrl = url;
		return self;

	def withContentType(self, contentType):
		self.__contentType = contentType;
		if (not "json" in contentType):
			self.__isJsonBody = False;

		return self;

	def result(self):
		if (self.response is None):
			return None;
		return self.response.json();

	def execute(self):
		self.validate();
		logging.info("executing request using url : %s" % self.__resourceUrl.uri);
		self.__headers[Headers.X_VOL_APP_CLAIMS] = self.appAuth.getAccessToken();
		self.__headers["Content-Type"] = self.__contentType;

		requestUrl = self.__baseAddress+self.__resourceUrl.uri;
		if self.__body is not None and self.__isJsonBody:
				self.__body = json.dumps(self.__body);
		
		self.response = util.http_call(requestUrl, self.__resourceUrl.verb,headers=self.__headers,data=self.__body, verify=self.verifySSLCert);

	def validate(self):
		logging.info("Validating request");
		logging.info("Uri Location : %s" % self.__resourceUrl.location);
		if (self.__resourceUrl.location is UrlLocation.HomePod):
			self.__baseAddress = self.baseAuthUrl;
		elif (self.__resourceUrl.location is UrlLocation.PCIPod):
			if (self.apicontext.tenantId is None):
				raise Exception("TenantId is missing");
			self.__baseAddress = self.basePCIUrl;
		elif (self.__resourceUrl.location is UrlLocation.TenantPod):
			if (self.apicontext is None):
				raise Exception("ApiContext is not provided");

			if (self.apicontext.tenantId is None):
				raise Exception("TenantId is missing in apiContext");

			if (self.apicontext.tenantUrl is None):
				tenant =  self.getTenant(self.apicontext.tenantId);
				self.__baseAddress = tenant["domain"];
			else:
				self.__baseAddress = self.apicontext.tenantUrl;

			scheme = urlparse(self.__baseAddress).scheme;

			if (not scheme):
				self.__baseAddress = self.__scheme+"://"+self.__baseAddress;
		logging.info("Base URi address set to %s " % self.__baseAddress);

	def getTenant(self, tenantId: int):
		requestUrl = self.baseAuthUrl+"/api/platform/tenants/"+str(tenantId);
		headers = {};
		headers[Headers.X_VOL_APP_CLAIMS] = self.appAuth.getAccessToken();
		response = util.http_call(requestUrl,"GET", headers=headers, verify=self.verifySSLCert);
		return response.json();

	
__mozuclient__ = None

def default():
	global __mozuclient__
	if (__mozuclient__ is None):
		configFile = os.getenv("mozuConfig", None);

		if (configFile is not None):
			__mozuclient__ = MozuClient(config=configFile);
		else:
			applicationKey = os.getenv("ApplicationKey", None);
			sharedSecret = os.getenv("SharedSecret", None);
			baseAuthUrl = os.getenv("AuthUrl",__baseUrl__);
			basePCIUrl = os.getenv("PCIUrl", __basePciUrl__);
			__mozuclient__ = MozuClient(applicationKey=applicationKey, sharedSecret=sharedSecret,baseAuthUrl=baseAuthUrl,basePCIUrl=basePCIUrl);
	return __mozuclient__;

def set_config(options=None, **args):
	global __mozuclient__;
	__mozuclient__ = MozuClient(options, **args);
	return __mozuclient__;

configure = set_config