# =================================================================
#
# Terms and Conditions of Use
#
# Unless otherwise noted, computer program source code of this
# distribution is covered under Crown Copyright, Government of
# Canada, and is distributed under the MIT License.
#
# The Canada wordmark and related graphics associated with this
# distribution are protected under trademark law and copyright law.
# No permission is granted to use them outside the parameters of
# the Government of Canada's corporate identity program. For
# more information, see
# http://www.tbs-sct.gc.ca/fip-pcim/index-eng.asp
#
# Copyright title to all 3rd party software distributed with this
# software is held by the respective copyright holders as noted in
# those files. Users are asked to read the 3rd Party Licenses
# referenced with those assets.
#
# Copyright (c) 2016 Government of Canada
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import os
import unittest
import woudc_extcsv
from woudc_qa import qa, WOUDCQaNotImplementedError

__dirpath = os.path.dirname(os.path.realpath(__file__))

# test qa definitions
WOUDC_QA_RULES = os.path.join(__dirpath, 'woudc-qa-rules-test1.csv')


def msg(test_id, test_description):
    """helper function to print out test id and desc"""

    return '%s: %s' % (test_id, test_description)


def read_file(filename, dataset=None):
    """helper function to open test file and return content as string"""

    try:
        with open(filename) as ff:
            return ff.read()
    except IOError:
        with open('tests/{}'.format(filename)) as ff:
            return ff.read()


class QaTest(unittest.TestCase):
    """
    Test WOUDC automatic quality assessment framework using
    OzoneSonde and TotalOzone data
    """

    def setUp(self):
        """setup test fixtures, etc."""

        print(msg(self.id(), self.shortDescription()))

    def tearDown(self):
        """return to pristine state"""

        pass

    def test_good_preconditions(self):
        """test good/pass preconditions"""

        # ozonesonde
        file_s = read_file(
            'data/ozonesonde/20130227.ECC.6A.6A28027.UKMO-sample1.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)

        self.assertTrue('file1' in qa_results.keys(), 'file check')
        self.assertTrue('1' in qa_results['file1'].keys(), 'test id check')
        self.assertTrue(qa_results['file1']['1'][1]['precond_result'],
                        'precond result check')

    def test_bad_preconditions(self):
        """test bad/fail precondition"""

        # totalozone
        file_s = read_file(
            'data/totalozone/19870501.Dobson.Beck.092.DMI-sample1.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertFalse(qa_results['file1']['35'][1]['precond_result'],
                         'precond result check')

    def test_good_related_test(self):
        """test good/pass related test"""

        # ozonesonde
        file_s = read_file('data/ozonesonde/20070505.ecc.2z.6674.uah.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertEqual(True,
                         qa_results['file1']['40'][1]['related_test_result'],
                         'related test result result check')

    def test_bad_related_test(self):
        """test bad related test"""

        # ozonesonde
        file_s = read_file('data/ozonesonde/20070505.ecc.2z.6674.uah.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertFalse(qa_results['file1']['38'][1]['related_test_result'],
                         'related test result check')

    def test_good_related_test_profile(self):
        """test good/pass related test in profile"""

        # ozonesonde
        file_s = read_file(
            'data/ozonesonde/20130227.ECC.6A.6A28027.UKMO-sample1.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertTrue(qa_results['file1']['25P'][4]['related_test_result'],
                        'related test result in profile check')

    def test_bad_related_test_profile(self):
        """test bad related test in profile"""

        # ozonesonde
        file_s = read_file(
            'data/ozonesonde/20130227.ECC.6A.6A28027.UKMO-sample1.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertFalse(qa_results['file1']['25P'][7]['related_test_result'],
                         'related test result in profile check')

    def test_good_presence_check(self):
        """test good presence"""

        # ozonesonde
        file_s = read_file(
            'data/ozonesonde/20130227.ECC.6A.6A28027.UKMO-sample1.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertEqual('100', qa_results['file1']['22P'][2]['result'],
                         'presence check in profile')

    def test_bad_presence_check(self):
        """test good presence"""

        # totalozone
        file_s = read_file(
            'data/totalozone/19870501.Dobson.Beck.092.DMI-sample1.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertEqual('-1', qa_results['file1']['41'][20]['result'],
                         'presence check in profile')

    def test_good_presence_check2(self):
        """test good presence"""

        # totalozone
        file_s = read_file(
            'data/totalozone/19870501.Dobson.Beck.092.DMI-sample2.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertEqual('100', qa_results['file1']['41'][20]['result'],
                         'presence check in profile')

    def test_good_range_check(self):
        """test good range check"""

        # ozonesonde
        file_s = read_file(
            'data/ozonesonde/20130227.ECC.6A.6A28027.UKMO-sample1.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertEqual('100', qa_results['file1']['25P'][10]['result'],
                         'range check in profile')

    def test_bad_range_check(self):
        """test bad range check"""

        # ozonesonde
        file_s = read_file(
            'data/ozonesonde/20130227.ECC.6A.6A28027.UKMO-sample1.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertEqual('0', qa_results['file1']['42'][5]['result'],
                         'range check in profile')

    def test_bad_range_check2(self):
        """test bad range check"""

        # totalozone
        file_s = read_file(
            'data/totalozone/19870501.Dobson.Beck.092.DMI-sample1.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertIsNone(qa_results['file1']['36'][1]['result'],
                          'range check in profile')

    def test_good_step_check(self):
        """test good step check"""

        # ozonesonde
        file_s = read_file(
            'data/ozonesonde/20130227.ECC.6A.6A28027.UKMO-sample1.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertEqual('100', qa_results['file1']['27'][1]['result'],
                         'step check in profile')

    def test_bad_step_check(self):
        """test bad step check"""

        # ozonesonde
        file_s = read_file(
            'data/ozonesonde/20130227.ECC.6A.6A28027.UKMO-sample1.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertEqual('0', qa_results['file1']['23P'][2]['result'],
                         'step check in profile')

    def test_non_supported_dataset(self):
        """try a non supported dataset"""

        file_s = \
            read_file(
                'data/lidar/19930208.dial.lotard.001.crestech.csv'
            )

        with self.assertRaises(WOUDCQaNotImplementedError):
            qa(file_s, rule_path=WOUDC_QA_RULES)

    def test_bad_range_check3(self):
        """test range check"""

        # spectral
        file_s = read_file(
            'data/spectral/20030215.brewer.mkiv.130.epa_uga-bad.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertEqual('0', qa_results['file1']['36'][1]['result'],
                         'range check')
        self.assertEqual('0', qa_results['file1']['36'][2]['result'],
                         'range check')
        self.assertEqual('0', qa_results['file1']['36'][9]['result'],
                         'range check')
        self.assertEqual('0', qa_results['file1']['36'][23]['result'],
                         'range check')
        self.assertEqual('100', qa_results['file1']['36'][4]['result'],
                         'range check')
        self.assertEqual('100', qa_results['file1']['36'][6]['result'],
                         'range check')

    def test_bad_range_check4(self):
        """test range check"""

        # spectral
        file_s = read_file(
            'data/spectral/20030215.brewer.mkiv.130.epa_uga-good.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES)
        self.assertEqual('100', qa_results['file1']['36'][1]['result'],
                         'range check')
        self.assertEqual('100', qa_results['file1']['36'][2]['result'],
                         'range check')
        self.assertEqual('100', qa_results['file1']['36'][23]['result'],
                         'range check')
        self.assertEqual('100', qa_results['file1']['36'][23]['result'],
                         'range check')
        self.assertEqual('100', qa_results['file1']['36'][4]['result'],
                         'range check')
        self.assertEqual('100', qa_results['file1']['36'][6]['result'],
                         'range check')

    def test_validator_error1(self):
        """test that bad metadata throws error"""

        file_s = read_file(
            'data/totalozone/19870501.Dobson.Beck.092.DMI-sample3.csv')
        with self.assertRaises(woudc_extcsv.ExtCSVValidatorException):
            qa(file_s, rule_path=WOUDC_QA_RULES, summary=True)

    def test_validator_error2(self):
        """test that bad metadata results in correct error"""

        file_s = read_file(
            'data/totalozone/19870501.Dobson.Beck.092.DMI-sample3.csv')
        try:
            qa(file_s, rule_path=WOUDC_QA_RULES, summary=True)
        except Exception, err:
            self.assertTrue('Platform name of Arhus does \
not match database' in str(err))

    def test_validator_warnings(self):
        """test that warnings are passed along"""

        file_s = read_file(
            'data/totalozone/19870501.Dobson.Beck.092.DMI-sample4.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES, summary=True)
        self.assertTrue('Some lines in this file have \
fewer commas than there are headers' in qa_results)

    def test_validator_no_warnings(self):
        """test that a file with no warnings affects nothing"""

        file_s = read_file(
            'data/totalozone/19870501.Dobson.Beck.092.DMI-sample2.csv')
        qa_results = qa(file_s, rule_path=WOUDC_QA_RULES, summary=True)
        self.assertEqual('File passed all defined WOUDC \
quality assessment checks.', qa_results)


# main
if __name__ == '__main__':
    unittest.main()
