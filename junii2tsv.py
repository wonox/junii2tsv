# Test Parser
# http://stackoverflow.com/questions/29155628/python-minidom-parse-xml-file-and-write-to-csv
# OAI-PMH example http://repository.kulib.kyoto-u.ac.jp/dspace-oai/request?verb=ListRecords&metadataPrefix=junii2&from=2009-01-01&until=2009-04-30
#         example http://repository.kulib.kyoto-u.ac.jp/dspace-oai/request?verb=ListRecords&metadataPrefix=junii2&set=com_2433_48884
#   http://repository.kulib.kyoto-u.ac.jp/dspace-oai/request?verb=ListRecords&metadataPrefix=junii2&set=com_2433_48884&from=2015-01-01&until=2015-04-30
# https://hermes-ir.lib.hit-u.ac.jp/rs-oai/request?verb=ListRecords&metadataPrefix=junii2&set=hdl_10086_26686
from xml.dom.minidom import parse
import csv
from sys import getsizeof

def writeToCSV(myLibrary):
    csvfile = open('output.csv', 'wb')
    fieldnames =  ["title", "alternative", "creator", "subject", "NIIsubject", "NDC", "NDLC", "BSH", "NDLSH", "MeSH", "DDC", "LCC", "UDC", "LCSH", "description", "publisher", "contributor", "date", "type", "NIItype", "format", "identifier", "URI", "fullTextURL", "issn", "NCID", "jtitle", "volume", "issue", "spage", "epage", "dateofissued", "source", "language", "relation", "pmid", "doi", "isVersionOf", "hasVersion", "isReplacedBy", "replaces", "isRequiredBy", "requires", "isPartOf", "hasPart", "isReferencedBy", "references", "isFormatOf", "hasFormat", "coverage", "spatial", "NIIspatial", "temporal", "NIItemporal", "rights", "textversion"]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator="\n", delimiter='\t')
    writer.writeheader()

    books = myLibrary.getElementsByTagName("meta") if myLibrary.getElementsByTagName("meta") else myLibrary.getElementsByTagName("junii2")

    for book in books:
        titleValue = book.getElementsByTagName("title")[0].childNodes[0].data if book.getElementsByTagName("title") else ""
        typeValue = book.getElementsByTagName("type")[0].childNodes[0].data if book.getElementsByTagName("type") else ""
        NIItypeValue = book.getElementsByTagName("NIItype")[0].childNodes[0].data if book.getElementsByTagName("NIItype") else ""
        formatValue = book.getElementsByTagName("format")[0].childNodes[0].data if book.getElementsByTagName("format") else ""
        URIValue = book.getElementsByTagName("URI")[0].childNodes[0].data if book.getElementsByTagName("URI") else ""
        fullTextURLValue = book.getElementsByTagName("fullTextURL")[0].childNodes[0].data if book.getElementsByTagName("fullTextURL") else ""
        languageValue = book.getElementsByTagName("language")[0].childNodes[0].data if book.getElementsByTagName("language") else ""
        # creatorValue = book.getElementsByTagName("creator")[0].childNodes[0].data if book.getElementsByTagName("creator") else ""
        dateofissuedValue = book.getElementsByTagName("dateofissued")[0].childNodes[0].data if book.getElementsByTagName("dateofissued") else ""
        subjectValue = book.getElementsByTagName("subject")[0].childNodes[0].data if book.getElementsByTagName("subject") else ""
        NIIsubjectValue = book.getElementsByTagName("NIIsubject")[0].childNodes[0].data if book.getElementsByTagName("NIIsubject") else ""
        NDCValue = book.getElementsByTagName("NDC")[0].childNodes[0].data if book.getElementsByTagName("NDC") else ""
        NDLCValue = book.getElementsByTagName("NDLC")[0].childNodes[0].data if book.getElementsByTagName("NDLC") else ""
        BSHValue = book.getElementsByTagName("BSH")[0].childNodes[0].data if book.getElementsByTagName("BSH") else ""
        NDLSHValue = book.getElementsByTagName("NDLSH")[0].childNodes[0].data if book.getElementsByTagName("NDLSH") else ""
        MeSHValue = book.getElementsByTagName("MeSH")[0].childNodes[0].data if book.getElementsByTagName("MeSH") else ""
        DDCValue = book.getElementsByTagName("DDC")[0].childNodes[0].data if book.getElementsByTagName("DDC") else ""
        LCCValue = book.getElementsByTagName("LCC")[0].childNodes[0].data if book.getElementsByTagName("LCC") else ""
        UDCValue = book.getElementsByTagName("UDC")[0].childNodes[0].data if book.getElementsByTagName("UDC") else ""
        LCSHValue = book.getElementsByTagName("LCSH")[0].childNodes[0].data if book.getElementsByTagName("LCSH") else ""
        descriptionValue = book.getElementsByTagName("description")[0].childNodes[0].data if book.getElementsByTagName("description") else ""
        descriptionValue = book.getElementsByTagName("description")[0].childNodes[0].data if book.getElementsByTagName("description") else ""
        publisherValue = book.getElementsByTagName("publisher")[0].childNodes[0].data if book.getElementsByTagName("publisher") else ""
        contributorValue = book.getElementsByTagName("contributor")[0].childNodes[0].data if book.getElementsByTagName("contributor") else ""
        dateValue = book.getElementsByTagName("date")[0].childNodes[0].data if book.getElementsByTagName("date") else ""
        identifierValue = book.getElementsByTagName("identifier")[0].childNodes[0].data if book.getElementsByTagName("identifier") else ""
        issnValue = book.getElementsByTagName("issn")[0].childNodes[0].data if book.getElementsByTagName("issn") else ""
        NCIDValue = book.getElementsByTagName("NCID")[0].childNodes[0].data if book.getElementsByTagName("NCID") else ""
        jtitleValue = book.getElementsByTagName("jtitle")[0].childNodes[0].data if book.getElementsByTagName("jtitle") else ""
        volumeValue = book.getElementsByTagName("volume")[0].childNodes[0].data if book.getElementsByTagName("volume") else ""
        issueValue = book.getElementsByTagName("issue")[0].childNodes[0].data if book.getElementsByTagName("issue") else ""
        spageValue = book.getElementsByTagName("spage")[0].childNodes[0].data if book.getElementsByTagName("spage") else ""
        epageValue = book.getElementsByTagName("epage")[0].childNodes[0].data if book.getElementsByTagName("epage") else ""
        sourceValue = book.getElementsByTagName("source")[0].childNodes[0].data if book.getElementsByTagName("source") else ""
        relationValue = book.getElementsByTagName("relation")[0].childNodes[0].data if book.getElementsByTagName("relation") else ""
        pmidValue = book.getElementsByTagName("pmid")[0].childNodes[0].data if book.getElementsByTagName("pmid") else ""
        doiValue = book.getElementsByTagName("doi")[0].childNodes[0].data if book.getElementsByTagName("doi") else ""
        isVersionOfValue = book.getElementsByTagName("isVersionOf")[0].childNodes[0].data if book.getElementsByTagName("isVersionOf") else ""
        hasVersionValue = book.getElementsByTagName("hasVersion")[0].childNodes[0].data if book.getElementsByTagName("hasVersion") else ""
        isReplacedByValue = book.getElementsByTagName("isReplacedBy")[0].childNodes[0].data if book.getElementsByTagName("isReplacedBy") else ""
        replacesValue = book.getElementsByTagName("replaces")[0].childNodes[0].data if book.getElementsByTagName("replaces") else ""
        isRequiredByValue = book.getElementsByTagName("isRequiredBy")[0].childNodes[0].data if book.getElementsByTagName("isRequiredBy") else ""
        requiresValue = book.getElementsByTagName("requires")[0].childNodes[0].data if book.getElementsByTagName("requires") else ""
        isPartOfValue = book.getElementsByTagName("isPartOf")[0].childNodes[0].data if book.getElementsByTagName("isPartOf") else ""
        hasPartValue = book.getElementsByTagName("hasPart")[0].childNodes[0].data if book.getElementsByTagName("hasPart") else ""
        isReferencedByValue = book.getElementsByTagName("isReferencedBy")[0].childNodes[0].data if book.getElementsByTagName("isReferencedBy") else ""
        referencesValue = book.getElementsByTagName("references")[0].childNodes[0].data if book.getElementsByTagName("references") else ""
        isFormatOfValue = book.getElementsByTagName("isFormatOf")[0].childNodes[0].data if book.getElementsByTagName("isFormatOf") else ""
        hasFormatValue = book.getElementsByTagName("hasFormat")[0].childNodes[0].data if book.getElementsByTagName("hasFormat") else ""
        coverageValue = book.getElementsByTagName("coverage")[0].childNodes[0].data if book.getElementsByTagName("coverage") else ""
        spatialValue = book.getElementsByTagName("spatial")[0].childNodes[0].data if book.getElementsByTagName("spatial") else ""
        NIIspatialValue = book.getElementsByTagName("NIIspatial")[0].childNodes[0].data if book.getElementsByTagName("NIIspatial") else ""
        temporalValue = book.getElementsByTagName("temporal")[0].childNodes[0].data if book.getElementsByTagName("temporal") else ""
        NIItemporalValue = book.getElementsByTagName("NIItemporal")[0].childNodes[0].data if book.getElementsByTagName("NIItemporal") else ""
        rightsValue = book.getElementsByTagName("rights")[0].childNodes[0].data if book.getElementsByTagName("rights") else ""
        textversionValue = book.getElementsByTagName("textversion")[0].childNodes[0].data if book.getElementsByTagName("textversion") else ""
        alternativeValue = book.getElementsByTagName("alternative")[0].childNodes[0].data if book.getElementsByTagName("alternative") else ""

        counta = 0
        for creatorValue in book.getElementsByTagName("creator"):
            # authorValue = author.childNodes[0].data
            counta += 1
            if counta > 1:
                authorValue = authorValue + '/' + author.childNodes[0].data
            else:
                authorValue = author.childNodes[0].data

        writer.writerow({'title': titleValue.encode('utf-8'), 'alternative': alternativeValue.encode('utf-8'), 'creator': creatorValue.encode('utf-8'), 'subject': subjectValue.encode('utf-8'), 'NIIsubject': NIIsubjectValue.encode('utf-8'), 'NDC': NDCValue.encode('utf-8'), 'NDLC': NDLCValue.encode('utf-8'), 'BSH': BSHValue.encode('utf-8'), 'NDLSH': NDLSHValue.encode('utf-8'), 'MeSH': MeSHValue.encode('utf-8'), 'DDC': DDCValue.encode('utf-8'), 'LCC': LCCValue.encode('utf-8'), 'UDC': UDCValue.encode('utf-8'), 'LCSH': LCSHValue.encode('utf-8'), 'description': descriptionValue.encode('utf-8'), 'publisher': publisherValue.encode('utf-8'), 'contributor': contributorValue.encode('utf-8'), 'date': dateValue.encode('utf-8'), 'type': typeValue.encode('utf-8'), 'NIItype': NIItypeValue.encode('utf-8'), 'format': formatValue.encode('utf-8'), 'identifier': identifierValue.encode('utf-8'), 'URI': URIValue.encode('utf-8'), 'fullTextURL': fullTextURLValue.encode('utf-8'), 'issn': issnValue.encode('utf-8'), 'NCID': NCIDValue.encode('utf-8'), 'jtitle': jtitleValue.encode('utf-8'), 'volume': volumeValue.encode('utf-8'), 'issue': issueValue.encode('utf-8'), 'spage': spageValue.encode('utf-8'), 'epage': epageValue.encode('utf-8'), 'dateofissued': dateofissuedValue.encode('utf-8'), 'source': sourceValue.encode('utf-8'), 'language': languageValue.encode('utf-8'), 'relation': relationValue.encode('utf-8'), 'pmid': pmidValue.encode('utf-8'), 'doi': doiValue.encode('utf-8'), 'isVersionOf': isVersionOfValue.encode('utf-8'), 'hasVersion': hasVersionValue.encode('utf-8'), 'isReplacedBy': isReplacedByValue.encode('utf-8'), 'replaces': replacesValue.encode('utf-8'), 'isRequiredBy': isRequiredByValue.encode('utf-8'), 'requires': requiresValue.encode('utf-8'), 'isPartOf': isPartOfValue.encode('utf-8'), 'hasPart': hasPartValue.encode('utf-8'), 'isReferencedBy': isReferencedByValue.encode('utf-8'), 'references': referencesValue.encode('utf-8'), 'isFormatOf': isFormatOfValue.encode('utf-8'), 'hasFormat': hasFormatValue.encode('utf-8'), 'coverage': coverageValue.encode('utf-8'), 'spatial': spatialValue.encode('utf-8'), 'NIIspatial': NIIspatialValue.encode('utf-8'), 'temporal': temporalValue.encode('utf-8'), 'NIItemporal': NIItemporalValue.encode('utf-8'), 'rights': rightsValue.encode('utf-8'), 'textversion': textversionValue.encode('utf-8')})

doc = parse('request5.xml')
myLibrary = doc.getElementsByTagName("ListRecords")[0]

# Get book elements in library
# books = myLibrary.getElementsByTagName("meta")

# Print each book's title
writeToCSV(myLibrary)
