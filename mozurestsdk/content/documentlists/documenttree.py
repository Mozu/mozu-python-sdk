
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class DocumentTree(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext is not None and apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		else:
			apiContext = ApiContext(dataViewMode = dataViewMode);
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getTreeDocumentContent(self,documentListName, documentName):
		""" Retrieve the content associated with the document, such as a product image or PDF specifications file.
		
		Args:
			| documentListName (string) - Name of content documentListName to delete
			| documentName (string) - The name of the document in the site.
		
		Returns:
			| Stream 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/documentTree/{documentName}/content", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("documentListName", documentListName);
		url.formatUrl("documentName", documentName);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def transformTreeDocumentContent(self,documentListName, documentName, width = None, height = None, max = None, maxWidth = None, maxHeight = None, crop = None, quality = None):
		""" Performs transformations on a document. For example, resizing an image.
		
		Args:
			| documentListName (string) - Name of content documentListName to delete
			| documentName (string) - The name of the document in the site.
			| width (int) - Specifies an exact width dimension for the image, in pixels.
			| height (int) - Specifies an exact height dimension for the image, in pixels.
			| max (int) - Specifies a pixel limitation for the largest side of an image.
			| maxWidth (int) - Specifies a pixel limitation for the width of the image, preserving the aspect ratio if the image needs resizing.
			| maxHeight (int) - Specifies a pixel limitation for the height of the image, preserving the aspect ratio if the image needs resizing.
			| crop (string) - Crops the image based on the specified coordinates. The reference point for positive coordinates is the top-left corner of the image, and the reference point for negative coordinates is the bottom-right corner of the image.Usage: Example:  removes 10 pixels from all edges of the image.  leaves the image uncropped.
			| quality (int) - Adjusts the image compression. Accepts values from 0-100, where 100 = highest quality, least compression.
		
		Returns:
			| Stream 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/documentTree/{documentName}/transform?width={width}&height={height}&maxWidth={maxWidth}&maxHeight={maxHeight}&crop={crop}&quality={quality}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("crop", crop);
		url.formatUrl("documentListName", documentListName);
		url.formatUrl("documentName", documentName);
		url.formatUrl("height", height);
		url.formatUrl("max", max);
		url.formatUrl("maxHeight", maxHeight);
		url.formatUrl("maxWidth", maxWidth);
		url.formatUrl("quality", quality);
		url.formatUrl("width", width);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getTreeDocument(self,documentListName, documentName, includeInactive = False, responseFields = None):
		""" Retrieves a document based on its document list and folder path in the document hierarchy.
		
		Args:
			| documentListName (string) - Name of content documentListName to delete
			| documentName (string) - The name of the document in the site.
			| includeInactive (bool) - Include inactive content.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Document 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/documentTree/{documentName}?includeInactive={includeInactive}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("documentListName", documentListName);
		url.formatUrl("documentName", documentName);
		url.formatUrl("includeInactive", includeInactive);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def updateTreeDocumentContent(self,stream, documentListName, documentName, contentType = None):
		""" Updates the binary data or content associated with a document, such as a product image or PDF specifications file, by supplying the document name.
		
		Args:
			| stream(stream) - Data stream that delivers information. Used to input and output data.
			| documentListName (string) - Name of content documentListName to delete
			| documentName (string) - The name of the document in the site.
			| contentType (string) - set content type of the data uploaded|
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/documentTree/{documentName}/content?folderPath={folderPath}&folderId={folderId}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("documentListName", documentListName);
		url.formatUrl("documentName", documentName);
		self.client.withResourceUrl(url).withBody(stream).withContentType(contentType).execute();

	
		
	def deleteTreeDocumentContent(self,stream, documentListName, documentName, contentType = None):
		""" Deletes the content associated with a document, such as a product image or PDF specifications file.
		
		Args:
			| stream(stream) - Data stream that delivers information. Used to input and output data.
			| documentListName (string) - Name of content documentListName to delete
			| documentName (string) - The name of the document in the site.
			| contentType (string) - set content type of the data uploaded|
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/documentTree/{documentName}/content?folderPath={folderPath}&folderId={folderId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("documentListName", documentListName);
		url.formatUrl("documentName", documentName);
		self.client.withResourceUrl(url).withBody(stream).withContentType(contentType).execute();

	
	
	