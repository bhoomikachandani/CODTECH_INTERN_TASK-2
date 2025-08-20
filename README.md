## Task 2 - Automated Report Generation 

<h3>Website Traffic Analysis Report Generator</h3>

<h4>CodTech IT Solutions Internship Task</h4>
<p>This project is a Python script developed as part of my internship at CodTech IT Solutions. It is designed to analyze website traffic data from a CSV file and generate a professional, well-structured PDF report. The tool helps to quickly understand key metrics and insights from raw data.</p>
<h3>Features</h3>
<ul>
   <li>CSV Data Ingestion: Reads and processes website traffic data from website_traffic.csv, handling data types and potential errors.</li>
   <li>Key Metrics Calculation: Automatically computes essential metrics such as total page views and average visit duration.</li>
   <li>Data Aggregation: Identifies and ranks the most popular pages and top user locations based on total views.</li>
   <li>PDF Report Generation: Creates a clean, professional PDF report named website_traffic_report.pdf using the fpdf library, presenting the analysis in an easy-to-read format.</li>
   <li>Console Output: Prints a summary of the analysis results directly to the console for quick verification.</li>
</ul>

<h3>How It Works</h3>
<p>The script follows a simple workflow:</p>
<ul>
    <li>Data Ingestion: It reads website traffic data from website_traffic.csv, preparing it for analysis by converting key columns to numeric types.</li>
    <li>Analysis: It performs calculations to determine total views and average duration. It then aggregates data by page and location to identify the most popular pages and top user locations.</li>
    <li>Report Generation: Using the fpdf library, it creates a new PDF document. It populates the PDF with a title and formatted sections presenting the calculated key metrics and the sorted lists of popular pages and locations. The final report is saved as website_traffic_report.pdf.</li>
</ul>

<img src="C:\Users\bhoomika_chandani\Pictures\Screenshots\report">


