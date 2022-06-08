"""

Classify el image by rule condition.

"""
import yaml


class RuleEngine:

    def __init__(self, config):
        """
        Init RuleEngine var config filename

        Args:
            config: str, config filename
        """
        self.config = yaml.load(open(config, 'r').read(), yaml.FullLoader)

    def defect_handle(self, defects):
        """
        Handle a list of defects in one image

        Args:
            defects: dict, defect to handle
        """

        current_level_defect = []
        lowest_level = None

        for defect_category in self.config['defect']:
            for defect in defects:
                if defect['category'] == defect_category:
                    for level in self.config['defect'][defect_category]['level']:
                        logic = self.config['defect'][defect_category]['level'][level]['logic']
                        items = self.config['defect'][defect_category]['level'][level]['items']
                        if self.logic_handle(defect=defect, logic=logic, items=items) is True:
                            if level == lowest_level:
                                current_level_defect.append(defect_category)
                            else:
                                lowest_level = level
                                current_level_defect = [defect_category]

        if len(current_level_defect):
            return lowest_level, current_level_defect

    @staticmethod
    def meta_handle(defect, meta_key, meta_spec):
        """
        Is defect's attribute between spec high and spec low

        Args:
            defect: dict, defect to handle
            meta_key: str, key name of meta info
            meta_spec: list, spec of meta info

        Returns: Ture or False

        """
        assert hasattr(defect, meta_key)

        if meta_spec[0] <= defect[meta_key] <= meta_spec[1]:
            return True
        else:
            return False

    def logic_handle(self, defect, logic, items):
        """
        Logical operations between items

        Args:
            defect: dict, defect to handle
            logic: str, key name of meta info
            items: list, spec of meta info

        Returns: True or False
        """
        logic_bool = True
        for item in items:
            metas_bool = True
            for meta_key in item['metas']:
                metas_bool = metas_bool and self.meta_handle(defect,
                                                             meta_key=meta_key, meta_spec=item['metas'][meta_key])
            if logic == "AND":
                logic_bool = logic_bool and metas_bool
            elif logic == "OR":
                logic_bool = logic_bool or metas_bool

        return logic_bool


if __name__ == "__main__":
    ruleEngine = RuleEngine(config='rule_engine_config.yaml')
