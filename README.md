# SchoolDigger K-12 School Data API MCP Server

## Overview

The SchoolDigger K-12 School Data API MCP Server is a comprehensive solution for accessing detailed information about schools and school districts across the United States. With over 15 years of data collection experience, this service provides users with a unified platform to access essential metrics concerning school performance, demographics, and rankings. It is specifically designed for nationwide applications, making it an invaluable tool for analysis, data display, and more.

## Key Features

- **School Directory**: Access detailed information for over 120,000 public, charter, and private schools, including their names, addresses, contact details, and geographical coordinates.
  
- **District Directory**: Get data on over 18,000 school districts, including their names, addresses, and member schools.

- **Student Metrics**: Obtain insights into student demographics, including ethnicity, pupil/teacher ratios, and free-reduced lunch program statistics.

- **Standardized Test Scores**: Access test scores at various levels, including state, district, and school levels, with the capability to view proficiency breakdowns.

- **School Rankings**: View state-wide rankings calculated by SchoolDigger for elementary, middle, and high schools, as well as district and city rankings.

- **Spending Per Student**: Review average spending data per student at the school building level, compliant with ESSA standards.

- **School Reviews**: Read reviews submitted by SchoolDigger website visitors for a more comprehensive understanding of each school.

## Data Characteristics

- **Update Frequency**: The data is continuously updated throughout the year, ensuring access to the most current information.

- **Geographic Coverage**: The data encompasses schools and districts across the entire United States.

- **Format**: Data is returned in a JSON format, making it easy to integrate into various applications.

## Use Cases

- **Real Estate Websites**: Provide potential homebuyers with information about nearby schools, enhancing property listings with valuable educational data.

- **Performance Analysis**: Analyze school and district performance to identify trends and areas of improvement.

- **Neighborhood Analysis**: Discover high-performing schools within under-performing neighborhoods.

- **Autocomplete/Selection Lists**: Enable easy school and district searches for users with autocomplete and selection list capabilities.

- **Product Effectiveness Analysis**: Evaluate the impact of educational products by correlating their use with academic performance metrics.

## Tools Provided

The API MCP Server offers a range of tools categorized by functionality:

- **Schools**: Tools for retrieving and searching school records.
  - *GetSchool*: Retrieve a specific school record.
  - *GetSchools*: Search for schools based on various criteria.

- **Districts**: Tools for retrieving and searching district records.
  - *GetDistrict*: Retrieve a specific district record.
  - *GetDistricts*: Search for districts based on various criteria.

- **Rankings**: Tools to access school and district rankings.
  - *GetRankSchools*: Retrieve a ranking list of schools.
  - *GetRankDistricts*: Retrieve a ranking list of districts.

- **Autocomplete**: Tool for generating school lists for autocomplete functionality.
  - *Autocomplete*: Provides a quick list of schools for client-typed autocomplete searches.

## Contact and Support

For questions or assistance, users can reach out for support and additional resources. The server provides immediate and comprehensive access to a wealth of school data, making it a key resource for anyone needing detailed educational metrics.