# working with XML.....
 
#XML stands for eXtensible Markup Language
#XML is a markup language much like HTML
#XML was designed to store and transport data
#XML is a W3C Recommendation

import pandas as pd
pd.read_xml('test.xml')

<?xml version="1.0" encoding="UTF-8"?>
<Users>
    <User id="1">
        <Name>John Doe</Name>
        <Email>john.doe@example.com</Email>
        <Age>25</Age>
        <Country>USA</Country>
    </User>
    <User id="2">
        <Name>Jane Smith</Name>
        <Email>jane.smith@example.com</Email>
        <Age>30</Age>
        <Country>UK</Country>
    <User id="2">
            <Name>Jane Smith</Name>
            <Email>max123@example.com</Email>
            <Age>24</Age>
            <Country>canada</Country>
    </User>
</Users>



