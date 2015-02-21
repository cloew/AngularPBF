from pbf.helpers.filename_helper import GetPythonClassnameFromFilename
from pbf.templates.template_loader import TemplateLoader
from pbf_ng.templates import TemplatesRoot

class NewModule:
    """ ADD DESCRIPTION HERE """
    TEMPLATE_LOADER = TemplateLoader("module.js", TemplatesRoot)
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('filepath', action='store', help='Path to Filename to copy template to')
    
    def run(self, arguments):
        """ Run the command """
        filepath = arguments.filepath
        self.createModule(filepath)
        
    def createModule(self, filepath):
        """ Create a Module """
        keywords = {"%ModuleName%":GetPythonClassnameFromFilename(filepath)}
        self.TEMPLATE_LOADER.copy(filepath, keywords=keywords)