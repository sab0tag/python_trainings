from sys import maxsize


class Group:  # модель предметной области

    def __init__(self, groupName=None, headerDescr=None, footerDescr=None, id=None):
        self.groupName = groupName
        self.headerDescr = headerDescr
        self.footerDescr = footerDescr
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.groupName)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.groupName == other.groupName

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
