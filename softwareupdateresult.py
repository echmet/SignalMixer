from enum import Enum


class SoftwareUpdateResult:
    class State:
        NO_ERROR = 1
        NETWORK_ERROR = 2
        PROCESSING_ERROR = 3
        DATA_ERROR = 4

    def __init__(self, state, update_avail, extra_info,
                 new_ver_maj, new_ver_min, new_ver_rev,
                 link):
        self.state = state
        self.update_available = update_avail,
        self.extra_info = extra_info
        self.new_ver_maj = new_ver_maj
        self.new_ver_min = new_ver_min
        self.new_ver_rev = new_ver_rev
        self.link = link

