from analysis.PluginBase import AnalysisBasePlugin


class AnalysisPlugin(AnalysisBasePlugin):
    '''
    Hello World Plug-in
    '''
    NAME = 'Hello_World'
    DESCRIPTION = 'Hello World Plug-in'
    DEPENDENCIES = []
    VERSION = '0.1'

    def __init__(self, plugin_adminstrator, config=None, recursive=True):
        '''
        recursive flag: If True recursively analyze included files
        '''
        self.config = config

        # additional init stuff can go here

        super().__init__(plugin_adminstrator, config=config, recursive=recursive, plugin_path=__file__)

    def process_object(self, file_object):
        '''
        This function must be implemented by the plug-in.
        Analysis result must be a dict stored in "file_object.processed_analysis[self.NAME]"
        CAUTION: Dict keys must be strings!
        If you want to propagate results to parent objects store a list of strings in
        "file_object.processed_analysis[self.NAME]['summary']".

        File's binary is available via "file_object.binary".
        File's local storage path is available via "file_object.file_path".
        Results of other plug-ins can be accesd via "file_object.processed_analysis['PLUGIN_NAME']".
        Do not forget to add these plug-ins to "DEPENDENCIES".
        '''

        # do some fancy stuff
        result_a = 'hello world'
        result_b = 1337

        # store the results
        file_object.processed_analysis[self.NAME] = dict()
        file_object.processed_analysis[self.NAME]['analysis_result_a'] = result_a
        file_object.processed_analysis[self.NAME]['analysis_result_b'] = result_b

        # propagate some summary to parent objects
        file_object.processed_analysis[self.NAME]['summary'] = ['{} - {}'.format(result_a, result_b)]

        return file_object
