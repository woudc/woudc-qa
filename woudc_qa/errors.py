# -*- coding: ISO-8859-15 -*-
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
# Copyright (c) 2015 Government of Canada
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

import logging

LOGGER = logging.getLogger(__name__)

# custom exception stubs to catch sigs


class WOUDCQa(Exception):
    """config errors"""
    pass


class BPSDatabaseError(Exception):
    """db errors"""
    pass


class BPSFatalError(Exception):
    """generic fatal error"""
    pass


class BPSNonFatalError(Exception):
    """non-fatal error"""
    pass


class BPSTaxonomyBuildError(Exception):
    """taxonomy build error"""
    pass


class BPSTaxonomyValidationError(Exception):
    """taxonomy validation error"""
    pass


class BPSTaxonomyMissingError(Exception):
    """taxonomy validation error"""
    pass


class BPSURIBuildError(Exception):
    """URI build error"""
    pass


class BPSURIValidationError(Exception):
    """URI validation error"""
    pass


class BPSExtendedCSVParseError(Exception):
    """extendedCSV parsing error"""
    pass


class BPSFileIdentificationError(Exception):
    """file identification error"""
    pass


class BPSDataPayloadLoadError(Exception):
    """data payload error"""
    pass


class BPSPlatformIDError(Exception):
    """platform_id error"""
    pass


class BPSInstrumentIDError(Exception):
    """instrument_id error"""
    pass


class BPSAgencyIDError(Exception):
    """agency_id error"""
    pass


class BPSAgencyNameError(Exception):
    """agency_name error"""
    pass


class BPSDatasetIDError(Exception):
    """dataset_id error"""
    pass


class BPSLoadDataTableError(Exception):
    """data_table load error"""
    pass


class BPSLoadDataTableFieldError(Exception):
    """data_table_field load error"""
    pass


class BPSLoadDataTableFieldValueError(Exception):
    """data_table_field_value error"""
    pass


class BPSMalformedExtCSVError(Exception):
    """Extended CSV parse error"""
    pass


class BPSFileProcessError(Exception):
    """Unable to process incoming extended csv error"""
    pass


class BPSMissingContentError(Exception):
    """Missing CONTENT.Category error"""
    pass


class BPSMissingCategoryError(Exception):
    """Missing CONTENT.Category error"""
    pass


class BPSMissingCategoryValueError(Exception):
    """Missing CONTENT.Category value error"""
    pass


class BPSCategoryValidationError(Exception):
    """
    Insufficient data to determine missing
    CONTENT.Category value error
    """
    pass


class BPSCategoryDeterminationError(Exception):
    """
    Insufficient data to determine missing
    CONTENT.Category value error
    """
    pass


class BPSLevelValidationError(Exception):
    """
    CONTENT.Level's value is invalid
    """
    pass


class BPSLevelDeterminationError(Exception):
    """
    Unable to determine CONTENT.Level's when missing
    in input
    """
    pass


class BPSFormValidationError(Exception):
    """
    CONTENT.Form's value is invalid
    """
    pass


class BPSDatasetHandlerError(Exception):
    """DatasetHandler failed for a given observation"""
    pass


class BPSDuplicateURIError(Exception):
    """
    Duplicate URI inserting into data_payload
    table detected and prevented
    """
    pass


class BPSDatasetHandlerInitError(Exception):
    """Failed to init DatasetHandler"""
    pass


class BPSPersistenceFailedError(Exception):
    """Persistence failed for given URI by the persistence module"""
    pass


class BPSDatasetPersistenceFailedError(Exception):
    """Persistence failed for the given URI"""
    pass


class BPSInstrumentGeomError(Exception):
    """Generic instrument geometry error"""
    pass


class BPSInstrumentGetGeomError(Exception):
    """Unable to get instrument geometry"""
    pass


class BPSInstrumentGeomUpdateError(Exception):
    """Unable to update instrument geometry"""
    pass


class BPSExtCSVValidationError(Exception):
    """Extended CSV contains at least one error"""
    pass


class BPSExtCSVSerializationError(Exception):
    """Unable to write extended CSV file"""
    pass

    
class BPSRelativeOutputPathBuildError(Exception):
    """Unable to create relative output path for file"""
    pass


class BPSConfigurationInitializationError(Exception):
    """Unable to initialize configuration"""
    pass

    
class BPSExtCSVValueRetrievalError(Exception):
    """
    Unable to get value for given table field pair
    from ext CSV file
    """
    pass
    
class BPSErrorMessagesLoadError(Exception):
    """Unable to load up error messages"""
    pass


class BPSReportInitializationError(Exception):
    """Unable to initialize report object"""
    pass

    
class BPSReportSerializationError(Exception):
    """Unable to serialize report object"""
    pass

class BPSAgencyValidationError(Exception):
    """Invalid agency"""
    pass 
    
class BPSAlternatePlatformNameError(Exception):
    """
    Unable to perform alternate platform name check
    """
    pass
    
class BPSTableConfigurationError(Exception):
    """
    Unable to get table configuration rules
    """
    pass
    
class BPSCommonTableValidationError(Exception):
    """
    Unable to validate common tables and their fields
    """
    pass
    
class BPSFatalError(Exception):
    """
    Unable to process a file due to component initialization
    error, eg: report, config, persistence, etc
    """
    pass 
