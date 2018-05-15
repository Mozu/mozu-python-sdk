
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Channel(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getChannels(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" 
		
		Args:
			| startIndex (int) - 
			| pageSize (int) - 
			| sortBy (string) - 
			| filter (string) - 
			| responseFields (string) - 
		
		Returns:
			| ChannelCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/channels/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getChannel(self,code, responseFields = None):
		""" 
		
		Args:
			| code (string) - User-defined code that identifies the channel to retrieve.
			| responseFields (string) - 
		
		Returns:
			| Channel 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/channels/{code}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("code", code);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createChannel(self,channel, responseFields = None):
		""" 
		
		Args:
			| channel(channel) - Properties of the channel to create.
			| responseFields (string) - 
		
		Returns:
			| Channel 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/channels/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(channel).execute();
		return self.client.result();

	
		
	def updateChannel(self,channel, code, responseFields = None):
		""" 
		
		Args:
			| channel(channel) - Properties of a the channel to update.
			| code (string) - User-defined code that identifies the channel to update.
			| responseFields (string) - 
		
		Returns:
			| Channel 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/channels/{code}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("code", code);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(channel).execute();
		return self.client.result();

	
		
	def deleteChannel(self,code):
		""" 
		
		Args:
			| code (string) - User-defined code that identifies the channel to delete.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/channels/{code}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("code", code);
		self.client.withResourceUrl(url).execute();

	
	
	