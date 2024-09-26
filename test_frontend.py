import pytest
import re
from utils import Raid, Shell


class TestVersion:
    raid = Raid("mdadm")

    def test_version_format(self):
        ret = self.raid.run("--version")
        assert re.search(r'v(\d+\.)+', ret.stdout)


    def test_version_v(self):
        ret = self.raid.run("-v")
        assert not re.search(r'v(\d+\.)+', ret.stdout)


class TestRaid:
    shell = Shell()
    raid = Raid("mdadm")

    @pytest.mark.parametrize("level,drives", [
        ("RAID0", 2),
        ("RAID1", 2),
        ("RAID10", 4),
        ("RAID5", 2),
        ("RAID6", 10)
    ])
    def test_create_delete(self, level, drives):
        all_devices = self.shell.list_dev()
        ret = self.raid.create(level, all_devices[:drives])
        all_devices = all_devices[drives:]


