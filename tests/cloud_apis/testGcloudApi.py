# -*- coding: utf-8 -*-

import unittest


from customCloudDeploy.cloudApis import GcloudApi

class testGcloudApi(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        cloud_config = {"a": 123}
        gcloudApi = GcloudApi.GcloudApi(cloud_config)
        print(gcloudApi.get_cloud_api_config())
        assert True


if __name__ == '__main__':
    unittest.main()