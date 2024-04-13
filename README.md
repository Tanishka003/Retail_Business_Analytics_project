# Retail Business Analytics Project
----
## Description

- In this project, we aim to analyze the ``` "retail_db" ``` dataset by providing reports on total completed orders and performing customer and product analytics.
  
- Implemented tasks outlined in the project requirements to analyze the retail dataset.
  
- Used PySpark for data exploration, filtering, and saving results in different formats and compression types on HDFS.
  
- Generated reports on completed orders, customer analytics, and product insights.
  
- Ensured adherence to project specifications and provided proper documentation for each task.

## Dataset Name
- data_files

## ER Diagram
![image](https://github.com/Tanishka003/Retail_Business_Analytics_project/assets/99746797/7d6f6595-cfe7-475d-96d5-9e766520c1ef)


## Understanding the Data Model
**The RETAIL_DB database contains the following tables:**
- Department
- Customer
- Categories
- Products
- Orders
- Orders items
  
## Steps to Be Performed
**Step 1: Upload the Dataset to HDFS through FTP**
- Download the relevant dataset from the ``` "Course Resources" ``` section or the project description.
- Upload the dataset to the ``` “FTP” ``` lab from your local system.
- Upload the dataset to “HDFS” from ``` “Web Console” ``` using the put command.
  + **Syntax of “put“ command for reference:**
    
      ``` hdfs dfs -put <FTP_folder_name_source> <hdfs_path_destination> ```

  + **Example:**
  
      ``` hdfs dfs -put data-files hdfs://localhost:port/data-files-project ```

**Step 2: Perform Tasks on the Uploaded Dataset using PySpark**

- Log in to ``` PySpark shell ```
- Explore Customer Records
  
   **Requirement:**
  
    + Show client information for those who live in California.
    + The final output must be in text format.
    + Save the results in the
           ``` "result/scenario1/solution" ```
      folder.
    + Only records with the state value ``` "CA" ``` should be included in the result.
    + Only the customer's entire name should be included in the output.
   
  **Example:**
     ``` “Robert Hudson” ```
  
- Explore Order Records
  
  **Requirement:**
  
    + Show all orders with the order status value ``` "COMPLETE" ```.
    + The output should be in ``` JSON ``` format.
    + Save the data in the ``` "result/scenario2/solution" ``` directory on HDFS.
    + The ``` "order date" ``` column should be in the ``` "YYYY-MM-DD" ``` format.
    + Use ``` GZIP compression ``` to compress the output.
      
      **Only the following column names should be included in the output:**
       - Order number
       - Order date
       - Current situation
  
- Explore Customer Records

  **Requirement:**
  
     + Produce a list of all consumers who live in the city of ``` "Caguas" ```.
     + Save the data in the ``` "result/scenario3/solution" ``` directory on HDFS.
     + The result should only contain records with the value ``` "Caguas" ``` for the customer city.
     + Use ``` snappy compression ``` to compress the output.
     + Save the file in the ``` ORC ``` format.
  
- Explore Category Records
  
  **Requirement:**
  
    + Save the result files in ``` CSV ``` format.
    + Save the data in the ``` "result/scenario4/solution" ``` directory on HDFS.
    + Use ``` lz4 compression ``` to compress the output.
  
- Explore Product Records

   **Requirement:**

   + Only products with a price of ``` more than 1000.0 ``` should be included in the output.
   + Save the output files in ``` parquet format ``` .
   + Remove data from the table if the product price is lesser than ``` 1000.0. ```
   + Save the data in the ``` "result/scenario5/solution" ``` directory on HDFS.
   + Use ``` snappy compression ``` to compress the output.
     
- Explore Product Records
- 
  **Requirement:**
  
   + Only products with a price of ``` more than 1000.0 ``` should be in the output.
   + The pattern ``` "Treadmill" ``` appears in the product name.
   + Save the output files in ``` parquet ``` format.
   + Save the data in the ``` "result/scenario6/solution" ``` directory on HDFS.
   + Use ``` GZIP compression ``` to compress the output.
     
- Explore Order Records
  
   **Requirement:**
  
  + Output all PENDING orders in ``` July 2013 ```.
  + Output files should be in ``` JSON ``` format.
  + Save the data in the ``` "result/scenario7/solution" ``` directory on HDFS.
  + Only entries with the order status value of ``` "PENDING" ``` should be included in the result.
  + Order date should be in the ``` YYY-MM-DD format ```.
  + Use ``` snappy compression ``` to compress the output, which should just contain the order date and order status.
    
## Project Summary:

This project involves analyzing a retail dataset using PySpark. Key tasks include exploring customer and order records, filtering data based on specific criteria, and saving results in various formats and compression types on HDFS. The objectives include generating reports on completed orders, customer analytics, and product insights. By following the outlined tasks, the project aims to extract valuable insights to aid decision-making in retail operations.

## Conclusion

This project aims to leverage PySpark for data analysis on the given retail dataset. Each task is designed to extract specific insights and perform analytics on different aspects of the retail business. Proper documentation and adherence to the requirements outlined in each task are crucial for successful completion.

## License:

 - Under MIT License - [LICENSE](https://github.com/Tanishka003/Retail_Business_Analytics_project/LICENSE)

## Acknowledgments: 

 - Acknowledge any contributions or support receive from team members, mentors, or other stakeholders during the project.
----
By incorporating these suggestion, the documentation will provide a comprehensive overview of the project, making it easier for others to understand, replicate, and build upon your work.
