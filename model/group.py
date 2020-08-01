class Group:  # модель предметной области

    def __init__(self, groupName=None, headerDescr=None, footerDescr=None, id=None):
        self.groupName = groupName
        self.headerDescr = headerDescr
        self.footerDescr = footerDescr
        self.id = id

