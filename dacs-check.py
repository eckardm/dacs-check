'''
import what we need'''


'''
create list of required elements'''

# reference code (local identifier, repository identifier, country identifier); name and location of repository; title; date; extent; name of creator(s); scope and content; conditions governing access; languages and scripts of the material
required_element_xpaths = [['ead/eadheader/eadid', 'ead/eadheader[@repositoryencoding]', 'ead/eadheader[@countryencoding]'], 'ead/eadheader/filedesc/publicationstmt/publisher', 'ead/eadheader/filedesc/titlestmt/titleproper',  


'''
go through directory of eads, compare existing elements with list of required elements, determine which required elements are missing'''


'''
export a csv file with filename and missing element
first for single-level and then for multi-level finding aids'''


'''
print a report of what percentage of eads are dacs compliant
first for single-level and then for multi-level finding aids'''
