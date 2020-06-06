from mdlistdialog import MDListDialog


class ServicesMarkerPopup(MDListDialog):

    def __init__(self, marker_data):
        super().__init__()
        keys = ["BID","Name","State","City","Village","Phone","Website","Instagram","AccessRoad","TraditionalResidence","OrganicFood","IndigenousMusic","Score","Update_Time"]

        for i in range(len(keys)):
            key = keys[i]
            value = marker_data[i]
            if value == None:
                value = "-"
            setattr(self, key, value)